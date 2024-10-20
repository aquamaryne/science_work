const { contextBridge, ipcRenderer } = require('electron');

// Экспортируем методы в контекст рендерера
contextBridge.exposeInMainWorld('api', {
    calculateBudget: (data) => ipcRenderer.invoke('calculate-budget', data)
});


