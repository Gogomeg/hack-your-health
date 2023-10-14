from django.contrib import admin
from .models import Post
from .models import Item
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')
