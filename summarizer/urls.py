from django.urls import path
from .views import HomeView, SignupView, SumDeleteView, SumDetailView, SumCreateView, SumListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('workspace/', SumListView.as_view(), name='summary_list'),
    path('workspace/api/create/', SumCreateView.as_view(), name='summary_create'),
    path("workspace/api/detail/<int:pk>/", SumDetailView.as_view(), name="summary_detail"),
    path('workspace/api/delete/<int:pk>/', SumDeleteView.as_view(), name='summary_delete'),

]