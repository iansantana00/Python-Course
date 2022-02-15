
import PyPDF2

file = open("sample.pdf", "rb")
reader = PyPDF2.PdfFileReader(file)
page1=reader.getPage(0)
print(reader.numPages)
pdfData=page1.extractText()
print(pdfData)
page2=reader.getPage(1)
print("Data from page 2", page2.extractText*())

"""
#install pyDF2
pip install PyPDF2

# importing all the required modules
import PyPDF2

# creating an object 
file = open('example.pdf', 'rb')

# creating a pdf reader object
fileReader = PyPDF2.PdfFileReader(file)

# print the number of pages in pdf file
print(fileReader.numPages)

"""