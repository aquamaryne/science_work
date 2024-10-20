# Класс для расчета финансирования дорог
class Road:
    def __init__(self, length_km, category, base_cost_II, inflation_index, mountain_coefficient=1.0, exploitation_coefficient=1.0, traffic_intensity_coefficient=1.0, bridge_coefficient=1.0, lighting_coefficient=1.0, recent_repair_coefficient=1.0, general_correction=1.16):
        self.length_km = length_km  # Протяженность дороги в км
        self.category = category    # Категория дороги
        self.base_cost_II = base_cost_II  # Базовый норматив для дорог II категории (грн/км)
        self.inflation_index = inflation_index  # Индекс инфляции для расчета
        self.mountain_coefficient = mountain_coefficient  # Коэффициент для горной местности (Додаток 5)
        self.exploitation_coefficient = exploitation_coefficient  # Коэффициент эксплуатационных условий (Додаток 6)
        self.traffic_intensity_coefficient = traffic_intensity_coefficient  # Коэффициент интенсивности движения (Додаток 7)
        self.bridge_coefficient = bridge_coefficient  # Коэффициент за наличие мостов (Додаток 8)
        self.lighting_coefficient = lighting_coefficient  # Коэффициент за наличие освещения (Додаток 8)
        self.recent_repair_coefficient = recent_repair_coefficient  # Коэффициент для участков после ремонта (Додаток 8)
        self.general_correction = general_correction  # Общий корректирующий коэффициент для дорог государственного значения

    def financial_normative_state(self, category_coefficients):
        """
        Рассчитывает приведенный норматив річных витрат на содержание дороги государственного значения (формула 3.2)
        :param category_coefficients: коэффициенты для категорий дорог (Додаток 3)
        :return: приведенный норматив (грн/км)
        """
        category_coefficient = category_coefficients.get(self.category, 1.0)
        financial_normative = self.base_cost_II * category_coefficient * self.inflation_index
        return financial_normative

    def financial_normative_local(self, local_category_coefficients):
        """
        Рассчитывает норматив річных витрат на содержание дороги местного значения (формула 3.3)
        :param local_category_coefficients: коэффициенты для местных дорог (Додаток 3)
        :return: норматив (грн/км)
        """
        local_category_coefficient = local_category_coefficients.get(self.category, 1.0)
        financial_normative = self.base_cost_II * local_category_coefficient * self.inflation_index
        return financial_normative

    def total_cost_state(self, category_coefficients):
        """
        Рассчитывает общий объем средств на содержание дорог государственного значения (формула 3.5)
        :param category_coefficients: коэффициенты для категорий дорог (Додаток 3)
        :return: общий объем расходов (грн)
        """
        normative_per_km = self.financial_normative_state(category_coefficients)
        total_cost = (normative_per_km * self.length_km * 
                      self.general_correction * 
                      self.mountain_coefficient *  
                      self.exploitation_coefficient *  
                      self.traffic_intensity_coefficient *  
                      self.bridge_coefficient *  
                      self.lighting_coefficient *  
                      self.recent_repair_coefficient)
        return total_cost

    def total_cost_local(self, local_category_coefficients):
        """
        Рассчитывает общий объем средств на содержание дорог местного значения (формула 3.6)
        :param local_category_coefficients: коэффициенты для категорий местных дорог (Додаток 3)
        :return: общий объем расходов (грн)
        """
        normative_per_km = self.financial_normative_local(local_category_coefficients)
        total_cost = (normative_per_km * self.length_km * 
                      self.general_correction * 
                      self.mountain_coefficient *  
                      self.exploitation_coefficient *  
                      self.traffic_intensity_coefficient *  
                      self.bridge_coefficient *  
                      self.lighting_coefficient *  
                      self.recent_repair_coefficient)
        return total_cost


# Функция для расчета объема средств на содержание дорог местного значения (формула 3.6)
def calculate_local_road_budget(lengths, cost_norms, K2, Kre, KintM):
    """
    Рассчитывает общий объем бюджетных средств на содержание дорог местного значения в области.
    
    :param lengths: словарь с длиной дорог каждой категории (Lij для j от 1 до 5)
    :param cost_norms: нормативные затраты для каждой категории (Hj для j от 1 до 5)
    :param K2: коэффициент эксплуатационных условий (Додаток 6)
    :param Kre: коэффициент интенсивности движения (Додаток 7)
    :param KintM: коэффициент дополнительных условий (например, мосты и горные условия - Додаток 8)
    :return: общий объем средств (Q_i^M)
    """
    total_budget = 0
    for j in range(1, 6):  # Цикл по категориям от 1 до 5
        HjM = cost_norms[j]  # Нормативные затраты для категории j
        LijM = lengths[j]  # Протяженность дорог категории j
        total_budget += HjM * LijM

    # Применение корректирующих коэффициентов
    total_budget *= K2 * Kre * KintM
    return total_budget


# Базовые данные из Додатка 3 (коэффициенты для категорий дорог государственного и местного значения)
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

# Входные параметры
base_cost_II = 604.761  # грн/км для дорог II категории (формула 3.2)
inflation_index = 1.08  # Пример индекса инфляции
length_km = 150  # Протяженность дороги в км

# Коэффициенты из Додатка 5 (горные условия)
mountain_coefficients = {
    'обычная_местность': 1.0,
    'горная_местность': 1.2,
    'экстремальная_местность': 1.4
}

# Коэффициенты из Додатка 6 (эксплуатационные условия)
exploitation_coefficients = {
    'обычные условия': 1.0,
    'сложные условия': 1.1,
    'очень сложные условия': 1.3
}

# Коэффициенты из Додатка 7 (интенсивность движения)
traffic_intensity_coefficients = {
    'низкая интенсивность': 1.0,
    'средняя интенсивность': 1.05,
    'высокая интенсивность': 1.1
}

# Коэффициенты из Додатка 8 (мосты, освещение, участки после ремонта)
bridge_coefficient = 1.1  # Пример коэффициента для дорог с мостами
lighting_coefficient = 1.2  # Пример коэффициента для дорог с освещением
recent_repair_coefficient = 0.5  # Пример коэффициента для дорог после ремонта (5 лет)

# Пример дороги категории III, длиной 150 км, с коэффициентами:
road = Road(
    length_km=length_km,
    category='III',
    base_cost_II=base_cost_II,
    inflation_index=inflation_index,
    mountain_coefficient=mountain_coefficients['горная_местность'],
    exploitation_coefficient=exploitation_coefficients['сложные условия'],
    traffic_intensity_coefficient=traffic_intensity_coefficients['высокая интенсивность'],
    bridge_coefficient=bridge_coefficient,
    lighting_coefficient=lighting_coefficient,
    recent_repair_coefficient=recent_repair_coefficient
)

# Расчет общего объема средств на содержание этой дороги государственного значения (формула 3.5)
total_budget_state = road.total_cost_state(state_category_coefficients)

# Расчет общего объема средств на содержание этой дороги местного значения (формула 3.6)
total_budget_local = road.total_cost_local(local_category_coefficients)

# Расчет общего бюджета для дорог местного значения по формуле 3.6
lengths = {
    1: 50,   # Протяженность дорог I категории в км
    2: 100,  # Протяженность дорог II категории в км
    3: 80,   # Протяженность дорог III категории в км
    4: 120,  # Протяженность дорог IV категории в км
    5: 150   # Протяженность дорог V категории в км
}

cost_norms = {
    1: 1800,  # Нормативные затраты для дорог I категории (грн/км)
    2: 1000,  # Нормативные затраты для дорог II категории (грн/км)
    3: 890,   # Нормативные затраты для дорог III категории (грн/км)
    4: 610,   # Нормативные затраты для дорог IV категории (грн/км)
    5: 390    # Нормативные затраты для дорог V категории (грн/км)
}

K2 = 1.1    # Коэффициент эксплуатационных условий (например, сложные условия)
Kre = 1.05  # Коэффициент интенсивности движения (средняя интенсивность)
KintM = 1.2 # Коэффициент для учета мостов и горных условий

# Финальный расчет
total_budget_for_local_roads = calculate_local_road_budget(lengths, cost_norms, K2, Kre, KintM)

# Вывод результатов
print(f"Общий объем средств на содержание дороги государственного значения: {total_budget_state:.2f} грн")
print(f"Общий объем средств на содержание дороги местного значения: {total_budget_local:.2f} грн")
print(f"Общий объем средств на содержание всех местных дорог: {total_budget_for_local_roads:.2f} грн")
