import json

from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse

from ..models import Schema, DataSet


def generate_csv_data(request: HttpRequest, pk: int):
    """
    API endpoint to generate csv dataset based on existing schema.
    """
    
    if request.method == 'POST':
        schema = get_object_or_404(Schema, pk=pk)
        dataset = DataSet.objects.create(schema=schema)

        json_data = json.loads(request.body)
        total = int(json_data.get('total', 10))

        dataset.generate(total)
        dataset.save()

        download_link = reverse('schemas:download', kwargs={'pk': dataset.pk})

        return JsonResponse({'download_link': download_link})

    return JsonResponse({}, status=405)
