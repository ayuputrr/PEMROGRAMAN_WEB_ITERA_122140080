export const STORAGE_KEY = 'jadwal_kuliah';

export const loadFromStorage = () => JSON.parse(localStorage.getItem(STORAGE_KEY)) || [];