from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Lesson
from .forms import SignUpForm, LoginForm, AddPostForm, AddLessonForm
from django.contrib.auth import login, logout

def home_page(request):
    return render(request, "./home.html")

def start_page(request):
    last_posts = Post.objects.all().order_by('-posted_date')[:4]
    context = {
        'last_posts': last_posts
    }
    return render(request, "./start.html", context)

# все новости
def news_page(request):
    posts = Post.objects.all().order_by('-posted_date')
    context = {
        'posts': posts
    }
    return render(request, "./news.html", context)
# чтение поста
def news_detail_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, "./post_detail.html", context)

def lessons_page(request):
    lessons = Lesson.objects.all()
    context = {
        'lessons': lessons
    }
    return render(request, "./lessons_page.html", context)

def lessons_detail_page(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    lessons = Lesson.objects.all()
    context = {
        'lesson': lesson,
        'lessons': lessons
    }
    return render(request, "./lesson_detail.html", context)

def simulator_page(request):
    return render(request, "./simulator.html")

# регистрация курсантов
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login_view')
    else:
        form = SignUpForm()
    return render(request, './register.html', {
        'form': form
    })

# вход в систему
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('start_page')
    else:
        form = LoginForm()
    return render(request, './login.html', {
        'form': form
    })

# выход из системы
def logout_view(request):
    logout(request)
    return redirect('start_page')






# сторона администратора системы
def post_list_page(request):
    posts = Post.objects.all().order_by('-posted_date')
    context = {
        'posts': posts
    }
    return render(request, "./admin/post_list.html", context)

def add_post_page(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list_page')
    else:
        form = AddPostForm()

    return render(request, "./admin/add_post.html", {
        'form': form
    })

def lesson_list_page(request):
    lessons = Lesson.objects.all()
    context = {
        'lessons': lessons
    }
    return render(request, "./admin/lesson_list.html", context)

def add_lesson_page(request):
    if request.method == "POST":
        form = AddLessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lesson_list_page')
    else:
        form = AddLessonForm()

    return render(request, "./admin/add_lesson.html", {
        'form': form
    })
