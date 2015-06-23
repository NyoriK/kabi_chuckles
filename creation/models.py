from django.db import models
from django.utils import timezone
from time import time
from datetime import date
import re
from bs4 import BeautifulSoup


# TYPES = (
# 	('BL', 'BLOG'),
# 	('IL', 'ILLUSTRATIONS'),
# 	('IN', 'INSPIRATION'),
# 	('FA', 'FASHION'),
# 	('SN', 'SNAPS'),
# 	)

# class Content(models.Model):
# 	title = models.CharField(max_length=300, blank=True, null=True)
# 	description = models.TextField(blank=True, null=True)
# 	# image = models.ImageField(upload_to=get_upload_file_name, blank=True, null=True, default='')
# 	pubdate = models.DateTimeField(default=timezone.now)
# 	update = models.DateTimeField(default=timezone.now)
# 	# of_type = models.CharField(max_length=2,choices=TYPES)
# 	for_home = models.BooleanField(default=False)

# 	# publish = models.booleanfield(default=True)

# 	def __unicode__(self):
# 		return ("%s : %s") % (self.of_type, self.title)

def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" %(str(time()).replace('.','_'), filename)


class Home(models.Model):
	image1 = models.ImageField(upload_to=get_upload_file_name)
	image2 = models.ImageField(upload_to=get_upload_file_name)
	image3 = models.ImageField(upload_to=get_upload_file_name)
	image4 = models.ImageField(upload_to=get_upload_file_name)
	image5 = models.ImageField(upload_to=get_upload_file_name)
	image6 = models.ImageField(upload_to=get_upload_file_name)
	pubdate = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ['-pubdate']

	def __unicode__(self):
		return unicode(self.pubdate)


class Blog(models.Model):
	title = models.CharField(max_length=150, blank=True)
	description = models.TextField()
	first_image = models.CharField(max_length=200, blank=True)
	default_first_image_size = models.BooleanField(default=False)
	pubdate = models.DateTimeField(default=timezone.now)
	publish = models.BooleanField(default=False)


	def save(self, *args, **kwargs):
		# This regex will grab your first img url
		# Note that you have to use double quotes for the src attribute
		img = re.search('src="([^"]+)"'[4:], self.description)
		self.first_image = img.group().strip('"')
		super(Blog, self).save(*args, **kwargs)

	class Meta:
		ordering = ['-pubdate']

	def __unicode__(self):
		return ("%s : %s") % (self.pubdate, self.title)


class Illustration(models.Model):
	title = models.CharField(max_length=150, blank=True)
	description = models.TextField()
	first_image = models.TextField(blank=True)
	default_first_image_size = models.BooleanField(default=False)
	pubdate = models.DateTimeField(default=timezone.now)
	publish = models.BooleanField(default=True)

	def save(self, *args, **kwargs):
	    soup = BeautifulSoup(self.description)
	    self.first_image = soup.find('img')['src']
	    super(Illustration, self).save(*args, **kwargs)

	class Meta:
		ordering = ['-pubdate']

	def __unicode__(self):
		return ("%s : %s") % (self.pubdate, self.title)


class Inspiration(models.Model):
	title = models.CharField(max_length=150, blank=True)
	description = models.TextField()
	first_image = models.TextField(blank=True)
	pubdate = models.DateTimeField(default=timezone.now)
	publish = models.BooleanField(default=True)

	def save(self, *args, **kwargs):
		# This regex will grab your first img url
		# Note that you have to use double quotes for the src attribute
		img = re.search('src="([^"]+)"'[4:], self.description)
		self.first_image = img.group().strip('"')
		super(Inspiration, self).save(*args, **kwargs)

	class Meta:
		ordering = ['-pubdate']

	def __unicode__(self):
		return ("%s : %s") % (self.pubdate, self.title)

class Fashion(models.Model):
	title = models.CharField(max_length=150, blank=True)
	description = models.TextField()
	first_image = models.TextField(blank=True)
	pubdate = models.DateTimeField(default=timezone.now)
	publish = models.BooleanField(default=True)

	def save(self, *args, **kwargs):
		# This regex will grab your first img url
		# Note that you have to use double quotes for the src attribute
		img = re.search('src="([^"]+)"'[4:], self.description)
		self.first_image = img.group().strip('"')
		super(Fashion, self).save(*args, **kwargs)

	class Meta:
		ordering = ['-pubdate']

	def __unicode__(self):
		return ("%s : %s") % (self.pubdate, self.title)

class SnapGroup(models.Model):
	name = models.CharField(max_length=150, blank=True, null=True)
	date = models.DateField(default=date.today)

	def __unicode__(self):
		if self.name:
			return ("%s : %s") % (self.date, self.name)
		else:
			return unicode(self.date)

class Snap(models.Model):
	date = models.ForeignKey(SnapGroup)
	image = models.ImageField(upload_to=get_upload_file_name)
	caption = models.CharField(max_length=150, blank=True, null=True)

	class Meta:
		ordering = ['-date']

	def __unicode__(self):
		return ("%s : %s") % (self.date, self.caption)

class About(models.Model):
	description = models.TextField()
	pubdate = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ['-pubdate']

	def __unicode__(self):
		return unicode(self.pubdate)