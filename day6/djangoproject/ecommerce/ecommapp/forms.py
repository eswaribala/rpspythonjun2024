from django import forms
from ecommapp.models import Employee,HLM,MLM,LLM
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"


class HLMForm(forms.ModelForm):
    class Meta:
        model = HLM
        fields = "__all__"

class MLMForm(forms.ModelForm):
    class Meta:
        model = MLM
        fields = "__all__"
class LLMForm(forms.ModelForm):
    class Meta:
        model = LLM
        fields = "__all__"