from django.contrib.auth.forms import UserCreationForm

# UpdateView용 Form : ID란이 수정되지 못하게
class AccountUpdateForm(UserCreationForm):  # UserCreationForm 상속받아서
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].disabled = True  # username 필드를 disable
