from django.shortcuts import render,redirect
from .forms import DocumentForm
from .models import Document





def home(request):
    documents = Document.objects.all()
    context = {
        'document':documents
    }
    return render(request,'home.html',context)


def upload_document(request):
    if request.method=='POST':
            form = DocumentForm(request.POST,request.FILES)
            if form.is_valid():
                 form.save()
                 return redirect('home')
    else:
         form = DocumentForm()
    return render(request,'document_upload.html',{'form':form})