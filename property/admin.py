from django.contrib import admin

from .models import Complaint, Flat, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ["town", "address"]
    readonly_fields = ["created_at"]
    list_display = [
        "address",
        "price",
        "new_building",
        "construction_year",
        "town",
    ]
    list_editable = ["new_building"]
    list_filter = ["new_building", "rooms_number", "has_balcony"]
    raw_id_fields = ["liked_by"]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ["сomplaining_user", "flat"]


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ["flats"]
    search_fields = ["full_name", "owners_phonenumber", "owner_pure_phone"]
    list_display = [
        "full_name",
        "owners_phonenumber",
        "owner_pure_phone",
        "get_owner_flats",
    ]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
