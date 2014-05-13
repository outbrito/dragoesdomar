from django.db import models
from tagging.fields import TagField
from tagging_autocomplete_tagit.widgets import TagAutocompleteTagIt
from django.contrib.admin.widgets import AdminTextInputWidget

# The following code is based on models.py file from django-tinymce by Joost Cassee

class TagAutocompleteTagItField(TagField):
    """
    TagField with jQuery UI Tag-it widget
    """
    
    def __init__(self, *args, **kwargs):
        super(TagAutocompleteTagItField, self).__init__(*args, **kwargs)
    
    def formfield(self, **kwargs):
        defaults = {'widget': TagAutocompleteTagIt()}
        defaults.update(kwargs)

        # As an ugly hack, we override the admin widget
        if defaults['widget'] == AdminTextInputWidget:
            defaults['widget'] = TagAutocompleteTagIt()

        return super(TagAutocompleteTagItField, self).formfield(**defaults)

from south.modelsinspector import add_introspection_rules
rules = [
    (
        (TagAutocompleteTagItField, ),
        [],
        {
            "blank": ["blank", {"default": True}],
            "max_length": ["max_length", {"default": 255}],
        },
    ),
]
add_introspection_rules(rules, ["^tagging_autocomplete_tagit\.models",])