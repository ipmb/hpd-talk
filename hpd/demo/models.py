from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    company = models.ForeignKey('demo.Company')
    title = models.ForeignKey('demo.JobTitle')
    website = models.URLField()
    birthday = models.DateField()
    bio = models.TextField()

    def shared_birthday(self, count=20):
        return (Profile.objects.filter(birthday__month=self.birthday.month,
                                       birthday__day=self.birthday.day)
                               .exclude(pk=self.pk))[:count]

    @models.permalink
    def get_absolute_url(self):
        return ('profile', (), {'pk': str(self.pk)})

class Company(models.Model):
    name = models.CharField(max_length=255)

    @models.permalink
    def get_absolute_url(self):
        return ('company', (), {'pk': str(self.pk)})

class JobTitle(models.Model):
    name = models.CharField(max_length=255)

    @models.permalink
    def get_absolute_url(self):
        return ('jobtitle', (), {'pk': str(self.pk)})
