from django.shortcuts import render
from . models import MovieInfo
# Create your views here.
from . forms import MovieForm
def create(request):
    frm=MovieForm() #Movieform object creation => frm#
    if request.POST:
        frm=MovieForm(request.POST)
        if frm.is_valid:
            frm.save() #if valid it can save to database#
    else:
        frm=MovieForm    
    return render(request,'create.html',{'frm':frm})

def list(request):
    movie_set=MovieInfo.objects.all()
    print(movie_set)
    return render(request,'list.html',{'movies':movie_set})

def edit(request,pk):
    edit_instance=MovieInfo.objects.get(pk=pk) #get the primary key#
    if request.POST: #if sumbit click?#
        frm=MovieForm(request.POST,instance=edit_instance)
        if frm.is_valid():
            edit_instance.save() #save the text#
    else:
        frm=MovieForm(instance=edit_instance)
    frm=MovieForm(instance=edit_instance) #this instance can goes to the forms.py and view already existing movieobj texts, form will create and render #
    return render(request,'create.html',{'frm':frm})

def delete(request,pk):
    instance=MovieInfo.objects.get(pk=pk) #when press delete in server the coressponding id comes to pk and the coresspodning movie_obj is assign to instance variable#
    instance.delete() #the coressponding movieobj is deleted with the help of movie id#
    movie_set=MovieInfo.objects.all()
    return render(request,'list.html',{'movies':movie_set})