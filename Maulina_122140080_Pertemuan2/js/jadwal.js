import { loadFromLocalStorage, saveToLocalStorage } from './modules/utils.js';
import { STORAGE_KEY } from './modules/data.js';

const createScheduleItem = ({ id, course, day, time }) => {
  return `
    <div class="card flex justify-between items-center" data-id="${id}">
      <div>
        <p class="font-semibold">${course}</p>
        <p>${day}, ${time}</p>
      </div>
      <div class="space-x-2 flex-shrink-0">
        <button class="editBtn bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded">Edit</button>
        <button class="deleteBtn bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded">Hapus</button>
      </div>
    </div>
  `;
};

const renderSchedules = (filterDay = '') => {
  const schedules = loadFromLocalStorage(STORAGE_KEY);
  const list = document.getElementById('scheduleList');
  list.innerHTML = '';

  const filtered = filterDay
    ? schedules.filter(j => j.day.toLowerCase().includes(filterDay.toLowerCase()))
    : schedules;

  if (filtered.length === 0) {
    list.innerHTML = '<p class="text-gray-500">Tidak ada jadwal ditemukan.</p>';
    return;
  }

  filtered.forEach(item => {
    list.innerHTML += createScheduleItem(item);
  });
};

const handleActions = () => {
  document.getElementById('scheduleList').addEventListener('click', (e) => {
    const card = e.target.closest('.card');
    const id = parseInt(card.dataset.id);
    let schedules = loadFromLocalStorage(STORAGE_KEY);

    if (e.target.classList.contains('deleteBtn')) {
      schedules = schedules.filter(j => j.id !== id);
      saveToLocalStorage(STORAGE_KEY, schedules);
      renderSchedules(document.getElementById('filterInput').value);
    }

    if (e.target.classList.contains('editBtn')) {
      const data = schedules.find(j => j.id === id);
      localStorage.setItem('edit_jadwal', JSON.stringify(data));
      window.location.href = 'index.html';
    }
  });
};

const setupFilter = () => {
  document.getElementById('filterInput').addEventListener('input', (e) => {
    renderSchedules(e.target.value);
  });
};

document.addEventListener('DOMContentLoaded', () => {
  renderSchedules();
  handleActions();
  setupFilter();
});
