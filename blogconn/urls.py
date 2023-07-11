from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("chat_home",views.chat_home,name="chat_home"),
   path("login",views.login,name="login"),
    path("upload",views.upload,name = "upload"),
   path("register",views.register,name="register"),
    path("logout",views.logout,name='logout'),
    path("settings",views.settings,name="settings"),
    path("feed",views.feed,name = "feed"),
    path("post/<str:pk>",views.post,name="post"),
    path("<str:room>/",views.room,name='room'),
    path("checkview",views.checkview,name='checkview'),
    path("send",views.send,name='send'),
    path("getMessages/<str:room>/",views.getMessages,name='getMessages'),
    path("chat_home",views.chat_home,name = "chat_home"),
    path("add_comment/<str:pk>",views.add_comment,name="add_comment"),
   # path("show_comment/<str:pk>",views.show_comment,name="show_comment"),
    path("profile_user/<str:pk>",views.profile_user,name = "profile_user"),
     path('like_post/<str:pk>/', views.like_post, name='like_post'),
    # path('unlike/<uuid:post_id>/', views.unlike_post, name='unlike_post'),
    path('search', views.search, name='search'),
   path("comment/<str:pk>/reply/",views.reply_to_comment,name="reply_to_comment"),
   path("personal_chat",views.personal_chat,name = "personal_chat"),
]