from django.urls import path
from .views import ListContactView, ContactDetail, ContactCreate

urlpatterns = [
    path('contact/', ListContactView.as_view(), name="contact-all"),
    path('contact/<int:pk>', ContactDetail.as_view()),
    path('contact/create', ContactCreate.as_view())
]
