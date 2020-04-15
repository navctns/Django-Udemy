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
    path('panel/manager/delgroup/<pk>/<name>', views.del_user_from_groups, name='del_user_from_groups'),
    path('panel/manager/perms/', views.manager_perms, name='manager_perms'),
    path('panel/manager/perms/del/<name>', views.manager_perms_del, name='manager_perms_del'),
    path('panel/manager/perms/add/', views.manager_perms_add, name='manager_perms_add'),
    path('panel/manager/perms/show/<pk>', views.user_perms, name='user_perms'),
    path('panel/manager/delperm/<pk>/<name>', views.user_perms_del, name='user_perms_del'),
    path('panel/manager/addperm/<pk>', views.user_perms_add, name='user_perms_add'),
    path('panel/manager/addpermtogroup/<name>', views.groups_perms, name='groups_perms'),
    path('panel/manager/group/delperm/<gname>/<name>', views.groups_perms_del, name='groups_perms_del'),
    path('panel/manager/group/addperms/<name>/', views.groups_perms_add, name='groups_perms_add'),

]


