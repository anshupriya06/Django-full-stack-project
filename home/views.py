from django.shortcuts import render, get_object_or_404, redirect
from .models import home
from .forms import homeform

def index(request):
    return render(request, 'index.html')

def item_list(request):
    items = home.objects.all().order_by('-created_at')
    return render(request, 'item_list.html', {'items': items})

def item_create(request):
    if request.method == "POST":
        form = homeform(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('item_list')
    else:
        form = homeform()
    return render(request, 'item_form.html', {'form': form})

def item_edit(request, item_id):
    item = get_object_or_404(home, pk=item_id, user=request.user)
    if request.method == 'POST':
        form = homeform(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('item_list')
    else:
        form = homeform(instance=item)
    return render(request, 'item_form.html', {'form': form})

def item_delete(request, item_id):
    item = get_object_or_404(home, pk=item_id, user=request.user)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'item_confirm_delete.html', {'item': item})


