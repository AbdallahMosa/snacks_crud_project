from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack
# Create your tests here.
class SnackTest(TestCase):
    def setUp(self):
        self.user=get_user_model().objects.create_user(username="test",email="test@test.come",password="test")
        self.snack=Snack.objects.create(title='test',purchaser=self.user,description="testtesttest")

    def test_snack_list(self):
        response = self.client.get(reverse('snack_list'))
        self.assertEqual(response.status_code,200)
    def test_snack_detail(self):
        response = self.client.get(reverse('snack_detail', args=[self.snack.id]))
        self.assertTemplateUsed(response,"snack_detail.html")
    def test_templates(self):
        response = self.client.get(reverse('snack_list'))
        self.assertTemplateUsed(response,"snack_list.html")
    def test_snack_create(self):
        response = self.client.get(reverse('snack_create'))
        self.assertTemplateUsed(response,"snack_create.html")
    def test_snack_update(self):
        response = self.client.get(reverse('snack_update', args=[self.snack.id]))
        self.assertTemplateUsed(response,"snack_update.html")
    def test_snack_delete(self):
        response = self.client.get(reverse('snack_delete', args=[self.snack.id]))
        self.assertTemplateUsed(response,"snack_delete.html")

    def test_str_method(self):
        self.assertEqual(str(self.snack),'test')
    
    def test_create_view(self):
        data={'title':'test','purchaser':self.user.id,'description':"testtesttest"}
        url = reverse('snack_create')
        response = self.client.post(path=url ,data=data,follow=True)
        self.assertEqual(len(Snack.objects.all()),2)

    def test_redirects(self):
        data={'title':'test','purchaser':self.user.id,'description':"testtesttest"}
        url = reverse('snack_create')
        response = self.client.post(path=url ,data=data,follow=True)
        self.assertRedirects(response,reverse('snack_detail',args=[2]))