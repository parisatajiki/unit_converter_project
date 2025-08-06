from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import Quantity


class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data()
        context['quantitis'] = Quantity.objects.all()
        return context


class Weight_converter(View):
    def get(self, request):
        quantity = Quantity.objects.get(title="Weight")
        return render(request, 'converter_app/weight.html', {'quantity': quantity})

    def post(self, request):
        quantity = Quantity.objects.get(title="Weight")
        number = float(request.POST.get('number'))
        result = 0
        from_unit = request.POST.get('from_unit')
        to_unit = request.POST.get('to_unit')
        if from_unit != 'grams(g)':
            # convert to gram
            if from_unit == 'milligrams(mg)':
                number = number / 1000

            elif from_unit == 'kilograms(kg)':
                number = number * 1000

            elif from_unit == 'tons(t)':
                number = number * 1000000

        if to_unit == 'grams(g)':
            result = number
        elif to_unit == 'milligrams(mg)':
            result = number * 1000

        elif to_unit == 'kilograms(kg)':
            result = number / 1000
        elif to_unit == 'tons(t)':
            result = number / 1000000
        return render(request, 'converter_app/weight.html', {'result': result, 'quantity': quantity})


class Temperature_converter(View):
    def get(self, request):
        quantity = Quantity.objects.get(title="temperature")
        return render(request, 'converter_app/temperature.html', {'quantity': quantity})

    def post(self, request):
        quantity = Quantity.objects.get(title="temperature")
        number = float(request.POST.get('number'))
        result = 0
        from_unit = request.POST.get('from_unit')
        to_unit = request.POST.get('to_unit')
        if from_unit != 'celsius(°C)':
            # convert to gram
            if from_unit == 'fahrenheit(°F)':
                number = (number - 32)*(5/9)

            elif from_unit == 'kelvin(K)':
                number = number - 273.15

        if to_unit == 'celsius(°C)':
            result = number
        elif to_unit == 'fahrenheit(°F)':
            result = number * (9/5) + 32

        elif to_unit == 'kelvin(K)':
            result = number + 273.15
        return render(request, 'converter_app/weight.html', {'result': result, 'quantity': quantity})

class Length_converter(View):
    def get(self, request):
        quantity = Quantity.objects.get(title="length")
        return render(request, 'converter_app/length.html', {'quantity': quantity})

    def post(self, request):
        quantity = Quantity.objects.get(title="length")
        result = 0
        from_unit = request.POST.get('from_unit')
        to_unit = request.POST.get('to_unit')
        number = float(request.POST.get('number'))
        if from_unit != 'meters(m)':
            if from_unit == 'millimeters(mm)':
                number = number / 1000
            elif from_unit == 'centimeters(cm)':
                number = number / 100
            elif from_unit == 'kilometers(km)':
                number = number * 1000
            elif from_unit == 'inches(in)':
                number = number * 0.0254

        if to_unit == 'meters(m)':
            result = number
        elif to_unit == 'millimeters(mm)':
            result = number * 1000
        elif to_unit == 'centimeters(cm)':
            result = number * 100
        elif to_unit == 'kilometers(km)':
            result = number / 1000
        elif to_unit == 'inches(in)':
            result = number / 0.0254
        return render(request, 'converter_app/weight.html', {'result': result, 'quantity': quantity})