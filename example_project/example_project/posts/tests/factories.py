import factory
from ..models import Post
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    first_name = "Leela"
    last_name = "Turanga"
    email = factory.sequence(lambda n:"leela{}@gmail.com".format(n))
    username = factory.sequence(lambda n:"leela{}".format(n))


class PublishedPostFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Post

    title = factory.sequence(lambda n:"Factory post #{}".format(n))
    is_published = True
    author = factory.SubFactory(UserFactory)
    content = factory.sequence(lambda n:"Post content {}".format(n))


class UnpublishedPostFactory(PublishedPostFactory):

    is_published = False
