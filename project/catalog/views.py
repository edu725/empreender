from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required
def home(request):
    games = Item.objects.all()
    return render(request, 'catalog/home.html', {'games': games})

def index(request):
    games = Item.objects.all()
    data_games = []
    for game in games:
        data_games.append(
            {
                'game': game,
            }
        )
    return render(request, 'catalog/index.html', {'games': data_games})


@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Card cadastrado com sucesso!')
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, 'catalog/add_item.html', {'form': form})

@login_required
def edit_item(request, item_id):
    game = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            form.save()
            messages.success(request, 'Card editado com sucesso!')
            return redirect('home')
    else:
        form = ItemForm(instance=game)
    return render(request, 'catalog/edit_item.html', {'form': form})

@login_required
def delete_item(request, item_id):
    game = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        game.delete()
        messages.success(request, 'Card deletado com sucesso!')
        return redirect('home')
    return render(request, 'catalog/delete_item.html', {'game': game})
