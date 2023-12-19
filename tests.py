import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from main_app.models import Carer, Photo
from main_app.views import add_photo

# Photo upload test
@pytest.mark.django_db
class TestAddPhoto(TestCase):
    def setUp(self):
        # create a test Carer
        self.carer = Carer.objects.create(nickname='Test Carer')

    def test_add_photo(self):
        # Create a dummy fake photo file
        file_content = b'Test file contains this'
        file = SimpleUploadedFile('test_image.jpg', file_content, content_type='image/jpeg')

        # create a add_photo URL and send a POST request to it 
        url = reverse('add_photo', kwargs={'pk': self.carer.id})
        response = self.client.post(url, {'photo-file': file})

        # Check that the view redirects to carers_detail page
        self.assertRedirects(response, reverse('carers_detail', kwargs={'pk': self.carer.id}))

        # Check that a photo object is created in the database
        self.assertTrue(Photo.objects.filter(carer_id=self.carer.id).exists())

    def tearDown(self):
        #  remove the test objects(which is optional)
        self.carer.delete()

        # Assert that the database is clean after teardown
        self.assertFalse(Carer.objects.filter(pk=self.carer.id).exists())
        self.assertFalse(Photo.objects.filter(carer_id=self.carer.id).exists())