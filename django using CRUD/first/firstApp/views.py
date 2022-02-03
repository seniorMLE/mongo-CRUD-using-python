from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.core.paginator import Paginator 
# Create your views here.
from .models import GeeksModel
from .forms import GeeksForm

import matplotlib.pyplot as plt
import io
import urllib, base64
import seaborn as sns
import numpy as np
from sklearn.cluster import KMeans
 
 
def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
         
    context['form']= form
    
    
    return render(request, "create_view.html", context)

def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={} 
    # add the dictionary during initialization
    pre_data = GeeksModel.objects.all()
    paginator = Paginator(pre_data, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context["dataset"] = page_obj      


    
    y =[]
    for i in pre_data:        
        x=i.score
        y.append(float(x))
    numLen = len(y)
    x = []
    for i in range (0, numLen):
        x.append(i)

    fig = plt.figure()
    plt.plot(x,y)            
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    context["data_plt1"] = uri   

    fig2 = plt.figure()
    plt.scatter(x,y)        
    buf2 = io.BytesIO()
    fig2.savefig(buf2,format='png')
    buf2.seek(0)
    string2 = base64.b64encode(buf2.read())
    uri2 = urllib.parse.quote(string2)
    context["data_plt2"] = uri2   

    fig = plt.figure()
    plt.boxplot(x,y)        
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    context["data_plt3"] = uri   

    
    
    empty_array1 = np. array(x)
    empty_array2 = np. array(y)
    is_empty1 = empty_array1. size == 0
    is_empty2 = empty_array2. size == 0
    if is_empty1 != True and is_empty2 != True:
        sns.set()
        fig = plt.figure()
        sns.barplot(x,y)        
        buf = io.BytesIO()
        fig.savefig(buf,format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)
        context["data_plt4"] = uri   

    lenx = len(x)
    leny = len(y)
   
    if lenx >= 2 and leny >= 2:
        fig = plt.figure()
        x = np.array(x)
        y = np.array(y)
        xx=np.array([x,y])
        xx=xx.transpose()    
        model = KMeans(n_clusters = 2)                     
        model.fit(xx)              
        labels = model.predict(xx)              
        labels = labels
        print(labels)
        xs = xx[:,0]       
        ys = xx[:,1]           
        colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
        plt.scatter(xs,ys,c=colors[labels])                  
        centroids = model.cluster_centers_              
        centroids_x = centroids[:,0]       
        centroids_y = centroids[:,1]  
        plt.scatter(centroids_x,centroids_y,marker='D', s=50)   
        
        buf = io.BytesIO()
        fig.savefig(buf,format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)
        context["ML"] = uri   

    return render(request, "list_view.html", context)    

def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = GeeksModel.objects.get(id = id)
         
    return render(request, "detail_view.html", context)    

# update view for details
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id = id)
 
    # pass the object as instance in form
    form = GeeksForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view.html", context)

def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "delete_view.html", context)    








