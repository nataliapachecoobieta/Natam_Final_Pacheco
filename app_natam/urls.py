

from django.urls import path
from .views import (nuevo_login,
    nuevo_register,
    nuevo_ticket,inicio,
    login2, 
    register,
    ticket,
    login_formulario,
    busqueda_usuario_formulario,
    busqueda_usuario_resultado,
    register_formulario,
    ticket_formulario,
    lista_tickets,
    elimina_ticket,
    editar_ticket,   
    bien,
    Registerlist,
    RegisterDetail,
    RegisterCreate,
    RegisterUpdate,
    RegisterDelete,
 
)

urlpatterns = [
  
    path('inicio/', inicio,name="inicio"),
    path('login/', login2,name="login"),
    path('register/', register,name="register"),
    path('ticket/', ticket,name="ticket"),
    path('login-formulario/',login_formulario,name="loginFormulario"),
    path('register-formulario',register_formulario,name="registerFormulario"),
    path('ticket-formulario',ticket_formulario,name="ticketFormulario"),
    path('Bien/',bien,name="bien"),
    path('busqueda-usuario/',busqueda_usuario_formulario, name="busquedaUsuario"),
    path('busquedaUsuarioResultado/',busqueda_usuario_resultado,name="busquedaUsuarioResultado"),
    path('lista-tickets/',lista_tickets,name="listaTickets"),
    path('eliminar-ticket/<int:id>/',elimina_ticket,name="eliminarTicket"),
    path('editar-ticket/<int:id>/',editar_ticket,name="editarTicket"),
    path('lista-register/',Registerlist.as_view(),name="listarRegister"),
    path('detalle-register/<pk>',RegisterDetail.as_view(),name="detalleRegister"),
    path('crear-register/',RegisterCreate.as_view(),name="crearRegister"),
    path('actualizar-register/<pk>',RegisterUpdate.as_view(),name="actualizarRegiter"),
    path('eliminar-register/<pk>',RegisterDelete.as_view(),name="eliminarRegister"),
]
