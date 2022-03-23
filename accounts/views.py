from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


# Create your views here.
def logedin(request):
    if request.method == 'POST':
        # Get Form Values

        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('index')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('logedin')
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        # Get Form Values

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if Password is matched
        if password == password2:

            # check user name
            if User.objects.filter(username=username).exists():
                messages.error(request, "User name taken")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email is bieng used")
                    return redirect('register')
                else:
                    # Every thing okay
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)

                    # Automatic login after registration use the below code:
                    # auth.login(request, user)
                    # messages.success(request, "You are now logged in")
                    # return redirect('index')

                    # After Registration go to login page for manual login.
                    user.save()
                    messages.success(request, "You are registered Successfully")
                    return redirect('logedin')

        else:
            messages.error(request, "password do not matched")
            return redirect('register')


    else:

        return render(request, 'accounts/register.html')


def logout(request):
    return render(request, 'accounts/login.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
