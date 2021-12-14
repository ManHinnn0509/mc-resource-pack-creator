from util.file_utils import *

# Example path
# .\Pack\assets\minecraft\models\item\prismarine_crystals.json

class ItemJsonList:

    def __init__(self, resourcePackName, itemID) -> None:
        self.resourcePackName = resourcePackName
        self.itemID = itemID

        self.folderPath = f"./{resourcePackName}/assets/minecraft/models/item"
        self.filePath = f"{self.folderPath}/{itemID}.json"

        self.data = readJSON_File(self.filePath)

        # If the file doesn't exists
        if (self.data == None):
            # Init the file then read again
            self.__initFile()
            self.data = readJSON_File(self.filePath)
    
    def addEntry(self, customModelData):
        d = {
            "predicate": {
                "custom_model_data": 2
            },
            "model": f"item/{self.itemID}/{customModelData}"
        }

        self.data['overrides'].append(d)
        r = writeJSON_File(self.filePath, self.data)

        return r

    def __initFile(self):
        mkdirs(self.folderPath)

        d = {
            "parent": "item/handheld",
            "textures": {
                "layer0": f"item/{self.itemID}"
            },
            "overrides": [
                
            ]
        }

        writeJSON_File(self.filePath, d)