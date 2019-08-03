"""
Created on 2019-07-18

@author: kapeed2091
"""
from django.db import models


class Post(models.Model):
    content = models.TextField()
    created_by_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        app_label = 'clean_arch_app'
