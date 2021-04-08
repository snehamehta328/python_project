from django.db import models

class UserReg(models.Model):
    uname=models.CharField(max_length=100)
    uemail=models.CharField(max_length=100)
    pwd=models.CharField(max_length=100)
    # contactNum=models.IntegerField()

    class Meta:
         db_table="usersignup"


    