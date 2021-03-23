import os
from tkinter import *
from tkinter import filedialog
import re
import json

class Window: 
          
    def __init__(self, master):     
        self.directoryname=""
        self.var = StringVar()
        # projectfile=Label(master, text="Folder").grid(row=1, column=0)
        # bar=Entry(master)
        # bar.insert(0, "Write your path here")
        # bar.grid(row=1, column=1)

        #Buttons  
        q1 = Label(master, text="Choose your folder")
        q1.pack(fill="both", padx=20)
        browseButton = Button(master, text='Browse', command=self.browse)
        browseButton.pack(fill="both", padx=20)
        label = Label( master, textvariable=self.var)
        self.var.set("")
        label.pack()
        send = Button(master, text='Save', command=self.parseFiles)
        send.pack(fill="both", padx=20)

    def browse(self):
        Tk().withdraw() 
        self.directoryname = filedialog.askdirectory()
        self.var.set(self.directoryname)

    def parseFiles(self):
        master.quit()
        outputFile = self.directoryname + '\ExternalURL.json'
        jsonFile = open(outputFile, "w+")
        jsonFile.write('[ ')
        for (root,dirs,files) in os.walk(self.directoryname):
            for i in files:
                count = 0
                if i.endswith('.html'):
                    pathFile = os.path.normpath(os.path.join(root, i))
                    self.findRegex("href", pathFile, jsonFile)
                    self.findRegex("src", pathFile, jsonFile)
                    self.findRegex("srcset", pathFile, jsonFile)
                    self.findRegex("data", pathFile, jsonFile)
                    self.findRegex("cite", pathFile, jsonFile)
        jsonFile.close()
        with open(outputFile, 'rb+') as filehandle:
            filehandle.seek(-2, os.SEEK_END)
            filehandle.truncate()
        with open(outputFile, 'a') as filehandle:
            filehandle.write(']')

    def findRegex(self, type, htmlFilePath, jsonFile):
        regex = "\s+" + type + "\=[\"\'](.*?)[\"\'][\s\>]"
        count = 0
        with open(htmlFilePath, "r") as htmlFile:
            lines = htmlFile.readlines()
            singleLine = ''
            for each in lines:
                singleLine += each + ' '
            allMatches = re.findall(regex, singleLine)
            for eachMatch in allMatches:
                if not eachMatch.startswith('#'):
                    count += 1
            if self.directoryname in htmlFilePath:
                fPath = htmlFilePath.split(self.directoryname)[-1].strip('\\')
            else:
                directory = self.directoryname.replace('/', '\\')
                fPath = htmlFilePath.split(directory)[-1].strip('\\')
            fPath = fPath.replace('\\', '/')
            if count != 0:
                data = {"name":type, "category":"External URL", "file":fPath,"value":count}
                jstr = json.dumps(data, indent=4)
                jsonFile.write(jstr)
                jsonFile.write(', ')

master = Tk()
windowWidth = master.winfo_reqwidth()
windowHeight = master.winfo_reqheight()
positionRight = int(master.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(master.winfo_screenheight()/2 - windowHeight/2)
master.geometry("+{}+{}".format(positionRight, positionDown))
window=Window(master)
master.mainloop() 