# djangocms-static-ace

This app provides the ace source code editor files under the static files urls for the django cms admin 
interface (plugin modals essentially).

It is only needed if the project does not have internet access, or, if it prefers third party resources 
not to be loaded over the internet.

This app is a conditional dependency of, potentially amongst others, `djangocms-frontend` and
`djangocms-snippet`. 

## Installation

The typical installation adds the `[static-ace]` optional argument to the add requiring ace, e.g., 
`djangocms-frontend[static-ace]`. If needed it can be installed explicitly by `pip install djangocms-static-ace`.

Finally, to make the static ace files available, they need to be declared in the projects `INSTALLED_APPS` setting:

    INSTALLED_APPS = [
        ...,
        "djangocms-static-ace",
        ...,
    ]

Once made available, compliant apps will load the ace editor locally from
static files.

## Using the ace editor for your own plugins

To make your own plugin aware of djangocms-static-ace you will need to define a custom form for your 
plugin (see xxx) and add a `Media` class

    from django.conf import settings as django_settings
    from django import forms

    from ... import MyFormModel


    class MyPluginForm(forms.ModelForm):

        class Media:
        js = (
            "admin/vendor/ace/ace.js"
            if "djangocms_static_ace" in django_settings.INSTALLED_APPS
            else "https://cdnjs.cloudflare.com/ajax/libs/ace/1.9.6/ace.js",
        )

        class Meta:
            model = MyFormModel


## Versions

Currently, django CMS uses ace 1.9.6
