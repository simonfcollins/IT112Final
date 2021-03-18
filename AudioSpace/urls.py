from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('reviews/', views.getreviews, name = 'reviews'),
    path('reviewdetail/<int:id>' , views.reviewdetail, name = 'rdetail'),
    path('forums/', views.getforums, name = 'forums'),
    path('forumdetail/<int:id>' , views.forumdetail, name = 'fdetail'),
    path('newreview/', views.newreview, name = 'newreview'),
    path('newforum/', views.newforum, name = 'newforum'),
    path('newcomment/', views.newcomment, name = 'newcomment'),
    path('loginmessage/', views.loginmessage, name = 'loginmessage'),
    path('logoutmessage/', views.logoutmessage, name = 'logoutmessage'),
]