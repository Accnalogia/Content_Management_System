from django.test import TestCase
from api.contentdata.models import ContentItem, Categories
from api.core.models import CMSUser
from content_management_system.settings import BASE_DIR
import base64


class ContentItemTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        CMSUser.objects.create(username='johndoe@gmail.com',
                               email='johndoe@gmail.com', password='qwerty12345', first_name='john', last_name='doe',
                               pincode='245875', phone_number='1547581247')
        user_john = CMSUser.objects.get(first_name='john')

        filename = BASE_DIR + "/gre_math.pdf"
        with open(filename, "rb") as image_file:
            filedata = image_file.read()
            encoded_str = "data:image/png;base64," + str(base64.b64encode(filedata))

        ContentItem.objects.create(user=user_john,
            title='this is the title', body='Body of the file', summary='Summary of the file', document=encoded_str)

        content_item = ContentItem.objects.get(body='Body of the file')

        Categories.objects.create(contentitem=content_item, category='Exam')

    def test_content_check(self):
        content_item = ContentItem.objects.get(body='Body of the file')
        self.assertEqual(
            content_item.title, 'this is the title')
        category = Categories.objects.get(contentitem_id=content_item)

        self.assertEqual(
            category.category, 'Exam')
