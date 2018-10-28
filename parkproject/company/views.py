# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from company.forms import CompanyForm
from company.models import Company


@method_decorator(csrf_exempt, name='dispatch')
class CompanyView(View):

    def post(self, request):
        res = CompanyForm(request.POST)  # 表单接受
        if not res.is_valid():
            return HttpResponse(status=422)
        company = Company.objects.create(company_name=res.data['company_name'])
        return HttpResponse(
            json.dumps({'company_id': company.company_id,
                        'created_time': str(company.created_time)}), status=201)

    def get(self, request):
        companys = Company.objects.all()
        companys_list = []
        for company in companys:
            companys_list.append(company.detail_info())
        print(companys_list)
        return HttpResponse(companys_list)


@method_decorator(csrf_exempt, name='dispatch')
class CompaniesView(View):

    def get(self, request, company_id):
        try:
            company = Company.objects.get(company_id=company_id)
        except Company.DoesNotExist:
            return HttpResponse(status=404)
        return JsonResponse(company.detail_info())

    def put(self, request, company_id):
        stream = request.body.decode()
        json_data = json.loads(stream)
        try:
            c = Company.objects.get(company_id=company_id)
        except Company.DoesNotExist:
            return HttpResponse(status=404)
        c.company_name = json_data['company_name']
        c.save()
        return HttpResponse(status=204)

    def delete(self, request, company_id):
        company = Company.objects.filter(company_id=company_id).delete()
        return HttpResponse(status=204)
