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
from django.views.generic.edit import FormView, DeleteView
from django.utils import timezone


# Create your views here.
def index(request):
    username = CustomUser
    today = timezone.now().date()
    upcoming = Program.objects.filter(Date=today).order_by('-start_time') | Program.objects.filter(Date__gt=today).order_by('Date')
    return render(request,'indexe.html', {'username':username, 'upcoming':upcoming})

@login_required
def hub(request):
    user = CustomUser.objects.get(id=request.user.id)
    profile = Program.objects.filter(user = user)
    return render(request,'hub.html', {'profile':profile})

def logout_view(request):
    logout(request)
    return redirect('login')


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


def programs(request):
    program = Program.objects.all
    Form = Search_Form
    return render(request,'prog.html', {'program':program,'form':Form})




def add_program(request, pk=None):
    if pk is not None:
        program = get_object_or_404(Program, pk= pk)
    else:
        program = None
    if request.method== "POST":
        form = Program_Form(request.POST, request.FILES, instance= program)
        if form.is_valid:
            program = form.save(False)
            image_file = (form.cleaned_data['cover_photo'])
            if image_file:
                image = Image.open(image_file)
                size = 300, 500
                image.thumbnail(size, Image.Resampling.LANCZOS)
                image_data = BytesIO()
                image.save(fp=image_data, format= image.format)
                image_field = ImageFile(image_data)
                program.cover_photo.save(image_file.name, image_field)
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



def search(request):
    if request.method == 'POST':
        form = Search_Form(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_results = Program.objects.filter(name__icontains=query)
            return render(request, 'search_results.html', {'search_results': search_results, 'query':query,})
    else:
        form = Search_Form()
    return render(request, 'search.html', {'Form':form})



class ProgView(DeleteView):
    model = Program
    success_url = "my_hub"
    template_name = "delete_view.html"
    
    

#def Create_Accounts(request):

#class ProgramView(DetailView):
 #   model = Program
  #  template_name = 'prog.html'
   
    