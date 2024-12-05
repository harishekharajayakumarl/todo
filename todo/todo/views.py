from django.http import HttpResponseRedirect
from django.shortcuts import render
from todo.models import Item

def TodoAppView(request):
    all_items = Item.objects.all()
    print(all_items)
    return render(request, 'index.html', {'all_items': all_items, 'ACTION_URL': '/todo/'})

# Adding to list
def AddTodo(request):
    new_item = Item(content=request.POST['content'])
    if request.POST['content'].strip() != '':
        new_item.save()
    return HttpResponseRedirect('/')

# Deletion
def DeleteTodo(_, item_id):
    item_to_delete = Item.objects.get(id=item_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/')

# Edit
def EditTodo(request, item_id):
    all_items = Item.objects.all()
    item_to_edit = Item.objects.get(id=item_id)
    return render(request, 'index.html', {'edit_item': item_to_edit, 'all_items': all_items})

# Updation
def UpdateTodoItem(request, item_id):
    item_to_update = Item.objects.get(id=item_id)
    item_to_update.content = request.POST['content']
    item_to_update.save()
    return HttpResponseRedirect('/')