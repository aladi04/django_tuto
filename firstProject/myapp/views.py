from django.shortcuts import render, redirect
from .form import ContactForm  # make sure the file is forms.py, not form.py

def home_view(request):
    return render(request, 'myapp/home.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contact-success')  # match the URL name
    else:
        form = ContactForm()  # create an empty form for GET requests

    context = {'form': form}
    return render(request, 'myapp/contact.html', context)

def contact_success_view(request):
    return render(request, 'myapp/contact_success.html')
