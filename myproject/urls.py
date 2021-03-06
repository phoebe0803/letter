"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import re_path

#urlpatterns = [
#    path('admin/', admin.site.urls),
#]

from myapp import views
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^register/', views.register),
    re_path(r'^login$', views.login),
    re_path(r'^write_letter/save$',views.write_letter),
    re_path(r'^all_message$',views.all_message),
    re_path(r'^collect_letter$', views.collect_letter),
    re_path(r'^delete_collect_letter$',views.delete_collect_letter),
    re_path(r'^collect_xinli$', views.collect_xinli),
    re_path(r'^delete_collect_xinli$', views.delete_collect_xinli),
    re_path(r'^show_collect$', views.show_collect),
    re_path(r'^send_xinli_message$',views.send_xinli_message),
    re_path(r'^show_letter$',views.show_my_letter),
    re_path(r'^reply_letter$',views.reply_letter),
    re_path(r'^get_reply_letter$', views.get_reply_letter),
    re_path(r'^receive_reply_letter$',views.receive_reply_letter),
    re_path(r'^show_my_collect$',views.show_my_collect),
    re_path(r'^unread_to_read$',views.unread_to_read),
    re_path(r'^show_my_xinli_collect$',views.show_my_xinli_collect),
    re_path(r'^get_letter_byID$',views.get_letter_byID),
    re_path(r'^report_letter$',views.report_letter),
    re_path(r'^report_reply_letter$', views.report_reply_letter),
    re_path(r'^show_rubbish_letter$', views.show_rubbish_letter),
    re_path(r'^delete_letter$', views.delete_letter),
    re_path(r'^completely_delete_letter$', views.completely_delete_letter),
    re_path(r'^edit_letter$', views.edit_letter),
    re_path(r'^recover_delete_letter$',views.recover_delete_letter),
    re_path(r'^correct_password$',views.correct_password),
    re_path(r'^getSession$',views.getSession),
    re_path(r'^logout$',views.logout),
    re_path(r'^userlist$', views.userlist),

]
# test