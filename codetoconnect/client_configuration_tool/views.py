from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest

from client_configuration_tool.models import ClientConfigurations
# from client_config_change_apis import get_client_configurations

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def api(request: HttpRequest):
    return get_client_configurations(request)
