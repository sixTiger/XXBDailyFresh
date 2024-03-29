"""XXBDailyFresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

# url(r'^register$', RegisterView.as_view(), name='register'), # 注册
#     url(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='active'), # 用户激活
#     url(r'^login$', LoginView.as_view(), name='login'), # 登录
from django.urls import path

from apps.user.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'), # 首页
    # path('', views.index, name='index'),  # 首页
]