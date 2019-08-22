from django.shortcuts import render
from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer


class ListContactView(generics.ListAPIView):
    """
    Provides a full list of Contacts
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactCreate(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
