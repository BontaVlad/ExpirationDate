import datetime

from django import forms
from django.contrib import admin
from django.forms import ValidationError
from django.utils import timezone

import reversion

from registers.models import (
    UpcomingFuneral, ExpiredGrave, Grave, FuneralMonument,
    AnnualOwnerlessDeathRegister, UpcomingFuneralArchive,
    GraveOwnershipRequestsRegister, GraveOwnership, AnnualDeathIndexRegister,
    GravesToExpireThisYear, GravesPayedThisYear, ContractsRegister
)


class UpcomingFuneralAdmin(reversion.VersionAdmin):
    list_display = ('deceased', 'grave', 'funeral_date',
                    'date_added')

    search_fields = ['grave', 'funeral_date', 'date_added']

    def get_queryset(self, request):
        queryset = self.model.objects.filter(
            funeral_date__gt=timezone.now())
        return queryset.order_by('funeral_date')


class UpcomingFuneralAdminArchive(reversion.VersionAdmin):
    list_display = ('deceased', 'grave', 'funeral_date',
                    'date_added')

    search_fields = ['grave', 'funeral_date', 'date_added']

    def get_queryset(self, request):
        queryset = self.model.objects.filter(
            funeral_date__lt=timezone.now())
        return queryset.order_by('funeral_date')


class GraveAdminForm(forms.ModelForm):

    def clean(self):
        if (self.cleaned_data.get('social_services_request')
                and self.cleaned_data.get('owner')):
            raise ValidationError("Can't set both owner and IML request")
        elif not (self.cleaned_data.get("social_services_request")
                  or self.cleaned_data.get('owner')):
            raise ValidationError("Owner or IML request must be set")

        if self.cleaned_data.get('owner'):
            if not self.cleaned_data.get('receipt_number'):
                raise ValidationError("Receipt number is mandatory if "
                                      "the grave has an owner")


class GraveAdmin(reversion.VersionAdmin):
    form = GraveAdminForm

    list_display = ('cemetery', 'owner', 'deceased',
                    'receipt_number', 'surface_area', 'parcel', 'row',
                    'position', 'social_services_request',
                    'render_image')

    list_display_links = ('cemetery', 'owner', 'deceased')

    search_fields = ['owner__first_name', 'owner__last_name',
                     'receipt_number', 'funeral_date']


class FuneralMonumentAdmin(reversion.VersionAdmin):
    form = GraveAdminForm
    list_display = ('cemetery', 'owner', 'deceased', 'receipt_number',
                    'surface_area', 'parcel', 'row', 'position',
                    'social_services_request', 'render_image')

    list_display_links = ('owner', 'deceased')

    search_fields = ['owner__first_name', 'owner__last_name',
                     'receipt_number']


class AnnualDeathIndexRegisterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'cemetery', 'parcel')

    search_fields = ['first_name', 'last_name']

    def get_queryset(self, request):
        q = self.model.objects.filter(grave__isnull=False)
        return q.order_by('last_name', '-date_of_death')

    def has_add_permission(self, request):
        return False


class AnnualOwnerlessDeathRegisterAdmin(admin.ModelAdmin):
    list_display = ('receipt_number', 'social_services_request', 'parcel',
                    'row', 'number')

    def get_queryset(self, request):
        return self.model.objects.filter(owner__isnull=True)

    def has_add_permission(self, request):
        return False


class GraveOwnershipRequestsRegisterAdmin(admin.ModelAdmin):
    list_display = ('current_number', 'registration_date',
                    'infocet_number', 'status')

    def get_queryset(self, request):
        return self.model.objects.all()

    # nobody has the right to delete a request, stated in docs
    def has_delete_permission(self, request, object=False):
        return False


class ExpiredGraveAdmin(admin.ModelAdmin):

    list_display = ('cemetery', 'owner', 'deceased',
                    'receipt_number', 'surface_area', 'parcel', 'row',
                    'position', 'social_services_request',
                    'render_image')

    list_display_links = ('cemetery', 'owner', 'deceased')

    search_fields = ['owner__first_name', 'owner__last_name',
                     'receipt_number', 'funeral_date']

    def has_add_permission(self, request):
        return False

    def get_queryset(self, request):
        expired_graves = GraveOwnership.objects.filter(
            expiration_date__lt=timezone.now())
        expired_grave_ids = [record.owned_grave.id
                             for record in expired_graves]
        return self.model.objects.filter(pk__in=expired_grave_ids)


class GravesToExpireThisYearAdmin(admin.ModelAdmin):

    list_display = ('cemetery', 'owner', 'deceased',
                    'receipt_number', 'surface_area', 'parcel', 'row',
                    'position', 'social_services_request',
                    'render_image')

    list_display_links = ('cemetery', 'owner', 'deceased')

    search_fields = ['owner__first_name', 'owner__last_name',
                     'receipt_number', 'funeral_date']

    def has_add_permission(self, request):
        return False

    def get_queryset(self, request):
        now = timezone.now()
        year_end = datetime.date(now.year + 1, 1, 1)

        to_expire = GraveOwnership.objects.filter(
            expiration_date__lt=year_end,
            expiration_date__gt=now)
        to_expire_ids = [record.owned_grave.id for record in to_expire]

        return self.model.objects.filter(pk__in=to_expire_ids)


class GravesPayedThisYearAdmin(admin.ModelAdmin):

    list_display = ('cemetery', 'owner', 'deceased',
                    'receipt_number', 'surface_area', 'parcel', 'row',
                    'position', 'social_services_request',
                    'render_image')

    list_display_links = ('cemetery', 'owner', 'deceased')

    search_fields = ['owner__first_name', 'owner__last_name',
                     'receipt_number', 'funeral_date']

    def has_add_permission(self, request):
        return False

    def get_queryset(self, request):
        now = timezone.now()
        lower_bound = datetime.date(now.year + 20, 1, 1)
        upper_bound = datetime.date(now.year + 20, now.month, now.day)
        payed = GraveOwnership.objects.filter(
            expiration_date__lt=upper_bound,
            expiration_date__gt=lower_bound)

        payed_ids = [record.owned_grave.id for record in payed]

        return self.model.objects.filter(pk__in=payed_ids)


class ContractsRegisterAdmin(admin.ModelAdmin):
    list_display = ('current_number', 'contract_number', 'release_date',
                    'first_name', 'last_name', 'address')

    def get_queryset(self, request):
        return self.model.objects.all()

admin.site.register(UpcomingFuneral, UpcomingFuneralAdmin)
admin.site.register(UpcomingFuneralArchive, UpcomingFuneralAdminArchive)
admin.site.register(Grave, GraveAdmin)
admin.site.register(FuneralMonument, FuneralMonumentAdmin)
admin.site.register(AnnualDeathIndexRegister, AnnualDeathIndexRegisterAdmin)
admin.site.register(AnnualOwnerlessDeathRegister,
                    AnnualOwnerlessDeathRegisterAdmin)
admin.site.register(GraveOwnershipRequestsRegister,
                    GraveOwnershipRequestsRegisterAdmin)
admin.site.register(ExpiredGrave, ExpiredGraveAdmin)
admin.site.register(GravesToExpireThisYear,
                    GravesToExpireThisYearAdmin)
admin.site.register(GravesPayedThisYear,
                    GravesToExpireThisYearAdmin)
admin.site.register(ContractsRegister, ContractsRegisterAdmin)
