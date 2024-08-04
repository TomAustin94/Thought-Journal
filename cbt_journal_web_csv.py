from flask import Flask, render_template, request
import csv
from datetime import datetime
import os
import matplotlib.pyplot as plt

app = Flask(__name__)

CSV_FILE = 'cbt_journal_entries.csv'
STATIC_DIR = 'static'
GRAPH_FILE = 'mood_trends.png'

# Ensure the static directory exists
if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR)

def save_to_csv(entry):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Date', 'Situation', 'Thoughts', 'Emotions', 'Evidence For', 'Evidence Against', 'Reframed Thoughts', 'Outcome', 'Initial Mood', 'Final Mood']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            'Date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'Situation': entry['situation'],
            'Thoughts': entry['thoughts'],
            'Emotions': entry['emotions'],
            'Evidence For': entry['challenge'],
            'Evidence Against': entry['alternative'],
            'Reframed Thoughts': entry['reframe'],
            'Outcome': entry['outcome'],
            'Initial Mood': entry['initial_mood'],
            'Final Mood': entry['final_mood']
        })

def generate_mood_graph():
    if not os.path.isfile(CSV_FILE):
        return False

    dates = []
    initial_moods = []
    final_moods = []
    with open(CSV_FILE, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dates.append(datetime.strptime(row['Date'], "%Y-%m-%d %H:%M:%S"))
            initial_moods.append(int(row['Initial Mood']))
            final_moods.append(int(row['Final Mood']))

    if not dates:  # If there are no entries, don't generate the graph
        return False

    plt.figure(figsize=(10, 5))
    plt.plot(dates, initial_moods, marker='o', label='Initial Mood')
    plt.plot(dates, final_moods, marker='o', label='Final Mood')
    plt.xlabel('Date')
    plt.ylabel('Mood')
    plt.title('Mood Trends Over Time')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(STATIC_DIR, GRAPH_FILE))
    plt.close()
    return True

@app.route('/', methods=['GET', 'POST'])
def journal():
    if request.method == 'POST':
        entry = {
            'initial_mood': request.form['initial_mood'],
            'situation': request.form['situation'],
            'thoughts': request.form['thoughts'],
            'emotions': request.form['emotions'],
            'challenge': request.form['challenge'],
            'alternative': request.form['alternative'],
            'reframe': request.form['reframe'],
            'outcome': request.form['outcome'],
            'final_mood': request.form['final_mood']
        }
        save_to_csv(entry)
        generate_mood_graph()  # Generate the graph after each new entry
        return render_template('entry.html', entry=entry, saved=True)
    return render_template('form.html')

@app.route('/mood_trends')
def mood_trends():
    if not os.path.isfile(CSV_FILE) or not generate_mood_graph():
        return render_template('error.html', message="No journal entries found or unable to generate mood trends. Please complete a thought journal first.")
    return render_template('mood_trends.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(STATIC_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)
