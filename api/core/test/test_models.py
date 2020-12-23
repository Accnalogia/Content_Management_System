from django.test import TestCase
from api.core.models import CMSUser


class CMSUserTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        CMSUser.objects.create(username='252ab5dd-140f-4a1a-be42-5893f9894544',
            email='johndoe@gmail.com', password='qwerty12345', first_name='john', last_name='doe')
        CMSUser.objects.create(username='4cb3bd1e-2193-48da-a6b1-8ccc0f64ec48',
            email='joeytribiani@yahoo.com', password='12345qwerty', first_name='joey', last_name='tribiani')

    def test_email_check(self):
        user_bhagyesh = CMSUser.objects.get(first_name='john')
        user_prithvi = CMSUser.objects.get(first_name='joey')
        self.assertEqual(
            user_bhagyesh.email, "johndoe@gmail.com")
        self.assertEqual(
            user_prithvi.email, "joeytribiani@yahoo.com")
