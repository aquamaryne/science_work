document.getElementById('calculateBtn').addEventListener('click', () => {
    const category = document.getElementById('category').value;
    const mountain = parseFloat(document.getElementById('mountain').value);
    const exploitation = parseFloat(document.getElementById('exploitation').value);
    const traffic = parseFloat(document.getElementById('traffic').value);

    const base_cost_II = 604.761;  // Предопределенное значение
    const inflation_index = 1.08;  // Пример
    const length_km = 150;  // Пример длины дороги

    // Подготовим данные для передачи в Flask
    const data = {
        category: category,
        base_cost_II: base_cost_II,
        inflation_index: inflation_index,
        length_km: length_km,
        general_correction: 1.0,  // Пример значения
        mountain_coefficient: mountain,
        exploitation_coefficient: exploitation,
        traffic_intensity_coefficient: traffic,
        bridge_coefficient: 1.1,  // Пример значения
        lighting_coefficient: 1.2,  // Пример значения
        recent_repair_coefficient: 0.5  // Пример значения
    };

    // Вызываем метод из preload.js для отправки запроса
    window.api.calculateBudget(data)
        .then(result => {
            document.getElementById('result').textContent = `Total Budget for State Roads: ${result.total_budget_state.toFixed(2)} грн`;
        })
        .catch(error => console.error('Error:', error));
});

