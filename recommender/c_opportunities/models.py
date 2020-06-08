from django.db import models

# Create your models here.
class ContractOpportunities(models.Model):
    title = models.TextField(help_text='title of notification',
                             verbose_name='Notification',
                             null=True,
                             blank=True
    )
    noticeId = models.TextField(help_text='ID to identify unique notifications',
                                primary_key=True
    )
    department = models.TextField(help_text='name of publishing agency or department',
                             verbose_name='Department',
                             null=True,
                             blank=True
    )
    subTier = models.TextField(help_text='name of publishing department sub-tier',
                             verbose_name='Sub-Tier',
                             null=True,
                             blank=True
    )
    postedDate	= models.DateField(verbose_name='Posted Date')
    deadline = models.DateTimeField(verbose_name='Deadline',
                                    null=True,
                                    blank=True
    )
    link = models.URLField(help_text='link to detailed website',
                           verbose_name='Details')

# class NotificationType(models.Model):
