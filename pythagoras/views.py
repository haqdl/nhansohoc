from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

from numerology import Pythagorean


from .models import (
    LifePath,
    DestinyPath,
    HearthDesire,
    Personality,
    PowerPath,
    ActivePath,
    LegacyPath,
    ExpressionPath
)
from .forms import CandidateForm


# Create your views here.
def index(request):
    details_dict = {}
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dob = request.POST['date_of_birth']
        # calculate
        numerology_results = Pythagorean(
            first_name=first_name,
            last_name=last_name,
            birthdate=dob,
            verbose=True
        )
        details_dict['info'] = numerology_results.key_figures
        # life path
        life_path = LifePath.objects.filter(
            life_path_number=numerology_results.life_path_number_alternative
        )
        if life_path:
            details_dict['lifepath'] = life_path[0].meaning

        # destiny path
        destiny_path = DestinyPath.objects.filter(
            destiny_path_number=numerology_results.destiny_number
        )
        if destiny_path:
            details_dict['destinypath'] = destiny_path[0].meaning

        # hearth desire
        hearth_desire = HearthDesire.objects.filter(
            hearth_desire_number=numerology_results.hearth_desire_number
        )
        if hearth_desire:
            details_dict['hearthdesire'] = hearth_desire[0].meaning

        # Personality
        personality = Personality.objects.filter(
            personality_number=numerology_results.personality_number
        )
        if personality:
            details_dict['personality'] = personality[0].meaning

        # Power path
        power_path = PowerPath.objects.filter(
            power_number=numerology_results.power_number
        )
        if power_path:
            details_dict['powerpath'] = power_path[0].meaning

        # Active path
        active_path = ActivePath.objects.filter(
            active_number=numerology_results.active_number
        )
        if active_path:
            details_dict['activepath'] = active_path[0].meaning

        # Legacy path
        legacy_path = LegacyPath.objects.filter(
            legacy_number=numerology_results.legacy_number
        )
        if legacy_path:
            details_dict['legacypath'] = legacy_path[0].meaning
        # Expression path
        expression_path = ExpressionPath.objects.filter(
            expression_number=numerology_results.destiny_number
        )
        if legacy_path:
            details_dict['expressionpath'] = expression_path[0].meaning            

    candidate_form = CandidateForm()
    return render(
        request,
        'pythagoras/index.html',
        {'form': candidate_form, 'details': details_dict}
    )


def details(request, index_number=0):
    response = "Details for %s"
    return HttpResponse(response % index_number)


def results(request, index_number=0):
    response = "Index Number %s"
    return HttpResponse(response % index_number)
