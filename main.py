import pyttsx3 as ptt
import PyPDF2
book = open('io/CSS Exercise.pdf', mode='rb')
read = PyPDF2.PdfFileReader(book)
pages = read.numPages
print(pages)


for x in range(0, pages):
    page = read.getPage(x)
    text = page.extractText()
    print(text)
    to_be_used = ptt.init()
    to_be_used.say(text)
    to_be_used.runAndWait()




