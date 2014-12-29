from django.db import models
from django.contrib.auth.models import User 
from django.core.urlresolvers import reverse
import uuid
from django.core import serializers

# Create your models here.

class Person(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=str(uuid.uuid1()))
    first_name = models.CharField(max_length=200, null=False, blank=False)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name   = models.CharField(max_length=200, null=False, blank=False)
    email_address = models.EmailField(blank=False, null=False)

    def full_name(self):
        if self.middle_name == "":
            return "%s %s" % (self.first_name, self.last_name)
        else:
            return "%s %s %s" % (self.first_name, self.middle_name, self.last_name)

    def __str__(self):
        return "%s %s (%s)" % (self.first_name, self.last_name, self.email_address)

    def __unicode__(self):
        return "%s %s (%s)" % (self.first_name, self.last_name, self.email_address)

    def get_absolute_url(self):
        return reverse('person-detail', kwargs={'pk': self.pk})

language = [('en', 'English'),('sp','Spanish')]

class Client(Person):
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    mailing_address = models.CharField(max_length=200, null=True, blank=True)
    city        = models.CharField(max_length=200, null=True, blank=True)
    state       = models.CharField(max_length=20, null=True, blank=True)
    zip_code    = models.IntegerField(null=True, blank=True)
    language    = models.CharField(max_length=2, choices=language, default='en')

class Attorney(models.Model):
    user = models.OneToOneField(User)
    bar_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "%s %s (%s)" % (self.user.first_name, self.user.last_name, self.user.email)

class Matter(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=str(uuid.uuid1()))
    clients = models.ManyToManyField(Client)
    attorneys = models.ManyToManyField(Attorney)
    case_number = models.CharField(max_length=200, unique=True, null=True, blank=True)
    plaintiff = models.CharField(max_length=20, null=True, blank=True)
    defendant = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return "%s v. %s (%s)" % (self.plaintiff, self.defendant, self.case_number)

    def __unicode__(self):
        return "%s v. %s (%s)" % (self.plaintiff, self.defendant, self.case_number)

    def get_absolute_url(self):
        return reverse('matter-detail', kwargs={'pk': self.pk})

class Document(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=str(uuid.uuid1()))
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    language    = models.CharField(max_length=2, choices=language, default='en')
# TODO: 
    # fields = define the fields that need to be added to the document, not sure how to implement this
    document_file = models.FileField()

    def __str__(self):
        return "%s (%s)" % (self.title, self.language)

class Bundle(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=str(uuid.uuid1()))
    matter = models.ForeignKey('Matter')
    documents = models.ManyToManyField(Document)
    # date_created = models.DateTimeField(auto_now_add=True, null=True)