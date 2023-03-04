from django.http import HttpRequest, FileResponse
from django.views.generic import DetailView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .forms import SchemaForm, ColumnFormSet, ColumnUpdateFormSet
from .models import Schema, DataSet


@login_required
def create_schema(request: HttpRequest):
    """
    View for creating a new schema.
    """

    if request.method == 'POST':
        schema_form = SchemaForm(request.POST)
        column_formset = ColumnFormSet(request.POST)

        if schema_form.is_valid() and column_formset.is_valid():
            schema = schema_form.save()
            column_formset.instance = schema
            column_formset.save()
            return redirect('schema_detail', pk=schema.pk)

    else:
        schema_form = SchemaForm()
        column_formset = ColumnFormSet()

    return render(request, 'schema_new.html', {'schema_form': schema_form, 'column_formset': column_formset})


@login_required
def update_schema(request: HttpRequest, pk: int):
    """
    View for updating an existing schema.
    """

    schema = get_object_or_404(Schema, pk=pk)

    if request.method == 'POST':
        schema_form = SchemaForm(request.POST, instance=schema)
        column_formset = ColumnUpdateFormSet(request.POST, instance=schema)

        if schema_form.is_valid() and column_formset.is_valid():
            schema = schema_form.save()
            column_formset.save()
            return redirect('schema_detail', pk=schema.pk)

    else:
        schema_form = SchemaForm(instance=schema)
        column_formset = ColumnUpdateFormSet(instance=schema)

    return render(request, 'schema_update.html', {
        'schema': schema,
        'schema_form': schema_form,
        'column_formset': column_formset,
    })


class SchemaDetailView(LoginRequiredMixin, DetailView):
    """
    View for displaying details of a schema.
    """

    model = Schema
    template_name = 'schema_detail.html'


class SchemaListView(LoginRequiredMixin, ListView):
    """
    View for listing all schemas.
    """

    model = Schema
    template_name = 'schema_list.html'


class SchemaDeleteView(LoginRequiredMixin, DeleteView):
    """
    View for deleting an existing schema.
    """

    model = Schema
    template_name = 'schema_delete.html'
    success_url = reverse_lazy('schema_list')


@login_required
def download_dataset(request: HttpRequest, pk: int):
    """
    View for downloading an existing csv dataset.
    """

    dataset = get_object_or_404(DataSet, pk=pk)

    csv_file = open(dataset.path, 'rb')

    return FileResponse(csv_file, as_attachment=True)
