from django.db import models


class Author(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Book(models.Model):

    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

    def __unicode__(self):
        return self.title
