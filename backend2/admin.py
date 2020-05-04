from django.contrib import admin

from backend2.models import Server, Hersteller, Lager

@admin.register(Server)
class ServerAdmin(admin.ModelAdmin) :
    #list_filter = ('title', )
    #search_fields = ('preis', 'description')
    pass


@admin.register(Hersteller)
class HerstellerAdmin(admin.ModelAdmin) :
    pass
    #list_display = ('__str__', 'description')


@admin.register(Lager)
class LagerAdmin(admin.ModelAdmin) :
    pass