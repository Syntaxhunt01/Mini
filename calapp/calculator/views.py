from django.shortcuts import render

# Create your views here.

def calculator_view(request):
    result = None
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        operator = request.POST.get('operator')

        try:
            n1 = float(num1)
            n2 = float(num2)

            if operator == '+':
                result = n1 + n2
            elif operator == '-':
                result = n1 - n2
            elif operator == '*':
                result = n1 * n2
            elif operator == '/':
                result = n1 / n2 if n2!=0 else '∞ (Cannot divide by 0)'

            else:
                result = 'Invaild operator'

        except ValueError:
            result = 'Invaild input'

    return render(request, 'index.html', {'result': result})
