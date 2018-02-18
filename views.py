from django.shortcuts import render
from django.views import generic
from .models import Marker
from .forms import MarkerModelForm, MarkerHiddenModelForm
# Create your views here.


class MarkerBaseView(object):
    model = Marker


class MarkerCreateView(MarkerBaseView, generic.CreateView):
    form_class = MarkerHiddenModelForm
