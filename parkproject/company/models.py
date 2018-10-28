from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50, null=True, db_index=True)
    updated_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True, db_index=True)


    class Meta:
        db_table = 'company'

    def detail_info(self):
        return {
            'company_id': self.company_id,
            'company_name': self.company_name,
            'updated_time': str(self.updated_time),
            'created_time': str(self.created_time)
        }