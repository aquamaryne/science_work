from flask import Flask, request, jsonify

app = Flask(__name__)

# Коэффициенты для категорий дорог
state_category_coefficients = {
    'I': 1.80,
    'II': 1.00,
    'III': 0.89,
    'IV': 0.61,
    'V': 0.39
}

local_category_coefficients = {
    'I': 1.71,
    'II': 1.00,
    'III': 0.85,
    'IV': 0.64,
    'V': 0.40
}

# Функции для расчета затрат
def calculate_total_cost_state(data):
    """
    Рассчитывает общий объем средств на содержание дорог государственного значения (формула 3.5)
    """
    base_cost_II = data['base_cost_II']
    inflation_index = data['inflation_index']
    category = data['category']
    length_km = data['length_km']
    
    coefficients = state_category_coefficients

    category_coefficient = coefficients.get(category, 1.0)
    normative_per_km = base_cost_II * category_coefficient * inflation_index

    total_cost = (normative_per_km * length_km *
                  data['general_correction'] *
                  data['mountain_coefficient'] *
                  data['exploitation_coefficient'] *
                  data['traffic_intensity_coefficient'] *
                  data['bridge_coefficient'] *
                  data['lighting_coefficient'] *
                  data['recent_repair_coefficient'])
    return total_cost


def calculate_total_cost_local(data):
    """
    Рассчитывает общий объем средств на содержание дорог местного значения (формула 3.6)
    """
    base_cost_II = data['base_cost_II']
    inflation_index = data['inflation_index']
    category = data['category']
    length_km = data['length_km']
    
    coefficients = local_category_coefficients

    category_coefficient = coefficients.get(category, 1.0)
    normative_per_km = base_cost_II * category_coefficient * inflation_index

    total_cost = (normative_per_km * length_km *
                  data['general_correction'] *
                  data['mountain_coefficient'] *
                  data['exploitation_coefficient'] *
                  data['traffic_intensity_coefficient'] *
                  data['bridge_coefficient'] *
                  data['lighting_coefficient'] *
                  data['recent_repair_coefficient'])
    return total_cost


# Flask route для расчета бюджета для дорог государственного значения
@app.route('/calculate/state', methods=['POST'])
def calculate_state():
    data = request.json
    print(f"Received data: {data}")  # Отладочный вывод
    total_cost = calculate_total_cost_state(data)
    return jsonify({'total_budget_state': total_cost})


# Flask route для расчета бюджета для дорог местного значения
@app.route('/calculate/local', methods=['POST'])
def calculate_local():
    data = request.json
    total_cost = calculate_total_cost_local(data)
    return jsonify({'total_budget_local': total_cost})

if __name__ == '__main__':
    app.run(debug=True)
