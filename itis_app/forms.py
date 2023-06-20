from django import forms

from itis_app.models import AnalysisResult

default_widget_class = 'form-control py-4'


class DataUploadForm(forms.Form):
    age = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Возраст'}))
    creatinine_phosphokinase = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Креатинфосфокиназа'}))
    ejection_fraction = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Выброс фракций'}))
    platelets = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Тромбоциты'}))
    time = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Время'}))

    class Meta:
        model = AnalysisResult
        fields = ('age', 'creatinine_phosphokinase', 'ejection_fraction', 'platelets', 'time')

    def __init__(self, *args, **kwargs):
        super(DataUploadForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = default_widget_class
