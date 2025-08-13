// const menu1 = document.getElementById('menu-1');


//     menu1.onclick = function(e) {
//         e.preventDefault();
//         menu1.classList.toggle('active');
//     }

function showLogin() {
    document.getElementById("loginForm").classList.add("active");
    document.getElementById("registerForm").classList.remove("active");
}

function showRegister() {
    document.getElementById("registerForm").classList.add("active");
    document.getElementById("loginForm").classList.remove("active");
}


// const menuOverlay = document.getElementById("menuOverlay");
// const mainContent = document.getElementById("mainContent");

// function openMenu() {
//     menuOverlay.classList.add("open");
// }

// function closeMenu() {
//     menuOverlay.classList.remove("open");
// }

// function closeMenuOutside(event) {
//     if (event.target === menuOverlay) {
//         closeMenu();
//     }
// }

// function loadContent(page) {
//     let content = "";

//     switch (page) {
//         case "home":
//         content = "<h2>หน้าแรก</h2><p>ยินดีต้อนรับสู่เว็บไซต์ของเรา!</p>";
//         break;
//         case "about":
//         content = "<h2>เกี่ยวกับเรา</h2><p>เราเป็นทีมพัฒนาที่มุ่งมั่นในการสร้างเว็บที่ดี</p>";
//         break;
//         case "services":
//         content = "<h2>บริการ</h2><ul><li>ออกแบบเว็บไซต์</li><li>พัฒนาแอปพลิเคชัน</li><li>การตลาดออนไลน์</li></ul>";
//         break;
//         case "contact":
//         content = "<h2>ติดต่อเรา</h2><p>อีเมล: example@email.com<br>โทร: 012-345-6789</p>";
//         break;
//         case "faq":
//         content = "<h2>คำถามที่พบบ่อย</h2><p>รวมคำถามที่ลูกค้าถามบ่อยและคำตอบที่มีประโยชน์</p>";
//         break;
//         default:
//         content = "<h2>ไม่พบหน้า</h2>";
//     }

//     mainContent.innerHTML = content;
//     closeMenu(); // ปิดเมนูหลังจากกดเลือก
// }

// toggle dropdown service submenu
document.getElementById('menu-1').addEventListener('click', function () {
  this.classList.toggle('active');
});

// toggle mobile menu
function toggleMenu() {
  const menu = document.getElementById('navMenu');
  menu.classList.toggle('show');
}
