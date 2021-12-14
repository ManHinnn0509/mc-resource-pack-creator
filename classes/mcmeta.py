import os

from util.file_utils import writeJSON_File

# Pack format: https://minecraft.fandom.com/wiki/Resource_Pack#Pack_format

class MCMetaFile:
    def __init__(self, resourcePackName) -> None:
        self.resourcePackName = resourcePackName

        self.filePath = f"./{resourcePackName}/pack.mcmeta"
    
    def exists(self):
        return os.path.exists(self.filePath)
    
    def create(self, pack_format=8, description="Custom Resource Pack"):
        template = {
            "pack": {
                "pack_format": pack_format,
                "description": f"{description}"
            }
        }

        writeJSON_File(self.filePath, template)