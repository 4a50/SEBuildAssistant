#Space Engineers Buidler Assistant
#SEBuildAsstV3.py
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

from pathlib import Path
from SEBuildAsstClass import *

def Main():
    if (Path('SEDataSheet.csv').exists()):
        fileUse =  Path('SEDataSheet.csv')
        dataFile = open (fileUse, "r")
        dataRead = (dataFile).readlines()
        dataFile.close
        itemDict = buildDict(dataRead)
    gui = Gui(itemDict)
    gui.initScreen()
    #print ("Project Complete")
    gui.win.mainloop()
    
def buildDict(dataRead):
    #--Remove the Pop AFTER you fix the .CSV
    dataRead.pop(0)
    itemDict = {}
    for i in range(len(dataRead)):
        item = dataRead[i].split(",")
        for i in range(2, 30):
            item[i] = int(item[i])
        for i in range(30, 33):
            item[i] = float(item[i])
        item[33] = bool(item[33])
        itemDict.update({item[0]: item})
    return itemDict


if __name__ == '__main__':
    Main()

