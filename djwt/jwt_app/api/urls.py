from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView, TokenObtainPairView

from jwt_app.api.views import CategoryAPIList, ProductAPIList

urlpatterns = [
    path('api/category/', CategoryAPIList.as_view(), name='category'),
    path('api/product/', ProductAPIList.as_view(), name='product'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify')
]