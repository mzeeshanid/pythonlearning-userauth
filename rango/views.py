from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime

from rango.forms import UserForm, UserProfileForm, CategoryForm, Category


def home(request):

    context = RequestContext(request)

    if request.session.get('last_visit'):
        last_visit_time = request.session.get('last_visit')
        visits = request.session.get('visits', 0)

        if (datetime.now() - datetime.strptime(last_visit_time[:-7], "%Y-%m-%d %H:%M:%S")).seconds > 1:
            request.session['visits'] = visits + 1
            request.session['last_visit'] = str(datetime.now())

        print "last visit exisits in session" + str(visits)
        
    else:
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = 1

    return render_to_response('rango/index.html', {}, context)


def register(request):
    if request.session.test_cookie_worked():
        print ">>>> TEST COOKIE WORKED!"
        request.session.delete_test_cookie()
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    param = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
    return render_to_response('rango/register.html', param, context)


def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/rango/')
            else:
                return HttpResponse('Your rango account is disabled')
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse('Invalid login details supplied.')
    else:
        return render_to_response('rango/login.html', {}, context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/rango/')


def categories(request):
    context = RequestContext(request)

    if request.user.is_authenticated():
        categories = Category.objects.filter(user=request.user)
    else:
        categories = Category.objects.all()

    return render_to_response('rango/categories.html', {'categories' : categories}, context)


@login_required
def add_category(request):
    context = RequestContext(request)

    category_added = False
    if request.method == 'POST':
        category_form = CategoryForm(data=request.POST)

        if category_form.is_valid():
            category = category_form.save(commit=False)
            category.user = request.user
            print "this is userid: " + str(request.user)
            category.save()

            category_added = True
        else:
            print category_form.errors
    else:
        category_form = CategoryForm()

    param = {'category_form' : category_form, 'category_added' : category_added}
    return render_to_response('rango/addcategory.html', param, context)