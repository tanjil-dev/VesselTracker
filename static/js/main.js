function togglePasswordVisibility(elementId, iconId) {
            var passwordField = document.getElementById(elementId);
            var icon = document.getElementById(iconId);
            if (passwordField.type === "password") {
                passwordField.type = "text";
                icon.classList.remove("fa-eye");
                icon.classList.add("fa-eye-slash");
            } else {
                passwordField.type = "password";
                icon.classList.remove("fa-eye-slash");
                icon.classList.add("fa-eye");
            }
}

// Function to hide alerts after a specified timeout
document.addEventListener("DOMContentLoaded", function() {
    var alertElements = document.querySelectorAll('.alert');
    alertElements.forEach(function(alert) {
        // Set timeout to hide the alert after 5 seconds (5000 milliseconds)
        setTimeout(function() {
            // Add fade-out class (or manually hide the element)
            alert.classList.remove('show');
            alert.classList.add('hide'); // Assuming you have a CSS class to hide elements
            // Alternatively, you can use alert.style.display = 'none'; to hide the element directly
        }, 30000); // 5000 milliseconds = 5 seconds
    });
});