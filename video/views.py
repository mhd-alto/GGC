from django.shortcuts import redirect, render
from django.utils.text import slugify
from video.forms import VideoForm
from video.models import Video


def add_video(request):
    # Is it a post request ?
    if request.method == 'POST':
        # Instantiate a Vermiform with the submitted data
        form = VideoForm(data=request.POST)
        # The data are valid ?
        if form.is_valid():
            # Create a new video object but don't save it to the database just yet
            new_form = form.save(commit=False)

            new_form.author = request.user

            new_form.slug = slugify(new_form.title)
            # Since we got a video for save it to the database
            new_form.save()
            # SAve tags
            form.save_m2m()
            # Everything went well render send the user to the registration success page
            return redirect('video')

    # Not a POST request
    else:
        # Instantiate an empty instance of both Videoform
        form = VideoForm()
    # A dictionary that holds the data to be sent to the corresponding html page
    context = {'form': form}
    # Registration wasn't successful for some reason so render the registration page with empty forms
    return render(request, 'videoadd.html', context)


def video(request):
    videos = Video.objects.all()
    count = videos.count()
    context = {'videos': videos, 'count': count}
    return render(request, 'video.html', context)
