#! /usr/bin/env python3

### Simple example to combine 2 PDF files
### Assuming first file name is meetingminutes1.pdf, and 2nd is
### meetingminutes2.pdf. Both are in the current working directory.

import os
import PyPDF2

pdfFile1 = open('meetingminutes1.pdf','rb')
pdfFile2 = open('meetingminutes2.pdf','rb')

myPdf1 = PyPDF2.pdf.PdfFileReader(pdfFile1)
myPdf2 = PyPDF2.pdf.PdfFileReader(pdfFile2)

myNewPdf = PyPDF2.pdf.PdfFileWriter()

for i in range(myPdf1.numPages):
    myPage = myPdf1.getPage(i)
    myNewPdf.addPage(myPage)


for i in range(myPdf2.numPages):
    myPage = myPdf2.getPage(i)
    myNewPdf.addPage(myPage)

mergedFile = open('Combined_Merged_PDF.pdf','wb')
myNewPdf.write(mergedFile)
mergedFile.close()
pdfFile1.close()
pdfFile2.close()
