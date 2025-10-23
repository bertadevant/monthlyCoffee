// Rating Modal Functions

function closeRatingModal() {
    document.getElementById('ratingModal').style.display = 'none';
}

function setRating(rating) {
    document.getElementById('ratingScore').value = rating;
    const stars = document.querySelectorAll('.star');
    stars.forEach((star, index) => {
        if (index < rating) {
            star.style.color = '#FFD700'; // Gold color for selected stars
        } else {
            star.style.color = '#ddd'; // Gray for unselected stars
        }
    });
}

// Initialize rating modal functionality
document.addEventListener('DOMContentLoaded', function() {
    const ratingModal = document.getElementById('ratingModal');

    if (ratingModal) {
        // Auto-open modal if it exists
        ratingModal.style.display = 'flex';

        // Close modal when clicking outside
        ratingModal.addEventListener('click', function(e) {
            if (e.target === this) {
                closeRatingModal();
            }
        });

        // Validate form before submission
        const ratingForm = document.getElementById('ratingForm');
        if (ratingForm) {
            ratingForm.addEventListener('submit', function(e) {
                const score = document.getElementById('ratingScore').value;
                if (!score) {
                    e.preventDefault();
                    alert('Please select a star rating before submitting.');
                }
            });
        }
    }
});
