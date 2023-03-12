from extra_views import InlineFormSetFactory

from .models import Column


class ColumnInline(InlineFormSetFactory):
    model = Column
    fields = ('name', 'datatype', 'order',)
    factory_kwargs = {'extra': 1}
