import random
from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):
    help = "This Command creates facilities"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="how many rooms you want to create?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        # 위에서 정의한 인수"number"를 가져오겠다
        seeder = Seed.seeder()
        all_user = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_user),
                "room_type": lambda x: random.choice(room_types),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "guests": lambda x: random.randint(1, 20),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} Rooms created!"))

