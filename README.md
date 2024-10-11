Hola, Natam es una empresa de aeronáutica que esta recién partiendo, sus directores nos encomendaron la tarea de crear su página web, pues hoy hacemos la primera entrega visible del proyecto se debe considerar que esta está en construcción y por ahora estamos demostrando una pequeña parte de su diseño y funcionalidad principalmente. En la página se encuentran 4 botones en la parte superior INICIO, LOG IN , REGISTRATE Y TICKETS.

¿Dónde se redirigen cada botón creado? Inicio: /app-natam/inicio/ , página inicial LOG IN : /app-natam/login-formulario/, se redirige al formulario para que la persona ingrese al sitio web. Regístrate: /app-natam/register-formulario: se redirige a el formulario para ingrese sus datos. Tickets : /app-natam/ticket-formulario: en este formulario un usuario podrá ingresar los datos de su ticket

Formularios de búsqueda En el caso del LOGIN podemos hacer búsqueda del username : El cliente al hacer el login los datos estos se guardan, al escribir busqueda-usuario/ en el url , este se redirige y en la mis pantalla nos avisa si este username se encuentra en los registros o no… Ceeelente .

A continuacion estan los links que son vastante intiutivo a lo que redirigen y contienen

path('inicio/', inicio,name="inicio"),
path('login/', login_formulario, name="login"),

path('register/', register,name="registerf"),
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
path('',RegisterDelete.as_view(),name="eliminarRegister"),
Espero sea de ayuda …. Sabemos que es solo el comienzo y falta por terminar, pero estamos muy satisfechos con los primeros resultados

En Natam , Nos encanta codiar 😊

A continuacion dejo el link del fucionamiento de la pagina https://www.loom.com/share/d2590f28c84f4fc0bad633c991cd3ea4

About
No description, website, or topics provided.
Resources
 Readme
 Activity
Stars
 0 stars
Watchers
 1 watching
Forks
 0 forks
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Languages
CSS
88.2%
 
Python
6.4%
 
HTML
5.3%
 
JavaScript
0.1%
Suggested workflows
Based on your tech stack
Python package logo
Python package
Create and test a Python package on multiple Python versions.
Python application logo
Python application
Create and test a Python application.
Publish Python Package logo
Publish Python Package
Publish a Python Package to PyPI on release.
More workflows
Footer
© 2024 GitHub, Inc.
