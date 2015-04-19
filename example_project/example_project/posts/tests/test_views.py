from extreme.testcase import TestCase

from django.test import RequestFactory
from django.http.response import Http404

from ..views import PostDetails
from .factories import PublishedPostFactory, UnpublishedPostFactory


class PostDetailsTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super(PostDetailsTests, cls).setUpClass()
        cls.post = PublishedPostFactory()
        cls.unpub_post = UnpublishedPostFactory()

    def setUp(self):
        self.view = PostDetails.as_view()
        self.factory = RequestFactory()
        self.request = self.factory.get("fake/uri")

    def test_get_with_existing_published_post_returns_200(self):
        response = self.view(self.request, pk=self.post.id)
        self.assertEqual(200, response.status_code)

    def test_get_with_unpublished_post_returns_404(self):
        with self.assertRaises(Http404):
            self.view(self.request, pk=self.unpub_post.id)

    def test_foo(self):
        self.assertTrue(True)

    def test_bar(self):
        self.assertTrue(True)

    def test_ble(self):
        self.assertTrue(True)

    def test_bla(self):
        self.assertTrue(True)

    def test_blo(self):
        self.assertTrue(True)
