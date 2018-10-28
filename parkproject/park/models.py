from company.models import Company
from django.db import models

# Create your models here.



class Park(models.Model):
    park_id = models.AutoField(primary_key=True)
    park_name = models.CharField(max_length=32, null=True, db_index=True)
    updated_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True, db_index=True)

    company = models.ForeignKey(
        'company.Company',
        related_name='park_company',
        on_delete=models.SET_NULL, null=True)

    def detail_info(self):
        return {
            'park_id': self.park_id,
            'park_name': self.park_name,
            'updated_time': str(self.updated_time),
            'created_time': str(self.created_time),
            'park_company': self.company
        }

    class Meta:
        db_table = 'park'