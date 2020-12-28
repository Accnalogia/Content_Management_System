from django.test import TestCase
from api.core.models import CMSUser


class CMSUserTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        CMSUser.objects.create(username='johndoe@gmail.com',
            email='johndoe@gmail.com', password='qwerty12345', first_name='john', last_name='doe', pincode='245875', phone_number='1547581247')
        CMSUser.objects.create(username='joeytribiani@yahoo.com',
            email='joeytribiani@yahoo.com', password='12345qwerty', first_name='joey', last_name='tribiani', pincode='123456', phone_number='1555555555')

    def test_email_check(self):
        user_john = CMSUser.objects.get(first_name='john')
        user_joey = CMSUser.objects.get(first_name='joey')
        self.assertEqual(
            user_john.email, "johndoe@gmail.com")
        self.assertEqual(
            user_joey.email, "joeytribiani@yahoo.com")
