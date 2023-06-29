"""
URL configuration for bitcoin_app project.

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
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.urls import path
from bitcoin_tracker.views import bitcoin_chart

urlpatterns = [

    path('bitcoin-chart/', bitcoin_chart, name='bitcoin_chart'),
]
"""
from django.urls import path
from bitcoin_tracker.views import bitcoin_chart_view

urlpatterns = [
    path('', bitcoin_chart_view, name='home'),  # Add this line to define the empty path
    path('bitcoin-chart/', bitcoin_chart_view, name='bitcoin_chart'),
    path('', bitcoin_chart_view, name='home'),
    # Add other URL patterns for your app
]


