from django.conf.urls import url
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^register/$', register, name='register'),
    # url(r'^test/$', test, name='test'),
    url(r'^register/admin/$', register_staff, name='register_staff'),
    # url(r'^profile/$', edit_profile),
    url(r'^$', home, name='home'),
    url(r'^users/$', user_list, name='user_list'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^(?P<id>\d+)/$', user_details, name='user_details'),
    # url(r'^update/$', edit_user, name='account_update'),
    url(r'^edit_profile/$', edit_profile, name='edit_profile'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^reset/$', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html',
        email_template_name='accounts/password_reset_email.html',
        subject_template_name='accounts/password_reset_subject.txt'), name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
        name='password_reset_complete'),
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$',
        auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
        name='password_change_done'),

]
