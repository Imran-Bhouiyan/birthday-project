from django.db import models



class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    birthdate = models.DateField()


class Report(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    