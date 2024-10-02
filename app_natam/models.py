from django.db import models

# Create your models here Login, register, Ticket

class login (models.Model):

    username = models.CharField (max_length= 50)
    password = models.CharField (max_length= 50)


class register (models.Model):
    name = models.CharField (max_length= 50)
    lastName = models.CharField (max_length= 50)
    rut =models.CharField (max_length= 15)
    email = models.EmailField (max_length= 50)
    phone = models.CharField (max_length= 50)
    birth_day = models.DateField( null= True )

class Ticket (models.Model):
    flight_number = models.CharField (max_length= 15)
    name_passenger = models.CharField (max_length= 30)
    lastName_passenger  = models.CharField (max_length= 15)
    fligt_date = models.DateField ()
    fligh_time = models.TimeField()
    gate = models.CharField (max_length= 10)
    origin = models.CharField (max_length= 15)
    destination =models.CharField (max_length= 15)

    def __str__(self):
        return f'{self.flight_number}   {self.name_passenger} {self.lastName_passenger}'
        







