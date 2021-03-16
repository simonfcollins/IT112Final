from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('reviews/', views.getreviews, name = 'reviews'),
    path('reviewdetail/<int:id>' , views.reviewdetail, name = 'rdetail'),
    path('forums/', views.getforums, name = 'forums'),
    path('forumdetail/<int:id>' , views.forumdetail, name = 'fdetail'),
    #path('addInForum/', views.addInForum, name = 'addInForum'),
    #path('addInDiscussion/', views.addInDiscussion, name = 'addInDiscussion'),
]