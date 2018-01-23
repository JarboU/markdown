from __future__ import unicode_literals

from django.db import models


class UpFile(models.Model):
    up_file = models.FileField(upload_to='upload/')

    def __unicode__(self):
        return self.up_file
