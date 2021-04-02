from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('contact/', contact, name='contact'),
    # path('' , index , name='home'),
    # path('', cache_page(60)(HomeFact.as_view()), name='home'),
    path('', HomeFact.as_view(), name='home'),
    # path('category/<int:category_id>/' , get_category , name='category'),
    path('category/<int:category_id>/', FactByCategory.as_view(), name='category'),
    # path('contents/<int:content_id>/' , get_content , name='read'),
    path('contents/<int:pk>/' , ViewContent.as_view(), name='read'),
    # path('contents/add_fact/', add_fact , name='add_fact'),
    path('contents/add_fact/', CreateFact.as_view() , name='add_fact'),

]

