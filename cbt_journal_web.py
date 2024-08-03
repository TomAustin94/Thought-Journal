from flask import Flask, render_template, request

app = Flask(__name__)

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
        return render_template('entry.html', entry=entry)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
