import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from company.models import Company
from park.forms import ParkForm
from park.models import Park



@method_decorator(csrf_exempt, name='dispatch')
class ParkView(View):
    def post(self, request):
        res = ParkForm(request.POST)
        if not res.is_valid():
            return HttpResponse(status=422)
        company, x = Company.objects.get_or_create(company_id=res.data.get('company_id'))
        park = Park.objects.create(
            park_name=res.data.get('park_name'),
            company_id=company.company_id
        )
        result = {'park_id': park.park_id, 'created_time': str(park.created_time)}
        return HttpResponse(json.dumps(result), status=201)

    def get(self, request):
        res = ParkForm(request.GET)
        if not res.is_valid():
            return HttpResponse(status=422)
        park = Park.objects.filter(park_name__contains=res.data)
        listl = []
        for x in park:
            listl.append(x.detail_info())
        return HttpResponse(listl)

@method_decorator(csrf_exempt, name='dispatch')
class ParksView(View):
    pass