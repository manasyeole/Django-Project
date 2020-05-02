from django.urls import path
from . import views

app_name="accounts"


urlpatterns = [
       path("register",views.register, name="register"),
       path("getin",views.getin,name="getin"),
       path("wheather",views.wheather,name="wheather"),
       path("getout",views.getout,name="getout"),
       path("csrd",views.csrd,name="csrd"),
       path("create",views.create,name="create_new"),
       path("edit/<username>",views.edit,name="edit"),



 ]