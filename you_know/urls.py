from rest_framework_nested import routers
from django.urls import path
from .views import index, user_setting, custom_user, library, category, keyword, tag


app_name = 'you_know'

# api routes
users_origin_router = routers.DefaultRouter()
users_origin_router.register(r'users', custom_user.CustomUserAjaxViewSet)
users_router = routers.SimpleRouter()
users_router.register(r'users', custom_user.CustomUserAjaxViewSet)
libraries_router = (routers.NestedSimpleRouter(users_router, 'users', lookup='you_know_customuser'))
libraries_router.register('libraries', library.LibraryAjaxViewSet)
categories_router = routers.NestedSimpleRouter(libraries_router, 'libraries', lookup='library')
categories_router.register('categories', category.CategoryAjaxViewSet)
keywords_router = routers.NestedSimpleRouter(categories_router, 'categories', lookup='category')
keywords_router.register('keywords', keyword.KeywordAjaxViewSet)
tags_router = routers.NestedSimpleRouter(users_router, 'users', lookup='you_know_customuser')
tags_router.register('tags', tag.TagAjaxViewSet)

# other routes
urlpatterns = [
  path("", index.IndexView.as_view(), name="index"),
  path(
    'user_setting/user/delete_account_reason/<token>',
    user_setting.UserDeleteAccountReasonView.as_view(),
    name='delete_account_reason'),
  path(
    'user_setting/user/delete_account_reason_done/',
    user_setting.UserDeleteAccountReasonDoneView.as_view(),
    name='delete_account_reason_done'),
]
