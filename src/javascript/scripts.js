document.addEventListener('DOMContentLoaded', () => {
    const uploadButton = document.getElementById('upload-button');
    const presetElements = document.querySelectorAll('.preset');

    // Event listener for the upload button
    uploadButton.addEventListener('click', () => {
        const imagePath = '/data/preset-images/placeholder_image.jpg';
        window.location.href = `view.html?image=${encodeURIComponent(imagePath)}`;
    });

    // Event listeners for preset images
    presetElements.forEach(presetElement => {
        presetElement.querySelector('button').addEventListener('click', () => {
            const selectedPreset = presetElement.getAttribute('data-preset');
            const imagePath = selectedPreset === 'preset1' ? '/data/preset-images/easy_image.jpg' : '/data/preset-images/hard_image.jpg';
            window.location.href = `view.html?image=${encodeURIComponent(imagePath)}`;
        });
    });
});
