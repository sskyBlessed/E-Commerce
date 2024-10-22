from rest_framework import viewsets
from rest_framework.response import Response
from django.apps import apps
from .models import CustomBaseProductModel, create_custom_model

class CustomModelViewSet(viewsets.ViewSet):

    def list(self, request):
        custom_models = apps.get_models(include_auto_created=True)
        data = [model._meta.model_name for model in custom_models if isinstance(model, CustomBaseProductModel)]
        return Response(data)

    def create(self, request):
        model_name = request.data.get('model_name')
        fields = request.data.get('fields')
        CustomModel = create_custom_model(model_name, fields)
        return Response({'status': 'created', 'model_name': model_name})

