from rest_framework_nested import routers
from django.urls import path
from .views import user_setting, custom_user, library, category, keyword


app_name = 'you_know'

# api routes
router = routers.SimpleRouter()
router.register(r'users', custom_user.CustomUserAjaxViewSet)
users_router = (routers.NestedSimpleRouter(router, 'users', lookup='you_know_customuser'))
users_router.register('libraries', library.LibraryAjaxViewSet)
libraries_router = routers.NestedSimpleRouter(users_router, 'libraries', lookup='library')
libraries_router.register('categories', category.CategoryAjaxViewSet)
categories_router = routers.NestedSimpleRouter(libraries_router, 'categories', lookup='category')
categories_router.register('keywords', keyword.KeywordAjaxViewSet)

# other routes
urlpatterns = [
  path('user_setting/user/delete_account_reason/<token>', user_setting.UserDeleteAccountReasonView.as_view(), name='delete_account_reason'),
  path('user_setting/user/delete_account_reason_done/', user_setting.UserDeleteAccountReasonDoneView.as_view(), name='delete_account_reason_done'),
]
