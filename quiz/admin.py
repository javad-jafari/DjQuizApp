from django.contrib import admin
from . import models
from django.utils.html import format_html


@admin.register(models.Category)

class CatAdmin(admin.ModelAdmin):
	list_display = [
        'name',
        ]

@admin.register(models.Quizzes)

class QuizAdmin(admin.ModelAdmin):
	list_display = [
        'id', 
        'title',
        ]

class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer_text', 
        'is_right'
        ]

@admin.register(models.Question)

class QuestionAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        if obj.image:
            img = format_html('<img src="{}" style="width:100px; height:100px;" />'.format(obj.image.url))
        else:
            img = format_html('<p>{}</p>'.format('no image') )
        return img

    image_tag.short_description = 'Image'
    fields = [
        'title',
        'quiz',
        'image',
        ]
    list_display = [
        'image_tag',
        'title', 
        'quiz',
        'date_updated'
        ]
    inlines = [
        AnswerInlineModel, 
        ] 





@admin.register(models.Answer)

class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text', 
        'is_right', 
        'question',
        'user'
        ]
