from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    return render(request, 'index.html', context={'num_books': num_books, 'num_instances': num_instances,
                                                  'num_instances_available': num_instances_available,
                                                  'num_authors': num_authors, 'num_visits': num_visits})


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book
    paginate_by = 5


class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author
    paginate_by = 25


class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_book_list'] = Book.objects.filter(author=self.object.id)
        return context
