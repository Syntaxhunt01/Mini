from django.shortcuts import render

def bmi_view(request):
    bmi = None
    category = None

    if request.method == 'POST':
        weight = request.POST.get('weight')
        height = request.POST.get('height')

        try:
            weight = float(weight)
            height = float(height) / 100  # cm to meters

            bmi = round(weight / (height ** 2), 2)

            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 24.9:
                category = "Normal weight"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
            else:
                category = "Obese"

        except:
            bmi = "Invalid input"
            category = ""

    return render(request, 'index.html', {'bmi': bmi, 'category': category})
