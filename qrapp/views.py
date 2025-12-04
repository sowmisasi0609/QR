from django.shortcuts import render, redirect
from django.conf import settings
from .forms import PDFUploadForm
from .models import PDFFile

import qrcode
from io import BytesIO
from django.core.files import File

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_obj = form.save()  # Save the PDF first

            # Generate URL for QR code
            pdf_url = request.build_absolute_uri(pdf_obj.pdf.url)

            # Generate QR image
            img = qrcode.make(pdf_url)
            buffer = BytesIO()
            img.save(buffer, format='PNG')
            buffer.seek(0)

            # Save QR image
            filename = f'qr_{pdf_obj.id}.png'
            pdf_obj.qr_image.save(filename, File(buffer), save=True)

            return redirect('pdf_detail', pk=pdf_obj.id)
    else:
        form = PDFUploadForm()

    return render(request, 'qrapp/upload_pdf.html', {'form': form})


def pdf_detail(request, pk):
    pdf = PDFFile.objects.get(pk=pk)
    return render(request, 'qrapp/pdf_detail.html', {'pdf': pdf})

