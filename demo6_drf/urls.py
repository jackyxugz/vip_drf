from django.contrib import admin
from django.urls import path
from app01.views import AuthView, CommonVideoView, VIPVideoView, SVIPVideoView

urlpatterns = [
    path('admin/', admin.site.urls),
    # 登录认证
    path('auth/', AuthView.as_view(), name='auth'),
    # 获取普通资源
    path('common/', CommonVideoView.as_view(), name='common'),
    # 获取VIP资源
    path('vip/', VIPVideoView.as_view(), name='vip'),
    # 获取SVIP资源
    path('svip/', SVIPVideoView.as_view(), name='svip'),


]
