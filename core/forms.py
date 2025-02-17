from django.forms import ModelForm, forms
from .models import (
    Question, Blog, Report, Media, Initiative
)


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'gender', 'number', 'question', 'answer', 'is_fqa', 'is_suggestion', 'answer_time']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full'
        self.fields['is_fqa'].widget.attrs.update({'class':'m-1 w-10'})
        self.fields['is_suggestion'].widget.attrs.update({'class':'m-1 w-10'})


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image', 'category',]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full'


        
class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['name', 'description', 'file', 'category']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full'


class MediaForm(ModelForm):
    class Meta:
        model = Media
        fields = ['name', 'category', 'file',]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full'


class InitiativeForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image', 'category',]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full'


