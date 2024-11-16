document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('upload-form');
    const fileInput = document.getElementById('scan-file');
    const fileNameDisplay = document.getElementById('file-name');
    const submitButton = form.querySelector('button[type="submit"]');
    const resultDiv = document.getElementById('result');
    const resultContent = document.getElementById('result-content');

    fileInput.addEventListener('change', function() {
        if (this.files && this.files[0]) {
            fileNameDisplay.textContent = this.files[0].name;
            submitButton.disabled = false;
        } else {
            fileNameDisplay.textContent = '';
            submitButton.disabled = true;
        }
    });

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const formData = new FormData();
        formData.append('file', fileInput.files[0]);

        try {
            submitButton.disabled = true;
            submitButton.textContent = 'Analyzing...';

            const response = await fetch('/upload', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (response.ok) {
                resultContent.innerHTML = `
                    <div class="bg-green-100 border-l-4 border-green-500 text-green-700 p-4">
                        <p>${data.message}</p>
                        <p>Filename: ${data.filename}</p>
                    </div>
                `;
            } else {
                throw new Error(data.error || 'Upload failed');
            }
        } catch (error) {
            resultContent.innerHTML = `
                <div class="bg-red-100 border-l-4 border-red-500 text-red-700 p-4">
                    <p>Error: ${error.message}</p>
                </div>
            `;
        } finally {
            submitButton.disabled = false;
            submitButton.textContent = 'Analyze Scan';
            resultDiv.classList.remove('hidden');
        }
    });
}); 