from django.shortcuts import render, HttpResponse

# Create your views here.
def principal(request):
    contexto = {
        "user_text": "lajlskdjaslk",
        "user_subtext": "DGS",
        "user_img": "inicio/images/home.png"}
    return render(request, "registros/principal.html", contexto)

def nuevo(request):
    contexto = {
        "user_text": "Yo",
        "user_subtext": "DGS",
        "user_img": "inicio/images/yo.png"
    }
    return render(request, "inicio/nuevo.html", contexto)

def contacto(request):
    contexto = {
        "user_text": "Contacto",
        "user_subtext": "DGS",
        "user_img": "inicio/images/registrar.png"
    }
    return render(request, "inicio/contacto.html", contexto)

def formulario(request):
    contexto = {
            "user_text": "Registro",
            "user_subtext": "DGS",
            "user_img": "inicio/images/regis.png"
        }
    return render(request, "inicio/formulario.html", contexto)

def ejemplo(request):
    return render(request, "inicio/ejemplo.html")