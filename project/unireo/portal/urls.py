from re import A
from django.contrib import admin
from django.urls import path,include
from portal.views.home import home

from .views.universitysignup import universitysignup
from .views.universitylogin import universitylogin
from .views.universitylogin import logout

from .views.univprofile import univdetail
from .views.univprofile import univcon
from .views.univprofile import univsecurity
from .views.newcourse import courses
from .views.newcourse import savedcourses
from .views.newcourse import coursesoverview
from .views.events import editevents
from .views.events import addevents
from .views.home import overview
from .views.home import support
from .views.home import security
from .views.home import newapplication
from .views.home import inprogressapplication
from .views.home import rejectedapplication

# from.views.payments import payment,charge


from .views.home import events
from .views.home import addblog
from .views.home import allblog
from .views.univappli import Univappli
from .views.home import table


from .views.home import stu_reject
from .views.home import stu_accept
from .views.home import landing



#student
from .views.studentsignupandlogin import studentsignup
from .views.studentsignupandlogin import studentlogin
from .views.studentsignupandlogin import logout1

from .views.home import student
from .views.student_home import stu_profile
from .views.student_home import stu_overview
from .views.student_home import testoverview
from .views.stdprofile import stdhome
from .views.student_home import stu_saved
from .views.student_home import stu_search
from .views.student_home import stu_settings
from .views.student_home import stu_support
from .views.student_home import stu_applied
from .views.student_home import stu_search

#from .views.student_home import personal_details
from .views.stdprofile import stdacd
from .views.stdprofile import stdcour
from .views.stdprofile import stdind
from .views.stdprofile import stdpro
from .views.stdprofile import stdsaved
from .views.stdprofile import stdsecurity
from .views.stdprofile import stdappli
from .views.stdprofile import stdapplicour
from .views.temp_pass import emailvalid
from .views.temp_pass import tempvalidator
from .views.temp_passstd import emailvalidstd
from .views.temp_passstd import tempvalidatorstd



from .views.student_home import professional
from .views.student_home import academic
from .views.student_home import password
from .views.student_home import progressbar
from .views.student_home import preference
#Agent
from .views.agentsignup import agentsignup
from .views.agentlogin import agentlogin
from .views.agentlogin import logout
from .views.temp_passagent import emailvalidagent
from .views.temp_passagent import tempvalidatoragent

from .views.agent_home import agent_home
from .views.agent_home import agent_application
from .views.agent_home import agent_inprogress_application
from .views.agent_home import agent_rejected_application
from .views.agent_home import new_applicant
from .views.agent_home import agent_security
from .views.agent_home import agent_support
from .views.agent_home import agent_academic
from .views.agent_home import agent_overview
from .views.agent_home import agent_update
from .views.agent_home import agent_new_application
from .views.agent_home import Consultbank
from .views.agent_home import viewcommision

from .views.login import login
from .views.login import new_student_signup
from .views.login import new_university_signup
from .views.agent_home import agent_course
from .views.agent_home import agent_personal
from .views.agent_home import agent_professional
from django.contrib.auth import views as auth_views

#employee
from .views.employee import Empdeatails
from .views.employee import Allemp

#super_admin

from .views.admin import Home
from .views.admin import Courses
from .views.admin import Settings
from .views.admin import students
from .views.admin import universities
from .views.admin import agent
from .views.admin import commision
from .views.admin import addcommision,adminlogin,adminlogout,addemployee



urlpatterns=[
     path('unihome',home,name="home"),
    #path('oauth/', include('social_django.urls', namespace='social')), 
     path('',landing,name='landing'),
    path('universitysignup',universitysignup.as_view(),name='universitysignup'),
    path('universitylogin',universitylogin.as_view(),name='universityloginpage'),
    path('univlogout',logout,name='unilogout'),
    path('stdlogout',logout1,name='stdlogout'),
    path('univdetail',univdetail.as_view(),name='univdetail'),
    path('univcon',univcon.as_view(),name='univcon'),
    path('univsecurity',univsecurity.as_view(),name='univsecurity'),
    path('addcourses',courses.as_view(),name='courses'),
    path('savedcourses/<str:name>/<str:name1>/',savedcourses.as_view(),name='savedcourses'),
    path('savedcourses/<str:name>/<str:name1>/',savedcourses.as_view(),name='savedcourses'),
    path('savedcourses',savedcourses.as_view(),name='savedcourses'),
    path('logout1/', auth_views.LogoutView.as_view(next_page='studentloginpage'), name='logout1'),
    path('coursesoverview/<str:name>/',coursesoverview.as_view(),name='coursesoverview'),
    path('editevents',editevents.as_view(),name='editevents'),
    path('addevents',addevents.as_view(),name='addevents'),
    path('newapplication',newapplication,name="name"),
    path('rejected',rejectedapplication,name="name"),
    path('inprogressapplication',inprogressapplication,name='name'),
    path('applicants',table,name='table'),
    path('security',security,name="name"),
    #path('courseCards',cards,name="cards")
    path('overview/<str:name>/',overview.as_view(),name='overview'),
    path('support',support,name="support"),
    path('support',support,name="support"),
    path('events',events.as_view(),name="events"),
    path('events/<str:name>/<str:name1>/',events.as_view(),name="events"),
    path('events/<str:name>/<str:name1>/',events.as_view(),name="events"),

    path('addblog',addblog.as_view(),name="addblog"),
    path('allblogs',allblog.as_view(),name="allblog"),
    path('allblogs/<str:name>/<str:name1>/',allblog.as_view(),name="allblog"),
    path('allblogs/<str:name>/<str:name1>/',allblog.as_view(),name="allblog"),

    path('applicationform',Univappli.as_view(),name="Univappli"),
    path('student',student,name="nme"),
    
    #student_portal urls
    path('testoverview',testoverview,name='testoverview'),
    path('studentsignup',studentsignup.as_view(),name='studentsignup'),
    path('studentlogin',studentlogin.as_view(),name='studentloginpage'),
    path('student/home',stdhome.as_view(),name="stdhome"),
    path('student/saved',stdsaved.as_view(),name="saved"),
    path('student/search',stu_search.as_view(),name="search"),
    path('student/overview',stu_overview,name="overview1"),
    path('student/overview/<str:name>',stu_overview,name="overview1"),
    path('student/settings',stu_settings,name="home"),
    path('student/support',stu_support,name="home"),
    path('student/progress/<str:name>',progressbar,name='progress'),

    # path('payment/<str:name>/<str:name1>',payment,name="payment"),
    # path('charge/<str:name>/<str:name1>',charge,name="charge"),

    path('student/saved/<str:name>/',stdsaved.as_view(),name="saved"),
    path('student/search/<str:name>/',stu_search.as_view(),name="search"),
    path('stdappli/<str:name>/<str:name1>/applicationform/<str:name2>',stdapplicour.as_view(),name="stdappli"),
    path('stdappli/<str:name>/<str:name1>/applicationform/',stdapplicour.as_view(),name="stdappli"),
    
    path('stdappli/<str:name>/<str:name1>/',stdappli.as_view(),name="stdappli"),
    
    path('student/profile',stu_profile,name="profile"),
    path('student/applied',stu_applied,name="applied"),
    path('student/security',stdsecurity.as_view(),name="stdsecurity"),
    
    path('student/password',password,name="password"),
    #path('student/preference',preference,name="password"),
    path('stdacd',stdacd.as_view(),name='stdacd'),
    path('stdcour',stdcour.as_view(),name='stdcour'),
    path('stdind',stdind.as_view(),name='stdind'),
    path('stdpro',stdpro.as_view(),name='stdpro'),


    path('student/application/<str:name>/accept',stu_accept.as_view(),name="accept"),
    path('student/application',stu_accept.as_view(),name="accept"),
    path('student/application/<str:name>/reject',stu_reject,name="reject"),

    path('emailvalid',emailvalid.as_view(),name='emailvalid'),
    path('tempvalidator',tempvalidator.as_view(),name='tempvalidator'),
    path('emailvalidstd',emailvalidstd.as_view(),name='emailvalidstd'),
    path('tempvalidatorstd',tempvalidatorstd.as_view(),name='tempvalidatorstd'),
    path('emailvalidagent',emailvalidagent.as_view(),name='emailvalidagent'),
    path('tempvalidator',tempvalidatoragent.as_view(),name='tempvalidatoragent'),
    #agent_portal
    path('agent/home',agent_home,name="agent_home"),
    path('agent/application',agent_application,name="name"),
    path('agent/inprogress',agent_inprogress_application,name="name"),
    path('agent/rejected',agent_rejected_application,name="name"),
    path('agent/newapplicant',new_applicant,name="name"),
    path('agent/security',agent_security.as_view(),name='name'),
    path('agent/support',agent_support,name="name"),
    path('agent/academic',agent_academic.as_view(),name='name'),
    path('agent/course',agent_course.as_view(),name="course"),
    path('agent/personal',agent_personal.as_view()),
    path('agent/professional',agent_professional.as_view(),name="professional"),
    path('agent/newappli',agent_new_application,name="name") ,
    path('login',login,name="name"),

    path('newstusignup',new_student_signup,name="name"),
    path('newunisignup',new_university_signup,name="name"),
    path('agent/overview',agent_overview,name="overview"),
    path('agent/update',agent_update,name="update"), 

    path('agentsignup',agentsignup.as_view(),name='agentsignup'),
    path('agentlogin',agentlogin.as_view(),name='agentloginpage'),
    path('agentlogout',logout,name='agentlogout'),
    #super_admin

    
    path('admin/home',Home,name="adminhome"),
    path('admin/courses',Courses,name="home"),
    path('admin/settings',Settings.as_view(),name="home"),
    path('admin/universities',universities,name="home"),
    path('admin/students',students,name="home"),
    path('admin/agent',agent,name="home"),
    path('admin/commision',commision.as_view(),name="commision"),
    path('admin/addcommision/<str:name>',addcommision.as_view(),name="addcommision"),
    path('agent/viewcommision',viewcommision.as_view(),name="viewcommision"),
    path('admin/addemployee',addemployee.as_view(),name="addemployee"),
    

    path('adminlogout',adminlogout,name='adminlogout'),
    path('adminlogin',adminlogin.as_view(),name='adminlogin'),
    path('addemployee',Empdeatails.as_view(),name='addemployee'),
    path('employees',Allemp,name='addemployee'),
    path('Cdetails',Consultbank.as_view(),name="Consultancy"),

    


]
# handler404 = 'portal.views.error.error_404'
# #handler500 = 'portal.views.error.error_500'
# handler403 = 'portal.views.error.error_403'
# handler400 = 'portal.views.error.error_400'