import os
import json

def mkdirs(dirName):
    """
        Creates directories recursively
    """
    if not os.path.exists(dirName):
        os.makedirs(dirName)

def readJSON_File(p: str, encoding="utf-8"):
    """
        Reads a json file's content from given path
        None will be returned if exception caught
    """
    try:
        with open(p, "r", encoding=encoding) as f:
            return json.load(f)
    except Exception as e:
        # print(e)
        return None

def writeJSON_File(p: str, d: dict):
    try:
        with open(p, 'w+', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=4)
        return True
    except:
        return False

def writeJSON_File(p: str, d: dict):
    try:
        with open(p, 'w+', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=4)
        return True
    except:
        return False