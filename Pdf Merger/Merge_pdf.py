import PyPDF2

pdfiles=["FYP.pdf", "SPM.pdf", "Sample.pdf"]
merger=PyPDF2.PdfMerger()

for filename in pdfiles:
    PdfFile=open(filename, 'rb')
    pdfreader=PyPDF2.PdfReader(PdfFile)
    merger.append(pdfreader)
PdfFile.close()
merger.write("NewPdf.pdf")
