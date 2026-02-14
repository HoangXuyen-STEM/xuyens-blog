document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('newsletter-form');
    if (!form) return;

    form.addEventListener('submit', function (e) {
        e.preventDefault();
        const email = document.getElementById('newsletter-email').value.trim();
        const msg = document.getElementById('newsletter-msg');

        if (!email) return;

        // Check trùng email
        let subscribers = JSON.parse(localStorage.getItem('blog_subscribers') || '[]');
        if (subscribers.includes(email)) {
            msg.textContent = '📧 Bạn đã đăng ký rồi! Cảm ơn bạn.';
            msg.style.display = 'block';
            msg.style.color = '#E8C9B0';
            return;
        }

        // Lưu email
        subscribers.push(email);
        localStorage.setItem('blog_subscribers', JSON.stringify(subscribers));

        msg.textContent = '🎉 Cảm ơn bạn đã đăng ký! Hẹn gặp trong bài viết tiếp theo.';
        msg.style.display = 'block';
        msg.style.color = '#A8C4D4';

        // Reset form
        document.getElementById('newsletter-email').value = '';
    });
});
