function showLogin() {
    document.getElementById("loginForm").classList.add("active");
    document.getElementById("registerForm").classList.remove("active");
}

function showRegister() {
    document.getElementById("registerForm").classList.add("active");
    document.getElementById("loginForm").classList.remove("active");
}

const toggleBtn = document.getElementById('menuToggle');
const menu = document.getElementById('menu');
const overlay = document.getElementById('overlay');
const nav = document.querySelector('nav');

toggleBtn.addEventListener('click', () => {
  const navHeight = nav.offsetHeight;

  if (menu.classList.contains('show')) {
    // กำลังจะปิดเมนู
    menu.style.top = '-100%'; // ซ่อนเมนู
    menu.classList.remove('show');
    overlay.classList.remove('show');
  } else {
    // กำลังจะเปิดเมนู
    menu.style.top = navHeight + 'px'; // ตั้งตำแหน่งเมนูใต้ nav
    menu.classList.add('show');
    overlay.classList.add('show');
  }
});

// ปิดเมนูเมื่อคลิกพื้นที่ว่าง
overlay.addEventListener('click', () => {
    menu.classList.remove('show');
    overlay.classList.remove('show');
});

function showPage(pageId) {
  const pages = document.querySelectorAll('.page');
  pages.forEach(page => {
    page.classList.remove('active');
  });

  document.getElementById(pageId).classList.add('active');
}