from django.shortcuts import render, redirect
from app.models import Client, Matter, Document, Bundle
from app.forms import ClientForm, MatterForm, DocumentForm, BundleForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from app.lib.create_bundle import bundle_documents
# Create your views here.

def home(request):
    return render(request,'app/index.html', {})

###
# Create a new Client
###
@login_required
def new_client(request):
    form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            return redirect('new_matter')
    return render(request,'app/new_client.html', {'form':form})

###
# Create a new Matter and Assign a Client to it
###
@login_required
def new_matter(request):
    form = MatterForm()
    if request.method == "POST":
        form = MatterForm(request.POST)
        if form.is_valid():
            client = form.save()
            return redirect('new_bundle')
    return render(request,'app/new_matter.html', {'form':form})

###
#  Update an existing Matter
###

class MatterUpdate(UpdateView):
    model = Matter
    form_class = MatterForm

###
# Delete an existing Matter
###

class MatterDelete(DeleteView):
    model = Matter
    success_url = '/'


###
# Create a new Document
###
def new_document(request):
    form = DocumentForm()
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()
            return redirect('/')
    return render(request,'app/new_document.html', {'form':form})

###
# TODO: Fill in the details for the case
###
@login_required
def new_bundle(request):
    form = BundleForm()
    if request.method == "POST":
        form = BundleForm(request.POST)
        if form.is_valid():
            bundle = form.save()
            bundle_documents(bundle.id)
            return redirect('/api')
    return render(request,'app/new_bundle.html', {'form':form})

###
# Logout
###
from django.contrib import auth
def logout(request):
    auth.logout(request)
    return redirect('/')

###
#   
###
# from django.views.generic.detail import DetailView

class DocumentDetailView(UpdateView):
    model = Document
    form_class = DocumentForm

###
# REST API
###

from rest_framework import viewsets
from app.serializers import ClientSerializer, BundleSerializer, DocumentSerializer

class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class BundleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Bundle.objects.all()
    serializer_class = BundleSerializer
