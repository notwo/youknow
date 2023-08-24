from rest_framework import routers
from django.urls import path, include
from .views import top, user_auth, user_setting, custom_user, library, category, keyword

router = routers.DefaultRouter()
router.register(r'users', custom_user.CustomUserAjaxViewSet)
router.register(r'libraries', library.LibraryAjaxViewSet)

app_name = 'you_know'
urlpatterns = [
  path("", top.IndexView.as_view(), name="index"),
  path('signup/', user_auth.SignupView.as_view(), name="signup"),
  path('login/', user_auth.LoginView.as_view(), name="login"),
  path('logout/', user_auth.LogoutView.as_view(), name="logout"),
  path('password_change/', user_auth.YouKnowPasswordChangeView.as_view(), name='password_change'),
  path('password_change/done/', user_auth.YouKnowPasswordChangeDoneView.as_view(), name='password_change_done'),
  path('password_reset/', user_auth.YouKnowPasswordResetView.as_view(), name='password_reset'),
  path('password_reset/done/', user_auth.YouKnowPasswordResetDoneView.as_view(), name='password_reset_done'),
  path('reset/<uidb64>/<token>/', user_auth.YouKnowPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
  path('reset/done/', user_auth.YouKnowPasswordResetCompleteView.as_view(), name='password_reset_complete'),
  path('user_setting/<str:username>/', user_setting.UserUpdateView.as_view(), name='profile'),
  path('user_setting/<str:username>/delete/', user_setting.UserDeleteView.as_view(), name='delete_account'),
  path('user_setting/user/delete_done/', user_setting.UserDeleteDoneView.as_view(), name='delete_account_done'),
  path('user_setting/user/delete_account_reason/<token>', user_setting.UserDeleteAccountReasonView.as_view(), name='delete_account_reason'),
  path('user_setting/user/delete_account_reason_done/', user_setting.UserDeleteAccountReasonDoneView.as_view(), name='delete_account_reason_done'),
  path('library/', library.LibraryViews.as_view(), name='library'),
  path('category/<int:library_id>/', category.CategoryIndexView.as_view(), name='category'),
  path('keyword/', keyword.KeywordIndexView.as_view(), name='keyword'),
]
