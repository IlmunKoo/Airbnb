from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
from users.models import User


class Command(BaseCommand):
    help = "This Command creates many users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="how many users do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        # 위에서 설정한 인수를 받아 온다.
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created!"))
