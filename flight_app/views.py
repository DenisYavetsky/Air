from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
from .parse import read_file
from .models import Airport


def main(request):
    return HttpResponse()


def airports_list(request):
    airports = Airport.objects.all()
    return render(request, 'Airports.html', context={'airports': airports})


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            with open('source/air.json', 'wb+') as destination:
                for chunk in request.FILES['file'].chunks():
                    print(chunk)
                    destination.write(chunk)

            read_file()
            return redirect('AirportsList')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

