"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from api.views import store_view, user_view, order_view
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/food/show_food', store_view.FoodInfo.as_view()),
    path('v1/food/show_detail', store_view.FoodInfo.as_view()),
    path('v1/user/login', user_view.UserLogin.as_view()),
    path('v1/shop_car/edite', order_view.EditCar.as_view()),
    path('v1/shop_car/check_current', order_view.ShopCar.as_view()),
    path('v1/shop_car/check_before', order_view.CheckBefore.as_view()),
    path('v1/address/edit', user_view.UserAddress.as_view()),
    path('v1/shop_car/delete', order_view.DeleteFood.as_view()),


    re_path('static/(?P<PATH>.*)', serve, {'document_root':settings.STATICFILES_DIRS})
]
