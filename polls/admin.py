

# Register your models here.


from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):

	# Enable filtering by pub_date
    list_filter = ["pub_date"]

	# Enable searching by question_text
    search_fields = ["question_text"]

    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    


admin.site.register(Question, QuestionAdmin)