// Evolving System Documentation - Feedback Widget

document.addEventListener('DOMContentLoaded', function() {
  // Rate limiting: max 5 feedback submissions per hour
  const RATE_LIMIT = 5;
  const RATE_LIMIT_WINDOW = 3600000; // 1 hour in ms

  function getFeedbackCount() {
    const stored = localStorage.getItem('feedback_submissions');
    if (!stored) return { count: 0, timestamp: Date.now() };

    const data = JSON.parse(stored);
    // Reset if window expired
    if (Date.now() - data.timestamp > RATE_LIMIT_WINDOW) {
      return { count: 0, timestamp: Date.now() };
    }
    return data;
  }

  function incrementFeedbackCount() {
    const data = getFeedbackCount();
    data.count++;
    localStorage.setItem('feedback_submissions', JSON.stringify(data));
    return data.count;
  }

  function canSubmitFeedback() {
    return getFeedbackCount().count < RATE_LIMIT;
  }

  // Track feedback submissions
  const feedbackButtons = document.querySelectorAll('[data-md-component="feedback"] button');

  feedbackButtons.forEach(button => {
    button.addEventListener('click', function(e) {
      if (!canSubmitFeedback()) {
        e.preventDefault();
        alert('Rate limit reached. Please try again later.');
        return;
      }

      const rating = this.getAttribute('data-md-value');
      const page = window.location.pathname;

      // Log feedback (could be sent to analytics)
      console.log('Feedback:', { page, rating, timestamp: new Date().toISOString() });

      incrementFeedbackCount();

      // Store locally for potential sync
      const feedbackHistory = JSON.parse(localStorage.getItem('feedback_history') || '[]');
      feedbackHistory.push({
        page: page,
        rating: rating,
        timestamp: new Date().toISOString(),
        lang: document.documentElement.lang || 'en'
      });

      // Keep only last 100 entries
      if (feedbackHistory.length > 100) {
        feedbackHistory.shift();
      }

      localStorage.setItem('feedback_history', JSON.stringify(feedbackHistory));
    });
  });
});
