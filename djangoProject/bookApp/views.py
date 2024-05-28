from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
def index(request):
    books = Book.objects.filter(isbn=1,author__name="Dame")
    context = {'books': books}
    return render(request,'index.html', context)

def viewbooks(request, id):
    books = Book.objects.filter(id=id)
    context = {
        'books': books
    }
    return render(request, 'books_id.html', context)
def add(request):
    if request.method == "POST":
        form = BookForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user= request.user
            book.save()
            return redirect('index')

    return render(request,'bookadd.html', context={'form':BookForm})
# Create your views here.
