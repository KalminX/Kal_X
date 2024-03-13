from django.contrib import admin

# Register your models here.
from .models import (
    UserProfile,
    Post,
)


admin.site.register(UserProfile)
admin.site.register(Post)