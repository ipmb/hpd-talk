import datetime
import random

from faker import Faker
from hpd.demo import models

FAKE = Faker()

def fake_profile():
    profile = FAKE.profile()
    company, _ = models.Company.objects.get_or_create(
        name=profile['company'])
    title, _ = models.JobTitle.objects.get_or_create(
        name=profile['job'])
    profile = models.Profile.objects.create(
        name=profile['name'],
        address=profile['residence'],
        email=profile['mail'],
        company=company,
        title=title,
        website=profile['website'][0],
        birthday=datetime.datetime.strptime(profile['birthdate'],
                                            '%Y-%m-%d').date(),
        bio=FAKE.text(random.randint(2000, 5000))
    )
    return profile
