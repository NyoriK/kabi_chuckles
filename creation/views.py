from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator

from models import Home, Blog, Illustration, Inspiration, Fashion, SnapGroup, About

# Create your views here.

def home(request):
	if Home.objects.all().count() > 0:
		slider_pics = Home.objects.latest('pubdate')
	else:
		slider_pics = 0

	return render(request, 'home.html', {
		'slider_pics':slider_pics
		})

################################################# BLOG
def blog(request):
	blogs_list = Blog.objects.all()

	paginator = Paginator(blogs_list, 5)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		blogs = paginator.page(page)
	except(EmptyPage, InvalidPage):
		blogs = paginator.page(page)

	# Get the index of the current page
	index = blogs.number - 1  # edited to something easier without index
	# This value is maximum index of your pages, so the last page - 1
	max_index = len(paginator.page_range)
	# You want a range of 7, so lets calculate where to slice the list
	start_index = index - 3 if index >= 3 else 0
	end_index = index + 3 if index <= max_index - 3 else max_index
	# My new page range
	page_range = paginator.page_range[start_index:end_index]

	return render(request, 'blogs.html', {
        'blogs': blogs,
        'page_range': page_range,
    })

def blog_detail(request, blog_pk):
	blog = Blog.objects.get(pk=blog_pk)

	return render(request, 'blog_detail.html', {
		'blog':blog
		})



############################################### ILLUSTRAION
def illustration(request):
	illustrations_list = Illustration.objects.all()

	paginator = Paginator(illustrations_list, 1)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		illustrations = paginator.page(page)
	except(EmptyPage, InvalidPage):
		illustrations = paginator.page(page)

	# Get the index of the current page
	index = illustrations.number - 1  # edited to something easier without index
	# This value is maximum index of your pages, so the last page - 1
	max_index = len(paginator.page_range)
	# You want a range of 7, so lets calculate where to slice the list
	start_index = index - 3 if index >= 3 else 0
	end_index = index + 3 if index <= max_index - 3 else max_index
	# My new page range
	page_range = paginator.page_range[start_index:end_index]

	return render(request, 'illustrations.html', {
        'illustrations': illustrations,
        'page_range': page_range,
    })

def illustration_detail(request, illustration_pk):
	illustration = Illustration.objects.get(pk=illustration_pk)

	return render(request, 'illustration_detail.html', {
		'illustration':illustration
		})



############################################### INSPIRATION
def inspiration(request):
	inspirations_list = Inspiration.objects.all()

	paginator = Paginator(inspirations_list, 1)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		inspirations = paginator.page(page)
	except(EmptyPage, InvalidPage):
		inspirations = paginator.page(page)

	# Get the index of the current page
	index = inspirations.number - 1  # edited to something easier without index
	# This value is maximum index of your pages, so the last page - 1
	max_index = len(paginator.page_range)
	# You want a range of 7, so lets calculate where to slice the list
	start_index = index - 3 if index >= 3 else 0
	end_index = index + 3 if index <= max_index - 3 else max_index
	# My new page range
	page_range = paginator.page_range[start_index:end_index]

	return render(request, 'inspirations.html', {
        'page_range': page_range,
		'inspirations':inspirations
		})

def inspiration_detail(request, inspiration_pk):
	inspiration = Inspiration.objects.get(pk=inspiration_pk)

	return render(request, 'inspiration_detail.html', {
		'inspiration':inspiration
		})




################################################ FASHION
def fashion(request):
	fashions_list = Fashion.objects.all()

	paginator = Paginator(fashions_list, 1)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		fashions = paginator.page(page)
	except(EmptyPage, InvalidPage):
		fashions = paginator.page(page)

	# Get the index of the current page
	index = fashions.number - 1  # edited to something easier without index
	# This value is maximum index of your pages, so the last page - 1
	max_index = len(paginator.page_range)
	# You want a range of 7, so lets calculate where to slice the list
	start_index = index - 3 if index >= 3 else 0
	end_index = index + 3 if index <= max_index - 3 else max_index
	# My new page range
	page_range = paginator.page_range[start_index:end_index]

	return render(request, 'fashion.html', {
        'page_range': page_range,
		'fashions':fashions
		})

def fashion_detail(request, fashion_pk):
	fashion = Fashion.objects.get(pk=fashion_pk)

	return render(request, 'fashion_detail.html', {
		'fashion':fashion
		})




############################################### SNAP
# def snaps(request):
# 	template = 'snapgroups.html'
# 	page_template = 'snaps.html'
# 	snapgroup = SnapGroup.objects.all()

# 	if request.is_ajax():
# 		template = page_template

# 	return render(request, template, {
# 		'page_template' = page_template
# 		'snapgroup':snapgroup
# 		})


# from endless_pagination.decorators import page_template

# def snaps(request,template = 'snaps.html',
#                   page_template = 'snapgroups.html' ):

#     context = {}    
#     snapgroup = SnapGroup.objects.order_by('-date')

#     context.update( {'snapgroup': snapgroup, 'page_template': page_template,} )

#     # override the template and use the 'page' style instead.
#     if request.is_ajax():
#         template = page_template

#     return render_to_response(
#         template, context, context_instance=RequestContext(request) )	

def snaps(request):
	snapgroup_list = SnapGroup.objects.all()

	paginator = Paginator(snapgroup_list, 2)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		snapgroup = paginator.page(page)
	except(EmptyPage, InvalidPage):
		snapgroup = paginator.page(page)

	# Get the index of the current page
	index = snapgroup.number - 1  # edited to something easier without index
	# This value is maximum index of your pages, so the last page - 1
	max_index = len(paginator.page_range)
	# You want a range of 7, so lets calculate where to slice the list
	start_index = index - 3 if index >= 3 else 0
	end_index = index + 3 if index <= max_index - 3 else max_index
	# My new page range
	page_range = paginator.page_range[start_index:end_index]

	return render(request, 'snaps.html', {
        'page_range': page_range,
		'snapgroup':snapgroup
		})




################################################ ABOUT
def about(request):
	if About.objects.all().count() > 0:
		about = About.objects.latest('pubdate')
	else:
		about = 0

	return render(request, 'about.html', {
		'about':about
		})