from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken

class CookieJWTAuthentication(JWTAuthentication):  # HERDANDO DE JWTAuthentication
    def authenticate(self, request):
        token = request.COOKIES.get('access_token')
        if not token:
            return None
        
        try:
            validated_token = self.get_validated_token(token)  # AGORA FUNCIONA
        except InvalidToken:
            return None
        
        return self.get_user(validated_token), validated_token
