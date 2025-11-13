from django.shortcuts import render, redirect
#from django.contrib.auth import logout
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Book, Review
# Create your views here.

def index_view(requesst):
    #print("テストテスト")
    object_list = Book.objects.order_by('category')
    return render(requesst, 'book/index.html',{'object_list': object_list})

class ListBookView(ListView):
    template_name = 'book/book_list.html'
    model = Book

class DetailBookView(DetailView):
    tempName = 'book/book_detail.html'
    model = Book

class CreateBookView(CreateView):
    template_name = 'book/book_create.html'
    model = Book
    fields = ['title', 'writter', 'text', 'category', 'thumbnail']
    #viewから名前を特定し、データを逆流 本来はbook->create
    success_url = reverse_lazy('list-book')

class DeleteBookView(DeleteView):
    template_name = 'book/book_delete.html'
    model = Book
    success_url = reverse_lazy('list-book')

class UpdateBookViews(UpdateView):
    template_name = 'book/book_update.html'
    model = Book
    fields = ['title', 'writter', 'text', 'category', 'thumbnail']
    success_url = reverse_lazy('list-book')

class CreateReviewView(CreateView):
    model = Review
    fields = ('book', 'title', 'text', 'rate')
    template_name = 'book/review_form.html'

    #Bookモデルからデータを取得
    #**kwags->urlに入力された数字を取得
    def get_context_data(self, **kwargs):
        #super()は継承元のメソッド(get_context_data())を呼び出します
        context = super().get_context_data(**kwargs)
        #選んだ書籍のデータを格納
        context['book'] = Book.objects.get(pk=self.kwargs['book_id'])
        #contextに情報を格納することで、データの追加をすることができる
        #print(context)
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        print("form_valid()が呼ばれました")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("⚠️ form_invalid: ", form.errors)
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('detail-book', kwargs={'pk': self.object.book.id})