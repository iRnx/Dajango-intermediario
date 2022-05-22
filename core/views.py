from django.shortcuts import render
from django.contrib import messages

from .forms import ContatoForm


def index(request):
    return render(request, 'index.html')


def contato(request):
    form = ContatoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.send_mail()

            messages.success(request, 'Mensagem enviada com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar o e-mail')

    return render(request, 'contato.html', {'form': form})


def produto(request):
    return render(request, 'produto.html')
