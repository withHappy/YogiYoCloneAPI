from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    star = models.FloatField()
    notification = models.TextField()
    opening_hours = models.CharField(max_length=20)
    tel_number = models.CharField(max_length=40)
    address = models.CharField(max_length=50)
    min_order = models.PositiveIntegerField()
    payment_method = models.CharField(max_length=50)
    business_name = models.CharField(max_length=20)
    company_registration_number = models.CharField(max_length=20)
    origin_information = models.TextField()


class MenuGroup(models.Model):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    name = models.CharField(max_length=40)


class Menu(models.Model):
    menu_group = models.ForeignKey('MenuGroup', on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='menu_image', null=True, blank=True)
    caption = models.CharField(max_length=200)
