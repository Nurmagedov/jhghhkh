from django.urls import path
from myapp.views import article_main ,article,article_uniq,main

urlpatterns = [
    path('',main),
    path('5/',article_uniq),
    path('<int:article_id>/',article),
    path('<int:article_id>/<slug:name>',article),
]
6