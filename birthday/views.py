from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from .models import * 
from .serializers import *
from core.pagination import MyPageNumberPagination
paginator = MyPageNumberPagination()




class CustomerView(APIView):
    def post(self, request):
        try:
            serializer = CustomerSerializer(data = request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return JsonResponse({'success': True,"status":status.HTTP_201_CREATED , "results":serializer.data})
        except Exception as e:
            return JsonResponse({"status":status.HTTP_500_INTERNAL_SERVER_ERROR,"success":False,"message":e.args[0]})
    def get(self, request,pk=None):
        try:
            if pk is not None:
                query = Customer.objects.filter(id=pk).last()
                if query is not None:
                    serializer = CustomerSerializer(query) 
                    return JsonResponse({'success': True,"status":status.HTTP_200_OK , "results":serializer.data})
                else:
                    return JsonResponse({'success': False,"status":status.HTTP_404_NOT_FOUND , "msg":"Data not found!"})
            else:
                queryset = Customer.objects.all().order_by('-id') 
                if len(queryset)>0:
                    result_page = paginator.paginate_queryset(queryset, request)
                    if result_page is not None:
                        
                        serializer = CustomerSerializer(result_page, many=True, context={'request':request})
                    else:
                        serializer = CustomerSerializer(queryset, many=True)
                    result = {
                            "status":status.HTTP_200_OK,
                            "success": True,
                            "results": serializer.data,
                            "count": len(queryset),

                        }
                    return JsonResponse(result)
        except Exception as e:
            return JsonResponse({"status":status.HTTP_500_INTERNAL_SERVER_ERROR,"success":False,"message":e.args[0]})


    def put(self,request,pk):
        try:
            query = Customer.objects.filter(id=pk).last() 
            if query:
                serializer = CustomerSerializer(instance=query,partial = True,data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return JsonResponse({'success': True,"status":status.HTTP_200_OK , "results":serializer.data})
        except Exception as e:
            return JsonResponse({"status":status.HTTP_500_INTERNAL_SERVER_ERROR,"success":False,"message":e.args[0]})                  
                


    def delete(self,request,pk):
        try:
            query = Customer.objects.filter(id=pk).last() 
            if query:
                query.delete()
                return JsonResponse({'success': True,"status":status.HTTP_204_NO_CONTENT})
        except Exception as e:
            return JsonResponse({"status":status.HTTP_500_INTERNAL_SERVER_ERROR,"success":False,"message":e.args[0]})                  
                



class ReportView(APIView):
    def get(self, request,pk=None):
        try:

            queryset = Report.objects.all().order_by('-id') 
            if len(queryset)>0:
                result_page = paginator.paginate_queryset(queryset, request)
                if result_page is not None:
                    
                    serializer = ReportSerializers(result_page, many=True, context={'request':request})
                else:
                    serializer = ReportSerializers(queryset, many=True)
                result = {
                        "status":status.HTTP_200_OK,
                        "success": True,
                        "results": serializer.data,
                        "count": len(queryset),

                    }
                return JsonResponse(result)
        except Exception as e:
            return JsonResponse({"status":status.HTTP_500_INTERNAL_SERVER_ERROR,"success":False,"message":e.args[0]})

