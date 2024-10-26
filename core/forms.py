from django import forms
from .models import Profile, Task, FinancialTransaction, SavingsGoal, Message


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['role', 'bio', 'avatar']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to', 'status', 'due_date', 'reward']


class FinancialTransactionForm(forms.ModelForm):
    class Meta:
        model = FinancialTransaction
        fields = ['transaction_type', 'amount', 'description']


class SavingsGoalForm(forms.ModelForm):
    class Meta:
        model = SavingsGoal
        fields = ['goal_name', 'target_amount', 'saved_amount', 'due_date']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
