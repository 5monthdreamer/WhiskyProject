from django.views.generic.base import TemplateView

from django.shortcuts import  render
from django.core.files.storage import FileSystemStorage

# from tensorflow import keras
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
# from tensorflow import keras model = keras.models.load_model('path/to/location')
import os
import time


class HomeView(TemplateView):
    
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_list'] = ['labelscanner','showcase']
        return context
    


def teachablemachine(image_path):
    
    # Load the model
    model = load_model(os.path.join(os.getcwd(),'mysite/keras_model.h5'))
    print(os.path.join(os.getcwd(),'keras_model.h5'))
# 'C:\\Users\\jiyon\\Desktop\\Python\\Project\\위스키 어플, 홈페이지 제작\\project test\\whisky\\mysite\\keras_model.h5'

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Replace this with the path to your image
    image = Image.open(os.path.join(os.getcwd(),'media/'+image_path))
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



def upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)

        #<Teachable Machine>
        img_result = teachablemachine(file)
        
        whisky_name = ["jameson","wildturckey"]
        

        
        for order in range(2):
            print(np.max(img_result),img_result[0,order])
            if img_result[0,order]>=0.9:
                global name1
                global percent1
                name1 = whisky_name[order]
                percent1 = str(round(img_result[0,order]*100))+"%"
                break
            else:
                name1 = "비슷한 위스키가 없습니다"
                percent1 = "-"
                continue

        
        return render(request, 'home.html', {'file_url': file_url, 'result1': name1, 'result2':percent1,'test_result1':img_result[0,0],'test_result2':img_result[0,1]})
    return render(request, 'home.html')







