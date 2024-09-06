from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from security.services.domainchecker import get_domain_checker_response
from security.services.hashchecker import get_hash_checker_response
from security.services.ipchecker import get_ip_checker_response
import csv
import io

@csrf_exempt
def domain_checker(request):
    if request.method == 'POST':
        api_key = request.POST.get('key')
        text = request.POST.get('text')
        
        domains = text.strip().split('\n')
        
        output = io.StringIO()
        writer = csv.writer(output)
        
        writer.writerow(['text', 'status'])
        
        for domain in domains:
            writer.writerow([domain, get_domain_checker_response(api_key, domain)])
        
        response = HttpResponse(output.getvalue(), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=domain_status.csv'
        
        return response
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def hash_checker(request):
    if request.method == 'POST':
        api_key = request.POST.get('key')
        text = request.POST.get('text')
        
        hashes = text.strip().split('\n')
        
        output = io.StringIO()
        writer = csv.writer(output)
        
        writer.writerow(['SHA256 Hash', 'MD5 Hash', 'SHA1 Hash'])
        
        for sha256 in hashes:
            writer.writerow(get_hash_checker_response(api_key, sha256))
        
        response = HttpResponse(output.getvalue(), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=domain_status.csv'
        
        return response
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def ip_checker(request):
    if request.method == 'POST':
        api_key = request.POST.get('key')
        text = request.POST.get('text')
        
        ips = text.strip().split('\n')
        
        output = io.StringIO()
        writer = csv.writer(output)
        
        writer.writerow(['IP Address', 'Country', 'Network Owner', 'Reputation'])
        
        for ip in ips:
            writer.writerow(get_ip_checker_response(api_key, ip))
        
        response = HttpResponse(output.getvalue(), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=domain_status.csv'
        
        return response
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)