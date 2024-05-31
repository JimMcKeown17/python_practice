from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    input_text = request.form['input_text']
    result = subprocess.check_output(['python', 'kimani.py', input_text]).decode('utf-8')
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
