from django.contrib.auth.forms import UserCreationForm #ユーザー作成に特化
from django.contrib.auth.models import User #Userモデルに作成したデータを追加するため


class SignupForm(UserCreationForm):
    #本来の実装(この場合はForm)とは関係ない処理(この場合はModel)を書く際に使う
    class Meta:
        model = User
        fields = ('username',)

