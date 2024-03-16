from django.contrib import admin

from .models.universityinfo import University

from .models.univdetail import Univdetail
from .models.univdetail import Univcon
from .models.courses import Courses
from .models.eventsinfo import Event
from .models.eventsinfo import Blog
from .models.application import Application
#student
from .models.studentinfo import Student

from .models.stddetail import Stdind
from .models.stddetail import Stdacd
from .models.stddetail import Stdpro
from .models.stddetail import Stdpro1
from .models.stddetail import Stdcour
# Register your models here.
from .models.stdappli import Stdappli

from .models.consultancyinfo import Consultancy
from .models.offer import Offerletter
from .models.superadmin import Superadmin
from .models.addemployee import Addemployee

from .models.saved import Saved
from .models.employeeinfo import Employee
from .models.consultdetails import Consultancydetails
from .models.coursecommision import Coursecommision

# Register your models here.
admin.site.register(University)

admin.site.register(Univdetail)
admin.site.register(Univcon)
admin.site.register(Courses)
admin.site.register(Event)
admin.site.register(Blog)
admin.site.register(Application)

admin.site.register(Student)
admin.site.register(Stdind)
admin.site.register(Stdcour)
admin.site.register(Stdacd)
admin.site.register(Stdpro)
admin.site.register(Stdpro1)
admin.site.register(Saved)
admin.site.register(Stdappli)
admin.site.register(Consultancy)

admin.site.register(Offerletter)
admin.site.register(Employee)
admin.site.register(Consultancydetails)
admin.site.register(Coursecommision)
admin.site.register(Superadmin)
admin.site.register(Addemployee)