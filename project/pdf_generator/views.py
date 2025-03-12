from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.template.loader import render_to_string
import pdfkit
from .serializers import LoanSerializer
from .models import Loan


# Define PDFKIT_CONFIG with the correct path
PDFKIT_CONFIG = pdfkit.configuration(
    wkhtmltopdf=r"C:\Users\rinee\Downloads\wkhtmltox-0.12.6-1.mxe-cross-win64\wkhtmltox\bin\wkhtmltopdf.exe"
)


@api_view(['POST'])
def generate_pdf(request):
    serializer = LoanSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()  
        data = serializer.data

        # Render HTML template with data
        html_content = render_to_string('pdf_template.html', {'data': data})

        # Convert HTML to PDF
        pdf_file = pdfkit.from_string(html_content, False, configuration=PDFKIT_CONFIG)

        # Create HTTP Response with PDF
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="loan_report.pdf"'
        return response

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
