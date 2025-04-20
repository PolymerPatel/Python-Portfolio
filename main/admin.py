from django.contrib import admin
from .models import Tag, Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    #specifies how many images to upload

class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "link"
    )
    inlines = [ProjectImageInline]
    search_fields = ("title", "description")
    list_filter = ("tag",)
    # search_fields defines how we search in this project - based on title or description
    
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    
admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)

#pass: pyp*rtf*lio