document.addEventListener('DOMContentLoaded', function() {
    const urlParams = new URLSearchParams(window.location.search);
    const feedbackSuccess = urlParams.get('feedback_success');
    
    if (feedbackSuccess && feedbackSuccess.toLowerCase() === 'true') {
        // Перенаправляем на страницу благодарности
        window.location.href = '/static/thankforfeedback.html';
    }
});