from django.shortcuts import render,redirect
from django.contrib import messages
from medinest.models import Service, Department, Doctor, DepartmentCategory, Doctorpage,FAQ,Testimonial
from .models import *
from medinest.forms import AppointmentForm, ContactForm

# Create your views here.
def home(request):
    # Dastlab formalarni bo'sh holda yaratamiz
    appointment_form = AppointmentForm()
    contact_form = ContactForm()

    if request.method == "POST":
        form_type = request.POST.get('form_type')

        if form_type == 'appointment':
            form = AppointmentForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Magliwmatlar tabisli jiberildi!")
                return redirect('home')
            else:
                print(form.errors.as_data())
                messages.error(request, f"Qatellik: {form.errors}")


        elif form_type == 'contact':

            form = ContactForm(request.POST)

            if form.is_valid():

                form.save()

                messages.success(request, "Magliwmatlar tabisli jiberildi!!")

                return redirect('home')

            else:
                print(form.errors)
                messages.error(request, f"Qatelik: {form.errors}")

    context = {
        'services': Service.objects.all(),
        'departments': Department.objects.all(),
        'doctors': Doctor.objects.all(),
        'home': Home.objects.last(),
        'about': About.objects.last(),
        'faq': FAQ.objects.all(),
        'departmentcategories': DepartmentCategory.objects.last(),
        'doctorpage': Doctorpage.objects.all(),
        'testimonials': Testimonial.objects.all(),
        'appointment_form': appointment_form,  # POST xatosi bo'lsa, o'sha xato bilan qaytadi
        'contact_form': contact_form,
    }

    return render(request, "index.html", context)
