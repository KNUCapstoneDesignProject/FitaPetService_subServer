import os

import cv2
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse, FileResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from pyfcm import FCMNotification
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from . import models
from .serializer import DocumentSerializer, PostSerializer


# Create your views here.
#파이어베이스 키 설정
#APIKEY = "Server Key"
#TOKEN = "Token"

#push_service = FCMNotification(APIKEY)


@csrf_exempt
def getloc(request):
    #global lat
    #global long
    if request.method == 'POST':
        userId = request.POST.get('strID')
        lat = request.POST.get('lat')
        long = request.POST.get('long')
        try:
            _id = models.Location.objects.get(userId=userId)
        except:
            _id = None
        if _id is None:
            location = models.Location(
                userId=userId,
                lat=lat,
                long=long
            )
            location.save()
        else:
            location = models.Location.objects.get(userId=userId)
            location.lat = lat
            location.long = long
            location.save()
        print(str(lat))
        print(str(long))
    return JsonResponse({'msg': 1}, status=200)
    #return redirect('petsitter:send')

@csrf_exempt
@api_view(['POST'])
def send(request):
    #파이어베이스로 알림 호출
    #data_message = {
    #    "body": "위치 요청",
    #    "title": "고객님으로부터 위치 정보 요청이 있습니다"
    #}

    #result = push_service.single_device_data_message(registration_id=TOKEN, data_message=data_message)
    if request.method == 'POST':
        otherId = request.POST.get('idStr')
    location = models.Location.objects.get(userId=otherId)
    return JsonResponse({'lat': location.lat, 'long': location.long}, status=200)

@csrf_exempt
def uploadFile(request):
    fileTitle = request.POST["fileTitle"]
    uploadedFile = request.FILES["uploadedFile"]
    base64Img = request.POST["base64_img"]
    base64Img = base64Img[1:-1]

    #vidcap = cv2.VideoCapture(uploadedFile)
    #ret, image = vidcap.read()
    #cv2.imwrite("../media/thumnail/thum.jpg", image)

    fileSize = uploadedFile.size / 1048576  #Byte를 MB단위로 변환
    fileSize = round(fileSize, 1)
    #DB에 파일의 정보를 저장
    document = models.Document(
        title=fileTitle,
        thumnail=base64Img,
        uploadedFile=uploadedFile,
        fileSize=fileSize
    )
    document.save()
    #vidcap.release()
    #documents = models.Document.objects.all() #모델 객체 얻어오기
    return JsonResponse({'id': document.id, 'title': document.title, 'date': document.dateTimeOfUpload.strftime('%m-%d %H:%M')}, status=200)

@csrf_exempt
@api_view(['GET'])
def downloadFile(request):
    #파일 다운로드 기능 구현
    namestr = request.GET["position"]
    file_path = os.path.abspath("media/Uploaded Files/")
    #file_name = os.listdir("media/Uploaded Files/") #이 경로 하에 있는 파일 목록을 가져오는 것
    fs = FileSystemStorage(file_path)
    response = FileResponse(fs.open(namestr, 'rb'), content_type='video/*')
    response['Content-Disposition'] = 'attachment; filename="downloaded.mp4"'
    return response

@csrf_exempt
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def videoList(request):
    msg = request.POST["msg"]
    print(msg)
    documents = models.Document.objects.all()
    serializer = DocumentSerializer(documents, many=True) #queryset을 json형태로 직렬화하기 위해(many=True인자 필수)
    print(serializer.data)
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST']) #Response 사용시 필수
@permission_classes((permissions.AllowAny,)) #Response 사용시 필수
def uploadPetImage(request):
    fileTitle = request.POST["fileTitle"]
    uploadedImg = request.FILES["uploadedImg"]
    document = models.ImgDocument(
        title=fileTitle,
        uploadedImg=uploadedImg
    )
    print(fileTitle)
    document.save()
    imgdocuments = models.ImgDocument.objects.get(title=fileTitle)
    serializer = PostSerializer(imgdocuments)
    #serializer.data.uploadedImg = 'http://118.45.212.21:8000/pets'+serializer.data.uploadedImg
    print(serializer.data)
    return Response(serializer.data)


'''
def practice(request):
    return render(request, 'test/download.html')
'''


