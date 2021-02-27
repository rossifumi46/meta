from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Psychoterapist, Method
import json

def doctors(request):
    response = []
    doctors = Psychoterapist.objects.all().values('id', 'name', 'photo')
    print(doctors)
    for doctor in doctors:
        doctor['methods'] = list(Method.objects.filter(psychoterapist__pk=doctor['id']).values('name'))
        response.append(doctor)
    data = json.dumps(response, ensure_ascii=False).encode('utf8')
    return HttpResponse(data, content_type="application/json")