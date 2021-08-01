from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from datetime import datetime

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


def get_number_details(model_class, model_number: int) -> dict:
    res = {}
    model_path = model_class.objects.filter(
            model_number=model_number
        )
    res =  model_path[0].to_dict() if model_path else model_class().to_dict()
    return res


# Create your views here.
def index(request):
    details_dict = {}
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dob = request.POST['date_of_birth']
        fortune_day = datetime.today()   
        
        birthday = datetime.strptime(dob, '%Y-%m-%d')
        # calculate
        numerology_results = Pythagorean(
            first_name=first_name,
            last_name=last_name,
            birthdate=dob,
            verbose=False
        )
        details_dict['info'] = numerology_results.key_figures
        details_dict['dob'] = datetime.strptime(dob, '%Y-%m-%d').strftime('%d-%m-%Y')
        details_dict['fortune_day'] = fortune_day.strftime('%d-%m-%Y')  

        # chi so nam ca nhan - current year
        curr_year_num = Pythagorean.get_numerology_sum(
            (birthday.day, birthday.month, fortune_day.year), master_number=True
        )
        curr_month_num = Pythagorean.get_numerology_sum((curr_year_num, fortune_day.month), master_number=False)

        next_year_num = Pythagorean.get_numerology_sum(
            (birthday.day, birthday.month, fortune_day.year+1), master_number=True
        )

        # life path
       
        details_dict['lifepath'] = get_number_details(
            model_class=LifePath,
            model_number=numerology_results.life_path_number
        )
        # destiny path
        details_dict['destinypath'] =get_number_details(
            model_class=DestinyPath,
            model_number=numerology_results.destiny_number
        )

        # hearth desire
        details_dict['hearthdesire'] =get_number_details(
            model_class=HearthDesire,
            model_number=numerology_results.hearth_desire_number
        )

        # Personality
        details_dict['personality'] =get_number_details(
            model_class=Personality,
            model_number=numerology_results.personality_number
        )

        # Power path
        details_dict['powerpath'] =get_number_details(
            model_class=PowerPath,
            model_number=numerology_results.power_number
        )     

        # Active path
        details_dict['activepath'] =get_number_details(
            model_class=ActivePath,
            model_number=numerology_results.active_number
        )           
       
        # Legacy path
        details_dict['legacypath'] =get_number_details(
            model_class=LegacyPath,
            model_number=numerology_results.legacy_number
        )             

        # Expression path
        details_dict['expressionpath'] =get_number_details(
            model_class=ExpressionPath,
            model_number=numerology_results.destiny_number
        )                 
         

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
