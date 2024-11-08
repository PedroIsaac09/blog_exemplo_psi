from django.shortcuts import render
from .models import Post, Blog, Mensagem

def index(request):
    context = {
        "posts": Post.objects.all(),
        "blog": Blog.objects.first(),
    }

    return render(request, "index.html", context)

def post(request, post_id):
    context = {
        "post": Post.objects.get(pk=post_id),
        "blog": Blog.objects.first(),

    }

    return render(request, "post.html", context)

def sobre(request):
    context = {
        "blog": Blog.objects.first(),
    }

    return render(request, "about.html", context)

def mensagens(request):
    context = {
        "mensagens": Mensagem.objects.all(),
        "blog": Blog.objects.first(),
    }
    
    return render(request, "mensagem.html", context)

def contato(request):
    context = {
        "blog": Blog.objects.first(),
        
    }



    if request.method == "POST":
        context['error'] = {}
        if not request.POST['nome']:
            context['error']['nome'] = True
        if not request.POST['email']:
            context['error']['email'] = True
        if not request.POST['telefone']:
            context['error']['telefone'] = True
        if not request.POST['mensagem']:
            context['error']['mensagem'] = True
        if context['error']:
            return render(request, "contact.html", context)

        mensagem = Mensagem(nome=request.POST['nome'], email=request.POST['email'], telefone=request.POST['telefone'], mensagem=request.POST['mensagem'], cidade=request.POST['cidade'])
        mensagem.save()

        return render(request, "contact.html", context)
    else:
        return render(request, "contact.html", context)