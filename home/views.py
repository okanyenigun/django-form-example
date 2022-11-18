from django.shortcuts import render, redirect
from django.views import View
from django.forms import formset_factory
from .forms import CustomerForm, AnyForm, PlayerForm, SquadForm
from .models import Customer

# class HomeView(View):

#     def get(self, request):
#         #form = CustomerForm()
#         # form = AnyForm()
#         # context= {"form": form}
#         # records = Customer.objects.all()
#         MyFormSet = formset_factory(PlayerForm, extra=2)
#         formset = MyFormSet()
#         print("MyFormSet: ",MyFormSet)
#         print("formset: ",formset)
#         context = {"formset":formset}
#         return render(request, './templates/home.html', context)

#     def post(self, request):
#         #print(request.POST)
#         form = CustomerForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect("home")

def squad_page(request):
    SquadFormSet = formset_factory(SquadForm, extra=1)
    formset = SquadFormSet()
    if request.method == "POST":
        formset = SquadFormSet(request.POST)
    return render(request, './templates/home.html', context={"formset":formset})