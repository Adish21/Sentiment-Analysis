document.querySelector('.upload-box input').addEventListener('change', function(event) {
    const fileName = event.target.files[0] ? event.target.files[0].name : 'No file chosen';
    alert('Selected file: ' + fileName);
});