from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from react_backend.models import CsvData
from datetime import datetime
# Create your views here.


@csrf_exempt
def upload_csv(request):
    if request.method == "POST":
        csv_data = json.loads(request.body)
        for data in csv_data:
            if data["image_name"]!="":
                # print("---------->",data)
                image_name = data["image_name"]
                objects_detected = data["objects_detected"]
                timestamp = data["timestamp"]
                
                csv_data_obj = CsvData(image_name=image_name, objects_detected=objects_detected, timestamp=timestamp)
                csv_data_obj.save()
        return JsonResponse({"status": "success"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"})

@csrf_exempt
def get_filtered_data(request):
    if request.method == 'GET':
        start_date_str = request.GET.get('start_date')
        end_date_str = request.GET.get('end_date')
        # print("type of date--->",start_date_str)
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        data = CsvData.objects.filter(timestamp__range=(start_date, end_date)).values()
        # print("data---->",data)
        return JsonResponse({'data': list(data)})
    return JsonResponse({'error': 'Invalid request method'})