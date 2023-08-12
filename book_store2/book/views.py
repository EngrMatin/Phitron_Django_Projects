from typing import Any, Dict, List
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AddBookForm
from .models import AddBook
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
# Function based view:
# def about(request):
#     return render(request, 'about.html')

# Class based view:
# Option 1. without defining view: just add path('about/', views.TemplateView.as_view(template_name='about.html')), in the urlpatterns in urls.py
# Option 2. Define Class based view
class MyTemplateView(TemplateView):
    template_name = 'about.html'
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context = {'name':'sakib', 'age':25}
        # print(kwargs)   # if we enter 12 after about/ in the url, it will print {'roll': 12} in the terminal
        context.update(kwargs)
        return context
    
    
# Function based view:
# def add_book(request):
#     if request.method == 'POST':
#         obj = AddBookForm(request.POST)
#         if obj.is_valid():
#             print(obj.cleaned_data)
#             obj.save()
#             return redirect("show_book")
#     else:
#         obj = AddBookForm()        
            
#     return render(request, 'add_book.html', {'form':obj})

# Class based view:
# class AddBookView(FormView):
#     model = AddBook
#     template_name = 'add_book.html'
#     form_class = AddBookForm
#     def form_valid(self, form):
#         form.save()
#         return redirect("show_book")
    
class AddBookView(CreateView):
    model = AddBook
    template_name = 'add_book.html'
    form_class = AddBookForm
    success_url = reverse_lazy('show_book')
    


# Function based view:
# def show_book(request):
#     book = AddBook.objects.all()
#     return render(request, 'show_book.html', {'book_list':book})


# Class based view:
class BookListView(ListView):
    model = AddBook
    template_name = 'show_book.html'
    context_object_name = 'book_list'
    # def get_queryset(self):
    #     return AddBook.objects.filter(category='Computer Science')
    
    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     # context = {'book_list' : AddBook.objects.filter(category='Computer Science')}
    #     context = {'book_list' : AddBook.objects.all().order_by('author')}
    #     return context
    ordering = ['-book_name']
    
    # def get_template_names(self):
    #     if self.request.user.is_superuser:
    #         template_name = 'superuser.html'
    #     elif self.request.user.is_staff:
    #         template_name = 'staff.html'
    #     else:
    #         template_name = self.template_name
    #     return [template_name]

class BookDetailsView(DetailView):
    model = AddBook
    template_name = 'book_details.html'
    context_object_name = 'book'
    pk_url_kwarg = 'id'


# Function based view:
# def edit_book(request, id):
#     book = AddBook.objects.get(pk=id)
#     form = AddBookForm(instance=book)
#     if request.method == 'POST':
#         obj = AddBookForm(request.POST, instance = book)
#         if obj.is_valid():
#             print(obj.cleaned_data)
#             obj.save()
#             return redirect("show_book")
#     return render(request, 'add_book.html', {'form':form})

# Class based view:
class UpdateBookView(UpdateView):
    model = AddBook
    template_name = 'add_book.html'
    form_class = AddBookForm
    success_url = reverse_lazy('show_book')


# Function based view:
# def delete_book(request, id):
#     book = AddBook.objects.get(pk=id).delete()
#     return redirect("show_book")

# Class based view:
class DeleteBookView(DeleteView):
    model = AddBook
    template_name = 'delete_alert.html'
    success_url = reverse_lazy('show_book')