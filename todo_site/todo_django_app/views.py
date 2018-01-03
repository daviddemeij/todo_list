from .todo import todo_app


from django.http import HttpResponse
from django.template import loader

from .forms import todoForm
todo_list = todo_app()
todo_list.add(["Print important documents", "Fitness training", "Cinema", "Read year report", "update finances", "invite mom and dad for dinner", "crossfit", "plan holiday"])

def index(request):
    template = loader.get_template('index.html')
    if request.GET.get('remove'):
        todo_list.remove(str(request.GET.get('remove')))
    if request.method == 'POST':
        form = todoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.keys())
            todo_list.add(form.cleaned_data['todo'])
    else:
        form = todoForm()
    context = {
        'todo_lists': todo_list.todo_lists,
        'form': form
    }

    return HttpResponse(template.render(context, request))
