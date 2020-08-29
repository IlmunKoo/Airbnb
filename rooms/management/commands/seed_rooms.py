import random
from django.core.management.base import BaseCommand, CommandError
from django.contrib.admin.utils import flatten
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
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()

        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 30)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1, 31)}.webp",
                )
                # 사진을 만든다
            for a in amenities:  # 쿼리셋을 주는 장고 모듈
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:  # 짝수일 때 amenity 추가(다대다필드에서 무언가를 추가하는 방법)
                    room.amenities.add(a)

            # facilities와 rules도 똑같이 해준다.
            # 다대다 필드 다루는 방법!

            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:  # 짝수일 때 amenity 추가(다대다필드에서 무언가를 추가하는 방법)
                    room.facilities.add(f)

            for r in rules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:  # 짝수일 때 amenity 추가(다대다필드에서 무언가를 추가하는 방법)
                    room.house_rules.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number} Rooms created!"))

