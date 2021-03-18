from django.shortcuts import render, get_object_or_404, redirect
from .models import Review, Forum, Discussion
from .forms import DiscussionForm, ForumForm, ReviewForm
from django.contrib.auth.decorators import login_required

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


@login_required
def newreview(request):
    form = ReviewForm
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            post = form.save(commit = True)
            post.save()
            return redirect('reviews')
    else:
        form = ReviewForm
    return render(request, 'audiospace/newreview.html', {'form' : form})


@login_required
def newforum(request):
    form = ForumForm
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            post = form.save(commit = True)
            post.save()
            return redirect('forums')
    else:
        form = ForumForm
    return render(request, 'audiospace/newforum.html', {'form' : form})


@login_required
def newcomment(request):
    form = DiscussionForm
    if request.method == 'POST':
        form = DiscussionForm(request.POST)
        if form.is_valid():
            post = form.save(commit = True)
            post.save()
            return redirect('forums')
    else:
        form = DiscussionForm
    return render(request, 'audiospace/newcomment.html', {'form' : form})


def loginmessage(request):
    return render(request, 'audiospace/loginmessage.html')


def logoutmessage(request):
    return render(request, 'audiospace/logoutmessage.html')


# Create your views here.
