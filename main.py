from flask import Flask, render_template, request

app = Flask(__name__)

def number_convert(value):
    if value is None or value == '':
        return 0
    try:
        return int(value)
    except ValueError:
        return float(value)
    
def calculate_budget(Q1, Qt, Qmizh, Qias, Qlits, Qn, Qvp, Qupr, Qdpp):
    Qoz = Q1 - Qt - Qmizh - Qias - Qlits - Qn - Qvp - Qupr - Qdpp
    return Qoz

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.form
    Q1 = number_convert(data.get('Q1'))
    Qt = number_convert(data.get('Qt'))
    Qmizh = number_convert(data.get('Qmizh'))
    Qias = number_convert(data.get('QIAS'))
    Qlits = number_convert(data.get('Qlits'))
    Qn = number_convert(data.get('Qn'))
    Qvp = number_convert(data.get('Qvp'))
    Qupr = number_convert(data.get('Qup'))
    Qdpp = number_convert(data.get('QDPP'))

    Qoz = calculate_budget(Q1, Qt, Qmizh, Qias, Qlits, Qn, Qvp, Qupr, Qdpp)

    return render_template('index.html', Qoz=Qoz)

if __name__ == '__main__':
    app.run(debug=True)