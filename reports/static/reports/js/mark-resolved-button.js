document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('mark-resolved-button').addEventListener('click', function() {
        csrf = document.getElementById('csrfmiddlewaretoken').value;
        reportID = document.getElementById('report-id').value;

        fetch(`/reports/mark-report-resolved/${reportID}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrf
            },
            body: JSON.stringify(this.textContent)
        })
        .then(response => response.json())
        .then(() => {
            location.reload();
        })
        .catch(() => {
            document.getElementById('mark-resolved-error-msg').classList.remove('hide');
        });
    });
});