// Tracking events cho portfolio analytics
document.addEventListener('DOMContentLoaded', function () {
    // Track click CTA coffee
    document
        .querySelectorAll('a[href*="coffee.xuyenlab.com"], a[href*="eakar"]')
        .forEach(function (el) {
            el.addEventListener('click', function () {
                if (typeof umami !== 'undefined') {
                    umami.track('cta-coffee-click', { page: window.location.pathname });
                }
            });
        });

    // Track click CTA khóa học
    document
        .querySelectorAll('a[href*="khoa-hoc"], a[href*="course"]')
        .forEach(function (el) {
            el.addEventListener('click', function () {
                if (typeof umami !== 'undefined') {
                    umami.track('cta-course-click', { page: window.location.pathname });
                }
            });
        });

    // Track scroll depth 75% — chỉ trên bài viết
    if (document.querySelector('.post-content')) {
        var tracked75 = false;

        window.addEventListener('scroll', function () {
            if (!tracked75) {
                var scrolled = window.scrollY + window.innerHeight;
                var total = document.body.scrollHeight;

                if (scrolled / total >= 0.75) {
                    tracked75 = true;
                    if (typeof umami !== 'undefined') {
                        umami.track('read-75pct', { page: window.location.pathname });
                    }
                }
            }
        });
    }
});
