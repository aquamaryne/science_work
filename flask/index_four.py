class RoadConstruction:
    def __init__(self):
        self.budget = 0
        self.projects = []

    def set_budget(self, amount):
        self.budget = amount

    def add_project(self, name, base_cost, priority, category):
        # Добавляем проект с базовой стоимостью, приоритетом и категорией
        self.projects.append({'name': name, 'base_cost': base_cost, 'priority': priority, 'category': category})

    def calculate_final_cost(self, project):
        # Применяем коэффициенты в зависимости от категории
        coefficients = {
            'I': 1.80,
            'II': 1.00,
            'III': 0.89,
            'IV': 0.61,
            'V': 0.39
        }
        category = project['category']
        if category in coefficients:
            return project['base_cost'] * coefficients[category]
        return project['base_cost']

    def allocate_budget(self):
        # Сортируем проекты по приоритету (от высшего к низшему)
        sorted_projects = sorted(self.projects, key=lambda x: x['priority'], reverse=True)
        allocated_projects = []

        for project in sorted_projects:
            final_cost = self.calculate_final_cost(project)
            if self.budget >= final_cost:
                allocated_projects.append({'name': project['name'], 'final_cost': final_cost, 'priority': project['priority']})
                self.budget -= final_cost

        return allocated_projects, self.budget

# Пример использования
road_construction = RoadConstruction()
road_construction.set_budget(100000)  # Установка бюджета

# Добавление проектов (название, базовая стоимость, приоритет, категория)
road_construction.add_project("Строительство дороги A", 30000, 1, 'I')
road_construction.add_project("Строительство дороги B", 50000, 2, 'II')
road_construction.add_project("Строительство дороги C", 20000, 3, 'III')

# Распределение бюджета
allocated_projects, remaining_budget = road_construction.allocate_budget()

# Вывод результатов
print("Распределенные проекты:")
for project in allocated_projects:
    print(f"Проект: {project['name']}, Окончательная стоимость: {project['final_cost']}, Приоритет: {project['priority']}")
print(f"Оставшийся бюджет: {remaining_budget}")