from django.shortcuts import render, redirect
from .forms import ThreadForm
from django.utils.text import slugify
from .models import Thread


def thread(request):
    """Handles user adding thread to the website"""
    # Make query to all objects at thread
    forums = Thread.objects.all()
    # Define var to count forms at page
    count = forums.count()
    # A dictionary that holds form and count
    context = {'forums': forums,
               'count': count, }
    # Everything went well render send the user to the posting thread success page
    return render(request, 'thread.html', context)


def add_thread(request):
    # Is it a post request ?
    if request.method == 'POST':
        # Instantiate a create thread form with the submitted data
        form = ThreadForm(data=request.POST)
        # The data are valid ?
        if form.is_valid():
            # Create a new thread object but don't save it to the database just yet
            new_form = form.save(commit=False)
            # request user name to put it in thread
            new_form.author = request.user
            # create friendly links
            new_form.slug = slugify(new_form.title)
            # save thread
            new_form.save()
            # to go to thread page
            return redirect('thread')
    else:
        # recreate thread if not
        form = ThreadForm()
        # A dictionary that holds form of thread
    context = {'form': form}
    # to represent add thread page
    return render(request, 'addInThread.html', context)
