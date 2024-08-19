from flask import Flask, request, render_template

app = Flask(__name__)

def number_convert(value):
    if value is None or value == '':
        return 0
    try:
        return int(value)
    except ValueError:
        return float(value)
    
def calculate(Q2, Qkred, QIAS2, Qn2, Qdpp2, Qkom):
    QMZ = Q2 - Qkred - QIAS2 - Qn2 - Qdpp2 - Qkom
    return QMZ

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/calculate_1', methods=['POST'])
def calculate():
    data = request.form
    Q2 = number_convert(data.get('Q2'))
    Qkred = number_convert(data.get('Qkred'))
    QIAS2 = number_convert(data.get('QIAS2'))
    Qn2 = number_convert(data.get('Qn2'))
    Qdpp2 = number_convert(data.get('Qdpp2'))
    Qkom = number_convert(data.get('Qkom'))

    QMZ = calculate(Q2, Qkred, QIAS2, Qn2, Qdpp2, Qkom)
    return render_template('index1.html', QMZ=QMZ)

if __name__ == '__main__':
    app.run(debug=True)
    