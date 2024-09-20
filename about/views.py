from django.shortcuts import render
from .models import About
from .forms import CollaborateForm
from django.contrib import messages

def about(request):
    """
    Renders the About page
    """
    about_field = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()
    return render(
        request,
        "about/about.html",
        {
            "about": about_field,
            "collaborate_form": collaborate_form
            },
        )

def contact(request):
    """
    Renders the Contact page
    """
    if request.method == "POST":
        collaborate_form = CollaborateForm(request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, "Collaboration request received! I endeavour to respond within 2 working days.")
    collaborate_form = CollaborateForm()
    return render(
        request,
        "about/contact.html",
        {
            "collaborate_form": collaborate_form
            },
        )