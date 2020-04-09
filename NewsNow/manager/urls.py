from django.urls import path

from . import views

urlpatterns=[

    path('panel/manager/list/', views.manager_list, name='manager_list'),
    path('panel/manager/del/<pk>', views.manager_del, name='manager_del'),
    path('panel/manager/group/', views.manager_group, name='manager_group'),
    path('panel/manager/group/add', views.manager_group_add, name='manager_group_add'),
    path('panel/manager/group/del/<name>', views.manager_group_del, name='manager_group_del'),
    path('panel/manager/group/show/<pk>', views.user_groups, name='user_groups'),
    path('panel/manager/addtogroup/<pk>', views.add_user_to_groups, name='add_user_to_groups'),

]


