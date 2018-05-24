from django.test import TestCase
from .models import Store

# Create your tests here.
class HomeViewTests(TestCase):

    def setUp(self):
        Store.objects.create(user_id = '2', tel = '0988888888', name='肯德基', notes='沒有薄皮嫩雞倒一倒算了啦')

    def tearDown(self):
        Store.objects.all().delete()

    def test_home_view(self):
        response = self.client.get('/index')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')