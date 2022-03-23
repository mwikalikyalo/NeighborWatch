from django.shortcuts import render, redirect
from .models import Post, Business, Neighborhood, Profile
from .forms import CreateUserForm, ProfileForm, BusinessForm, PostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    if request.user.profile.neighborhood == None:
        messages.success(request, 'Please fill out you Neighbourhood')
        return redirect('profile')
    else:
        neighbor_details = Neighborhood.objects.get(
            name=request.user.profile.neighborhood)
        businesses = Business.objects.filter(
            neighborhood=request.user.profile.neighborhood)
        updates = Post.objects.filter(
            neighborhood=request.user.profile.neighborhood)

        parameters = {
            'neighbor_details': neighbor_details,
            'businesses': businesses,
            'updates': updates,
        }
        return render(request, 'home.html', parameters)
        

@login_required(login_url='/accounts/login/')
def profile(request):
    print(request.GET)
    if request.method == 'POST':
        print(request.POST)
        createuserform = CreateUserForm(request.POST or None, instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        businessform = BusinessForm(request.POST)
        postform = PostForm(request.POST)

        current_neighbourhood = request.user.profile.neighborhood

        if createuserform.is_valid and profileform.is_valid():
            createuserform.save()
            profileform.save()
            messages.success(request, 'Profile updated successfully')

        if businessform.is_valid():
            business = businessform.save(commit=False)
            business.username = request.user
            business.neighborhood = current_neighbourhood
            business.save()

        if postform.is_valid():
            post = postform.save(commit=False)
            post.postuser = request.user
            post.neighborhood = current_neighbourhood
            post.save()

        return redirect('updateprofile')
        
    current_user = Profile.objects.get(username=request.user)
    createuserform = CreateUserForm(instance=request.user)
    profileform = ProfileForm(instance=request.user.profile)
    businessform = BusinessForm()
    postform = PostForm()

    allbusiness = Business.objects.filter(username=request.user)
    updates = Post.objects.filter(postuser=request.user)

    params = {
        'current_user': current_user,
        'createuserform': createuserform,
        'profileform': profileform,
        'businessform': businessform,
        'postform': postform,
        'allbusiness': allbusiness,
        'updates': updates
    }
    return render(request, 'profile.html', params)


@login_required(login_url='/accounts/login/')
def find(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        searchresults = Business.searchbusiness(search_term)
        return render(request, 'find.html', {'searchresults': searchresults, 'search_term': search_term})
    else:
        return redirect('home')

def searchajax(request):
    search_term = request.GET.get('search')
    searchresults = Business.searchbusiness(search_term)
    data = {
        'searchresults':searchresults,
        'search_term':search_term
    }
    return JsonResponse(data)









     