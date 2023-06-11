from tkinter import *
from PIL import Image
import pytesseract as OCR
from win10toast import ToastNotifier
from tkinter import filedialog



root=Tk()
root.withdraw()
#root.iconbitmap("ICO.ico")
toaster=ToastNotifier()

filetype=(("PNG files","*.png"),("JPG files","*.mkv"),("All files","*.*"))
image_file = filedialog.askopenfilename(initialdir = None, title="Select a image file",filetypes=filetype)
OCR.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
open_image=Image.open(image_file)
text=OCR.image_to_string(open_image)
_dir=r"C:\DEVELOPMENT\PROGRAMMING\Platform\Python\Blaze\blazeScan\output"

saveAs=filedialog.asksaveasfilename(initialdir=_dir,title="Save As", defaultextension=".txt")
with open(saveAs,"w") as scan:
	scan.write(text)
	scan.write('\n')

toaster.show_toast(title='blazeScan', msg='Scanning Done', icon_path=None, duration=5, threaded=True)


