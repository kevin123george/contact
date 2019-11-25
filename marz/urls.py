from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
from datafun import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.marz_index,name = "home")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)