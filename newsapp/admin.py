from django.contrib import admin
from .models import New, Person, Partner, Comment, Service


@admin.register(New)
class NewsAdmin(admin.ModelAdmin):
	list_display = ("title", "date", "is_publish")
	date_hierarchy = "date"
	search_fields = ["title"]
	ordering = ["-date"]
	list_filter = ["is_publish", "date"]

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
	list_display = ("name", "occupation")
	search_fields = ["name"]
	ordering = ["name"]


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
	list_display = ("name", )
	search_fields = ("name", )
	ordering = ["name"]	

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ["name", "phone", "email"]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	list_display = ["title"]
