
from django.contrib import admin
from django.urls import path,include
from app import views
from app.views import CustomAuthToken
from rest_framework.routers import DefaultRouter,SimpleRouter
from rest_framework.authtoken import views as view1
router=DefaultRouter()
router.register('users',views.UserView)
router.register('slot',views.SlotView)
router.register('book',views.BookView)
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('bookdetail/<int:pk>',views.BookDetail.as_view())
    path('',include(router.urls)),
    path('search',views.SearchView.as_view()),
    path('login/',CustomAuthToken.as_view()),
    path('logout',views.LogoutView.as_view()),
    path("me/", views.MeView.as_view()),
]

from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)