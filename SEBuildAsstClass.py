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
class Blocks:
    def __init__(self):
        self.name = ""
        self.catagory = ""
        self.materials = [0]* 24
        self.mass = 0
        self.maxMass = 0
        self.power = 0
        self.dimensions = [0]*3
        self.isLarge = True
        self.thrust = 0
        self.materialsNomen = ["200mm Missile Container", "25x184mm NATO Ammo Container", "Bulletproof Glass", "Canvas",
            "Computer", "Construction Components", "Detector Equipment", "Display", "Explosives", "Girders",
            "Gravity Generator Components", "Interior Plate", "Large Steel Tube", "Medical Components",
            "Metal Grid", "Motor", "Power Cell", "Radio Communication Components", "Reactor Comp", "Small Steel Tube",
            "Solar Cell", "Steel Plate", "Super Conductor", "Thruster"]

    ##Gets
    def getListAll (self):
        print ("----------------------------------------------------------------")
        print ("Block Name: ", self.name)
        print ("Catagory: ", self.catagory)
        for i in range(len(self.materials)):
            print (self.materialsNomen[i], ":", self.materials[i])
        print ("Mass:", self.mass)
        print ("Max Mass:", self.maxMass)
        print ("Power: ", self.power)
        print ("Thrust: ", self.thrust)
        print ("Dimensions (LxWxH):", self.dimensions)
        print ("Is a Large Block: ", self.isLarge)

    def getName(self):
        return self.name
    def getMaterials(self):
        getMaterials = []
        for i in range(len(self.materials)):
            getMaterials.append(self.materials[i])
        return getMaterials
    def getCatagory(self):
        return self.catagory
    def getMass(self):
        return self.mass
    def getMaxMass(self):
        return self.maxMass
    def getPower(self):
        return self.power
    def getThrust(self):
        return self.thrust
    def getDimensions(self):
        return self.dimensions
    def getIsLarge(self):
        return self.isLarge

    ##Sets
    def setName(self, name):
        self.name = name
    def setCatagory(self, catagory):
        self.catagory = catagory
    # See comments above to determine elementNum
    def setMaterial(self, elementNum, qty):
        try:
            self.setMaterial[elementNum - 2]  = qty
        except:
            print ("Unable to set the material value")
    def setMass(self, qty):
        self.mass=qty
    def setMaxMass(self, qty):
        self.maxMass = qty
    def setPower(self, qty):
        self.power = qty
    def setThrust(self, qty):
        self.thrust = qty
    def setDimensionLength(self, qty):
        self.dimensions[0] = qty
    def setDimensionWidth(self, qty):
        self.dimensions[1]
    def setDimensionHeight(self, qty):
        self.dimensions[2]
    def setIsLarge(self, bool):
        if bool != True or bool !=False:
            print ("Not a TRUE or FALSE statement.")
        else:
            self.isLarge = bool


    def UpdateAllMaterials(self, indexNumber, componentQty):
        #print ("IndexNumber:", indexNumber)
        if indexNumber == 0:
            self.name = componentQty
        elif indexNumber == 1:
            self.catagory = componentQty
        elif indexNumber >= 2 and indexNumber <= 25:
            self.materials[indexNumber - 2] = componentQty
        elif indexNumber == 26:
            self.mass = componentQty
        elif indexNumber == 27:
            self.maxMass = componentQty
        elif indexNumber == 28:
            self.power = componentQty
        elif indexNumber >= 29 and indexNumber<= 31:
            self.dimensions[indexNumber - 29] = componentQty
        elif indexNumber == 32:
            self.thrust = componentQty
        elif indexNumber == 33:
            self.isLarge = componentQty
        else:
            print ("SEBuildAsstClass has no where to put the componentQty for indexNumber:", indexNumber)


        #print ("Updated Component Index: %s" %indexNumber-2, "Qty: %s" %componentQty)



class Gui:
    #items (Wind Turbine) -> components (Steel Plate)
    #                     -> characterisitics
    def __init__(self, items):
        self.itemList = []
        for i in items.keys():
            self.itemList.append(i)
        self.itemList.sort()
        self.runningTotal = [0] * 24
        self.blockTracker = []
        self.runningTotalLabels = [""] * 24
        self.materials = []
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


        self.win = Tk()
        self.win.title("Space Engineer Build Assistant")

     ####    FRAMES
        self.frameListBox = LabelFrame(self.win, labelanchor='n',text="Block List", padx=4, pady=4, bd=6 )
        self.frameMaterials = LabelFrame(self.win, labelanchor='n',text="Materials Required", padx=10, pady=10, bd=6)
        self.frameRunningTotals = LabelFrame(self.win, labelanchor='n', text="Total Units Required", padx=10, pady=10, bd=6)
        self.frameMassThrust = LabelFrame(self.win, labelanchor='n', text="Mass/Thrust", padx=4, pady=4, bd=6)
        self.frameBlockMaterialsButtons = LabelFrame(self.win,padx=10, pady=10, bd=6)
        self.frameBlocksUsed = LabelFrame(self.win, labelanchor='n', text="Blocks Used", padx=4, pady=4, bd=6)
     ####
        self.itemListBox = Listbox(self.frameListBox, height=12)
        #self.itemListBox.bind('<<ListboxSelect>>', self.selection)

        self.blocksUsedListBox = Listbox(self.frameBlocksUsed, height=12, disabledforeground='Black')
       ####    BUTTONS
        self.removeButton = Button(self.frameBlockMaterialsButtons, text="remove")
        self.addButton = Button(self.frameBlockMaterialsButtons, text="add")
        self.clearButton = Button(self.frameBlockMaterialsButtons, text="clear all")
        self.exportButton = Button(self.frameBlockMaterialsButtons, text="export")
        self.quitButton = Button(self.frameBlockMaterialsButtons, text="quit", command=self.quitApp)

    def quitApp(self):
        print ("Attempting Self Destruct")
        self.win.destroy()

    def initScreen(self):
        row = -1
        column = 0
        #itemListBox is populated with items
        for i in range(0, len(self.itemList)):
            self.itemListBox.insert(END, self.itemList[i])
        #materialLabel for both frameMaterials and frameRunningTotals Populated
        print ("Length of materialLabels:", len(self.materialLabels))
        for i in range(0,len(self.materialLabels)):
            row = row + 1
            if (row >= 9):
                column = column + 2
                row = 0
            (Label(self.frameMaterials, text="0", justify=LEFT)).grid(row=row, column=column+1, sticky=E)
            (Label(self.frameMaterials, text=self.materialLabels[i], justify=LEFT)).grid(row=row, column=column, sticky=E, padx=5)
            (Label(self.frameRunningTotals, text=self.materialLabels[i], justify=LEFT)).grid(row=row, column=column, sticky=E, padx=5)
        ###Draw all the Frames not already drawn by other functions
        self.itemListBox.grid(pady=3)
        self.blocksUsedListBox.grid()
        self.frameListBox.grid(column=0, row=0)
        self.frameMaterials.grid(column=1, row=0)
        self.frameRunningTotals.grid(column=1, row=2)
        
        self.frameBlockMaterialsButtons.grid(row=1,column=1, columnspan=4)

        #self.updateRunningTotals()
        #self.updateMaterialList()
        self.frameMassThrust.grid(column=0, row=1, sticky=N+E+S+W)
        self.frameBlocksUsed.grid(column=0, row=2, stick=N+E+W+S)
        print("Frames Gridded")

        #Material selection Buttons
        self.addButton.grid(column=0)
        self.removeButton.grid(row=0, column=1)
        self.clearButton.grid(row=0, column=2)
        self.exportButton.grid(row=0, column=3)
        self.quitButton.grid(row=0, column=4)
            #Total Mass and thrust needed
    def updateMaterialList(self):
        (self.frameMaterials.grid_remove())

        row, column = -1, 1
        if self.selectedBlockIndex == None:
            self.selectedBlockIndex = 0
            print ("It's None Type: setting 0")
        for i in range(0, len(self.materialLabels)):
            row = row + 1
            if (row >= 9):
                column = column + 2
                row = 0
            # self.runningTotalLabels[i].grid_forget()
            ## Use Error catching for free up display.
            try:
                self.blockList[self.selectedBlockIndex].materials[i].grid_forget()
            except:
                print("Material List not displayed yet")

            self.materialLabels[i] = Label(self.frameMaterials, text=self.blockList[self.selectedBlockIndex].materials[i], justify=LEFT, width=5)
            self.materialLabels[i].grid(row=row, column=column)

        (self.frameMaterials).grid(column=1, row=0, sticky=N+E+S+W)
        self.frameMassThrust.grid(column=0, row=1, sticky=N + E + S + W)
    
    