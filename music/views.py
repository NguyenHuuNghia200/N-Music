from django.shortcuts import render
from .models import Song, history_listen
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, HttpResponse
from .forms import registerview, loginview,formsong
from django.views import View
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    song1 = Song.objects.all().order_by('-id')[:9]
    topviews = Song.objects.all().order_by('-views')[:3]
    array_song=[]
    check_user=False
    if request.user.is_authenticated:
        history = history_listen.objects.filter(user=request.user).order_by('-create_at')[:4]
        array_song = []
        print()
        for i in history:
            song = Song.objects.get(pk=i.Song_id)
            array_song.append(song)

        check_user=User.objects.filter(is_superuser=True,id=request.user.id).exists()

    return render(request, 'music/home.html', {'s': song1,'history':array_song,'check':check_user,'top':topviews})


def signup(request):
    if request.method == 'POST':
        form = registerview(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/home')
    else:
        form = registerview()
    return render(request, 'music/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        user_name1 = User.objects.filter(username=user_name)

        for i in user_name1:
            mess_user = "1"

        user = auth.authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return redirect('/home')
    else:
        form = AuthenticationForm()
    return render(request, 'music/signin.html', {'f': form})


class loginclass(View):
    def get(self, request):
        user1 = True
        user2 = ""
        return render(request, 'music/signin.html', {'m': user1, 'm1': user2})

    def post(self, request):
        user1 = True
        user2 = ''
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        user_name1 = User.objects.filter(username=user_name)
        user = auth.authenticate(username=user_name, password=pass_word)
        if user is not None:
            auth.login(request, user)
            return redirect('/home')
        user1 = User.objects.filter(username=user_name).exists()
        user2 = "Password is uncorrect"
        if user1 == False:
            user2 = ""

        return render(request, 'music/signin.html', {'m': user1, 'm1': user2})


def logout(request):
    auth.logout(request)

    return redirect('/home')


def playsong(request, id):
    q = Song.objects.get(id=id)
    category = Song.objects.filter(category=q.category).exclude(id=19).order_by('?')[:3]
    q.views=q.views+1
    q.save()
    print(q.views)
    array_song = []
    check_user = False

    if request.user.is_authenticated:
        history = history_listen.objects.filter(user=request.user).order_by('-create_at')[:4]
        array_song = []
        print()
        for i in history:
            song = Song.objects.get(pk=i.Song_id)
            array_song.append(song)
            id = i.user.id
        check_user = User.objects.filter(is_superuser=True, id=id).exists()
    return render(request, 'music/musicplay.html', {'i': q,'history':array_song,'check':check_user,'cate':category})


def history1(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            if request.user is not None:
                songid = request.POST['song_id']
                history1 = history_listen(user=user, Song_id=songid)
                history1.save()
                return redirect(f'/song/{songid}')
            else:
                return redirect('/home')
        #x=history().get
        history = history_listen.objects.filter(user=request.user).order_by('-create_at')[:4]
        array_song = []

        for i in history:
            song = Song.objects.get(pk=i.Song_id)
            array_song.append(song)
        print(array_song)
        return render(request, 'music/history.html', {'s': array_song})
    else:
        return redirect('music:index')


class history(View):
    def get(self, request):
        if request.user.is_authenticated:
            history = history_listen.objects.filter(user=request.user).order_by('-create_at')[:4]
            array_song = []

            for i in history:
                song = Song.objects.get(pk=i.Song_id)
                array_song.append(song)
            print(array_song)
            return render(request, 'music/history.html', {'s': array_song})
        else:
            return redirect('music:index')

    def post(self, request):
        if request.user.is_authenticated:

            user = request.user
            if request.user is not None:
                songid = request.POST['song_id']
                history1 = history_listen(user=user, Song_id=songid)
                history1.save()
                return redirect(f'/song/{songid}')
            else:
                return redirect('/home')
        else:
            return redirect('music:index')


def addsong(request):

    if request.method == 'POST':
        f=formsong(request.POST,request.FILES)
        if f.is_valid():
            f.save()
            print('ok1')
    else:
        f=formsong()
    print('ok')
    return render(request,'music/add_song.html',{'f':f})

class add(View):
    def get(self,request):

        if request.user.is_superuser:
            f = formsong()
            array_song = []
            check_user = User.objects.filter(is_superuser=True, id=request.user.id).exists()
            history = history_listen.objects.filter(user=request.user).order_by('-create_at')[:4]
            for i in history:
                song = Song.objects.get(pk=i.Song_id)
                array_song.append(song)
            return render(request, 'music/add_song.html', {'f': f,'check':check_user,'history':array_song})
        else:
            return redirect('/home')
    def post(self,request):
        f = formsong(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            return redirect('/manage')
        else:
            return HttpResponse("k dc")



def admin(request):

    if request.user.is_superuser:
        print('admin')
        s = Song.objects.all()
        array_song = []
        paginator = Paginator(s, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        history = history_listen.objects.filter(user=request.user).order_by('-create_at')[:4]
        for i in history:
            song = Song.objects.get(pk=i.Song_id)
            array_song.append(song)
        check_user=User.objects.filter(is_superuser=True, id=request.user.id).exists()
        print(check_user)
        return render(request,'music/admin.html',{'p':page_obj,'check':check_user,'history':array_song})
    else:
        return redirect('/home')

def edit(request,id):
    if request.user.is_superuser:
        song=Song.objects.get(pk=id)
        form=formsong(instance=song)
        array_song = []
        check_user=False
        if request.method == 'POST':
            form=formsong(request.POST,instance=song)
            if form.is_valid():
                form.save()
                return redirect('/manage')

        history = history_listen.objects.filter(user=request.user).order_by('-create_at')[:4]
        check_user=User.objects.filter(is_superuser=True, id=request.user.id).exists()
        print(check_user)
        for i in history:
            song = Song.objects.get(pk=i.Song_id)
            array_song.append(song)
        return render(request,'music/edit_song.html',{'form':form,'check':check_user,'history':array_song})
    else:
        return redirect('/home')
def delete(request,id):
    song=Song.objects.get(pk=id)
    song.delete()
    if request.user.is_authenticated:
        check_user=User.objects.filter(is_superuser=True, id=id).exists()
    return  redirect('/manage')

def search(request):
    query=request.GET.get("text")
    ds=[]
    array_song=[]
    check_user=[]
    print(query)
    song=Song.objects.filter(title__icontains=query)|Song.objects.filter(author__icontains=query)
    print(song)

    for i in song:
        ds.append(i)
    paginator = Paginator(ds, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    history = history_listen.objects.filter(user=request.user).order_by('-create_at')[:4]
    for i in history:
        song = Song.objects.get(pk=i.Song_id)
        array_song.append(song)
    check_user = User.objects.filter(is_superuser=True, id=request.user.id).exists()
    return render(request,'music/search.html',{'p':page_obj,'query':query,'check':check_user,'history':array_song})
