
export const saveToLocalStorage = (key, data) => localStorage.setItem(key, JSON.stringify(data));
export const loadFromLocalStorage = (key) => JSON.parse(localStorage.getItem(key)) || [];
export const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));
