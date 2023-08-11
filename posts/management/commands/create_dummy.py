from django.core.management.base import BaseCommand
from random import randint
from faker import Faker
from ...models import Program, Category

class Command(BaseCommand):
    help = 'Creates dummy data for the Program model'

    def handle(self, *args, **options):
        fake = Faker()

        categories = ['Category 1', 'Category 2', 'Category 3']
        for category_name in categories:
            Category.objects.get_or_create(detail_category=category_name)

        for _ in range(30):
            program = Program.objects.create(
                image = fake.image_url(),
                title = fake.word(),
                district = fake.city(),
                agency = fake.company(),
                deadline_yy = randint(2023, 2024),
                deadline_mm = randint(1, 12),
                deadline_dd = randint(1, 30),
                like = randint(0, 100),
                iflike = fake.boolean(),
            )

            selected_categories = Category.objects.order_by('?')[:2]
            program.category.set(selected_categories)

        self.stdout.write(self.style.SUCCESS('Dummy data created successfully'))
