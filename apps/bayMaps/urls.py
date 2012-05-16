# __BEGIN_LICENSE__
# Copyright (C) 2008-2010 United States Government as represented by
# the Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
# __END_LICENSE__

from django.conf.urls.defaults import *  # pylint: disable=W0401

from bayMaps import settings
from bayMaps import views

urlpatterns = patterns(
    '',

    url(r'^$', views.welcome,
        {},
        name='bayMaps_welcome'),

    url(r'^home/$', views.home,
        {},
        name='bayMaps_home'),

    url(r'^map.json$', views.mapJson,
        {},
        name='bayMaps_mapJson'),

    #url(r'^accounts/register/$', views.register,
    #    {'loginRequired': False},
    #    name='bayMaps_register'),

    # accounts
    url(r'^accounts/login/$', views.welcome, # 'django.contrib.auth.views.login',
        {'loginRequired': False,  # avoid redirect loop
         'securityTags': ['loginRelated']
         },
        name='bayMaps_login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        # show logout page instead of redirecting to log in again
        {'loginRequired': False,
         'securityTags': ['loginRelated']
         },
        name='bayMaps_logout'),

    url(r'^m/checkLogin/$', views.checkLogin,
        {'challenge': 'basic',
         'securityTags': ['dumbClient']},
        name='bayMaps_checkLogin'),

#    url(r'^m/register/$', views.register,
#        {'loginRequired': False,
#         'securityTags': ['loginRelated'],
#         'useJson': True},
#        name='bayMaps_register'),

    )

if settings.USE_STATIC_SERVE:
    urlpatterns += patterns(
        '',

        (r'^data/(?P<path>.*)$', 'geocamUtil.views.staticServeWithExpires.staticServeWithExpires',
         {'document_root': settings.DATA_DIR,
          'show_indexes': True,
          'readOnly': True}))
