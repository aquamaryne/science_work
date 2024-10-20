const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const fetch = require('node-fetch');

function createWindow() {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
            nodeIntegration: false,
            contextIsolation: true
        }
    });

    win.loadFile(path.join(__dirname, 'index.html'));
}

app.whenReady().then(createWindow);

// Обработка события от рендерера
ipcMain.handle('calculate-budget', async (event, data) => {
    try {
        const response = await fetch('http://127.0.0.1:5000/calculate/state', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        return result;  // Возвращаем результат в рендерер
    } catch (error) {
        console.error('Error:', error);
        throw error;  // Возвращаем ошибку в рендерер
    }
});



