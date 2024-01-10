from rest_framework_simplejwt.authentication import JWTAuthentication

def get_current_authenticated_user(request):
    try:
        authentication = JWTAuthentication()
        user, jwt_token = authentication.authenticate(request)
        return user
    except Exception as e:
        # Handle authentication errors or return None if user is not authenticated
        return None
