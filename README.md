# todo_list
Simple todo list app that automatically categorizes todo list items based on the word2vec distance of the keywords linked to a certain category and vocabulary words in the todo item.

# Install instructions
1) (optional) create and activate virtualenv
2) `pip3 install -r requirements.txt`
3) Download word2vec model https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit and unzip in todolist/todo_site
4) `cd todo_site`
5) `python3 manage.py runserver`
6) go to http://127.0.0.1:8000/todo_django_app
