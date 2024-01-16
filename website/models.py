from django.db import models

# Create your models here.


SUBJECT = (
    ('ERP SOLUTIONS', 'Erp Solutions'),
    ('WEBSITE DEVELOPMENT', 'Website Development'),
    ('ECOMMERCE', 'E-Commerce'),
    ('MOBILE APP', 'Mobile App Development'),
    ('DIGITAL MARKETING', 'Digital Marketing'),
)


class ContactUs(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=150, choices=SUBJECT)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name