document.addEventListener('DOMContentLoaded', () => {
    const imgContainers = document.querySelectorAll('.img-container img');
    const modal = document.querySelector('.modal');
    const fullImage = document.querySelector('.full-image');

    // ตรวจสอบว่ามี Element ครบไหม
    if (!imgContainers.length || !modal || !fullImage) {
        console.error('Error: ไม่พบ Element ที่ต้องการในหน้า HTML');
        return;
    }

    imgContainers.forEach(img => {
        img.addEventListener('click', () => {
            // ดึงค่า src ปัจจุบัน เช่น 'images/small/s_1.jpg'
            const currentSrc = img.getAttribute('src');
            
            // เปลี่ยน path จาก small/s_ เป็น full/ เพื่อดึงรูปใหญ่
            // ตัวอย่าง: 'images/small/s_1.jpg' -> 'images/full/1.jpg'
            const fullSizeSrc = currentSrc.replace('small/s_', 'full/');
            
            fullImage.src = fullSizeSrc;
            modal.classList.add('open');
        });
    });

    // ปิด modal เมื่อคลิกที่พื้นที่ว่าง
    modal.addEventListener('click', () => {
        modal.classList.remove('open');
        fullImage.src = ""; // ล้างค่า src เมื่อปิด
    });
});