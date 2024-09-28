from flask import Flask, request, jsonify
from flask_cors import CORS
import openpyxl


app = Flask(__name__)
CORS(app)

def read_excel_file():
    excel_data = []  # Ініціалізуємо список для зберігання даних з Excel
    try:
        file_path = 'Book1.xlsx'  # Вказуємо шлях до файлу Excel
        workbook = openpyxl.load_workbook(file_path)  # Відкриваємо файл Excel
        sheet = workbook.active  # Отримуємо активний лист

        # Проходимо по рядках, починаючи з другого (щоб пропустити заголовок)
        for row in sheet.iter_rows(min_row=2, values_only=True):  
            if row[0]:  # Перевіряємо, чи є значення в колонці "Рівень вимог"
                
                # Отримуємо значення з колонок і очищаємо їх від пробілів
                level_requirements = str(row[0]).strip()  
                road_value = str(row[1]).strip() if len(row) > 1 else ''  # Перевіряємо, чи існує друга колонка
                traffic_intensity = str(row[2]).strip() if len(row) > 2 else ''  # Перевіряємо, чи існує третя колонка
                level_description = str(row[3]).strip() if len(row) > 3 and row[3] else 'Немає опису'  # Перевіряємо, чи існує четверта колонка

                # Додаємо об'єкт до списку з отриманими даними
                excel_data.append({
                    'Рівень вимог': level_requirements,
                    'Значення автомобільної дороги загального користування': road_value,
                    'Інтенсивність руху в транспортних одиницях, авт./добу': traffic_intensity,
                    'Опис рівня': level_description
                })
                
    except FileNotFoundError:
        return {"error": "Excel file not found"}, 404  # Обробка помилки, якщо файл не знайдено
    except Exception as e:
        return {"error": f"Error reading Excel file: {str(e)}"}, 500  # Загальна обробка помилок
    
    return excel_data  # Повертаємо отримані дані

    
    
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
    data = read_excel_file()
    print(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)