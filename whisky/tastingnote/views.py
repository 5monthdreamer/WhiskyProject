from ssl import HAS_TLSv1_1
from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse

# 이미지 경로 지정
from django.core.files.storage import FileSystemStorage

# image form 저장
from showcase.forms import *  
from showcase.models import *
from common.forms import *  

from django.db.models import Count

# pagination 설정
from django.core.paginator import Paginator

# 유저모델 사용
from django.contrib.auth import get_user_model



# Create your views here.
def tastingnote(request):

    form = UserProfileForm()
    
    
    if request.user.is_authenticated:
        obj = UploadImageModel.objects.filter(owner=request.user).order_by('-pub_date')
        
        paginator = Paginator(obj,9)
        page = request.GET.get('page')
        images = paginator.get_page(page)
        
        
        followers = UserFollowModel.objects.filter(User=request.user).count()
        following = UserFollowModel.objects.filter(follower=request.user).count()
        
        return render(request, 'tastingnote/tastingnote_main.html', {'form':form, 'images':images, 'following':following, 'followers':followers})
    else:
        error_message = "If you want to use more fantastic functions, Sign in!"
        
        return render(request, 'tastingnote/tastingnote_main.html', {'form':form,'error_message':error_message})




# whiskyname list
whiskynamelist = ["None", "Angel’s Envy Kentucky Straight Bourbon Whiskey", "Basil Hayden’s Dark Rye Whiskey", "Basil Hayden’s Kentucky Straight Bourbon Whiskey", "Blanton’s Single Barrel Bourbon", "Buffalo Trace Bourbon", "Bulleit Bourbon", "Bulleit Rye", "Crown Royal Black Blended Canadian Whisky", "Crown Royal Fine Deluxe Blended Canadian Whisky", "Crown Royal Peach Flavored Whisky", "Crown Royal Regal Apple Flavored Whisky", "Crown Royal Salted Caramel Flavored Whisky", "Crown Royal Vanilla Flavored Whisky", "Eagle Rare 10yr Bourbon", "Elijah Craig Small Batch Bourbon", "Evan Williams Bourbon", "Fireball Cinnamon Whisky", "Four Roses Bourbon", "Four Roses Small Batch Bourbon", "Hibiki Japanese Harmony Whisky", "High West American Prairie Bourbon Whiskey", "Jack Daniel’s Gentleman Jack Tennessee Whiskey", "Jack Daniel’s Old No. 7 Tennessee Whiskey", "Jack Daniel’s Tennessee Fire Flavored Whiskey", "Jack Daniel’s Tennessee Honey", "Jameson Black Barrel", "Jameson Cold Brew", "Jameson Irish Whiskey", "Jim Beam Black Extra Aged Bourbon Whiskey", "Jim Beam Bourbon Whiskey", "Johnnie Walker Black Label Blended Scotch Whisky", "Johnnie Walker Red Label Blended Scotch Whisky", "Knob Creek Kentucky Straight Bourbon Whiskey", "Laphroaig 10 Year Old Islay Single Malt Scotch Whisky", "Maker’s 46 Bourbon Whisky", "Maker’s Mark Bourbon Whisky", "Monkey Shoulder Blended Scotch", "Proper No. Twelve Irish Whiskey", "Skrewball Peanut Butter Whiskey", "Southern Comfort Original", "Suntory Toki Japanese Whisky", "The Balvenie 12 Year Old DoubleWood Single Malt Scotch Whisky", "The Balvenie 14 Year Old Caribbean Cask Single Malt Scotch Whisky", "The Glenlivet 12 Year", "The Macallan Double Cask 12 Years Old", "Tullamore D.E.W. Irish Whiskey", "Uncle Nearest 1856 Premium Whiskey", "Wild Turkey 101", "Woodford Reserve Double Oaked Kentucky Straight Bourbon Whiskey", "Woodford Reserve Kentucky Straight Bourbon Whiskey"]

   
    
# Create your views here.
def tastingnote_write(request, UploadImagekey_id):
    
    if request.user.is_authenticated:
        the_uploadimagemodel = get_object_or_404(UploadImageModel, pk=UploadImagekey_id, owner=request.user)
        
        
        fss = FileSystemStorage()
        file_url = fss.url(the_uploadimagemodel.image)
        

        # form = UserTastingNoteForm()
        # form.UploadImageModel.queryset = UploadImageModel.objects.filter(UploadImagekey_id=UploadImagekey_id)


        # 사용자만 볼 수 있는 조건식
        if the_uploadimagemodel.owner == request.user:
            
            if request.method == 'POST':
                
                form1 = UserwhiskynameForm(request.POST)
                form2 = UserTastingNoteForm(request.POST)
                
                # form.fields['UploadImagekey'].queryset = UploadImageModel.objects.filter(pk=UploadImagekey_id)
                
                
                
                # 테이스팅노트 작성 시 노트이름과 테이스팅노트 둘다 변경할 경우
                if form1.is_valid() and form2.is_valid():  

                    global note
                    note = form2.save(commit=False)
                    note.UploadImagekey = the_uploadimagemodel
                    form2.save()
                    note.save()
                    

                    
                    # <위스키이름 수정방법 : form 두개 쓰면 됨>
                    # 노트만 추가할수도 있기 때문에 whiskyname 선택안하면 노트만 저장
                    if form1.cleaned_data['whiskyname'] is not None:
                        the_uploadimagemodel.whiskyname = form1.cleaned_data['whiskyname']
                        
                    # <노트 추가 저장>
                    the_uploadimagemodel.tastingnotemodel_set.add(note)
                    the_uploadimagemodel.save()

                    
                    
                    # <테이스팅노트 부여>
                    name = form2.cleaned_data['name']
                    drumtong_rating = form2.cleaned_data['drumtong_rating']
                    one_line_review = form2.cleaned_data['one_line_review']
                    taste = form2.cleaned_data['taste']
                    taste_intensity = form2.cleaned_data['taste_intensity']
                    flavor = form2.cleaned_data['flavor']
                    flavor_intensity = form2.cleaned_data['flavor_intensity']
                    alchol_finish = form2.cleaned_data['alchol_finish']
                    etc = form2.cleaned_data['etc']
                    etc_intensity = form2.cleaned_data['etc_intensity']
                    long_review = form2.cleaned_data['long_review']

                    return render(request, 'tastingnote/tastingnote.html', {'name':name, 'drumtong_rating': drumtong_rating, 'one_line_review':one_line_review, 'taste':taste, 'taste_intensity':taste_intensity, 'flavor':flavor, 'flavor_intensity':flavor_intensity, 'alchol_finish':alchol_finish, 'etc':etc, 'etc_intensity':etc_intensity, 'long_review':long_review, 'the_uploadimagemodel':the_uploadimagemodel, 'file_url':file_url})
                
                return redirect('/')
                
                    
            else:
                    
                # return render(request, 'tastingnote/tastingnote.html')
            
                form1 = UserwhiskynameForm()
                form2 = UserTastingNoteForm()
                
                
                whiskynamelist = ["None", "1792 Small Batch Kentucky Straight Bourbon Whiskey", "Angel’s Envy Kentucky Straight Bourbon Whiskey", "Barrell Dovetail Whiskey", "Basil Hayden’s Dark Rye Whiskey", "Basil Hayden’s Kentucky Straight Bourbon Whiskey", "Blanton’s Single Barrel Bourbon", "Booker’s Bourbon", "Breckenridge Bourbon Whiskey", "Buchanan’s DeLuxe Aged 12 Years Blended Scotch Whisky", "Buffalo Trace Bourbon", "Bulleit Bourbon", "Bulleit Rye", "Bushmills Irish Whiskey", "Canadian Club Whisky", "Chivas Regal 12 Year", "Clan Macgregor Scotch", "Crown Royal Black Blended Canadian Whisky", "Crown Royal Fine Deluxe Blended Canadian Whisky", "Crown Royal Peach Flavored Whisky", "Crown Royal Regal Apple Flavored Whisky", "Crown Royal Salted Caramel Flavored Whisky", "Crown Royal Vanilla Flavored Whisky", "E.H. Taylor, Jr. Small Batch Bourbon", "Eagle Rare 10yr Bourbon", "Elijah Craig Small Batch Bourbon", "Evan Williams Bourbon", "Fireball Cinnamon Whisky", "Fireball Sleeve", "Four Roses Bourbon", "Four Roses Single Barrel Bourbon", "Four Roses Small Batch Bourbon", "Four Roses Small Batch Select Bourbon", "Glenfiddich 12 Year Old Single Malt Scotch Whisky", "Glenfiddich Bourbon Barrel Reserve 14 Year", "Glenmorangie Original 10 Year Old Single Malt Whisky", "Hibiki Japanese Harmony Whisky", "High West American Prairie Bourbon Whiskey", "High West Double Rye Whiskey", "Hochstadter’s Slow & Low Rock and Rye", "Hudson Bourbon Whiskey", "Jack Daniel’s Gentleman Jack Tennessee Whiskey", "Jack Daniel’s Old No. 7 Tennessee Whiskey", "Jack Daniel’s Tennessee Apple Flavored Whiskey", "Jack Daniel’s Tennessee Fire Flavored Whiskey", "Jack Daniel’s Tennessee Honey", "Jameson Black Barrel", "Jameson Caskmates IPA Edition", "Jameson Caskmates Stout Edition", "Jameson Cold Brew", "Jameson Irish Whiskey", "Jim Beam Black Extra Aged Bourbon Whiskey", "Jim Beam Bourbon Whiskey", "Jim Beam Devil’s Cut Bourbon Whiskey", "Johnnie Walker Black Label Blended Scotch Whisky", "Johnnie Walker Double Black Label Blended Scotch Whisky", "Johnnie Walker Red Label Blended Scotch Whisky", "Johnnie Walker White Walker Blended Scotch Whisky", "Knob Creek Kentucky Straight Bourbon Whiskey", "Knob Creek Rye Whiskey", "Knob Creek Smoked Maple Bourbon Whiskey", "Laphroaig 10 Year Old Islay Single Malt Scotch Whisky", "Larceny Small Batch", "Legent Bourbon Whiskey", "Maker’s 46 Bourbon Whisky", "Maker’s Mark Bourbon Whisky", "Michter’s US-1 Kentucky Straight Bourbon", "Michter’s US-1 Kentucky Straight Rye", "Monkey Shoulder Blended Scotch", "Nikka Coffey Grain Whisky", "Nikka Whisky From The Barrel", "Oban 14 Year Single Malt", "Old Forester 86 Proof Kentucky Straight Bourbon Whisky", "Proper No. Twelve Irish Whiskey", "Redbreast 12 Year", "Redemption Straight Rye Whiskey", "Rittenhouse Rye", "Sazerac Rye Whiskey", "Skrewball Peanut Butter Whiskey", "Southern Comfort Original", "Suntory Toki Japanese Whisky", "The Balvenie 12 Year Old DoubleWood Single Malt Scotch Whisky", "The Balvenie 14 Year Old Caribbean Cask Single Malt Scotch Whisky", "The Glenlivet 12 Year", "The Glenlivet Founder’s Reserve", "The Macallan Double Cask 12 Years Old", "The Macallan Sherry Oak 12 Years Old", "TINCUP American Whiskey", "Tullamore D.E.W. Irish Whiskey", "TX Blended Whiskey", "Uncle Nearest 1856 Premium Whiskey", "Uncle Nearest 1884 Small Batch Whiskey", "Weller Special Reserve Bourbon", "Wild Turkey 101", "Wild Turkey American Honey", "Wild Turkey Bourbon", "Wild Turkey Longbranch", "Willett Pot Still Reserve Bourbon", "Woodford Reserve Double Oaked Kentucky Straight Bourbon Whiskey", "Woodford Reserve Kentucky Straight Bourbon Whiskey", "Woodford Reserve Kentucky Straight Rye Whiskey"]          
                
                return render(request, 'tastingnote/tastingnote.html', {'form1':form1, 'form2':form2, 'tastingnote':tastingnote, 'the_uploadimagemodel':the_uploadimagemodel, 'file_url':file_url, 'whiskynamelist':whiskynamelist})
        
        else:
            return render(request, 'labelscanner/labelscanner.html')
        
    else:
        return render(request, 'labelscanner/labelscanner.html')

        
    
    
    
def tastingnote_delete(request, TastingNoteModel_id):
    
    # images = UploadImageModel.objects.filter(owner=request.user)

    
    the_tastingNoteModel = get_object_or_404(TastingNoteModel, pk=TastingNoteModel_id)

    if the_tastingNoteModel.UploadImagekey.owner == request.user:
        the_tastingNoteModel.delete()

    return redirect(reverse('tastingnote:tastingnote'))
        

        

# Create your views here.
def tastingnote_edit(request, TastingNoteModel_id):
    
    
    the_tastingnotemodel = get_object_or_404(TastingNoteModel, pk=TastingNoteModel_id)
    
    the_uploadimagemodel = get_object_or_404(UploadImageModel, pk=the_tastingnotemodel.UploadImagekey.id)
    
    
    fss = FileSystemStorage()
    file_url = fss.url(the_uploadimagemodel.image)
    

    # form = UserTastingNoteForm()
    # form.UploadImageModel.queryset = UploadImageModel.objects.filter(UploadImagekey_id=UploadImagekey_id)


    # 사용자만 볼 수 있는 조건식
    if the_uploadimagemodel.owner == request.user:
        
        if request.method == 'POST':
            
            form = UserTastingNoteForm(request.POST)
            
            # form.fields['UploadImagekey'].queryset = UploadImageModel.objects.filter(pk=UploadImagekey_id)
            
            # form.save()
            if form.is_valid():  

                # global note
                # note = form.save(commit=False)
                # note.UploadImagekey = the_uploadimagemodel
                # form.save()
                # note.save()
                
                
                the_tastingnotemodel.name = form.cleaned_data['name']
                the_tastingnotemodel.drumtong_rating = form.cleaned_data['drumtong_rating']
                the_tastingnotemodel.one_line_review = form.cleaned_data['one_line_review']
                the_tastingnotemodel.taste = form.cleaned_data['taste']
                the_tastingnotemodel.taste_intensity = form.cleaned_data['taste_intensity']
                the_tastingnotemodel.flavor = form.cleaned_data['flavor']
                the_tastingnotemodel.flavor_intensity = form.cleaned_data['flavor_intensity']
                the_tastingnotemodel.alchol_finish = form.cleaned_data['alchol_finish']
                the_tastingnotemodel.etc = form.cleaned_data['etc']
                the_tastingnotemodel.etc_intensity = form.cleaned_data['etc_intensity']
                the_tastingnotemodel.long_review = form.cleaned_data['long_review']
                the_tastingnotemodel.save()
                
                # form.save()
                
                # review.save()
                # sweetness.save()
                # acidity.save()
                # alchol.save()
                
                
                
                # record = UploadImageModel.objects.all()
                # record.delete()
                # form.save()  #form.save(commit=False)
                

                return render(request, 'tastingnote/tastingnote.html', {'the_uploadimagemodel':the_uploadimagemodel, 'the_tastingnotemodel':the_tastingnotemodel, 'file_url':file_url})
                

                
        else:
                
            # return render(request, 'tastingnote/tastingnote.html')
        
            form = UserTastingNoteForm()
            
            
            
            
            return render(request, 'tastingnote/tastingnote.html', {'form':form, 'the_uploadimagemodel':the_uploadimagemodel, 'the_tastingnotemodel':the_tastingnotemodel, 'file_url':file_url})
    


def tastingnote_public(request, TastingNoteModel_id):
    

    # images = UploadImageModel.objects.filter(owner=request.user)

    the_tastingnotemodel = get_object_or_404(TastingNoteModel, pk=TastingNoteModel_id)

    if the_tastingnotemodel.UploadImagekey.owner == request.user:

        if the_tastingnotemodel.is_public == False:
            the_tastingnotemodel.is_public = True
            the_tastingnotemodel.save()
        else:
            the_tastingnotemodel.is_public = False
            the_tastingnotemodel.save()
            
        
    return redirect(reverse('tastingnote:tastingnote'))





        
    
def whisky_delete(request, UploadImagekey_id):
    

    # images = UploadImageModel.objects.filter(owner=request.user)

    the_UploadImageModel = get_object_or_404(UploadImageModel, pk=UploadImagekey_id, owner=request.user)

    if the_UploadImageModel.owner == request.user:
        the_UploadImageModel.delete()
        
    return redirect(reverse('tastingnote:tastingnote'))



def whisky_public(request, UploadImagekey_id):
    

    # images = UploadImageModel.objects.filter(owner=request.user)

    the_UploadImageModel = get_object_or_404(UploadImageModel, pk=UploadImagekey_id, owner=request.user)

    if the_UploadImageModel.owner == request.user:

        if the_UploadImageModel.is_public == False:
            the_UploadImageModel.is_public = True
            the_UploadImageModel.save()
        else:
            the_UploadImageModel.is_public = False
            the_UploadImageModel.save()
            
        
    return redirect(reverse('tastingnote:tastingnote'))



def whisky_edit(request, UploadImagekey_id):
    
    
    the_UploadImageModel = get_object_or_404(UploadImageModel, pk=UploadImagekey_id, owner=request.user)
    
    if request.method == 'POST' and request.FILES:
        form = UserImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            if request.user.is_authenticated:
                form.owner = request.user

            else:
                pass
            
            form.save()
            
            if form.cleaned_data['whiskyname']:      
                the_UploadImageModel.image = form.cleaned_data['image']
                the_UploadImageModel.whiskyname = form.cleaned_data['whiskyname']
                the_UploadImageModel.save()

            else:      
                the_UploadImageModel.image = form.cleaned_data['image']
                the_UploadImageModel.save()
            
            
            return redirect(reverse('tastingnote:tastingnote'))
    
    
    elif request.method == 'POST':
        form = UserImageForm(request.POST)
        
        if form.is_valid():
            
            if request.user.is_authenticated:
                form.owner = request.user              
            else:
                pass
            
            form.save()
            
            the_UploadImageModel.whiskyname = form.cleaned_data['whiskyname']
            the_UploadImageModel.save()
            
            return redirect(reverse('tastingnote:tastingnote'))
        
           
    else:
        form = UserImageForm()
        
        whiskynamelist = ["None", "1792 Small Batch Kentucky Straight Bourbon Whiskey", "Angel’s Envy Kentucky Straight Bourbon Whiskey", "Barrell Dovetail Whiskey", "Basil Hayden’s Dark Rye Whiskey", "Basil Hayden’s Kentucky Straight Bourbon Whiskey", "Blanton’s Single Barrel Bourbon", "Booker’s Bourbon", "Breckenridge Bourbon Whiskey", "Buchanan’s DeLuxe Aged 12 Years Blended Scotch Whisky", "Buffalo Trace Bourbon", "Bulleit Bourbon", "Bulleit Rye", "Bushmills Irish Whiskey", "Canadian Club Whisky", "Chivas Regal 12 Year", "Clan Macgregor Scotch", "Crown Royal Black Blended Canadian Whisky", "Crown Royal Fine Deluxe Blended Canadian Whisky", "Crown Royal Peach Flavored Whisky", "Crown Royal Regal Apple Flavored Whisky", "Crown Royal Salted Caramel Flavored Whisky", "Crown Royal Vanilla Flavored Whisky", "E.H. Taylor, Jr. Small Batch Bourbon", "Eagle Rare 10yr Bourbon", "Elijah Craig Small Batch Bourbon", "Evan Williams Bourbon", "Fireball Cinnamon Whisky", "Fireball Sleeve", "Four Roses Bourbon", "Four Roses Single Barrel Bourbon", "Four Roses Small Batch Bourbon", "Four Roses Small Batch Select Bourbon", "Glenfiddich 12 Year Old Single Malt Scotch Whisky", "Glenfiddich Bourbon Barrel Reserve 14 Year", "Glenmorangie Original 10 Year Old Single Malt Whisky", "Hibiki Japanese Harmony Whisky", "High West American Prairie Bourbon Whiskey", "High West Double Rye Whiskey", "Hochstadter’s Slow & Low Rock and Rye", "Hudson Bourbon Whiskey", "Jack Daniel’s Gentleman Jack Tennessee Whiskey", "Jack Daniel’s Old No. 7 Tennessee Whiskey", "Jack Daniel’s Tennessee Apple Flavored Whiskey", "Jack Daniel’s Tennessee Fire Flavored Whiskey", "Jack Daniel’s Tennessee Honey", "Jameson Black Barrel", "Jameson Caskmates IPA Edition", "Jameson Caskmates Stout Edition", "Jameson Cold Brew", "Jameson Irish Whiskey", "Jim Beam Black Extra Aged Bourbon Whiskey", "Jim Beam Bourbon Whiskey", "Jim Beam Devil’s Cut Bourbon Whiskey", "Johnnie Walker Black Label Blended Scotch Whisky", "Johnnie Walker Double Black Label Blended Scotch Whisky", "Johnnie Walker Red Label Blended Scotch Whisky", "Johnnie Walker White Walker Blended Scotch Whisky", "Knob Creek Kentucky Straight Bourbon Whiskey", "Knob Creek Rye Whiskey", "Knob Creek Smoked Maple Bourbon Whiskey", "Laphroaig 10 Year Old Islay Single Malt Scotch Whisky", "Larceny Small Batch", "Legent Bourbon Whiskey", "Maker’s 46 Bourbon Whisky", "Maker’s Mark Bourbon Whisky", "Michter’s US-1 Kentucky Straight Bourbon", "Michter’s US-1 Kentucky Straight Rye", "Monkey Shoulder Blended Scotch", "Nikka Coffey Grain Whisky", "Nikka Whisky From The Barrel", "Oban 14 Year Single Malt", "Old Forester 86 Proof Kentucky Straight Bourbon Whisky", "Proper No. Twelve Irish Whiskey", "Redbreast 12 Year", "Redemption Straight Rye Whiskey", "Rittenhouse Rye", "Sazerac Rye Whiskey", "Skrewball Peanut Butter Whiskey", "Southern Comfort Original", "Suntory Toki Japanese Whisky", "The Balvenie 12 Year Old DoubleWood Single Malt Scotch Whisky", "The Balvenie 14 Year Old Caribbean Cask Single Malt Scotch Whisky", "The Glenlivet 12 Year", "The Glenlivet Founder’s Reserve", "The Macallan Double Cask 12 Years Old", "The Macallan Sherry Oak 12 Years Old", "TINCUP American Whiskey", "Tullamore D.E.W. Irish Whiskey", "TX Blended Whiskey", "Uncle Nearest 1856 Premium Whiskey", "Uncle Nearest 1884 Small Batch Whiskey", "Weller Special Reserve Bourbon", "Wild Turkey 101", "Wild Turkey American Honey", "Wild Turkey Bourbon", "Wild Turkey Longbranch", "Willett Pot Still Reserve Bourbon", "Woodford Reserve Double Oaked Kentucky Straight Bourbon Whiskey", "Woodford Reserve Kentucky Straight Bourbon Whiskey", "Woodford Reserve Kentucky Straight Rye Whiskey"]
        
        return render(request, 'tastingnote/tastingnote_whiskyedit.html', {'the_UploadImageModel': the_UploadImageModel, 'form':form, 'whiskynamelist':whiskynamelist})
            

    
# Create your views here.
def tastingnote_user(request,user_id):

    obj = UploadImageModel.objects.filter(owner = user_id, is_public=True)
    
    paginator = Paginator(obj,9)
    page = request.GET.get('page')
    images = paginator.get_page(page)
    
    User = get_user_model()
    tastingnoteuser = User.objects.get(pk = user_id)
    
    followers = UserFollowModel.objects.filter(User=tastingnoteuser).count()
    following = UserFollowModel.objects.filter(follower=tastingnoteuser).count()
    
    if UserFollowModel.objects.filter(User=tastingnoteuser, follower=request.user):
        followbutton = "Unfollow"
    else:
        followbutton = "Follow"
        
    
    return render(request, 'tastingnote/tastingnote_user.html', {'images':images, 'following':following, 'followers':followers, 'tastingnoteuser':tastingnoteuser, "followbutton":followbutton}) 



def tastingnote_userfollow(request, userfollow_id):
    
   
    try:
        the_userfollowmodel = get_object_or_404(UserFollowModel, User_id = userfollow_id, follower=request.user)     
        the_userfollowmodel.delete()

    except:
        User = get_user_model()
        followmodel = UserFollowModel()
        
        if User.objects.get(pk = userfollow_id) == request.user:
            pass
        else:
            followmodel.User = User.objects.get(pk = userfollow_id)
            followmodel.follower = request.user
            followmodel.save()
    
    return redirect('tastingnote:user_tastingnote', userfollow_id)



