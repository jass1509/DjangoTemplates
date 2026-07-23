from django.shortcuts import render

def welcome_view(request):
    # Reemplaza esta URL con el enlace real de tu Frontend desplegado (ej. Vercel, Netlify, Github Pages)
    FRONTEND_URL = "https://tu-frontend-devjobs.vercel.app" 

    context = {
        'frontend_url': FRONTEND_URL,
    }
    return render(request, 'index.html', context)