document.addEventListener('DOMContentLoaded', function() {
    console.log('DevOps Notes - Taller loaded successfully!');
    
    const topicCards = document.querySelectorAll('.topic-card');
    
    topicCards.forEach(card => {
        card.addEventListener('click', function() {
            const topic = this.querySelector('h3').textContent;
            console.log(`Topic clicked: ${topic}`);
        });
    });
});
