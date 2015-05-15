from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from api.models import Comment, Page, User


class CommentTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='one', email='one@exmaple.com', password='one')

        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_get_page_comments(self):
        page = Page.objects.create(name='First', user=self.user)
        comment = Comment.objects.create(text='This is awesome!', user=self.user, page=page)
        url = reverse('page-comments', kwargs={'id': page.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [comment.to_JSON()])
