from django.core.management.base import BaseCommand
from random import randint
from faker import Faker
from ...models import Program

class Command(BaseCommand):
    help = 'Creates dummy data for the Program model'

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(30):
            Program.objects.create(
                image = fake.image_url(),
                title = fake.word(),
                district = fake.city(),
                ministry = fake.company(),
                deadline_yy = randint(2023, 2024),
                deadline_mm = randint(1, 12),
                deadline_dd = randint(1, 30),
                like = randint(0, 100),
                iflike = fake.boolean()
            )

        self.stdout.write(self.style.SUCCESS('Dummy data created successfully'))