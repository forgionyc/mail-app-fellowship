"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from mailapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mails/get/received/<str:user_mail>/', MailsReceivedUserGetterEndpoint.as_view()),
    path('mails/get/sent/<str:user_mail>/', MailsSentUserGetterEndpoint.as_view()),
    path('mail/get/information/<str:mail_id>', InformationForMailGetterEndpoint.as_view()),
    path('mail/post/mail/', SendMailPostEndpoint.as_view()),
    path('user/post/create/', CreateUserPostEndpoint.as_view()),
]
