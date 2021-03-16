from django.shortcuts import render, get_object_or_404
from .models import Review, Forum, Discussion

def index (request):
    return render(request, 'AudioSpace/index.html')


def getreviews(request):
    review_list = Review.objects.all()
    return render(request, 'audiospace/reviews.html', {'review_list' : review_list})


def reviewdetail(request, id):
    review = get_object_or_404(Review, pk = id)
    return render(request, 'audiospace/reviewdetail.html', {'review' : review})


def getforums(request):
    forum_list = Forum.objects.all()
    return render(request, 'audiospace/forums.html', {'forum_list' : forum_list})


def forumdetail(request, id):
    forum = get_object_or_404(Forum, pk = id)
    discussions=[]
    discussions.append(forum.discussion_set.all())
 
    context={'forum' : forum,
              'discussions' : discussions}
    return render(request, 'audiospace/forumdetail.html', context)



# Create your views here.
