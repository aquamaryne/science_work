from flask import Flask, render_template, request

app = Flask(__name__)

def number_convert(value):
    if value is None or value == '':
        return 0
    try:
        return int(value)
    except ValueError:
        return float(value)
    
def calculate_qoz(Q1, Qt, Qmizh, Qias, Qlits, Qn, Qvp, Qupr, Qdpp):
    Qoz = Q1 - Qt - Qmizh - Qias - Qlits - Qn - Qvp - Qupr - Qdpp
    return Qoz

def calculate_qmz(Q2, Qkred, Qias2, Qn2, Qdpp2, Qkom):
    QMZ = Q2 - Qkred - Qias2 - Qn2 - Qdpp2 - Qkom
    return QMZ

@app.route('/api/calculate_qoz', methods=['POST'])
def calculate_qoz_view():
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

    Qoz = calculate_qoz(Q1, Qt, Qmizh, Qias, Qlits, Qn, Qvp, Qupr, Qdpp)
    return Qoz

@app.route('/api/calculate_qmz', methods=['POST'])
def calculate_qmz_view():
    data = request.form
    Q2 = number_convert(data.get('Q2'))
    Qkred = number_convert(data.get('Qkred'))
    Qias2 = number_convert(data.get('Qias2'))
    Qn2 = number_convert(data.get('Qn2'))
    Qdpp2 = number_convert(data.get('Qdpp2'))
    Qkom = number_convert(data.get('Qkom'))

    QMZ = calculate_qmz(Q2, Qkred, Qias2, Qn2, Qdpp2, Qkom)
    return QMZ

if __name__ == '__main__':
    app.run(debug=True)