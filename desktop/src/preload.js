const { contextBridge, ipcRenderer } = require('electron');

// Экспортируем методы в контекст рендерера
contextBridge.exposeInMainWorld('api', {
    navigateTo: (page) => ipcRenderer.send('navigate', page)
});


