#https://www.youtube.com/watch?v=LXsdt6RMNfY
import PyPDF2
import pyttsx3

#MyFile = 'Jose Medina RESUME 2022 Software Developer'
MyFile = 'Download of Discrete Mathematics and Its Applications 8th Edition PDF'

pdfreader = PyPDF2.PdfReader(open(MyFile+'.pdf', 'rb'))
speaker  = pyttsx3.init()


for page_num in range(len(pdfreader.pages)):
    #text = pdfreader.getPage(page_num).extractText()
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)
speaker.save_to_file(clean_text, MyFile+'.mp3')  
speaker.runAndWait() 

speaker.stop()
