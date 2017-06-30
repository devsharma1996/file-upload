import json
import logging

from .USBFinder import attemptMount,transfer_file
from hashlib import sha1
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView, DeleteView, ListView
from .models import EkFile
from django.contrib.auth.models import User
from .response import JSONResponse, response_mimetype
from .serialize import serialize
from django.urls import reverse

def index(request):
    return render(request,'fileupload/LOGIN.html')

def verify(request):
    user=User.objects.get(username=request.POST['email'])
    logger = logging.getLogger(__name__)
    password=request.POST['password']
    #_,salt,hashpw=user.password.split('$')
    logger.error(request.POST['email']+","+request.POST['password']+" \n next line")
    logger.error(user.password+", username is "+user.username)
    if(user is not None and user.check_password(password)):
        return HttpResponseRedirect('new/')
    else:
        return render(request,'fileupload/LOGIN.html',{'invalid':'not a valid username or password'})
        
    
    
    
class EkFileCreateView(CreateView):
    model = EkFile
    fields = "__all__"

    def form_valid(self, form):
    	
        self.object = form.save()
        print self.object
        files = [serialize(self.object)]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        print 'Before you send post request'
        return response

    def form_invalid(self, form):
        data = json.dumps(form.errors)
        return HttpResponse(content=data, status=400, content_type='application/json')


#class BasicPlusVersionCreateView(EkFileCreateView):
 #   template_name_suffix = '_basicplus_form'


class EkFileDeleteView(DeleteView):
    model = EkFile

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = JSONResponse(True, mimetype=response_mimetype(request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response


class EkFileListView(ListView):
    model = EkFile
    
    def render_to_response(self, context, **response_kwargs):
        files = [ serialize(p) for p in self.get_queryset() ]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response
    
def transfer(request):
    files=[]
    #Returns list of files that correspond to requirements
    files=attemptMount()
    files_existing=[]
    unique_files_existing=[]
    unique_files=[]
    if files is not None:
        unique_files  = [file for file in files if file not in files_existing_names]
    else:
        unique_files = None
    total_done = 0
    if unique_files is not None:
        for file1 in unique_files:
            if file1 != 'content.json':
                try:
                    x =  File.objects.get(file_link=file)
                except File.DoesNotExist:
                    x = None
                if x == None:

                    fModel = EkFile(file = file1)
                    fModel.save()
                    unique_files_existing.append(fModel)
    files_existing.append(unique_files_existing)
    files_existing_names.append(unique_files)
    if request.method == 'GET':
            unique_files_existing
            total_amount = len(files)
            download_more = True
            fileCount = request.POST.get("file_descriptor", "")
            try:
                return_code = transfer_file(files[int(fileCount)])
                if return_code != 0:
                    print ('USB unexpectedly removed!')
                    return HttpResponse(content=data, status=400, content_type='application/json')
            except IndexError as error:											#Thrown when there are no more files to #download 
                download_more = None
            total_done += 1
            percentage_done = int(total_done*100/total_amount)
            template = loader.get_template('checkUpdates/downloadFiles.html')
            context = {
            'files_existing' : unique_files_existing,
            'show_output' : download_more,
            'percentage_done' : percentage_done,
            'current_count'	: total_done,
            'btn_check_flag' : 'disabled',
            'download_more' : download_more,
            }
            return HttpResponseRedirect('new/')
    return HttpResponse("Please access this URL properly")
    

