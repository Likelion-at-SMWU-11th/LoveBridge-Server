from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import DocumentForm

class DocumentCreateView(FormView):
    template_name = "documents/documents.html"
    form_class = DocumentForm
    success_url = reverse_lazy('document_list')

    def form_valid(self, form):
        if self.request.FILES:
            form.instance.attached = self.request.FILES['upload']
        
        form.save()
        return super().form_valid(form)