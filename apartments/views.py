from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ApartmentDetailsUpdateForm, ApartmentQualitiesUpdateForm


@login_required
def updateApartment(request):
    if request.user.is_owner is False:
        return redirect('home')

    if request.method == 'POST':
        apartment_form = ApartmentDetailsUpdateForm(request.POST, instance=request.user.apartment)
        qualities_form = ApartmentQualitiesUpdateForm(request.POST, instance=request.user)
        if apartment_form.is_valid() and qualities_form.is_valid():
            apartment_form.save()
            qualities_form.save()
            return redirect('apartment-update')
    else:
        apartment_form = ApartmentDetailsUpdateForm(instance=request.user.apartment)
        qualities_form = ApartmentQualitiesUpdateForm(instance=request.user)

    context = {
        'apartment_form': apartment_form,
        'qualities_form': qualities_form
    }

    return render(request, 'apartments/update-apartment.html', context)
