from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker

class Command(BaseCommand):
    help = 'Create 100 fake users'

    def handle(self, *args, **kwargs):
        fake = Faker()
        password = 'defaultpassword'  # La contraseña predeterminada para todos los nuevos usuarios

        for _ in range(100):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            username = fake.user_name()

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )

        self.stdout.write(self.style.SUCCESS('Successfully created 100 users'))
