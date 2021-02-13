from django.shortcuts import render, redirect
from django.utils.text import slugify
from .models import Review
from .forms import ReviewForm


def reviews_list(request):
    """Handles user adding review to the website"""
    # Make query to all objects at review
    forums = Review.objects.all()
    # Define var to count forms at page
    count = forums.count()
    # A dictionary that holds form and count
    context = {'forums': forums,
               'count': count, }
    # Everything went well render send the user to the posted reviews page
    return render(request, 'reviews/review.html', context)


def add_review(request):
    # Is it a post request ?
    if request.method == 'POST':
        # Instantiate a create review form with the submitted data
        form = ReviewForm(data=request.POST)
        # The data are valid ?
        if form.is_valid():
            # Create a new thread object but don't save it to the database just yet
            new_form = form.save(commit=False)
            # request user name to put it in thread
            new_form.author = request.user
            # Coverts the text into slug
            new_form.slug = slugify(new_form.title)
            # save review
            new_form.save()
            # save tags
            form.save_m2m()
            # to go to review page
            return redirect('review')
    else:
        # recreate review if not
        form = ReviewForm()
        # A dictionary that holds form of review
    context = {'form': form}
    # to represent add review page
    return render(request, 'reviews/addreview.html', context)
