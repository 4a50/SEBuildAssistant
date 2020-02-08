#Space Engineers Buidler Assistant
#SEBuildAsst.py
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
#   26. Mass (kg)
#   27. Max Mass (kg) <-- If Storage Container number will be different than Mass
#   28. Power (+ Used / - Supplier)(kW)
#   29. Dl (Dimensions Length)
#   30. Dw (Dimensions Width)
#   31. Dh (Dimensions Height)
#   32. Thrust (kN)
#   33. IsLarge
#   VSCODE
from pathlib import Path


def Main():
    if (Path('SEDataSheet.csv').exists()):
        fileUse =  Path('SEDataSheet.csv')
        dataFile = open (fileUse, "r")
        dataRead = (dataFile).readlines()
        dataFile.close
    #--Remove the Pop AFTER you fix the .CSV#
    dataRead.pop(0)
    print (dataRead[0])
    print ("Data Read Number of Lines:", len(dataRead))

    item = dataRead[0].split(",")
    for i in range(2, 32):
        item[i] = int(item[i])
    item[32] = float(item[32])
    item[33] = bool(item[33])
    print ("item:", item)
    itemDict = {item[0]: item}
    
    print (itemDict)


if __name__ == '__main__':
    Main()

