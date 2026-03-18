// newsletter.js — Formspree integration
// Thay YOUR_FORM_ID bằng ID từ formspree.io

const FORMSPREE_ENDPOINT = 'https://formspree.io/f/YOUR_FORM_ID';

document.addEventListener('DOMContentLoaded', function () {
    const forms = document.querySelectorAll('.newsletter-form');

    forms.forEach(function (form) {
        form.addEventListener('submit', async function (e) {
            e.preventDefault();

            const emailInput = form.querySelector('input[type="email"]');
            const submitBtn = form.querySelector('button[type="submit"]');
            const messageEl =
                form.querySelector('.newsletter-message') ||
                form.parentElement.querySelector('.newsletter-message');

            if (!emailInput || !emailInput.value || !submitBtn) return;

            const email = emailInput.value.trim();

            // UI: loading state
            submitBtn.disabled = true;
            submitBtn.textContent = 'Đang gửi...';

            try {
                const response = await fetch(FORMSPREE_ENDPOINT, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        Accept: 'application/json'
                    },
                    body: JSON.stringify({
                        email: email,
                        source: window.location.href,
                        _subject: 'Subscriber mới từ XuyenLab Blog'
                    })
                });

                if (response.ok) {
                    // Success
                    emailInput.value = '';
                    submitBtn.textContent = 'Đã đăng ký';
                    if (messageEl) {
                        messageEl.textContent = 'Cảm ơn bạn! Mình sẽ gửi bài mới sớm nhất.';
                        messageEl.className = 'newsletter-message success';
                    }

                    // Track event nếu có Umami
                    if (typeof umami !== 'undefined') {
                        umami.track('newsletter-subscribe', { page: window.location.pathname });
                    }
                } else {
                    throw new Error('Server error');
                }
            } catch (error) {
                submitBtn.disabled = false;
                submitBtn.textContent = 'Đăng ký';
                if (messageEl) {
                    messageEl.textContent = 'Có lỗi xảy ra, thử lại nhé!';
                    messageEl.className = 'newsletter-message error';
                }
            }
        });
    });
});
