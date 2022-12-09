from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


class AppTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self , email, password):
        return (text_type(email)+text_type(password))
    
token_generator = AppTokenGenerator()