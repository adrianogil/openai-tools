
from .uploadpdf import upload_pdf

import sys

pdf_path = sys.argv[1]
upload_pdf(pdf_path)
