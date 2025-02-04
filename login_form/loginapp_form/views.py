from django.shortcuts import render,redirect
from .models import user
from django.contrib import messages
def loginform(request):
    if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            data = user.objects.all()
            for data in data:
                if email == data.email and password == data.password: 
                    return redirect('/success/')
                else:
                    messages.error(request, 'Incorrect email or password.')
    return render(request, 'index.html')

def signform(request):
    if 'signup-btn' in request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')
        c_data = user(full_name=name, email=email, password=password, confirm_password=c_password)
        c_data.save()
        messages.success(request, "Your Account Has Been Created!")
    return render(request, 'sing_up.html')


def forgotform(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'forgot_password.html')
        data = user.objects.get(email=email)
        data.password = new_password
        data.confirm_password = confirm_password
        data.save()
        messages.success(request, "Your password has been successfully updated. Now You Can Login")
        # return redirect('/')  # Redirect to a success page or home
    return render(request, 'forgot_password.html')

def success_view(request):
    return render(request, 'success.html')