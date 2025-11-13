from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('', include('book.urls')),
]

#setting.py　のMEDIA_URLの場所を示す
# requestされたurlとMEDIA_URL で指定した文字列が合致したとき。次のdocument_rootで定義した画像を呼び出す
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
