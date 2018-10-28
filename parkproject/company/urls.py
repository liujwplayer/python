from django.conf.urls import include, url
from django.contrib import admin

from company.views import CompanyView, CompaniesView

urlpatterns = [
    url(r'^companies$', CompanyView.as_view()),
    url(r'^companies/(?P<company_id>\w+)$', CompaniesView.as_view())


]