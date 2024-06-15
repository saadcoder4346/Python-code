from pypdf import pywriter
import os
a=pywriter
pdfs=os.listdir()
for pdf in pdfs:
    if pdf.endswith(".pdf"):
        a.append(pdf)
a.write("merged pdf.pdf")
a.close()

