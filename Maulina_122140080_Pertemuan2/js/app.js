import { loadFromLocalStorage, saveToLocalStorage, delay } from './modules/utils.js';
import { STORAGE_KEY } from './modules/data.js';

class Schedule {
  constructor(course, day, time, id = Date.now()) {
    this.course = course;
    this.day = day;
    this.time = time;
    this.id = id;
  }
}

document.addEventListener('DOMContentLoaded', async () => {
  await delay(200);

  let schedules = loadFromLocalStorage(STORAGE_KEY);

 
  const editData = localStorage.getItem('edit_jadwal');
  if (editData) {
    try {
      const { course, day, time, id } = JSON.parse(editData);
      document.getElementById('courseInput').value = course;
      document.getElementById('dayInput').value = day;
      document.getElementById('timeInput').value = time;
      document.getElementById('editId').value = id;
      console.log('Data edit ditemukan dan ditampilkan:', { course, day, time, id });
    } catch (err) {
      console.error('Gagal memuat data edit:', err);
    }
    localStorage.removeItem('edit_jadwal');
  }

  const form = document.getElementById('scheduleForm');
  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const course = document.getElementById('courseInput').value;
    const day = document.getElementById('dayInput').value;
    const time = document.getElementById('timeInput').value;
    const id = document.getElementById('editId').value;

    if (id) {
      schedules = schedules.map(item => item.id == id ? new Schedule(course, day, time, parseInt(id)) : item);
    } else {
      schedules.push(new Schedule(course, day, time));
    }

    saveToLocalStorage(STORAGE_KEY, schedules);
    alert('Jadwal berhasil disimpan!');
    form.reset();
  });
});
