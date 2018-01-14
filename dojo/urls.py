from django.urls import path, re_path
from . import views

urlpatterns = [ 
    re_path(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    path('hello/<name>/<int:age>/', views.hello),
    path('postlist1/', views.post_list1),
    path('postlist2/', views.post_list2),
    path('excel_download/', views.excel_download),
]