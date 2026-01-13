from django.urls import path
from .views import (
    home,
    about,
    contact,
    contact_list,
    contact_edit,
    contact_delete,
    login_view,
    logout_view,
    signup_view
)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),

    # CONTACT LIST
    path('contacts/', contact_list, name='contact_list'),

    # EDIT & DELETE
    path('contacts/edit/<int:id>/', contact_edit, name='contact_edit'),
    path('contacts/delete/<int:id>/', contact_delete, name='contact_delete'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('signup/', signup_view, name='signup'),

]
