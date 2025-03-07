from django.views.generic import TemplateView
from .forms import CustomUserCreationForm,SummaryForm
from django.views.generic import CreateView, DetailView, DeleteView, ListView
from django.urls import reverse, reverse_lazy
from .models import Summarization
from .utils import summary,keywords
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

class HomeView(TemplateView):
    template_name = "summarizer/home.html"


class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def form_valid(self, form):
        user = form.save()
        print(f"User {user.username} created successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("login")


class SumListView(LoginRequiredMixin, ListView):
    model = Summarization  # Use model instead of queryset for automatic template naming
    template_name = 'summarizer/summarization_list.html'  # Explicit template path
    context_object_name = 'summarizations'  # Recommended for clearer template context


class SumDetailView(LoginRequiredMixin, DetailView):
    model = Summarization
    template_name = "summarizer/detail.html"


class SumCreateView(LoginRequiredMixin, CreateView):
    model = Summarization
    form_class = SummaryForm
    template_name = "summarizer/create.html"


    def form_valid(self, form):
        instance = form.save(commit=False)

        sum_res = summary(instance.text, instance.depth)[0]["summary_text"]

        instance.user = self.request.user  # Assign the logged-in user
        instance.title = "Generated Summary"  # Placeholder title
        instance.summary = sum_res  # Generate summary
        instance.keywords = keywords(sum_res)

        instance.save()

        return super().form_valid(form)


    def get_success_url(self):
        return reverse("summary_detail", kwargs={"pk": self.object.id})


class SumDeleteView(LoginRequiredMixin, DeleteView):
    model = Summarization
    template_name = 'summarizer/delete.html'
    success_url = reverse_lazy('summary_list')

