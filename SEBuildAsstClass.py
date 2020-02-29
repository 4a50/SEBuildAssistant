#Space Engineers Buidler Assistant Class File
#SEBuildAsstClass.py
#   blockElements list fed in from Main program
#   0. Name (String)
#   1. Catagory (String)
#   2. 200mm Missile Container
#   3. 25x184mm NATO Ammo Container
#   4. Bulletproof Glass
#   5. Canvas
#   6. Computer
#   7. Construction Components
#   8. Detector Equipments
#   9. Display
#   10. Explosive
#   11. Girder
#   12. Gravity Generator Components
#   13. Interior Plate
#   14. Large Steel Tube
#   15. Medical Components
#   16. Metal Grid
#   17. Motor
#   18. Power Celld
#   19. Radio Communication Components
#   20. Reactor Comp
#   21. Small Steel Tube
#   22. Solar Cell
#   23. Steel Plate
#   24. Super Conductor
#   25. Thruster
#   26. Power (+ Used / - Supplier)(kW)
#   27. Dl (Dimensions Length)
#   28. Dw (Dimensions Width)
#   29. Dh (Dimensions Height)
#   30. Mass (kg)
#   31. Max Mass (kg) <-- If Storage Container number will be different than Mass
#   32. Thrust (kN)
#   33. IsLarge
#SEBuildAsst.py
from tkinter import *
class Gui:
    #items (Wind Turbine) -> components (Steel Plate)
    #                     -> characterisitics
    def __init__(self, items):
        self.win = Tk()
        self.win.title("Space Engineer Build Assistant")
        self.items = items          #Dictionary of items
        self.itemList = list(self.items.keys())          #Capture the names of the items for the listBox
         #Populate the keys into a usable list
        self.itemList.sort()
        self.itemClickList = []
        self.itemToAddList=[]
        self.runningTotal = [0] * 24
        self.preTotal = [0] * 24
        self.blockTracker = []
        #Labels for easier update of information 
        self.selectedItemsLabels = [None] * 24
        self.selectedItemsStrVar = [None] * 24
        for i in range(len(self.selectedItemsStrVar)):
            self.selectedItemsStrVar[i] = StringVar()
            self.selectedItemsStrVar[i].set("0")
        self.runningTotalLabels = [None] * 24
        self.runningTotalLabelsStrVar = [None] * 24
        for i in range(len(self.runningTotalLabelsStrVar)):
            self.runningTotalLabelsStrVar[i] = StringVar()


        self.materialLabels = ["200mm Missile Container",
        "25x184mm NATO Ammo Container",
        "Bulletproof Glass",
        "Canvas",
        "Computer",
        "Construction Components",
        "Detector Equipments",
        "Display",
        "Explosive",
        "Girder",
        "Gravity Generator Components",
        "Interior Plate",
        "Large Steel Tube",
        "Medical Components",
        "Metal Grid",
        "Motor",
        "Power Cell",
        "Radio Communication Components",
        "Reactor Comp",
        "Small Steel Tube",
        "Solar Cell",
        "Steel Plate",
        "Super Conductor",
        "Thruster"]
        self.runningMaxMass = 0
        self.gravity = 9.8
        self.atmospheres = 1
        self.thrust = 0
        self.selectedBlockIndex = None
        
        ####    FRAMES
        self.frameListBox = LabelFrame(self.win, labelanchor='n',text="Block List", padx=4, pady=4, bd=6 )
        self.frameMaterials = LabelFrame(self.win, labelanchor='n',text="Materials Required", padx=10, pady=10, bd=6)
        self.frameRunningTotals = LabelFrame(self.win, labelanchor='n', text="Total Units Required", padx=10, pady=10, bd=6)
        self.frameAddRemoveItems = LabelFrame(self.win, labelanchor='n', text="Add/Remove Items", padx=4, pady=4, bd=6)
        self.frameBlockMaterialsButtons = LabelFrame(self.win,padx=10, pady=10, bd=6)
        self.frameBlocksUsed = LabelFrame(self.win, labelanchor='n', text="Blocks Used", padx=4, pady=4, bd=6)
        ####
        self.itemListBox = Listbox(self.frameListBox, height=12, selectmode=MULTIPLE)
        self.itemListBox.bind('<<ListboxSelect>>', self.addSelection)

        self.blocksUsedListBox = Listbox(self.frameBlocksUsed, height=12, selectmode=MULTIPLE)
        self.blocksUsedListBox.bind('<<ListboxSelect>>', self.subSelection)
        ####    BUTTONS
        self.removeButton = Button(self.frameAddRemoveItems, justify=CENTER, text="-", command=self.subRunTotal)
        self.addButton = Button(self.frameAddRemoveItems, justify=CENTER, text="+", command=self.addRunTotal)
        self.clearButton = Button(self.frameBlockMaterialsButtons, text="clear all")
        self.exportButton = Button(self.frameBlockMaterialsButtons, text="export")
        self.quitButton = Button(self.frameBlockMaterialsButtons, text="quit", command=self.quitApp)

    def quitApp(self):
        print ("Attempting Self Destruct")
        self.win.destroy()
        
    def initScreen(self):        
        #itemListBox is populated with items
        for i in range(0, len(self.itemList)):
            self.itemListBox.insert(END, self.itemList[i])
        #materialLabel for both frameMaterials and frameRunningTotals Populated
        row = -1
        column = 0
        for i in range(0,len(self.materialLabels)):
            row = row + 1
            if (row >= 9):
                column = column + 2
                row = 0
            # Labels are updated based on the string value given by the runningTotals and 
            
            (Label(self.frameMaterials, text="0", justify=LEFT)).grid(row=row, column=column+1, sticky=E)
            
            self.runningTotalLabelsStrVar[i].set(self.runningTotal[i])
            self.selectedItemsStrVar[i].set("0")
            self.selectedItemsLabels[i] = (Label(self.frameMaterials, textvariable=self.selectedItemsStrVar[i], justify=LEFT))
            self.selectedItemsLabels[i].grid(row=row, column=column+1, sticky=E)
            self.runningTotalLabels[i] = (Label(self.frameRunningTotals, textvariable=self.runningTotalLabelsStrVar[i], justify=LEFT))
            self.runningTotalLabels[i].grid(row=row, column=column+1, sticky=E)
            
            (Label(self.frameMaterials, text=self.materialLabels[i], justify=LEFT)).grid(row=row, column=column, sticky=E, padx=5)
            (Label(self.frameRunningTotals, text=self.materialLabels[i], justify=LEFT)).grid(row=row, column=column, sticky=E, padx=5)
        ###Draw all the Frames not already drawn by other functions
        self.itemListBox.grid(pady=3)
        self.blocksUsedListBox.grid()
        self.frameListBox.grid(column=0, row=0)
        self.frameMaterials.grid(column=1, row=0)
        self.frameRunningTotals.grid(column=1, row=2)
        
        self.frameBlockMaterialsButtons.grid(row=1,column=1, columnspan=4)
        self.frameAddRemoveItems.grid(column=0, row=1, sticky=N+E+S+W)
        self.frameBlocksUsed.grid(column=0, row=2, stick=N+E+W+S)
        print("Frames Gridded")

        #Material selection Buttons
        self.addButton.grid(column=0)
        self.removeButton.grid(row=0, column=1)
        self.clearButton.grid(row=0, column=2)
        self.exportButton.grid(row=0, column=3)
        self.quitButton.grid(row=0, column=4)
            #Total Mass and thrust needed
        self.updateMaterialList()
    def updateMaterialList(self):
        row = -1
        column = 0
        for i in range(0,len(self.materialLabels)):
            row = row + 1
            if (row >= 9):
                column = column + 2
                row = 0
            # Populated by zeros until data is filled in
            #(Label(self.frameMaterials, text="0", justify=LEFT)).grid(row=row, column=column+1, sticky=E)
            self.runningTotalLabelsStrVar[i].set(self.runningTotal[i])
            

    def addRunTotal(self):
        selectedMaterialList = []
        #itemClickList stores the index numbers from the selection event.  selectedMaterialList breake out
        #materials into an integered list.  The materialList for loop adds the integers from selectedMaterial List to runningTotals.
        print (self.itemClickList)
        print("addRunTotal Started Correctly")
        if self.itemClickList!= []:
            for lists in self.itemClickList:
                print("lists:", lists)
                selectedMaterialList.append(self.items[self.itemList[lists]][2:26])
                self.blocksUsedListBox.insert(END, self.itemList[lists])
            for materialList in selectedMaterialList:
                for materials in range(len(materialList)):
                    self.runningTotal[materials] += materialList[materials]
            self.updateMaterialList()
            print("Done with the AddRunTotal")
            self.blocksUsedListBox.grid()
    def subRunTotal(self):
        selectedMaterialList = []
        #itemClickList stores the index numbers from the selection event.  selectedMaterialList breaks out
        #materials into an integered list.  The materialList for loop subtracts the integers from selectedMaterial List to runningTotals.
        print("subRunTotal Started Correctly")
        if self.itemClickList!= []:
            #This will cycle through the strings in the itemClickList and add it to the local variable selectedMaterialList[]
            for lists in self.itemClickList:
                selectedMaterialList.append(self.items[self.blocksUsedListBox.get(lists)][2:26])

            #This will loop through local var selectedMaterialList and subtract each value from the runningTotal List
            for materialList in selectedMaterialList:
                for materials in range(len(materialList)):
                    if self.runningTotal[materials] > 0:                        
                        self.runningTotal[materials] -= materialList[materials] 
                    else:                        
                        self.runningTotal[materials] = 0
            self.updateMaterialList()
        print("Done with the subRunTotal")

    def addSelection(self, evt):
        materialCount = 0
        self.itemClickList = list(evt.widget.curselection())
        
        for i in self.itemClickList:
            for q in range(2,26):
                print("i", i, "q:", q, "MaterialCount:", materialCount)
                print("self.item Entry:", self.items[self.itemList[i]][q])
                self.selectedItemsStrVar[materialCount].set(self.items[self.itemList[i]][q])
                print("StrVar:", self.selectedItemsStrVar[materialCount].get())
                materialCount += 1
        #print (self.itemList[self.itemClickList])

    def subSelection(self, evt):
        self.itemClickList = list(evt.widget.curselection())   
    