# __BEGIN_LICENSE__
# Copyright (C) 2008-2010 United States Government as represented by
# the Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
# __END_LICENSE__

import re
import os

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.utils.http import urlquote
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
import django.contrib.auth.views

from geocamUtil.auth import getAccountWidget
from geocamUtil import anyjson as json

from responderMaps import settings


def welcome(request):
    return render_to_response('responderMaps/welcome.html',
                              {},
                              context_instance=RequestContext(request))

# @csrf_exempt
# def register(request, useJson=False):
#     if request.method == 'POST':

#         # Get Account Information from User Creation Form
#         user_form = ExtendedUserCreationForm(request.POST)
#         # profile_form = ProfileForm(request.POST)

#         if user_form.is_valid():
#             user = user_form.save()

#             if useJson:
#                 result = {"message": "created user %s" % user.username}
#                 if 'token' in request.POST:
#                     result['token'] = request.POST['token']
#                 return HttpResponse(json.dumps({"result": result}),
#                                     mimetype='application/json')

#             # profile_form = ProfileForm(request.POST, instance=user.get_profile())
#             # profile_form.save()

#             nextUrl = request.POST.get('next', reverse('home'))

#             user = authenticate(username=request.POST['username'], password=request.POST['password1'])

#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponseRedirect(nextUrl)

#             return HttpResponseRedirect(reverse('responderMaps_login') + '?next=%s' % nextUrl)
#         else:
#             if useJson:
#                 errInfo = {'code': -32099,
#                            'message': 'invalid value in form field',
#                            'data': user_form._get_errors()}
#                 return HttpResponseServerError(json.dumps({'error': errInfo}),
#                                                mimetype='application/json')

#     else:
#         # profile_form = ProfileForm()
#         user_form = ExtendedUserCreationForm()

#     # return render_to_response('registration/register.html',  { 'profile_form':profile_form, 'user_form':user_form })
#     return render_to_response('registration/register.html',
#                                 {'account_widget': getAccountWidget(request),
#                                  'user_form': user_form,
#                                 },
#                                 context_instance=RequestContext(request))


def checkLogin(request):
    return HttpResponse('ok')


def feature(request):
    return render_to_response('responderMaps/home.html',
                              {},
                              # {'account_widget': getAccountWidget(request)},
                              context_instance=RequestContext(request))


def mapJson(request):
    text = open(os.path.join(settings.STATIC_ROOT, 'responderMaps', 'js', 'map.json')).read()
    return HttpResponse(text,
                        mimetype='application/json')

def profile(request):
    if request.method == 'POST':
        # Get the user from the request
        u = User.objects.get(username=request.user.username)

        # Get the profile data, check if its valid, save if it is
        profile_form = ProfileForm(request.POST, instance=u.get_profile())
        if profile_form.is_valid():
            profile_form.save()

        # Get the user data, check if its valid, save if it is
        user_form = UserDataForm(request.POST, instance=u)
        if user_form.is_valid():
            user_form.save()
        else:
            # Populate the profile and user data forms with data from the db
            u = User.objects.get(username=request.user.username)

            # Need to wrap this because the user might not have a profile
            try:
                profile_form = ProfileForm(instance=u.get_profile())
            except:
                profile_form = ProfileForm()

            user_form = UserDataForm(instance=u)

        return render_to_response('manage/profile_manage.html',
                                  {'account_widget': getAccountWidget(request),
                                   'profile_form': profile_form,
                                   'user_form': user_form,
                                   },
                                  context_instance=RequestContext(request))
