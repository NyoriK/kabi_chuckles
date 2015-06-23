from django.contrib import admin
from django import forms
from redactor.widgets import RedactorEditor
from models import Home, Blog, Illustration, Inspiration, Fashion, SnapGroup, Snap, About


# home

class HomeAdmin(admin.ModelAdmin):
	class Meta:
		model = Home

admin.site.register(Home, HomeAdmin)		


# blog

class BlogAdminForm(forms.ModelForm):
	class Meta:
		model = Blog
		widgets = {
			'description': RedactorEditor(),
		}

class BlogAdmin(admin.ModelAdmin):
	form = BlogAdminForm

admin.site.register(Blog, BlogAdmin)


# Illustration

class IllustrationAdminForm(forms.ModelForm):
	class Meta:
		model = Illustration
		widgets = {
			'description': RedactorEditor(),
		}

class IllustrationAdmin(admin.ModelAdmin):
	form = IllustrationAdminForm

admin.site.register(Illustration, IllustrationAdmin)


# Inspiration

class InspirationAdminForm(forms.ModelForm):
	class Meta:
		model = Inspiration
		widgets = {
			'description': RedactorEditor(),
		}

class InspirationAdmin(admin.ModelAdmin):
	form = InspirationAdminForm

admin.site.register(Inspiration, InspirationAdmin)


# Fashion

class FashionAdminForm(forms.ModelForm):
	class Meta:
		model = Fashion
		widgets = {
			'description': RedactorEditor(),
		}

class FashionAdmin(admin.ModelAdmin):
	form = FashionAdminForm

admin.site.register(Fashion, FashionAdmin)


# Snap

class SnapInline(admin.TabularInline):
	model = Snap
	extra = 1

class SnapGroupAdmin(admin.ModelAdmin):
	inlines = [SnapInline]

admin.site.register(SnapGroup, SnapGroupAdmin)


# About

class AboutAdminForm(forms.ModelForm):
	class Meta:
		model = About
		widgets = {
			'description': RedactorEditor(),
		}

class AboutAdmin(admin.ModelAdmin):
	form = AboutAdminForm

admin.site.register(About, AboutAdmin)