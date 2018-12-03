import jwt
from django.db import models
from flask import current_app
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta

# Create your models here.


class CustomUser(models.Model):
    user_id = models.IntegerField(primary_key=True, unique=True, blank=False, auto_created=True)
    user_email = models.CharField(max_length=256, unique=True, null=False)
    user_password = models.CharField(max_length=256, null=False)

    def __init__(self, email, password):
        self.user_email = email
        self.user_password - Bcrypt().generate_password_hash(password).decode()

    def password_is_valid(self, password):
        return Bcrypt().check_password_hash(self.user_password, password)

    def generate_token(self, user_id):
        try:
            payload: {
                'exp': datetime.utcnow() + timedelta(minutes=5),
                'iat': datetime.utcnow(),
                'sub': user_id
            }

            jwt_string = jwt.encode(
                payload,
                current_app.config.get('SECRET'),
                algorithm='HS256'
            )
            return jwt_string

        except Exception as e:
            return str(e)

    @staticmethod
    def decode_toke(token):
        try:
            payload = jwt.decode(token, current_app.config.get('SECRET'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Expired token, Please login again'
        except jwt.InvalidTokenError:
            return 'Invalid Token, Please register or login'


class Appointment(models.Model):
    appointment_id = models.IntegerField(blank=False, unique=True)
    appointment_date = models.DateTimeField(auto_now=False)
    appointment_user = CustomUser.username
