from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import Room,Message
from django.contrib import  messages
from itertools import chain
from django.contrib.auth.models import User,auth
from .models import Profile,Uploads,Room,Message,Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
User = get_user_model()


def index(request):
    return render(request,"main.html")

# Create your views here.



@login_required(login_url="/")
def chat_home(request):
    return render(request,"chatroom_home.html")

@login_required(login_url="/")
def room(request,room):
    info = User.objects.get(username=request.user)
    room_details = Room.objects.get(name=room)
    return render(request, 'chatroom.html', {
        'username':info.username,
        'room': room,
        'room_details': room_details
    })

@login_required(login_url="/")
def checkview(request):
    room = request.POST['room_name']
    info = User.objects.get(username=request.user)
    username = info.username
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)

    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)


@login_required(login_url="/")
def send(request):
    message = request.POST['message']
    info = User.objects.get(username=request.user)
    username = info.username
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value = message,user=username,room=room_id)
    new_message.save()
    return HttpResponse("Message sent successfully")

@login_required(login_url="/")
def getMessages(request,room):
      room_details = Room.objects.get(name = room)
      messages = Message.objects.filter(room=room_details.id)
      return JsonResponse({"messages":list(messages.values())})





@login_required(login_url="/")
def upload(request):
    if request.method == "POST":
        title = request.POST.get('title')
        blog = request.POST.get('blog')

        blog_upload = Uploads.objects.create(user=request.user, title=title, body=blog)
        messages.info(request, "Post uploaded successfully!")
        return redirect("feed")

    return render(request, "blogcreate.html")



@login_required(login_url="/")
def feed(request):
    posts = Uploads.objects.all()
    infos = Profile.objects.get(user=request.user)
    return render(request,"post.html",{"posts":posts,"infos": infos})

@login_required(login_url="/")
def post(request,pk):
    posts = get_object_or_404(Uploads, id=pk)

    comments = posts.comments.all()

    return render(request, 'read_blog.html', {'posts': posts, 'comments': comments})


@login_required(login_url='/')
def reply_to_comment(request,pk):
    parent_comment = get_object_or_404(Comment,id =pk)
    if request.method=="POST":
        content = request.POST.get("reply_content")
        user = request.user

        reply_comment = Comment(post = parent_comment.post,user=user,content=content,parent_comment=parent_comment)
        reply_comment.save()
    return redirect("post",pk = parent_comment.post.id)
@login_required(login_url="/")
def add_comment(request,pk):
    post = get_object_or_404(Uploads, id=pk)
    content = request.POST.get('comment_content')

    if content:
        user = request.user
        comment = Comment.objects.create(user=user, post=post, content=content)
        post.comments.add(comment)

    return redirect('post',pk=pk)


@login_required(login_url="/")
def like_post(request, pk):
    post = get_object_or_404(Uploads,id = pk)
    action = request.GET.get('action')
    if action == 'like':
        post.no_of_likes +=1
        post.save()

    return JsonResponse({"likes":post.no_of_likes})

#
# @login_required(login_url="/")
# def unlike_post(request, post_id):
#     post = get_object_or_404(Uploads, id=post_id)
#     if post.no_of_likes > 0:
#         post.no_of_likes -= 1
#         post.save()
#     data = {'likes_count': post.no_of_likes}
#     return JsonResponse(data)



@login_required(login_url = '/')
def search(request):
    user_object = User.objects.get(username = request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    infos = Profile.objects.get(user=request.user)

    if request.method == "POST":
        username=request.POST['username']
        username_object = User.objects.filter(username = username)

        username_profile = []
        username_profile_list = []

        for users in username_object:
            username_profile.append(users.id)

        for ids in username_profile:
            profile_list = Profile.objects.filter(user_id=ids)
            username_profile_list.append(profile_list)

        username_profile_list = list(chain(*username_profile_list))
        return render(request, 'search.html',
                      {'user_profile': user_profile, 'username_profile_list': username_profile_list,"infos":infos})


@login_required(login_url="/")
def settings(request):
    user_profile = Profile.objects.get(user = request.user)

    if request.method == "POST":

        if request.FILES.get('image') == None:
            image = user_profile.profile_image
            about = request.POST['about']
            interest = request.POST['interest']


            user_profile.profile_image = image
            user_profile.about = about
            user_profile.interest = interest

            user_profile.save()

        else:
            image = request.FILES.get("image")
            about = request.POST['about']
            interest = request.POST['interest']


        user_profile.profile_image = image
        user_profile.about = about
        user_profile.interest = interest

        user_profile.save()

        return redirect("settings")


    return render(request, "account_settings.html", {"user_profile": user_profile})


@login_required(login_url="/")
def personal_chat(request):
    return render(request,"personal_chat.html")

@login_required(login_url='/')
def profile_user(request,pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Uploads.objects.filter(user=user_object)

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
    }

    return render(request,"page_user.html",context)

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email=request.POST['email']
        password = request.POST['password']
        password2 = request.POST["password2"]

        if "sece.ac.in" in email and "20" in email:
                if password == password2:

                      if User.objects.filter(username=username).exists():
                         messages.info(request,"Username already exists")
                         return redirect("register")
                      elif User.objects.filter(email = email).exists():
                          messages.info(request,"Email already used")
                          return redirect("register")
                      else:
                        user = User.objects.create_user(username=username, email=email, password=password)
                        user.save();

                        #log user in and redirect to settings
                        user_login = auth.authenticate(username=username,password=password)
                        auth.login(request,user_login)

                        user_model = User.objects.get(username=username)
                        new_profile = Profile.objects.create(user=user_model)
                        new_profile.save()

                        return redirect("settings")

                else:
                    messages.info(request, "Password didn't match")
                    return redirect("register")

        else:
            messages.info(request, "Use your official Mail Id")
            return redirect("register")

    else:
            return render(request,"register.html")







def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST['password']

        user = auth.authenticate(username = username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Credential is invalid")
            return redirect('login')
    else:
        return render(request,"login.html")







@login_required(login_url="/")
def logout(request):
    auth.logout(request)
    return redirect('/')



