from django.views.generic.base import TemplateView


class HomePage(TemplateView):
    template_name = "homepage.html"


class HelpPage(TemplateView):
    template_name = "helppage.html"


class LicensePage(TemplateView):
    template_name = "licensepage.html"
