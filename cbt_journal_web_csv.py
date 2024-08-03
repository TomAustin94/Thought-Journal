from flask import Flask, render_template, request
import csv
from datetime import datetime
import os

app = Flask(__name__)

CSV_FILE = 'cbt_journal_entries.csv'

def save_to_csv(entry):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Date', 'Situation', 'Thoughts', 'Emotions', 'Evidence For', 'Evidence Against', 'Reframed Thoughts', 'Outcome']
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
            'Outcome': entry['outcome']
        })

@app.route('/', methods=['GET', 'POST'])
def journal():
    if request.method == 'POST':
        entry = {
            'situation': request.form['situation'],
            'thoughts': request.form['thoughts'],
            'emotions': request.form['emotions'],
            'challenge': request.form['challenge'],
            'alternative': request.form['alternative'],
            'reframe': request.form['reframe'],
            'outcome': request.form['outcome']
        }
        save_to_csv(entry)
        return render_template('entry.html', entry=entry, saved=True)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
