import random
from django.core.management.base import BaseCommand, CommandError
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists import models as list_models
from rooms import models as room_models
from users import models as user_models

NAME = "lists"


class Command(BaseCommand):
    help = f"This Command creates {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help=f"how many { NAME } you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        # 위에서 정의한 인수"number"를 가져오겠다
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        room = room_models.Room.objects.all()
        seeder.add_entity(
            list_models.List, number, {"user": lambda x: random.choice(users),},
        )
        created = seeder.execute()
        cleaned = flatten(list(created.values()))
        for pk in cleaned:
            list_model = list_models.List.objects.get(pk=pk)
            to_add = room[random.randint(0, 5) : random.randint(6, 30)]
            list_model.room.add(*to_add)

        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))
