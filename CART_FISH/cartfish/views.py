
from django.shortcuts import render,redirect
from cartfish.forms import SignUpForm
from cartfish.models import Aqua
from cartfish.forms import PostForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    return render(request,'cartfish/index.html')

# @login_required
# def loginproduct(request):
#     return render(request,'cartfish/products.html')

@login_required
def login(request):
    return render(request,'registration/login.html')

def disSignUp(request):
    form=SignUpForm
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return redirect('reset/')
    return render(request,'registration/signup.html',{'form':form})

def home(request):

	if request.method =='POST':

		# Pass the form data to the form class
		details = PostForm(request.POST)

		# In the 'form' class the clean function
		# is defined, if all the data is correct
		# as per the clean function, it returns true
		if details.is_valid():

			# Temporarily make an object to be add some
			# logic into the data if there is such a need
			# before writing to the database
			post = details.save(commit = False)

			# Finally write the changes into database
			post.save()

			# redirect it to some another page indicating data
			# was inserted successfully
			return redirect('/contus/')
			
		else:
		
			# Redirect back to the same page if the data
			# was invalid
			return render(request, "cartfish/contact_us.html", {'form':details})
	else:

		# If the request is a GET request then,
		# create an empty form object and
		# render it into the page
		form = PostForm(None)
		return render(request, "cartfish/contact_us.html", {'form':form})

def aboutme(request):
    return render(request,'cartfish/about.html')


class AquaListView(ListView):
    model = Aqua
    template_name = 'cartfish/aqua_list.html'
    context_object_name = 'aqua'

class AquaDetailView(DetailView):
    model = Aqua
    template_name = 'cartfish/aqua_detail.html'
    context_object_name = 'aqua'
    
class AquaCreateView(CreateView):
    model = Aqua
    fields = ('id','image','fishname','orgin','quantity','price')

class AquaUpdateView(UpdateView):
    model = Aqua
    fields = '__all__'

class AquaDeleteView(DeleteView):
    model = Aqua
    success_url = reverse_lazy('list')