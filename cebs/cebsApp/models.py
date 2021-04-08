from django.db import models

class UserReg(models.Model):
    uname=models.CharField(max_length=100)
    uemail=models.CharField(max_length=100)
    pwd=models.CharField(max_length=100)
    # contactNum=models.IntegerField()

    class Meta:
         db_table="usersignup"
    # def __str__(self):
    #     return self.uname

    

# class Tag(models.Model):
# 	uname = models.CharField(max_length=200, null=True)

# 	def __str__(self):
# 		return self.uname

    