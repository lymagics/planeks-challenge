import json

from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse

from ..models import Schema, DataSet, ProcessingStatus
from ..utils import generate_csv


def generate_csv_data(request: HttpRequest, pk: int):
    """
    API endpoint to generate csv dataset based on existing schema.
    """

    if request.method == 'POST':
        success_status = ProcessingStatus.objects.filter(state='Success').first()
        processing_status = ProcessingStatus.objects.filter(state='Processing').first()

        schema = get_object_or_404(Schema, pk=pk)
        dataset = DataSet.objects.create(schema=schema, status=processing_status)

        json_data = json.loads(request.body)
        total = int(json_data.get('total', 10))

        dataset.path = generate_csv(dataset, total)
        dataset.status = success_status
        dataset.save()

        download_link = reverse('dataset_download', kwargs={'pk': dataset.pk})

        return JsonResponse({'download_link': download_link})

    return JsonResponse({}, status=405)
