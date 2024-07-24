from django.db import models

# Create your models here.
class GeneralInfo(models.Model):
    company_name = models.CharField(max_length=125, default='Company Name')
    company_logo = models.ImageField(upload_to='media/uploads/company_logo', blank=True, null=True)
    company_address = models.CharField(max_length=99, blank=True, null=True)
    company_phone = models.CharField(max_length=25, blank=True, null=True)
    company_email = models.EmailField(blank=True, null=True)
    company_website = models.URLField(blank=True, null=True)
    company_facebook = models.URLField(blank=True, null=True)
    company_twitter = models.URLField(blank=True, null=True)
    company_linkedin = models.URLField(blank=True, null=True)
    company_instagram = models.URLField(blank=True, null=True)
    company_youtube = models.URLField(blank=True, null=True)
    company_tiktok = models.URLField(blank=True, null=True)
    company_about = models.TextField(blank=True, null=True)
    company_mission = models.TextField(blank=True, null=True)
    company_vision = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'General Informations'
        
    def __str__(self):
        return self.company_name