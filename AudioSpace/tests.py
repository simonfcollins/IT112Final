from django.test import TestCase
from .models import Review, Discussion, Forum
from .views import getreviews, getforums, forumdetail, reviewdetail, newreview, newforum, newcomment
from django.contrib.auth.models import User
from .forms import ForumForm, DiscussionForm, ReviewForm
from django.urls import reverse_lazy, reverse


# model tests
class ReviewTest(TestCase):
    def setUp(self):
        self.title = Review(revTitle = 'New Song')

    def test_revstring(self):
        self.assertEqual(str(self.title), 'New Song')

    def test_tablename(self):
        self.assertEqual(str(Review._meta.db_table), 'Review')

class ForumTest(TestCase):
    def setUp(self):
        self.topic = Forum(topic = 'New Forum')

    def test_meetstring(self):
        self.assertEqual(str(self.topic), 'New Forum')

    def test_tablename(self):
        self.assertEqual(str(Forum._meta.db_table), 'Forum')


class DiscussionTest(TestCase):
    def setUp(self):
        testforum = Forum(topic = 'New Forum')
        self.forum = Discussion(forum = testforum)

    def test_meetstring(self):
        self.assertEqual(str(self.forum), 'New Forum')

    def test_tablename(self):
        self.assertEqual(str(Discussion._meta.db_table), 'Discussion')


# view tests
class GetReviewsTest(TestCase):
    def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('reviews'))
       self.assertEqual(response.status_code, 200)


class GetForumsTest(TestCase):
    def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('forums'))
       self.assertEqual(response.status_code, 200)


class ReviewDetailTest(TestCase):
    def setUp(self):
        self.usr = User.objects.create(username = 'testuser')
        self.rev = Review.objects.create(
            revTitle = 'New Review',
            userID = self.usr, 
            datePosted = '03/18/21', 
            rating = '4', 
            revText = 'Solid product'
        )

    def test_review_detail_success(self):
        response = self.client.get(reverse('rdetail', args=(self.rev.id,)))
        self.assertEqual(response.status_code, 200)


class ForumDetailTest(TestCase):
    def setUp(self):
        self.usr = User.objects.create(username = 'testuser')
        self.forum = Forum.objects.create(
            userID = self.usr,
            topic = 'New Forum', 
            description = 'stuff stuff stuff', 
            date_created = '03/18/21' 
        )

    def test_forum_detail_success(self):
        response = self.client.get(reverse('fdetail', args=(self.forum.id,)))
        self.assertEqual(response.status_code, 200)


# form tests
class NewReviewTest(TestCase):
    def test_reviewform(self):
        data = {'revTitle' : 'New Review', 'userID' : 'testUser', 'datePosted' : '03/18/21', 
       'revtext' : 'Very happy with purchase.'}
        form = ReviewForm(data)
        self.assertTrue(form.is_valid)


class NewForumTest(TestCase):
    def test_forumform(self):
        data = {'userID' : 'testUser', 'topic' : 'New Song?', 
        'description' : 'What are your thoughts on this new track?', 'date_created' : '03/18/21'}
        form = ForumForm(data)
        self.assertTrue(form.is_valid)


class NewDiscussionTest(TestCase):
    def test_discussionform(self):
        data = {'userID' : 'testUser', 'forum' : 'New Song?', 
        'discuss' : 'I thought it was pretty goof', 'date_created' : '03/18/21'}
        form = DiscussionForm(data)
        self.assertTrue(form.is_valid)

# login authentication test
class NewReviewAuthenticationsTest(TestCase):
    def setUp(self):
        self.testusr = User.objects.create_user(
            username = 'testuser1',
            password = 'P@ssw0rd'
        )
        self.rev = Review.objects.create(
            revTitle = 'New Review',
            userID = self.testusr, 
            datePosted = '03/18/21', 
            rating = '4', 
            revText = 'Solid product'
        )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('newreview'))
        self.assertRedirects(response, '/accounts/login/?next=/audiospace/newreview/')
