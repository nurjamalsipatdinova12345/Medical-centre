from django.contrib import admin
from .models import Doctor,Department,Service,DepartmentCategory,Doctorpage,Appointment,Contact,FAQ,Testimonial
admin.site.register(DepartmentCategory)
admin.site.register(Doctor)
admin.site.register(Department)
admin.site.register(Service)
admin.site.register(Doctorpage)
admin.site.register(Appointment)
admin.site.register(Contact)
admin.site.register(FAQ)
admin.site.register(Testimonial)
# Register your models here.
