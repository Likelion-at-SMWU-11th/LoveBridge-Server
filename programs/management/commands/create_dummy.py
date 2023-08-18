from django.conf import settings
from django.core.management.base import BaseCommand
from random import randint, sample
from faker import Faker
from ...models import *
import random
import os

class Command(BaseCommand):
        help = 'Creates dummy data for the Program model'

        def handle(self, *args, **options):
                fake = Faker()

                Program.objects.all().delete()
                MyProgram.objects.all().delete()

                static_image_path = os.path.join(settings.BASE_DIR, 'media/programs/images')
                image_filenames = sorted(os.listdir(static_image_path))

                title = ['꽃꽂이 체험반', '비누만들기 체험반', '필라테스 체험반', '필라테스 성인반', '수영 성인반', '바이올린 체험반', '플룻 체험반', '첼로 체험반', 
                        '피아노 체험반', '줄넘기 청소년반', '태권도 청소년반', '바리스타 자격증', '바리스타 자격증', '바리스타 자격증', '바리스타 자격증', '댄스 자격증',
                        '바리스타 자격증', '캘리스라피자격증', '영어 자격증', '영어 자격증', '중국어 자격증', '야외 운동 심리치료', '실내 운동 심리치료', '클래식과 함께하는 심리치료',
                        '재즈와 함께하는 심리치료', '음악감상표현 심리치료', '꽃꽂이 체험', '카페 창업', '카페 창업', '카페 창업']
                
                categories = [['취미', '체험'], ['취미', '체험'], ['취미', '운동'], ['취미', '운동'], ['취미', '운동'], ['체험', '운동'], ['체험', '음악'], ['체험', '음악'],
                                ['체험', '음악'], ['체험', '음악'], ['체험', '운동'], ['체험', '운동'], ['자격증', '초급'], ['자격증', '초급'], ['자격증', '초급'], ['자격증', '초급'],
                                ['자격증', '초급'], ['자격증', '초급'], ['자격증', '중급'], ['자격증', '중급'], ['자격증', '중급'], ['운동', '심리'], ['운동', '심리'], ['음악', '심리'],
                                ['음악', '심리'], ['음악', '심리'], ['취미', '체험'], ['창업', '자격증'], ['창업', '자격증'], ['창업', '자격증']]
                
                district = ['서울특별시 강남구', '서울특별시 도봉구', '서울특별시 중랑구', '서울특별시 서초구', '서울특별시 서초구', '서울특별시 영등포구', '서울특별시 노원구', '서울특별시 강남구',
                                '대구광역시 달서구', '부산광역시 해운대구', '대전광역시 동구', '대전광역시 북구', '부산광역시 북구', '인천광역시 부평구', '인천광역시 미추홀구', '서울특별시 은평구',
                                '서울특별시 종로구', '서울특별시 광진구', '서울특별시 중랑구', '서울특별시 광진구', '서울특별시 중랑구', '서울특별시 서초구', '대구광역시 북구', '부산광역시 북구',
                                '서울특별시 도봉구', '서울특별시 영등포구', '서울특별시 용산구', '서울특별시 은평구', '서울특별시 서초구', '서울특별시 종로구']
                
                agency = ['행복한가족복지관', '미소나눔복지관', '다함께행복센터', '희망나눔복지원', '따뜻한마음복지관', '고마운도움복지관', '사랑나눔복지센터', '사랑의복지관',
                        '함께하는복지관', '행복한나눔복지관', '미래희망복지관', '열린마음복지센터', '행복한일상복지관', '믿음과희망의복지관', '자립과행복복지관', '소망복지관',
                        '따뜻한사랑복지관', '미소복지관', '행복복지센터', '씨앗복지관', '새싹복지관', '함께하는복지관', '사랑의복지관', '행복한일상복지관',
                        '미소와행복복지관', '소망복지관', '드림복지관', '자립과행복복지관', '힘찬일상복지원', '무지개복지관']
                
                year = [2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023,
                        2023, 2023, 2023, 2024, 2023, 2024, 2023, 2023,
                        2023, 2023, 2023, 2023, 2023, 2024, 2023, 2024,
                        2023, 2023, 2023, 2023, 2023, 2023]

                month = [9, 10, 11, 9, 8, 12, 8, 11, 
                        9, 9, 9, 1, 9, 1, 8, 8,
                        10, 9, 11, 8, 9, 2, 11, 1,
                        12, 9, 9, 10, 11, 12]
                
                day = [23, 12, 5, 6, 25, 19, 27, 9,
                        12, 16, 4, 6, 26, 8, 30, 31,
                        12, 6, 24, 30, 18, 24, 6, 9,
                        25, 8, 7, 4, 13, 6]
                
                phone = ['010-5165-8656', '010-1984-1565', '010-9521-1498', '010-6655-2035', '010-4957-1204', '02-151-9841', '02-982-1482', '010-1652-1852',
                        '053-955-2665', '010-1952-8890', '010-6515-0955', '010-1951-0652', '010-6510-9522', '010-6557-1015', '010-1765-5621','02-152-6519',
                        '02-985-1656', '010-9517-9513', '010-7957-2620', '010-9123-9810', '02-985-9072', '010-0824-9512', '010-5147-6051', '010-9517-6581',
                        '02-517-6510', '010-6528-0151', '010-9510-1192', '010-9417-9063', '02-984-9805', '010-3928-0651']
                
                number = [10, 15, 20, 30]

                for i, image_filename in enumerate(image_filenames):
                        program = Program.objects.create(
                                image = f'programs/images/{image_filename}',
                                title = title[i],
                                district = district[i],
                                agency = agency[i],
                                deadline_yy = year[i],
                                deadline_mm = month[i],
                                deadline_dd = day[i],
                                phone = phone[i],
                                like = randint(0, 100),
                                iflike = False,
                                category1 = categories[i][0],
                                category2 = categories[i][1],
                                applicant = random.choice(number),
                        )
        
                # programs = MyProgram.objects.all()
                # my_programs = sample(list(programs), 4)

                # for program in programs:
                #     MyProgram.objects.create(
                #         program = program,
                #         process = '서류전달'
                #     )
                
                # my_likes = sample(list(programs), 5)

                # for program in my_likes:
                #     MyLike.objects.create(
                #         program = program,
                #     )
                self.stdout.write(self.style.SUCCESS('Dummy data created successfully'))