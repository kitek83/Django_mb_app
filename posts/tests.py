from django.test import TestCase
from .models import Post
# Create your tests here.

#testing Post database
class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text='just a test')  #created object text in database model Post / id =1

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEquals(expected_object_name, 'just a test')

