from extreme.testcase import TestCase

from django.test import RequestFactory
from django.http.response import Http404
from django.contrib.auth.models import AnonymousUser

from ..views import PostDetails
from .factories import PublishedPostFactory, UnpublishedPostFactory


class PostDetailsTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super(PostDetailsTests, cls).setUpClass()
        cls.post = PublishedPostFactory()
        cls.unpub_post = UnpublishedPostFactory()

    def setUp(self):
        # self.post = PublishedPostFactory()
        # self.unpub_post = UnpublishedPostFactory()
        self.view = PostDetails.as_view()
        self.factory = RequestFactory()
        self.request = self.factory.get("fake/uri")
        self.request.user = AnonymousUser()

    def test_get_with_existing_published_post_returns_200(self):
        response = self.view(self.request, pk=self.post.id)
        self.assertEqual(200, response.status_code)

    def test_get_with_unpublished_post_returns_404_for_regular_user(self):
        with self.assertRaises(Http404):
            self.view(self.request, pk=self.unpub_post.id)

    def test_get_returns_unpublished_post_for_its_author(self):
        self.request.user = self.unpub_post.author
        response = self.view(self.request, pk=self.unpub_post.id)
        self.assertEqual(200, response.status_code)

    def test_one_more_to_make_a_better_point(self):
        self.assertTrue(True)

    def test_another_one_to_make_a_better_point(self):
        self.assertTrue(True)

    def test_yet_another_one_to_make_a_better_point(self):
        self.assertTrue(True)
