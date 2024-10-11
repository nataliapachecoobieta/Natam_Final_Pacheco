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

    #username = models.CharField (max_length= 50)
    #password = models.CharField (max_length= 50)

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
        


# class Flight(models.Model):
#     airline = models.CharField(max_length=50)
#     flight_number = models.CharField(max_length=10)
#     origin = models.CharField(max_length=50)
#     destination = models.CharField(max_length=50)
#     departure_time = models.DateTimeField()
#     arrival_time = models.DateTimeField()
#     capacity = models.IntegerField()

#     def __str__(self):
#         return f"{self.airline} - {self.flight_number}"

# class Booking(models.Model):
#     user = models.ForeignKey('register', on_delete=models.CASCADE)
#     flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
#     booking_date = models.DateTimeField(auto_now_add=True)
#     passengers = models.IntegerField()
#     seat_class = models.CharField(max_length=20, choices=[('Economy', 'Economy'), ('Business', 'Business')])
#     status = models.CharField(max_length=20, default='Confirmed')

#     def __str__(self):
#         return f"Reserva de {self.user.name} para vuelo {self.flight.flight_number}"

# class Airport(models.Model):
#     name = models.CharField(max_length=100)
#     city = models.CharField(max_length=50)
#     country = models.CharField(max_length=50)
#     iata_code = models.CharField(max_length=3, unique=True)

#     def __str__(self):
#         return f"{self.name} ({self.iata_code})"








