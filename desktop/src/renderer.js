const { ipcRenderer } = require('electron');

window.api = {
    calculateBudget: (url, data) => {
        return ipcRenderer.invoke('calculate-budget', { url, data });
    }
};
