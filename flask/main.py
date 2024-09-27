from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import csv
import pandas as pd

app = Flask(__name__)
CORS(app)

def read_csv_file():
    csv_data = []
    try:
        with open('Book1.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
            for row in reader:
                if row['Рівень вимог']:  # Игнорируем строки без значения
                    csv_data.append({
                        'Рівень вимог': row['Рівень вимог'].strip(),
                        'Значення автомобільної дороги загального користування': row['Значення автомобільної дороги загального користування'].strip(),
                        'Інтенсивність руху в транспортних одиницях, авт./добу': row['Інтенсивність руху в транспортних одиницях, авт./добу'].strip(),
                        'Опис рівня': row.get('Опис рівня', '').strip() or 'Немає опису'
                    })
    except FileNotFoundError:
        return {"error": "CSV file not found"}, 404
    except Exception as e:
        return {"error": f"Error reading CSV file: {str(e)}"}, 500
    
    return csv_data
    
    
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
    Qmz = Q2 - Qkred - Qias2 - Qn2 - Qdpp2 - Qkom
    return Qmz

@app.route('/calculate_qoz', methods=['POST'])
def calculate_qoz_view():
    data = request.json
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
    return jsonify({"Qoz": Qoz})

@app.route('/calculate_qmz', methods=['POST'])
def calculate_qmz_view():
    data = request.json
    Q2 = number_convert(data.get('Q2'))
    Qkred = number_convert(data.get('Qkred'))
    Qias2 = number_convert(data.get('Qias2'))
    Qn2 = number_convert(data.get('Qn2'))
    Qdpp2 = number_convert(data.get('Qdpp2'))
    Qkom = number_convert(data.get('Qkom'))

    Qmz = calculate_qmz(Q2, Qkred, Qias2, Qn2, Qdpp2, Qkom)
    return jsonify({"Qmz": Qmz})

@app.route('/road_levels', methods=['GET'])
def get_road_levels():
    data = read_csv_file()
    print(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)