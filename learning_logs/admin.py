from django.contrib import admin
from .models import Topic, Entry

# Register your models here.

admin.site.register(Topic)
admin.site.register(Entry) 



#to run this code, try running ***python manage.py runserver*** in the terminal 

## IN TERMINAL ##
#The command ***python manage.py shell*** (run in an active virtual environment) launches a Python interpreter that you can use to 
#explore the data stored in your project’s database.
# >>>from learning_logs.models import Topic 
# >>>Topic.objects.all()
#We can loop over a queryset just as we’d loop over a list