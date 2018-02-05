from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from .forms import NameGetter
import json
# Create your views here.

def index(request):
    if request.method == 'GET':
        form = NameGetter(request.GET)
        if form.is_valid():
            greeting = request.GET['greeting']
            name = request.GET['name']
            message = "message"
            resp_data = {message: greeting + ' ' + name, }
            jsonObject = json.dumps(resp_data, cls=DjangoJSONEncoder)
            print(jsonObject)
            return render(request, 'index.html', {'form': jsonObject})
        else:
            form = NameGetter()
            return render(request, 'index.html', {'form': form})
    else:
        form = NameGetter()
        return render(request, 'index.html', {'form': form})

