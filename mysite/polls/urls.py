from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logged_out/', views.LogoutView.as_view(), name='logged_out'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/delete/<int:pk>/', views.UserProfileDeleteView.as_view(), name='edit_profile'),
    path('profile/change/<int:pk>/', views.UserProfileUpdateView.as_view(), name='delete_profile'),
]