from django.shortcuts import render, get_object_or_404

# 이미지 경로 지정
from django.core.files.storage import FileSystemStorage

# image form 저장
from showcase.forms import *  
from showcase.models import *




# Create your views here.
def tastingnote_write(request, UploadImagekey_id):
    
    the_uploadimagemodel = get_object_or_404(UploadImageModel, pk=UploadImagekey_id)
    fss = FileSystemStorage()
    file_url = fss.url(the_uploadimagemodel.image)
    
    global modelforeignkey
    modelforeignkey = UploadImageModel.objects.get(pk=UploadImagekey_id)

    
    # form = UserTastingNoteForm()
    # form.UploadImageModel.queryset = UploadImageModel.objects.filter(UploadImagekey_id=UploadImagekey_id)
    
    
    if request.method == 'POST':
        
        form = UserTastingNoteForm(request.POST)
        
        # form.fields['UploadImagekey'].queryset = UploadImageModel.objects.filter(pk=UploadImagekey_id)
        
        tastingnote = TastingNoteModel.objects.all()
        
        
        # form.save()
        if form.is_valid():  

            global note
            note = form.save(commit=False)
            note.UploadImagekey = the_uploadimagemodel
            form.save()
            
            # review = note.one_line_review
            # sweetness = note.sweetness
            # acidity = note.acidity
            # alchol = note.alchol_finish
            
            # review = tastingform.cleaned_data['one_line_review']
            # sweetness = tastingform.cleaned_data['sweetness']
            # acidity = tastingform.cleaned_data['acidity']
            # alchol = tastingform.cleaned_data['alchol_finish']
            
            name = form.cleaned_data['name']
            drumtong_rating = form.cleaned_data['drumtong_rating']
            one_line_review = form.cleaned_data['one_line_review']
            taste = form.cleaned_data['taste']
            taste_intensity = form.cleaned_data['taste_intensity']
            flavor = form.cleaned_data['flavor']
            flavor_intensity = form.cleaned_data['flavor_intensity']
            alchol_finish = form.cleaned_data['alchol_finish']
            
            note.save()
            
            # form.save()
            
            # review.save()
            # sweetness.save()
            # acidity.save()
            # alchol.save()
            
            
            
            # record = UploadImageModel.objects.all()
            # record.delete()
            # form.save()  #form.save(commit=False)
            

            return render(request, 'tastingnote/tastingnote.html', {'name':name, 'drumtong_rating': drumtong_rating, 'one_line_review':one_line_review, 'tastingnote':tastingnote, 'the_uploadimagemodel':the_uploadimagemodel, 'file_url':file_url})
            

            
    else:
               
        # return render(request, 'tastingnote/tastingnote.html')
    
        form = UserTastingNoteForm(UploadImagekey_id)
        tastingnote = TastingNoteModel.objects.all()
        
        return render(request, 'tastingnote/tastingnote.html', {'form':form, 'tastingnote':tastingnote, 'the_uploadimagemodel':the_uploadimagemodel, 'file_url':file_url})
    
        # , "id":id
    
        
    
    
    