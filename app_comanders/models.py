from django.db import models

# Create your models here.


class Commander(models.Model):
    name = models.CharField(max_length=50,verbose_name='Commander name')
    year = models.IntegerField(verbose_name='Commander year')
    did = models.CharField(max_length=255,verbose_name='Commander did')
    area = models.CharField(max_length=255,verbose_name='Commander area')
    image = models.ImageField(verbose_name='commander image',upload_to='comman_images',default='comman_images/comander.jpeg')


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'commander'
        verbose_name = 'Commander list'
        ordering = ('id',)