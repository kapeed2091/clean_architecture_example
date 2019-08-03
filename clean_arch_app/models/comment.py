"""
Created on 2019-07-18

@author: kapeed2091
"""
from django.db import models


class Comment(models.Model):
    post = models.ForeignKey('clean_arch_app.Post', on_delete=models.CASCADE)
    content = models.TextField()
    commented_by_id = models.IntegerField()
    commented_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        app_label = 'clean_arch_app'
