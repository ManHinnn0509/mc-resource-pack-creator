import os
from util.file_utils import mkdirs, writeJSON_File

# Example path
# .\Pack\assets\minecraft\models\item\prismarine_crystals\2.json

class SingleItemJson:

    def __init__(self, resourcePackName, itemID, customModelData) -> None:
        self.resourcePackName = resourcePackName
        self.itemID = itemID
        self.customModelData = int(customModelData)

        self.folderPath = f"./{resourcePackName}/assets/minecraft/models/item/{itemID}"

        self.filePath = f"{self.folderPath}/{customModelData}.json"
    
    def exists(self):
        return os.path.exists(self.filePath)
    
    def create(self):
        mkdirs(self.folderPath)
        
        template = {
            "parent": "item/handheld",
            "textures": {
                "layer0": f"item/{self.itemID}/{self.customModelData}"
            },
            "display": {
                "firstperson_righthand": {
                    "rotation": [
                        0,
                        -90,
                        0
                    ],
                    "translation": [
                        1.13,
                        3,
                        1.13
                    ],
                    "scale": [
                        0.5,
                        0.5,
                        0.15
                    ]
                },
                "thirdperson_lefthand": {
                    "rotation": [
                        0,
                        90,
                        -55
                    ],
                    "translation": [
                        0,
                        3,
                        -1
                    ],
                    "scale": [
                        0.5,
                        0.5,
                        0.15
                    ]
                },
                "firstperson_lefthand": {
                    "rotation": [
                        0,
                        90,
                        0
                    ],
                    "translation": [
                        1.13,
                        3,
                        1.13
                    ],
                    "scale": [
                        0.5,
                        0.5,
                        0.15
                    ]
                },
                "thirdperson_righthand": {
                    "rotation": [
                        0,
                        -90,
                        55
                    ],
                    "translation": [
                        0,
                        3,
                        -1
                    ],
                    "scale": [
                        0.5,
                        0.5,
                        0.15
                    ]
                },
                "gui": {"scale": [
                    1,
                    1,
                    1
                ]},
                "fixed": {
                    "rotation": [
                        180,
                        0,
                        180
                    ],
                    "translation": [
                        0,
                        0,
                        0
                    ],
                    "scale": [
                        0.75,
                        0.75,
                        0.15
                    ]
                },
                "ground": {
                    "rotation": [
                        180,
                        0,
                        180
                    ],
                    "translation": [
                        0,
                        3.5,
                        0
                    ],
                    "scale": [
                        0.35,
                        0.35,
                        0.15
                    ]
                }
            }
        }

        r = writeJSON_File(self.filePath, template)