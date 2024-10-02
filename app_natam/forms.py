from django import forms
from django.db import models



class TicketFormulario (forms.Form):
    
    flight_number = forms.CharField ()
    name_passenger = forms.CharField ()
    lastName_passenger  = forms.CharField ()
    fligt_date =forms.DateField ()
    fligh_time = forms .TimeField()
    gate = forms.CharField ()
    origin = forms.CharField ()
    destination =forms.CharField ()