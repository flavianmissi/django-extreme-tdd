from django.views.generic.detail import DetailView
from django.http.response import Http404

from .models import Post


class PostDetails(DetailView):

    model = Post

    def get(self, request, *args, **kwargs):
        response = super(PostDetails, self).get(request, *args, **kwargs)
        if not self.object.is_published and request.user != self.object.author:
            raise Http404("Post does not exist.")
        return response
