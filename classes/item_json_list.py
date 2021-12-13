from util.file_utils import readJSON_File, writeJSON_File

class ItemJsonList:

    def __init__(self, resourcePackName, itemID) -> None:
        self.resourcePackName = resourcePackName
        self.itemID = itemID

        self.filePath = f'./{resourcePackName}/assets/minecraft/models/item/{itemID}.json'
        self.data = readJSON_File(self.filePath)

        # If the file doesn't exists
        if (self.data == None):
            self.__initFile()
    
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
        pass