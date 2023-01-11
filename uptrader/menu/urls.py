from django.urls import path
from uptrader.menu.admin import tree_menu_admin_site

from uptrader.menu.views import IndexView


urlpatterns = [
    path("admin/", tree_menu_admin_site.urls),
    path("menu/", IndexView.as_view())
]
