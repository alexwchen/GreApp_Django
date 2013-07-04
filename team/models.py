from django.db import models

class team_member(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class paragraph(models.Model):
    master_member = models.ForeignKey(team_member)
    title = models.CharField(max_length=200)
    content = models.TextField()
    def __unicode__(self):
        return self.title
