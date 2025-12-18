// Frontend JavaScript for SHL Assessment Recommender

const API_URL = 'http://localhost:5000/api';

document.getElementById('recommendBtn').addEventListener('click', async () => {
    const jobDescription = document.getElementById('jobDescription').value;
    
    if (!jobDescription.trim()) {
        alert('Please enter a job description');
        return;
    }
    
    try {
        const response = await fetch(`${API_URL}/recommend`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                job_description: jobDescription,
                num_recommendations: 5
            })
        });
        
        const data = await response.json();
        displayRecommendations(data.assessments);
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to get recommendations. Please try again.');
    }
});

function displayRecommendations(assessments) {
    const listElement = document.getElementById('assessmentList');
    listElement.innerHTML = '';
    
    assessments.forEach((assessment, index) => {
        const card = document.createElement('div');
        card.className = 'assessment-card';
        card.innerHTML = `
            <h3>${index + 1}. ${assessment.name}</h3>
            <p>${assessment.description}</p>
            <span class="score">Match Score: ${(assessment.score * 100).toFixed(1)}%</span>
        `;
        listElement.appendChild(card);
    });
}
