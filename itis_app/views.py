from django.shortcuts import render
from django.contrib import messages

from itis_app.forms import DataUploadForm
from itis_app.core.start_check import start
from itis_app.models import AnalysisResult


def index(request):
    context = {
        'title': 'SSZ Site',
    }
    if request.method == 'POST':
        form = DataUploadForm(data=request.POST)
        if form.is_valid():
            print(request.POST)
            age = request.POST['age']
            cr_ph = request.POST['creatinine_phosphokinase']
            ej_fr = request.POST['ejection_fraction']
            platelets = request.POST['platelets']
            time = request.POST['time']

            death_event = start(age, cr_ph, ej_fr, platelets, time)

            result = AnalysisResult(age=age, creatinine_phosphokinase=cr_ph, ejection_fraction=ej_fr,
                                    platelets=platelets, time=time, death_event=death_event)
            result.save()

            context['result'] = bool(death_event)

        else:
            messages.info(request, 'Format Error: Form not valid!')

    else:
        form = DataUploadForm()

    context['form'] = form

    return render(request, 'itis_app/index.html', context)
