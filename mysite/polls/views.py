from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import UserProfileForm, RegistrationUserForm
from .models import Question, Choice, UserProfile, Vote
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')


class ProfileView(generic.DetailView):
    model = UserProfile
    template_name = 'polls/templates/profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_object_or_404(UserProfile, username=self.request.user.username)


class UserProfileDeleteView(DeleteView):
    model = UserProfile
    success_url = reverse_lazy('polls:index')
    template_name = 'polls/templates/delete_profile.html'


class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfile
    success_url = reverse_lazy('polls:profile')
    template_name = 'polls/templates/edit_profile.html'


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/templates/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/templates/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/templates/detail.html', {
            'question': question,
            'error_message': 'Вы не сделали выбор'
        })
    else:
        if Vote.objects.filter(question=question, user=request.user).exists():
            return render(request, 'polls/results.html', {
                'question': question,
                'error_message': 'вы уже голосовали'
            })
        else:
            question.question_votes += 1
            question.save()
            selected_choice.votes += 1
            selected_choice.save()
            voted = Vote.objects.create(question=question, user=request.user)
            voted.save()

            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class LoginView(LoginView):
    template_name = 'polls/registration/login.html'
    success_url = reverse_lazy('profile')


class LogoutView(LogoutView):
    template_name = 'polls/index.html'


class RegistrationView(CreateView):
    form_class = RegistrationUserForm
    template_name = 'polls/registration/registration.html'
    success_url = reverse_lazy('index')
