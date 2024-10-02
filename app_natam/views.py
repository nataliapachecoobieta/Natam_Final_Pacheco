from django.shortcuts import redirect
from django.shortcuts import render
from. models import login,register,Ticket
from.forms import  TicketFormulario
from django .contrib.auth.forms import AuthenticationForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView,UpdateView,CreateView


from django .http import HttpResponse
# Create your views here.

def nuevo_login(req,username, password ):

    nuevo_login = login(username=username ,password =password)
    nuevo_login.save()

    return HttpResponse("""<p> Login:{nuevo_login.username} - Password {nuevo_login.password} creado con exito </p> 
    """)

def nuevo_register(req,name,lastName,rut,email,phone,birth_day):

        nuevo_register = register (name=name,lastName =lastName,rut=rut,email=email,phone=phone,birth_day=birth_day)
        nuevo_register.save()
        
        return HttpResponse("""<p> Registro:{nuevo_register.name} -  {nuevo_register.lastName}- {nuevo_register.rut} - {nuevo_register.email} - {nuevo_register.phone}- {nuevo_register.birth_day} creado con exito </p> 
        """)



def nuevo_ticket(req,flight_number,name_passenger,lastName_passenger,fligt_date, fligh_time,gate, origin, destination):

        nuevo_ticket = Ticket (
               flight_number=flight_number,
               name_passenger=name_passenger,
               lastName_passenger=lastName_passenger,
               fligt_date=fligt_date,
               fligh_time=fligh_time,
               gate=gate,
               origin=origin,
               destination=destination
            )
        nuevo_ticket.save()
        
        return HttpResponse("""<p> Ticket:{nuevo_ticket.flight_number} -  {nuevo_register.name_passenger}- {nuevo_register.lastName_passenger} - {nuevo_ticket.fligt_date} - {nuevo_ticket.fligh_time}- 
                            {nuevo_ticket.gate}-{nuevo_ticket.origin}-{nuevo_ticket.destination} creado con exito </p> 
        """)

def inicio (req):
       return render (req,"inicio.html")


def login2 (req):
       return render (req,"login.html ")
       


def ticket(req):
        return render (req, "ticket.html")


def bien(req):
        return render (req, "bien.html")



def login_formulario(req):
    print (req.POST)
       
    if req.method =='POST':
        nuevo_login = login(username=req.POST["username"], password=req.POST["password"])
        nuevo_login.save()

        return render(req,"bien.html",{})
    else:

       return render (req,"login_formulario.html",{})
    

def busqueda_usuario_formulario(req):
      return render (req,"busqueda_usuario.html")


# def busqueda_usuario_resultado (req):
#       return HttpResponse (f'Buscando usuario {req.GET["usuario"]}')




def busqueda_usuario_resultado(req):

    username = req.GET.get("usuario")

    username = login.objects.filter (username=username)

    if username:
      
        return render(req,"Usuario_Encontrado.html",{"Username":username})
    else:

        return render(req, "Usuario_NoEncontrado.html")
    

    
def register_formulario(req):
    print (req.POST)
       
    if req.method =='POST':
            nuevo_register = register (name=req.POST["name"],  
            lastName =req.POST["lastName"],
            rut =req.POST["rut"],
            email =req.POST["email"],
            phone =req.POST["phone"],
            birth_day =req.POST["birth_day"])

            nuevo_register.save()

            return render(req,"bien.html",{})
    else:

            return render (req,"register_formulario.html",{})
    

def ticket_formulario(req):
    print ('method', req.POST)
    print ('data',req.POST)
       
    if req.method =='POST':

        mi_formulario = TicketFormulario(req.POST)
        if mi_formulario.is_valid ():
            
            
             data = mi_formulario.clean_data


        nuevo_ticket = Ticket (
            flight_number =req.POST["flight_number"], 
            name_passenger=req.POST["name_passenger"],
            lastName_passenger=req.POST["lastName_passenger"],
            fligt_date =req.POST["flight_date"],
            fligh_time=req.POST["flight_time"],
            gate=req.POST["gate"],
            origin=req.POST["origin"],
            destination=req.POST["destination"]


    
        )

        nuevo_ticket.save()
        
        
        tickets = Ticket.objects.all ()

        return render(req,"leer_tickets.html",{"tickets":tickets})
    else:

         return render (req,"ticket_formulario.html",{})


def lista_tickets(req):

 tickets = Ticket.objects.all ()
 return render (req,"leer_tickets.html",{"tickets":tickets})


def elimina_ticket (req,id):
     
     if req.method =='POST':
          
          ticket = Ticket.objects.get (id=id)
          ticket.delete ()

          tickets = Ticket.objects.all ()

          return render (req,"leer_tickets.html",{"tickets":tickets})
     


def editar_ticket(req, id):
    # Obtener el ticket específico
    ticket = Ticket.objects.get(id=id)
    
    if req.method == 'POST':
        mi_formulario = TicketFormulario(req.POST)
        
        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data
            
            # Actualizar los datos del ticket existente
            ticket.flight_number = data['flight_number']
            ticket.name_passenger = data['name_passenger']
            ticket.lastName_passenger = data['lastName_passenger']
            ticket.fligt_date = data['fligt_date']
            ticket.fligh_time = data['fligh_time']
            ticket.gate = data['gate']
            ticket.origin = data['origin']
            ticket.destination = data['destination']
            
            # Guardar cambios en el ticket
            ticket.save()
            
            # Redirigir a la vista de tickets después de editar
            tickets = Ticket.objects.all()
            return render(req, "leer_tickets.html", {"tickets": tickets})
    
    else:
        print(ticket)
        # Pre-popular el formulario con los datos actuales del ticket
        mi_formulario = TicketFormulario(initial={
             
            "flight_number": ticket.flight_number,
            "name_passenger": ticket.name_passenger,
            "lastName_passenger": ticket.lastName_passenger,
            "fligt_date": ticket.fligt_date,
            "fligh_time": ticket.fligh_time,
            "gate": ticket.gate,
            "origin": ticket.origin,
            "destination": ticket.destination,
        })
        
        # Mostrar el formulario de edición
        return render(req, "editar_ticket.html", {"mi_formulario": mi_formulario,"id":ticket.id})


class Registerlist(ListView):
     
     model = register
     template_name = 'register_list.html'
     context_object_name ='registers'

class RegisterDetail (DetailView):
     
    model = register
    template_name = 'register_detail.html'
    context_object_name ='register'

class RegisterCreate(CreateView):
     
    model = register
    template_name = 'register_create.html'
    fields= ['name','lastName','rut','email','phone','birth_day']
    success_url = '/app-natam/Bien'

class RegisterUpdate (UpdateView):

    model = register
    template_name = 'register_update.html'
    fields= ('__all__')
    success_url =  '/app-natam/Bien'
    context_object_name ='register'

class RegisterDelete(DeleteView):
     model=register
     template_name = 'register_delete.html'
     success_url = '/app-natam/inicio'
     context_object_name ='register'












