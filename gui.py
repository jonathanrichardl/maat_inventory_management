from tkinter import *
from tkinter import filedialog
from pathlib import Path
from uploader import uploadFile

def openFile():
    try:
        filepath = filedialog.askopenfilename(title="Are you gonna upload this?", filetypes= (("jpg", '*.jpg'),("jpeg", "*.jpeg")) )
        path = Path(filepath)
        
        isUploading = Label(window, text="uploading...", pady=50)
        isUploading.pack()

        if ( uploadFile(path.name, path.parent.absolute()) ):
            # isUploading.destroy()
            myLabel = Label(window, text="The image {0} is uploaded".format(path.name), pady=50)
            myLabel.pack()
        else:
            # isUploading.destroy()
            myLabel = Label(window, text="An error occured. The image {0} is not uploaded".format(path.name), pady=50)
            myLabel.pack()

    except:
        pleaseSelect = Label(window, text="please select the image", pady=50)
        pleaseSelect.pack()
    
    


window = Tk()
window.geometry("500x350")
button = Button(window, text="Select Image", command=openFile, padx=50, pady=25)
button.pack()
window.mainloop()