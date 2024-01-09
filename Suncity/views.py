from django.shortcuts import render, redirect, get_object_or_404
from .models import Program, CustomUser
from django.contrib import messages
from.forms import Search_Form,Program_Form,Signup_Form
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from PIL import Image
from io import BytesIO
from django.core.files.images import ImageFile 
from django.views import View
from django.views.generic.edit import FormView


# Create your views here.
def index(request):
    username = CustomUser
    return render(request,'indexe.html', {'username':username})


def logout_view(request):
    logout(request)


class SignUpView(FormView):
    template_name = 'signup.html'
    form_class = Signup_Form
    success_url = 'entry_success'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class FormSuccesView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("user created successfully")

#def sign_up(request):
 #   if request.method == 'POST':
  #      form = Signup_Form(request.POST)
   #     if form.is_valid():
   #         user = form.save()
   #         #login(request,user)
   #         return redirect('home')
    #else:
     #   form = Signup_Form()
    #return render(request, 'signup.html', {'form':form})

@login_required
def programs(request):
    program = Program.objects.all
    Form = Search_Form
    return render(request,'prog.html', {'program':program,'form':Form})



@login_required
def add_program(request, pk=None):
    if pk is not None:
        program = get_object_or_404(Program, pk= pk)
    else:
        program = None
    if request.method== "POST":
        form = Program_Form(request.POST, request.FILES, instance= program)
        if form.is_valid:
            program = form.save(False)
            image_field = form.cleaned_data.get('cover_photo')
            if image_field:
                image = Image.open(image_field)
                image.thumbnail = ((300, 300))
                image_data = BytesIO()
                image.save(fp=image_data, format= image_field.image.format)
                image_file = ImageFile(image_data)
                program.cover_photo.save(image_field.name, image_file)
                program.save()
                if program is None:
                    messages.success(request, "{}was updated".format(program))
                else:
                    messages.success(request,"{} was created".format(program))
            #new_program.save = True
            return redirect('home')
    else:
        form = Program_Form(instance=program)
    return render(request, 'addprog.html', {'Form':form, 'instance':program , 'model_type':'Program', 'is_file_upload':True})


#def Create_Accounts(request):
   
    