from django.db import models
class user_reg(models.Model):
    uname=models.CharField(max_length=100)
    uemail=models.CharField(max_length=100)
    uphone=models.CharField(max_length=100)
    upassword=models.CharField(max_length=100)

class menu(models.Model):
    pcode=models.CharField(max_length=100)
    pname=models.CharField(max_length=100)
    pdescription=models.CharField(max_length=3000)
    pqty=models.CharField(max_length=100)
    pprice=models.CharField(max_length=100)
    pfile=models.FileField(max_length=100)

class cart(models.Model):
    urid=models.CharField(max_length=100)
    prcode=models.CharField(max_length=100)
    prname=models.CharField(max_length=100)
    prprice=models.CharField(max_length=100)
    prqty=models.CharField(max_length=100)
    prtprice=models.CharField(max_length=100)
    prfile=models.FileField(max_length=100)





    

