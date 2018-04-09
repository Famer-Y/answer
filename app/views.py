from django.shortcuts import render
from django.http import HttpResponse
from app.models import User, Book, Subject

# Create your views here.
def register(request):
    if request.session.get('is_login', None):
        return render(request, 'index.html')
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        if username and password and re_password:
            if password != re_password:
                content = {
                    'info': '两次密码不一致'
                }
                return render(request, 'register.html', content)
            user = User.objects.filter(username=username)
            if user:
                content = {
                    'info': '该用户名已存在'
                }
                return render(request, 'register.html', content)
            User(username=username, password=password).save()
            return render(request, 'login.html')
        content = {
            'info': '用户名和密码不能为空'
        }
        return render(request, 'register.html', content)
    return render(request, 'register.html')

def login(request):
    if request.session.get('is_login', None):
        return render(request, 'index.html')
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:
            check_user = User.objects.filter(username=username, password=password)
            if check_user:
                user = User.objects.get(username=username, password=password)
                request.session['user_id'] = user.id
                request.session['is_login'] = True
                request.session['username'] = user.username
                return render(request, 'index.html')
            else:
                content = {
                    'info': '用户名或密码错误'
                }
                return render(request, 'login.html', content)
        content = {
            'info': '用户名和密码不能为空'
        }
        return render(request, 'login.html', content)
    return render(request, 'login.html')

def logout(request):
    if request.session.get('is_login', None):
        request.session.clear()
    return render(request, 'login.html')

def book_create(request):
    if not request.session.get('is_login', None):
        return render(request, 'login.html')
    if request.method == 'POST':
        name = request.POST.get('name', None)
        type = request.POST.get('type', None)
        user_id = request.session.get('user_id', None)
        if name and type and user_id:
            user = User.objects.get(id=user_id)
            Book(name=name, type=type, author=user).save()
            content = {
                'info': '书单创建成功'
            }
            return render(request, 'book/createbook.html', content)
        content = {
            'info': '书名和类型不能为空'
        }
        return render(request, 'book/createbook.html', content)
    return render(request, 'book/createbook.html')

def book_list(request):
    if not request.session.get('is_login', None):
        return render(request, 'login.html')
    user_id = request.session.get('user_id', None)
    user = User.objects.get(id=user_id)
    books = Book.objects.filter(author=user)
    content = {
        'books': books
    }
    return render(request, 'book/booklist.html', content)

def book_view(request, id):
    if not request.session.get('is_login', None):
        return render(request, 'login.html')
    check_book = Book.objects.filter(id=id)
    if check_book:
        book = Book.objects.get(id=id)
        sub = Subject.objects.filter(book=book)
        content = {
            'book': book,
            'subject': sub
        }
        return render(request, 'book/subject.html', content)
    return HttpResponse('No Result!!!')

def subject_add_text(request, book_id):
    if not request.session.get('is_login', None):
        return render(request, 'login.html')
    check_book = Book.objects.filter(id=book_id)
    if not check_book:
        Info = {
            'info': '该书单不存在'
        }
        return render(request, 'error.html', Info)
    if request.method == 'POST':
        content = request.POST.get('content', None)
        book = Book.objects.get(id=book_id)
        if content:
            Subject(content=content, type=1, book=book).save()
            return render(request, '')







