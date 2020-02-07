from SEBuildAsstClass import *
from pathlib import Path
def Main():
    quit = False
    fileLines = 0
    blockElementCount = 0
    #print ("Opening File to Read")
    #print(Path('SEDataSheet.csv').exists())
    #print(Path('SEBuildAsstV2.py').exists())
    if (Path('SEDataSheet.csv').exists()):
        fileUse =  Path('SEDataSheet.csv')
        dataFile = open (fileUse, "r")
        dataRead = (dataFile).readlines()
        ##print ('DataRead: ', dataRead)
        dataFile.close
    else:
	    print ('File does not exists in the current directory')
    
    global blockList
    #print ("Length of dataRead: ", len(dataRead))
    blockList = [0] * (len(dataRead) - 1)
    #print ("Length of blockList:", len(blockList))
    for i in range(len(blockList)):
        #print (i)
        blockList[i] = Blocks()
    #print ("Created %s Block Objects" % len(blockList))
    for lines in dataRead:
        if lines[3:7] == "Name":
            print("Skipped Name Header of File")
        elif lines[0:4] == "Name":
            print("Skipped Name Header of File")
        else:
            #print ('asdf')
            #print ("Line Parse:", lines)
            dataFile.close
            SetupBlockObjects(lines, fileLines)
            fileLines = fileLines + 1
            blockElementCount = blockElementCount + 1
    #for i in range(len(blockList)):
    #print ("Block Name:", blockList[i].name)
    gui = Gui(blockList)
    gui.initScreen()
    #print ("Project Complete")
    gui.win.mainloop()
def SetupBlockObjects(blockString, blockListIndex):
    blockElements = blockString.split(",")
    if len(blockElements) >= 35:
        blockElements.pop()
    for i in blockElements:
        for i in range(2,33):
            try:
                try:
                    blockElements[i] = int(blockElements[i])
                except:
                    blockElements[i] = float(blockElements[i])
            except:
                print("Value %s cannot be converted to an int or float!"%blockElements[i])
        indexUpdater = 0
        for item in blockElements: 
            ##print('Item', item)
            blockList[blockListIndex - 1].UpdateAllMaterials(indexUpdater, item)
            indexUpdater = indexUpdater + 1
Main()      
        
