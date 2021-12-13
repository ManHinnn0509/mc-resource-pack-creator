from util.file_utils import *
from config import *

def main():
    texturePath = f"./{RESOURCE_PACK_NAME}/assets/minecraft/textures/item/{ITEM_ID}"
    mkdirs(texturePath)

    # Create .mcmeta file if it doesn't exists
    mcmetaPath = "./{RESOURCE_PACK_NAME}/pack.mcmeta"
    if not (os.path.exists(mcmetaPath)):
        d = {
            "pack": {
                "pack_format": 6,
                "description": "Resource pack ~"
            }
        }
        writeJSON_File(mcmetaPath, d)
    
    textures = os.listdir(texturePath)
    if (len(textures) == 0):
        print("No textures found. Now exiting...")
        return
    

if (__name__ == '__main__'):
    main()