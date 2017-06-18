from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline): # StackedInline
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text'] # 換順序
    fieldsets = [
        ('問題', {'fields': ['question_text']}),
        ('時間', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date', 'was_published_recently')

    list_filter = ['pub_date']

    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)