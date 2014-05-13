from django.conf import settings

def settings_context_processors(request):
    return { 
        'GRUNT_LIVE_RELOAD' : getattr(settings, 'GRUNT_LIVE_RELOAD', False),
        'GRUNT_LIVE_RELOAD_PORT' : getattr(settings, 'GRUNT_LIVE_RELOAD_PORT', 35729) 
    }