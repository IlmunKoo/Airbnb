from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
from reviews import models as review_models
from rooms import models as room_models
from users import models as user_models
import random


class Command(BaseCommand):
    help = "This Command creates reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="how many reviews you want to create?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        # 위에서 정의한 인수"number"를 가져오겠다
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(
            review_models.Review,
            number,
            {
                "accuracy": lambda x: random.randint(0, 6),
                "communication": lambda x: random.randint(0, 6),
                "cleanliness": lambda x: random.randint(0, 6),
                "location": lambda x: random.randint(0, 6),
                "check_in": lambda x: random.randint(0, 6),
                "value": lambda x: random.randint(0, 6),
                "room": lambda x: random.choice(rooms),
                "user": lambda x: random.choice(users),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reviews created!"))

