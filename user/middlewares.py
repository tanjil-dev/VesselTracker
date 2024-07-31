from django.shortcuts import redirect
from django.urls import resolve


class AuthenticatedUserRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of URL names to protect
        protected_urls = ['password_reset', 'password_reset_done', 'password_reset_confirm', 'password_reset_complete', 'signup']

        # Get the current URL name
        current_url_name = resolve(request.path_info).url_name

        # Check if the user is authenticated and trying to access a protected URL
        if request.user.is_authenticated and current_url_name in protected_urls:
            return redirect('home')  # Redirect to the desired page for authenticated users

        response = self.get_response(request)
        return response