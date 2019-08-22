from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Contact
from .serializers import ContactSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_contact(firstName="", lastName="", email=""):
        if firstName != "" and lastName != "" and email != "":
            Contact.objects.create(firstName=firstName, lastName=lastName, email=email)

    def setUp(self):
        self.create_contact("John", "Adams", "ja@test.com")
        self.create_contact("William", "Tell", "wt@test.com")
        self.create_contact("George", "Washington", "gw@test.com")
        self.create_contact("Bill", "Murray", "bm@test.com")


class GetAllContactsTest(BaseViewTest):
    def test_get_all_contacts(self):
        response = self.client.get(
            reverse("contact-all")
        )
        expected = Contact.objects.all()
        serialized = ContactSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
