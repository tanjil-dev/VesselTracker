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

$(document).ready(()=>{

  $('#open-sidebar').click(()=>{

      // add class active on #sidebar
      $('#sidebar').addClass('active');

      // show sidebar overlay
      $('#sidebar-overlay').removeClass('d-none');

   });


   $('#sidebar-overlay').click(function(){

      // add class active on #sidebar
      $('#sidebar').removeClass('active');

      // show sidebar overlay
      $(this).addClass('d-none');

   });

});


table = $('#myTable2').DataTable();
table = $('#myTable3').DataTable();

var base_url = "http://0.0.0.0:8000/api/v1";

$(document).ready(function () {
    // CSRF token setup
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

var table = $('#myTable1').DataTable({
        autoWidth: false,
        scrollX: true,
        pageLength: 5,
        ajax: {
        url: `${base_url}/vessel/`,
        type: "GET",
        cache: true,
        success: function (response) {
            table.clear().rows.add(response.data).draw();
        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.error('Error loading data:', errorThrown);
        }
    },
        columns: [
            { data: 'name' },
            { data: 'owner_id' },
            { data: 'naccs_code' },
            {
                data: null,
                className: "center",
                defaultContent: '<div class="btn-group">' +
                    '<button class="btn btn-sm btn-secondary edit-btn">Update</button>' +
                    '<button class="btn btn-sm btn-dark delete-btn">Delete</button>' +
                    '</div>',
                orderable: false,
            }
        ],
    });
});