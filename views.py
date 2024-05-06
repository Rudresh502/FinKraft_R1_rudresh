# views.py
from django.http import JsonResponse
from models import Transaction
import csv

def upload_csv(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        if file.name.endswith(".csv"):
            csv_data = csv.DictReader(file)
            for row in csv_data:
                Transaction.objects.create(
                    TransactionID=row['TransactionID'],
                    CustomerName=row['CustomerName'],
                    TransactionDate=row['TransactionDate'],
                    Amount=row['Amount'],
                    Status=row['Status'],
                    InvoiceURL=row['InvoiceURL']
                )
            return JsonResponse({'message': 'File uploaded successfully'}, status=201)
        else:
            return JsonResponse({'error': 'Only CSV files are allowed'}, status=400)
    else:
        return JsonResponse({'error': 'No file selected'}, status=400)
