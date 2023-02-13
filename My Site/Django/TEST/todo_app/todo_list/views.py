from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


dummy_todo_list = [
    {'date': 'some_date_1', 'content': 'some_content_1'},
    {'date': 'some_date_2', 'content': 'some_content_2'},
    {'date': 'some_date_3', 'content': 'some_content_3'},
    {'date': 'some_date_4', 'content': 'some_content_4'},
    {'date': 'some_date_5', 'content': 'some_content_5'},
]


def list(req):
    return render(req, 'todo_list/index.html', context={
        'list': dummy_todo_list,
        'nr': 1,
    })


def register(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(req, f'Account created form {username}')
    else:
        form = UserCreationForm()
    
    return render(req, 'todo_list/register_user.html', {'form': form, 'test': 'test'})

