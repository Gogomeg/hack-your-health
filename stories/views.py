from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm
# Create your views here.


def get_stories_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'stories/stories_list.html', context)


def add_story(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_stories_list')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'stories/add_story.html', context)


def edit_story(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_stories_list')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'stories/edit_story.html', context)


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_stories_list')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_stories_list')
