# Константы
BASE_NORM_STATE = 604.761  # тыс. грн/км для дорог II категории государственного значения
BASE_NORM_LOCAL = 360.544  # тыс. грн/км для дорог II категории местного значения

# Коэффициенты дифференциации из Додатка 3
differentiation_coefficients = {
    'state': {
        'II': 1.00,
        'III': 0.89,
        'IV': 0.61,
        'V': 0.39
    },
    'local': {
        'II': 1.00,
        'III': 0.85,
        'IV': 0.64,
        'V': 0.40
    }
}

# Коэффициенты для горной местности из Додатка 5
mountain_coefficients = {
    'Крим': 1.15,
    'Ивано-Франковская': 1.13,
    'Закарпатская': 1.11,
    'Львовская': 1.04,
    'остальные': 1.00
}

# Коэффициенты условий эксплуатации из Додатка 6
conditions_coefficients = {
    'Крим': 1.15,
    'Ивано-Франковская': 1.13,
    'Закарпатская': 1.11,
    'Львовская': 1.04,
    'остальные': 1.00
}

# Коэффициенты интенсивности из Додатка 7
intensity_coefficients = {
    'до 15000': 1.0,
    'от 15001 до 20000': 2.3,
    'от 20001 до 30000': 3.5,
    'от 30001 и более': 3.9
}

# Коэффициенты критической инфраструктуры из Додатка 8
critical_coefficients = {
    '1-5': 1.01,
    '5-10': 1.03,
    '10 и более': 1.05
}

def calculate_adjusted_norm(base_norm, category, road_type):
    """Рассчитывает приведенный норматив для дороги заданной категории"""
    return base_norm * differentiation_coefficients[road_type][category]

def get_intensity_coefficient(intensity):
    """Возвращает коэффициент интенсивности на основе значения интенсивности"""
    if intensity <= 15000:
        return intensity_coefficients['до 15000']
    elif 15001 <= intensity <= 20000:
        return intensity_coefficients['от 15001 до 20000']
    elif 20001 <= intensity <= 30000:
        return intensity_coefficients['от 20001 до 30000']
    else:
        return intensity_coefficients['от 30001 и более']

def calculate_state_road_funding(length, category, inflation_index, mountain_region, intensity):
    """Рассчитывает объем финансирования для дороги государственного значения"""
    norm = calculate_adjusted_norm(BASE_NORM_STATE, category, 'state')
    
    # Применяем коэффициенты
    k_mountain = mountain_coefficients.get(mountain_region, 1.0)
    k_conditions = conditions_coefficients.get(mountain_region, 1.0)
    k_intensity = get_intensity_coefficient(intensity)

    funding = length * norm * inflation_index * k_mountain * k_conditions * k_intensity
    return funding

def calculate_local_road_funding(length, category, inflation_index, mountain_region, intensity):
    """Рассчитывает объем финансирования для дороги местного значения"""
    norm = calculate_adjusted_norm(BASE_NORM_LOCAL, category, 'local')
    
    # Применяем коэффициенты
    k_mountain = mountain_coefficients.get(mountain_region, 1.0)
    k_conditions = conditions_coefficients.get(mountain_region, 1.0)
    k_intensity = get_intensity_coefficient(intensity)

    funding = length * norm * inflation_index * k_mountain * k_conditions * k_intensity
    return funding

# Пример использования
length_state = 100  # км
category_state = 'II'
inflation_index_state = 1.05  # Пример индекса инфляции
mountain_region_state = 'Ивано-Франковская'
intensity_state = 16000  # авт./ день

length_local = 50  # км
category_local = 'III'
inflation_index_local = 1.05  # Пример индекса инфляции
mountain_region_local = 'Ивано-Франковская'
intensity_local = 16000  # авт./день

state_road_funding = calculate_state_road_funding(length_state, category_state, inflation_index_state, mountain_region_state, intensity_state)
local_road_funding = calculate_local_road_funding(length_local, category_local, inflation_index_local, mountain_region_local, intensity_local)

print(f"Финансирование дороги государственного значения: {state_road_funding:.2f} тыс. грн")
print(f"Финансирование дороги местного значения: {local_road_funding:.2f} тыс. грн")