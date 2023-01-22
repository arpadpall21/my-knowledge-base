from django.shortcuts import render


dummy_todo_list = [
    {'date': 'some_date_1', 'content': 'some_content_1'},
    {'date': 'some_date_2', 'content': 'some_content_2'},
    {'date': 'some_date_3', 'content': 'some_content_3'},
    {'date': 'some_date_4', 'content': 'some_content_4'},
    {'date': 'some_date_5', 'content': 'some_content_5'},
]


def list(req):
    return render(req, 'list/index.html', context={
        'list': dummy_todo_list,
        'nr': 1,
    })
