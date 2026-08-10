import datetime
from django.shortcuts import render, get_object_or_404
from .models import Alumnos, Comentario, ComentarioContacto
from .forms import ComentarioContactoForm
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages



# Create your views here.
def registros(request):
    alumnos = Alumnos.objects.all() # all recuperar todos los objetos del modelo (registros de la tabla alumnos)
    comentario = Comentario.objects.all()
    
    return render(request, "registros/principal.html", {'alumnos': alumnos})
    #indicamso el lugar donde se renderiza el resultado de esta vista y enviamos la lista de alumnos recuperados

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            comentarios = ComentarioContacto.objects.all()
            return render(request, 'registros/consultar_comentarios.html', {'comentarios': comentarios})
    form = ComentarioContactoForm()
    #Si sale mal reenvian al formulario los datos ingresados
    return render(request, 'registros/contacto.html', {'form': form})

def contacto(request):
    return render(request, "registros/contacto.html")

def consultar_comentarios(request):
    comentarios = ComentarioContacto.objects.all()

    return render(
        request,
        "registros/consultar_comentarios.html",
        {"comentarios": comentarios}
    )

def eliminarComentarioContacto(request, id, confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request, "registros/consultar_comentarios.html", {'comentarios': comentarios})
    return render(request, confirmacion, {'comentario': comentario})

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save() 
            comentarios = ComentarioContacto.objects.all()
            return render(request, "registros/consultar_comentarios.html", {'comentarios': comentarios})
    return render(request, "registros/editarComentario.html", {'comentario': comentario})

# Vista para consultas.html

def consultas(request):
    alumnos = Alumnos.objects.all() # all recuperar todos los objetos del modelo (registros de la tabla alumnos)
    comentario = Comentario.objects.all()
    
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar1(request):
    alumnos = Alumnos.objects.filter(carrera="TI")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar2(request):
    # Múltiples condiciones adicionando .filter() se analiza como AND
    alumnos = Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar3(request):
    alumnos = Alumnos.objects.all().only("matricula", "nombre", "carrera", "turno", "imagen")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

#Propios, tarea, consultas 4, 5 y 6

def consultar4(request):
    alumnos = Alumnos.objects.all().order_by('nombre')
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar5(request):
    alumnos = Alumnos.objects.filter(nombre__icontains="j")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

#Tarea 2 pdf

def consultar6(request):
    alumnos = Alumnos.objects.filter(nombre__in=["Juan", "Ana"])
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar7(request):
    # Rango amplio para verificar
    fechaInicio = datetime.date(2020, 1, 1)
    fechaFin = datetime.date(2026, 12, 31)
    alumnos = Alumnos.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar8(request):
    alumnos = Alumnos.objects.filter(comentario__coment__icontains='No inscrito')
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultasSQL(request):
    alumnos = Alumnos.objects.raw('SELECT id, matricula, nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

#Tarea 3 Clasroom

# 1. Comentarios creados entre el 20 de junio y 5 de agosto
def consulta_orm_1(request):
    fecha_inicio = datetime.date(2026, 6, 20)
    fecha_fin = datetime.date(2026, 8, 5)
    
    #__date__ antes de __range (tuve problemas con la fecha y hora, por eso lo puse así)
    comentarios = ComentarioContacto.objects.filter(created__date__range=(fecha_inicio, fecha_fin))
    
    return render(request, "registros/consultar_comentarios.html", {'comentarios': comentarios})

# 2. Buscar una expresión en el comentario (ej. palabra 'Hola')
def consulta_orm_2(request):
    comentarios = ComentarioContacto.objects.filter(mensaje__icontains='Hola')
    return render(request, "registros/consultar_comentarios.html", {'comentarios': comentarios})

# 3. Comentarios pertenecientes a un usuario en específico (ej. 'Zaid')
def consulta_orm_3(request):
    comentarios = ComentarioContacto.objects.filter(usuario__icontains='Zaid')
    return render(request, "registros/consultar_comentarios.html", {'comentarios': comentarios})

# 4. Expresión alternativa 1: __startswith (Alumnos cuyos nombres empiezan con 'A')
def consulta_orm_4(request):
    alumnos = Alumnos.objects.filter(nombre__startswith='A')
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

# 5. Expresión alternativa 2: __gt (Alumnos con ID mayor a 2)
def consulta_orm_5(request):
    alumnos = Alumnos.objects.filter(id__gt=2)
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

# 1. SQL: Rango de fechas
def consulta_sql_1(request):
    comentarios = ComentarioContacto.objects.raw(
        "SELECT id, usuario, mensaje, created FROM registros_comentariocontacto WHERE DATE(created) BETWEEN '2026-06-20' AND '2026-08-05'"
    )
    return render(request, "registros/consultar_comentarios.html", {'comentarios': comentarios})

# 2. SQL: Buscar expresión en mensaje
def consulta_sql_2(request):
    comentarios = ComentarioContacto.objects.raw(
        "SELECT id, usuario, mensaje, created FROM registros_comentariocontacto WHERE mensaje LIKE '%%Hola%%'"
    )
    return render(request, "registros/consultar_comentarios.html", {'comentarios': comentarios})

# 3. SQL: Filtrar por usuario
def consulta_sql_3(request):
    comentarios = ComentarioContacto.objects.raw(
        "SELECT id, usuario, mensaje, created FROM registros_comentariocontacto WHERE usuario = 'Zaid'"
    )
    return render(request, "registros/consultar_comentarios.html", {'comentarios': comentarios})

# 4. SQL: Nombres que empiezan con 'A'
def consulta_sql_4(request):
    alumnos = Alumnos.objects.raw(
        "SELECT id, matricula, nombre, carrera, turno, imagen FROM registros_alumnos WHERE nombre LIKE 'A%%'"
    )
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

# 5. SQL: ID mayor que 2
def consulta_sql_5(request):
    alumnos = Alumnos.objects.raw(
        "SELECT id, matricula, nombre, carrera, turno, imagen FROM registros_alumnos WHERE id > 2"
    )
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def archivos(request):
  if request.method == 'POST':
    form = FormArchivos(request.POST, request.FILES)
    if form.is_valid():
      titulo = request.POST.get('titulo')
      descripcion = request.POST.get('descripcion')
      archivo = request.FILES.get('archivo')
      insert = Archivos(
          titulo=titulo, descripcion=descripcion, archivo=archivo
      )
      insert.save()
      return render(request, 'registros/archivos.html')  # 👈 En plural (.html)
    else:
      messages.error(request, 'Error al procesar el formulario.')
  else:
    return render(request, 'registros/archivos.html')  # 👈 En plural (.html)