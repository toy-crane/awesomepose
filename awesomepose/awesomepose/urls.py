"""awesomepose URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from users.views import *
from posts.views import *
from awesomepose.views import *
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', PostListView.as_view(), name="home"),
    url(r'signup/', SignupView.as_view(), name="sign-up"),

    url(r'', include('social.apps.django_app.urls', namespace='social')),

    url(r'login/', LoginView.as_view(), name="login"),
    url(r'welcome/', WelcomeView.as_view(), name="welcome"),
    url(r'logout/', LogoutView.as_view(), name="logout"),

    url(r'posts/$', PostListView.as_view(), name="posts"),
    url(r'posts/(?P<slug>\w+)/$', PostDetailView.as_view(), name="detail"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
