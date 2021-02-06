from django.shortcuts import render
from .forms import UserRegistrationForm, ProfileForm
from .models import Profile


def register(request):
    """Handles user registration to the website"""
    # Is it a post request ?
    if request.method == "POST":
        # Instantiate a UserCreationForm and ProfileForm with the submitted data
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(data=request.POST, files=request.FILES)
        # The data are valid ?
        if user_form.is_valid() and profile_form.is_valid():
            # Create a new user object but don't save it to the database just yet
            new_user = user_form.save(commit=False)
            # Set the provided password as this registration's password
            new_user.set_password(user_form.cleaned_data["password"])
            # Since we got a password for this registration save it to the database
            new_user.save()
            # Create a profile that corresponds to this user with and set the given birthday and bio
            profile = Profile.objects.create(user=new_user,
                                             date_of_birth=profile_form.cleaned_data["date_of_birth"],
                                             bio=profile_form.cleaned_data["bio"])
            # Did the user submit a profile picture?
            # If so set it as their picture otherwise it's blank ("gonna add a default pic later)
            if request.FILES:
                profile.picture = profile_form.files["picture"]
            # Save the profile in case more data were provided
            profile.save()
            # A dictionary that holds the data to be sent to the corresponding html page
            context = {"new_user": new_user, "profile_form": profile_form}
            # Everything went well render send the user to the registration success page
            return render(request, 'temp_home.html', context)

    # Not a POST request
    else:
        # Instantiate an empty instance of both UserCreationForm and ProfileForm
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()
    # A dictionary that holds the data to be sent to the corresponding html page
    context = {"user_form": user_form, "profile_form": profile_form}
    # Registration wasn't successful for some reason so render the registration page with empty forms
    return render(request, "registration/register.html", context)
