# from django.core.files.uploadedfile import SimpleUploadedFile
# from django.test import TestCase
# from django.urls import reverse
# from main_app.models import Carer, Photo
# from main_app.views import add_photo

# # Photo upload test
# class TestAddPhoto(TestCase):
#     # This will run before each test method
#     databases = ['test']

#     def setUp(self):
#         # Create a test Carer
#         self.carer = Carer.objects.create(nickname='Test Carer')

#     # This is your test method
#     def test_add_photo(self):
#         # Create a dummy photo file
#         file_content = b'Test file contains this'
#         file = SimpleUploadedFile('test_image.jpg', file_content, content_type='image/jpeg')

#         # create an add_photo URL and send a POST request to it
#         url = reverse('add_photo', kwargs={'pk': self.carer.id})
#         response = self.client.post(url, {'photo-file': file})

#         # Check that the view redirects to carers_detail page
#         self.assertRedirects(response, reverse('carers_detail', kwargs={'pk': self.carer.id}))

#         # Check that a photo object is created in the database
#         self.assertTrue(Photo.objects.filter(carer_id=self.carer.id).exists())

#     # This will run after each test method
#     def tearDown(self):
#         # remove the test objects (which is optional)
#         self.carer.delete()

import pytest 

@pytest.mark.django_db
def test_add_profile_photo():
    databases = ['test']

    # Create a test Carer
    carer = Carer.objects.create(nickname='Test Carer')

    # Create a dummy photo file
    file_content = b'Test file contains this'
    file = SimpleUploadedFile('test_image.jpg', file_content, content_type='image/jpeg')

    # create an add_photo URL and send a POST request to it
    url = reverse('add_photo', kwargs={'pk': carer.id})
    response = client.post(url, {'photo-file': file})

    # Check that the view redirects to carers_detail page
    # self.assertRedirects(response, reverse('carers_detail', kwargs={'pk': self.carer.id}))
    try:
        reverse('carers_detail', kwargs={'pk': carer.id})
        pytest.fail('Exception raised')
    except Exception:
        carer.delete()

    # Check that a photo object is created in the database
    # self.assertTrue(Photo.objects.filter(carer_id=carer.id).exists())
    assert(Photo.objects.filter(carer_id=carer.id).exists())