from django.http import HttpRequest, FileResponse
from django.views.generic import DetailView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from extra_views import NamedFormsetsMixin, CreateWithInlinesView, UpdateWithInlinesView

from .forms import ColumnInline
from .models import Schema, DataSet
from .mixins import SchemaFormMixin


class SchemaCreateView(LoginRequiredMixin, SchemaFormMixin, 
                       NamedFormsetsMixin, CreateWithInlinesView):
    """
    Create new schema.
    """

    model = Schema
    inlines = (ColumnInline,)
    inlines_names = ('columns',)
    fields = ('name',)
    template_name = 'schema_form.html'
    page_header = 'New schema'
    page_button = 'Create'


class SchemaUpdateView(LoginRequiredMixin, SchemaFormMixin, 
                       NamedFormsetsMixin, UpdateWithInlinesView):
    """
    Update an existing schema.
    """

    model = Schema
    inlines = (ColumnInline,)
    inlines_names = ('columns',)
    fields = ('name',)
    template_name = 'schema_form.html'
    page_button = 'Save'

    @property
    def page_header(self):
        return self.get_object().name


class SchemaDetailView(LoginRequiredMixin, DetailView):
    """
    Display details of a schema.
    """

    model = Schema
    template_name = 'schema_detail.html'


class SchemaListView(LoginRequiredMixin, ListView):
    """
    List all schemas.
    """

    model = Schema
    template_name = 'schema_list.html'


class SchemaDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete an existing schema.
    """

    model = Schema
    template_name = 'schema_delete.html'
    success_url = reverse_lazy('schemas:list')


@login_required
def download_dataset(request: HttpRequest, pk: int):
    """
    Download an existing csv dataset.
    """

    dataset = get_object_or_404(DataSet, pk=pk)
    csv_file = dataset.csv_file.file
    return FileResponse(csv_file, as_attachment=True)
