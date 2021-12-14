from util.file_utils import *
from config import *
from classes import *

def main():

    texturePath = f"./{RESOURCE_PACK_NAME}/assets/minecraft/textures/item/{ITEM_ID}"
    mkdirs(texturePath)
    
    textures = os.listdir(texturePath)
    if (len(textures) == 0):
        print("No textures found. Now exiting...")
        return
    
    # Order matters
    # These 2 lines are for creating order from smallest to largest
    textures = [int(i.split(".")[0]) for i in textures]
    textures = sorted(textures)
    
    # pack.mcmeta file
    mcmeta = MCMetaFile(RESOURCE_PACK_NAME)
    if not (mcmeta.exists()):
        mcmeta.create()
    
    jsonList = ItemJsonList(RESOURCE_PACK_NAME, ITEM_ID)
    for customModelData in textures:
    
        jsonItem = SingleItemJson(RESOURCE_PACK_NAME, ITEM_ID, customModelData)
        if (jsonItem.exists()):
            print(f"Skipping {customModelData} (Already exists)")
        
        else:
            jsonItem.create()
            print(f"Created {customModelData}")

        jsonList.addEntry(customModelData)
    
    print("--- End of Program ---")

if (__name__ == '__main__'):
    main()