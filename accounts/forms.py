from django import forms
from django.db.models import get_model
from django.utils.translation import ugettext_lazy as _

Account = get_model('accounts', 'Account')


class AccountForm(forms.Form):
    code = forms.CharField(label=_("Account code"))

    def clean_code(self):
        code = self.cleaned_data['code'].strip()
        try:
            self.account = Account.objects.get(
                code=code)
        except Account.DoesNotExist:
            raise forms.ValidationError(_(
                "No account found with this code"))
        return code
