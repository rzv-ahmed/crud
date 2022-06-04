from django.db import models

class stu_form(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField()
    phnne=models.IntegerField()

    def __str__(self):
        return str(self.pk)+" "+self.fname+" "+self.lname
