class SchemaFormMixin:
    """
    Mixin for schema form customization.
    """
    
    @property
    def page_header(self):
        raise NotImplementedError
    
    @property
    def page_button(self):
        raise NotImplementedError
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_header'] = self.page_header
        context['page_button'] = self.page_button
        return context
