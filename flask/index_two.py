# Константы для расчета бюджета
BASE_NORM_CURRENT_REPAIR = 300.0  # тыс. грн/км для текущего ремонта
BASE_NORM_CAPITAL_REPAIR = 500.0   # тыс. грн/км для капитального ремонта
BASE_NORM_RECONSTRUCTION = 800.0   # тыс. грн/км для реконструкции

# Функция для определения состояния дороги
def assess_road_condition(intensity, strength, evenness, rutting, adhesion):
    """Определяет необходимость ремонта на основе состояния дороги."""
    if intensity >= 15000 and strength >= 0.8 and evenness >= 1 and rutting < 0.05 and adhesion >= 0.35:
        return "Ремонт не требуется"
    elif strength < 0.8:
        return "Капитальный ремонт"
    elif evenness < 1:
        return "Текущий ремонт"
    else:
        return "Реконструкция"

# Функция для расчета бюджета на текущий ремонт
def calculate_current_repair_budget(length):
    return length * BASE_NORM_CURRENT_REPAIR

# Функция для расчета бюджета на капитальный ремонт
def calculate_capital_repair_budget(length):
    return length * BASE_NORM_CAPITAL_REPAIR

# Функция для расчета бюджета на реконструкцию
def calculate_reconstruction_budget(length):
    return length * BASE_NORM_RECONSTRUCTION

# Пример использования
length_current_repair = 100  # км
length_capital_repair = 50    # км
length_reconstruction = 30     # км

# Оценка состояния дороги
intensity = 16000  # авт./день
strength = 0.75    # коэффициент прочности
evenness = 0.9     # коэффициент равномерности
rutting = 0.04     # коэффициент колейности
adhesion = 0.36    # коэффициент сцепления

road_condition = assess_road_condition(intensity, strength, evenness, rutting, adhesion)

# Расчет бюджетов
current_repair_budget = calculate_current_repair_budget(length_current_repair)
capital_repair_budget = calculate_capital_repair_budget(length_capital_repair)
reconstruction_budget = calculate_reconstruction_budget(length_reconstruction)

print(f"Состояние дороги: {road_condition}")
print(f"Бюджет на текущий ремонт: {current_repair_budget:.2f} тыс. грн")
print(f"Бюджет на капитальный ремонт: {capital_repair_budget:.2f} тыс. грн")
print(f"Бюджет на реконструкцию: {reconstruction_budget:.2f} тыс. грн")