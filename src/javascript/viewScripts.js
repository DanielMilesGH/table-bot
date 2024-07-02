document.addEventListener('DOMContentLoaded', () => {
    const urlParams = new URLSearchParams(window.location.search);
    const imagePath = urlParams.get('image');
    const imageElement = document.getElementById('selected-image');
    const generateBordersButton = document.getElementById('generate-borders-button');
    const showMovementButton = document.getElementById('show-movement-button');

    // Set the image source to the selected image
    imageElement.src = imagePath;

    // Event listener for the "Generate Object Borders" button
    generateBordersButton.addEventListener('click', () => {
        // Example API endpoint for generating object borders
        const generateBordersURL = '/api/generate-borders';

        fetch(generateBordersURL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ image: imagePath }),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to generate object borders');
            }
            alert('Object borders generated successfully!');
            showMovementButton.style.display = 'block';
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Failed to generate object borders');
        });
    });

    // Event listener for the "Show Movement" button
    showMovementButton.addEventListener('click', () => {
        // Example API endpoint for showing movement
        const showMovementURL = '/api/show-movement';

        fetch(showMovementURL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ image: imagePath }),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to show movement');
            }
            alert('Movement animation shown successfully!');
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Failed to show movement');
        });
    });
});
