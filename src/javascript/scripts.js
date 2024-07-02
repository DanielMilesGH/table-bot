document.addEventListener('DOMContentLoaded', () => {
    const uploadButton = document.getElementById('upload-button');
    const presetSelect = document.getElementById('preset-select');

    uploadButton.addEventListener('click', () => {
        alert('Upload image button clicked!');
        // Future implementation: trigger file upload dialog
    });

    presetSelect.addEventListener('change', () => {
        const selectedPreset = presetSelect.value;
        if (selectedPreset) {
            alert(`Preset selected: ${selectedPreset}`);
            // Future implementation: load preset image
        }
    });
});
