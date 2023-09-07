from django.db import models



class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birthdate = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.full_name





class Report(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return str(self.id)


