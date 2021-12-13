class SingleItemJson:

    def __init__(self, resourcePackName, itemID, customModelData) -> None:
        self.resourcePackName = resourcePackName
        self.itemID = itemID
        self.customModelData = customModelData

        self.filePath = f""