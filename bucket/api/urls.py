from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie

bucket_urlpatterns = [
    path('create_bucket_name/',create_bucket_name, name="create_bucket_name"),
    path('create_bucket/', create_bucket, name="create_bucket"),

]