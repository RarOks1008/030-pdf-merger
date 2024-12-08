import os
from datetime import datetime
from PyPDF2 import PdfMerger

current_directory = os.getcwd()

to_merge_path = os.path.join(current_directory, "to_merge")
merged_path = os.path.join(current_directory, "merged")

os.makedirs(merged_path, exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_pdf_path = os.path.join(merged_path, f"merged_{timestamp}.pdf")

merger = PdfMerger()

if os.path.exists(to_merge_path):
    for filename in sorted(os.listdir(to_merge_path)):
        file_path = os.path.join(to_merge_path, filename)
        if os.path.isfile(file_path) and filename.lower().endswith(".pdf"):
            merger.append(file_path)
    
    if merger.pages:
        merger.write(output_pdf_path)
    merger.close()