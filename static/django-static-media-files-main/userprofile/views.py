

from django.shortcuts import render
from .models import Obstacle

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import messages 
from .forms import SignUpForm


def login_user (request):
	if request.method == 'POST': #if someone fills out form , Post it 
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:# if user exist
			login(request, user)
			messages.success(request,('Youre logged in'))
			return redirect('profile') #routes to 'home' on successful login  
		else:
			messages.success(request,('Error logging in'))
			return redirect('login') #re routes to login page upon unsucessful login
	else:
		return render(request, 'login.html', {})

 
def register_user(request):
	if request.method =='POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			print("yes")
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request,user)
			messages.success(request, ('Youre now registered'))
			return redirect('login')
	else: 
		print("no")
		form = SignUpForm() 

	context = {'form': form}
	return render(request, 'register.html', context)



def profile(request):
    if request.method == 'POST':
        s = request.POST.get('from')
        r = request.POST.get('to')
        s2=s
        r2=r
        s1=s.lower()
        s=s1.split(',',1)
        s = s[0].strip()
        r1=r.lower()
        r=r1.split(',',1)
        r= r[0].strip()
        
        obstacles = Obstacle.objects.filter(destination_address=r, source_address=s)
        if not obstacles.exists():
            obstacles = Obstacle.objects.filter(destination_address=s, source_address=r)
        obst_locations=[]
        if obstacles.exists():
            obst_locations = [obstacle.where for obstacle in obstacles]
            return render(request, "index1.html", {'r': r2, 's': s2, 'obst': obst_locations})
        else:
            return render(request, "index1.html", {'r': r2, 's': s2, 'obst':obst_locations})
    else:
        return render(request, 'index.html', {})
    



def func(request):
    if request.method == 'POST':
        # Retrieve the form data
        where = request.POST.get('where')
        point1 = request.POST.get('point1')
        point2 = request.POST.get('point2')
        
        # Create an Obstacle object
        obstacle = Obstacle.objects.create(
            where=where,
            source_address=point1,
            destination_address=point2
        )
        
        # Optionally, you can save the object to the database
        obstacle.save()
        return render(request, 'index.html', {})
    return render(request, 'obs.html', {})

