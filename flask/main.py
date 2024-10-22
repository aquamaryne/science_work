from flask import Flask, request, jsonify

app = Flask(__name__)

# Коэффициенты для категорий дорог (из Додаток 3)
state_category_coefficients = {
    'I': 1.80,  # Государственные дороги, категория I
    'II': 1.00,  # Государственные дороги, категория II
    'III': 0.89,  # Государственные дороги, категория III
    'IV': 0.61,  # Государственные дороги, категория IV
    'V': 0.39   # Государственные дороги, категория V
}

local_category_coefficients = {
    'I': 1.71,  # Местные дороги, категория I
    'II': 1.00,  # Местные дороги, категория II
    'III': 0.85,  # Местные дороги, категория III
    'IV': 0.64,  # Местные дороги, категория IV
    'V': 0.40   # Местные дороги, категория V
}

# Формулы 3.2 и 3.5 для расчета бюджета для дорог государственного значения
def calculate_total_cost_state(data):
    """
    Рассчитывает общий объем средств на содержание дорог государственного значения (формулы 3.2 и 3.5)
    с использованием коэффициентов из Додаток 3
    """
    base_cost = data['base_cost_II']  # Получаем базовую стоимость (может быть base_cost_I или base_cost_II)
    inflation_index = data['inflation_index']  # ИНФЛЯЦИЯ
    category = data['category']  # Категория дороги (I, II, III и т.д.)
    length_km = data['length_km']  # Протяженность дороги в километрах

    # Получаем коэффициент для категории дорог государственного значения
    category_coefficient = state_category_coefficients.get(category, 1.0)

    # Формула 3.2 — Расчет нормативных затрат на 1 км
    normative_per_km = base_cost * category_coefficient * inflation_index

    # Формула 3.5 — Общие затраты с учетом всех коэффициентов
    total_cost = (normative_per_km * length_km *
                  data['general_correction'] *
                  data['mountain_coefficient'] *
                  data['exploitation_coefficient'] *
                  data['traffic_intensity_coefficient'] *
                  data['bridge_coefficient'] *
                  data['lighting_coefficient'] *
                  data['recent_repair_coefficient'])
    return total_cost

# Формулы 3.3 и 3.6 для расчета бюджета для дорог местного значения
def calculate_total_cost_local(data):
    """
    Рассчитывает общий объем средств на содержание дорог местного значения (формулы 3.3 и 3.6)
    с использованием коэффициентов из Додаток 3
    """
    base_cost = data['base_cost_II']  # Получаем базовую стоимость (может быть base_cost_I или base_cost_II)
    inflation_index = data['inflation_index']  # ИНФЛЯЦИЯ
    category = data['category']  # Категория дороги (I, II, III и т.д.)
    length_km = data['length_km']  # Протяженность дороги в километрах

    # Получаем коэффициент для категории дорог местного значения
    category_coefficient = local_category_coefficients.get(category, 1.0)

    # Формула 3.3 — Расчет нормативных затрат на 1 км
    normative_per_km = base_cost * category_coefficient * inflation_index

    # Формула 3.6 — Общие затраты с учетом всех коэффициентов
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

