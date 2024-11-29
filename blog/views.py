from django.shortcuts import render, redirect, get_object_or_404
from django.forms.models import model_to_dict
from .models import Post, Blog, Mensagem
from .forms import Mensagemform

def index(request):
    context = {
        "posts": Post.objects.all(),
        "blog": Blog.objects.first(),
    }

    return render(request, "index.html", context)

def post(request, post_id):
    context = {
        "post": get_object_or_404(Post, pk=post_id),
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
        form = Mensagemform(request.Post)
        if form.is_valid():
            mensagem = Mensagem(
                nome = form.cleaned_data("nome"),
                email = form.cleaned_data("email"),
                telefone = form.cleaned_data("telefone"),
                mensagem = form.cleaned_data("mensagem"),
                cidade = form.cleaned_data("cidade"),
            )
            mensagem.save()
            
        return redirect("mesagens")
    else:
        context["form"] = Mensagemform()
        return render(request, "contact.html", context)
    
def editar_mensagem(request, mensagem_id):
    mensagem: get_object_or_404(Mensagem, pk=mensagem_id)
    context = {
        "blog": Blog.objects.first(),
        "form": Mensagemform(initial=model_to_dict(mensagem))
        
    }

    if request.method == "POST":
        form = Mensagemform(request.Post)
        if form.is_valid():
            mensagem.nome = form.cleaned_data("nome")
            mensagem.email = form.cleaned_data("email")
            mensagem.telefone = form.cleaned_data("telefone")
            mensagem.mensagem = form.cleaned_data("mensagem")
            mensagem.cidade = form.cleaned_data("cidade")
            mensagem.save()
        return redirect("mesagens")

    return render(request, "contact.html", context)

def deletar_mensagem(request, mensagem_id):
    context = {
        "blog": Blog.objects.first(),
        "mensagem": get_object_or_404(Mensagem, pk=mensagem_id),
    }

    if request.method == "POST":
        context["mensagem"].delete()
        return redirect('mensagem')
    else:
        return render(request, "delete.html", context)
    

