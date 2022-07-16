from django.shortcuts import render

from django.views.generic.base import TemplateView

from django.shortcuts import  render
from django.core.files.storage import FileSystemStorage

# from tensorflow import keras
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

import os
import time

# image form 저장
from showcase.forms import UserImageForm  
from showcase.models import UploadImageModel 


def teachablemachine(image_path):
    
    # Load the model # ☆☆☆☆☆ os.getcwd()는 다 다르다
    model = load_model(os.path.join(os.getcwd(),'mysite/keras_model.h5'))
    print(os.path.join(os.getcwd(),'keras_model.h5'))
    # pythonanywhere에서는 'WhiskyProject/whisky/mysite/keras_model.h5'

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Replace this with the path to your image
    image = Image.open(os.path.join(os.getcwd(),'media/'+str(image_path)))
    # pythonanywhere에서는 'WhiskyProject/whisky/media/'
    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    return prediction



# Create your views here.
def img_scanning(request):
    if request.method == 'POST' and request.FILES:
        # usernickname = UploadImageModel(nickname=request.user)

        form = UserImageForm(request.POST, request.FILES)  
        # form.save()
        if form.is_valid():  
            # form.nickname = request.user
            post = form.save(commit=False)
            
            if request.user.is_authenticated:
                post.owner = request.user
            else:
                pass
            post.save()
            
            # record = UploadImageModel.objects.all()
            # record.delete()
            # form.save()  #form.save(commit=False)
            
            saved_image = form.cleaned_data['image']
            fss = FileSystemStorage()
            file_url = fss.url(saved_image)
            
            # Getting the current instance object to display in the template  
            # img_object = form.instance  
            
            
            img_result = teachablemachine(saved_image)

            whisky_name = ["JAMESON","WILD TURCKEY"]


            for order in range(2):
                print(np.max(img_result),img_result[0,order])
                if img_result[0,order]>=0.999:
                    global name1
                    global percent1
                    name1 = whisky_name[order]
                    percent1 = str(round(img_result[0,order]*100))+"%"
                    break
                else:
                    name1 = "비슷한 위스키가 없습니다"
                    percent1 = "-"
                    continue


            return render(request, 'labelscanner/labelscanner.html', {'file_url': file_url, 'result1': name1, 'result2':percent1,'test_result1':'없음'})
                        
            # return render(request, 'showcase.showcase.html', {'form': form, 'img_obj': img_object})
            
    else:
        form = UserImageForm()
        images = UploadImageModel.objects.all()
        return render(request, 'labelscanner/labelscanner.html', {'form':form, 'images':images})