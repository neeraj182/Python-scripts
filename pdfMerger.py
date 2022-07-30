import fitz
import os
import sys

print("PDF MERGER")
print("ENTER THE NAME OF THE PDF1, WHICH YOU WANNA APPEND TO PDF2")
file = input(' ')
print("ENTER THE NAME OF THE PDF2")
file2 = input(' ')
pdf = fitz.open(file)
pdf2 = fitz.open(file2)

print("Enter the starting and ending page number of PDF1 which you wanna merge with pdf2 ")
print("from page:")
first = int(input())
print("to page:")
end = int(input())
pdf2.insert_pdf(pdf, from_page=first, to_page=end)
print('Enter a name to save this file, make sure to end it with ".pdf":')
name = input(' ')
pdf2.save(name)
