from django import forms
from .models import Transaction
from accounts.models import UserBankAccount
from .constants import TRANSFER ,RECEIVED
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'amount',
            'transaction_type'
        ]

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account') # account value ke pop kore anlam
        super().__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled = True # ei field disable thakbe
        self.fields['transaction_type'].widget = forms.HiddenInput() # user er theke hide kora thakbe

    def save(self, commit=True):
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance
        return super().save()


class DepositForm(TransactionForm):
    def clean_amount(self): # amount field ke filter korbo
        min_deposit_amount = 100
        amount = self.cleaned_data.get('amount') # user er fill up kora form theke amra amount field er value ke niye aslam, 50
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit_amount} $'
            )

        return amount


class WithdrawForm(TransactionForm):

    def clean_amount(self):
        account = self.account
        min_withdraw_amount = 500
        max_withdraw_amount = 20000
        balance = account.balance # 1000
        amount = self.cleaned_data.get('amount')
        if amount < min_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at least {min_withdraw_amount} $'
            )

        if amount > max_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at most {max_withdraw_amount} $'
            )

        if amount > balance: # amount = 5000, tar balance ache 200
            raise forms.ValidationError(
                f'You have {balance} $ in your account. '
                'You can not withdraw more than your account balance'
            )

        return amount



class LoanRequestForm(TransactionForm):
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')

        return amount
    

class TransferForm(TransactionForm):
    to_account_no = forms.IntegerField()

    
    def clean_to_account_no(self):
        to_account_no = self.cleaned_data.get('to_account_no')
        try:
            UserBankAccount.objects.get(account_no=to_account_no)
        except UserBankAccount.DoesNotExist:
            raise forms.ValidationError('Invalid account number.')
        return to_account_no
    
    def clean_amount(self):
       amount = self.cleaned_data.get('amount')
       if amount <= 0:
           raise forms.ValidationError('Amount must be greater than zero.')
       if amount > self.account.balance:
            raise forms.ValidationError('You do not have sufficient balance for this transfer.')
       return amount
    
    def save(self, commit=True):
        to_account = UserBankAccount.objects.get(account_no=self.cleaned_data['to_account_no'])

        transaction_from = super().save(commit=False)
        transaction_from.account = self.account
        transaction_from.balance_after_transaction = self.account.balance - self.cleaned_data['amount']

        transaction_to = Transaction.objects.create(
            account=to_account,
            amount=self.cleaned_data['amount'],
            balance_after_transaction=to_account.balance + self.cleaned_data['amount'],
            transaction_type=TRANSFER,  
        )
        transaction_received = Transaction.objects.create(
            account=to_account,
            amount=self.cleaned_data['amount'],
            balance_after_transaction=to_account.balance + self.cleaned_data['amount'],
            transaction_type=RECEIVED,  
        )

        self.account.balance -= self.cleaned_data['amount']
        to_account.balance += self.cleaned_data['amount']

        if commit:
            self.account.save()
            to_account.save()
            transaction_from.save()
            transaction_to.save()

        return transaction_from, transaction_to,transaction_received
