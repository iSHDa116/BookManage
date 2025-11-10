from django.urls import path
from . import views

urlpatterns = [
    #ホーム画面
    path('',views.index_view,name='index'),
    #書籍一覧ページ
    path('book/', views.ListBookView.as_view(), name='list-book'),
    #詳細ページ
    path('book/<int:pk>/detail', views.DetailBookView.as_view(), name='detail-book'),
    #作成画面
    path('book/create', views.CreateBookView.as_view(), name='create-book'),
    #削除画面
    path('book/<int:pk>/delete', views.DeleteBookView.as_view(), name="delete-book"),
    #編集画面
    path('book/<int:pk>/update', views.UpdateBookViews.as_view(), name='update-book'),
    #path('logout/' , views.logout_view, name='logout'),
]