from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Employee, Population


def index(request):
    return redirect('form')


def form(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullName', '').strip()
        age = request.POST.get('age', '').strip()

        if not full_name or not age:
            messages.error(request, '⚠️ กรุณากรอกข้อมูลให้ครบทุกช่อง')
            return render(request, 'form.html', {
                'full_name': full_name,
                'age': age,
            })

        try:
            age_int = int(age)
            if age_int < 1 or age_int > 120:
                messages.error(request, '❌ อายุต้องอยู่ระหว่าง 1-120 ปี')
                return render(request, 'form.html', {
                    'full_name': full_name,
                    'age': age,
                })
        except ValueError:
            messages.error(request, '❌ กรุณากรอกอายุเป็นตัวเลข')
            return render(request, 'form.html', {
                'full_name': full_name,
                'age': age,
            })

        Population.objects.create(
            full_name=full_name,
            age=age_int,
        )
        messages.success(request, f'✅ บันทึกข้อมูลของ {full_name} เรียบร้อยแล้ว!')
        return redirect('form')

    return render(request, 'form.html')


def contact(request):
    return render(request, 'contact.html')


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})
