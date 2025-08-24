from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', games_review, name='home'),
    path('games_review/', games_review, name='games'),
    path('order_review/', order_review, name='order'),
    path('game/<int:id>/', game_details, name="game_details"),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<int:game_id>/', cart_add, name='cart_add'),
    path('cart/remove/<int:game_id>/', cart_remove, name='cart_remove'),
    path('cart/update_quantity/<int:game_id>/', cart_update_quantity, name="cart_update_quantity"),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name = "login.html"), name='login'),
    path('logout/', LogoutView.as_view(next_page = "home"), name='logout'),
    path('profile/', profile, name='profile'),
    path('favorite_add/<int:game_id>/', favorite_add, name='favorite_add'),
    path('admin_dashboard/', admin_dashboard, name='admin'),
    path('admin_dashboard/game_add', add_new_game, name='game_add'),
    path('admin_dashboard/assign_group', assign_user_to_group, name='assign_group'),
    path('admin_dashboard/game_remove', remove_game, name='game_remove')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)