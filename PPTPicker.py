import os
import random

template = {
    "modern1.pptx": {"Blength": 56,"Clength":30},
    "modern2.pptx": {"Blength": 56,"Clength":30},
    "modern3.pptx": {"Blength": 56,"Clength":30},
    "modern4.pptx": {"Blength": 56,"Clength":30},
    "color1.pptx": {"Blength": 56,"Clength":30},
    "modern5.pptx":{"Blength": 56,"Clength":30},
    "modern6.pptx": {"Blength": 56,"Clength":30},
    "modern7.pptx": {"Blength": 56,"Clength":30},
    "modern8.pptx": {"Blength": 20,"Clength":30},
    "modern9.pptx": {"Blength": 20,"Clength":30},
    "color2.pptx": {"Blength": 56,"Clength":30},
    "color3.pptx": {"Blength": 56,"Clength":30},
    "color4.pptx": {"Blength": 56,"Clength":30},
    "color5.pptx": {"Blength": 56,"Clength":30},
    "color6.pptx": {"Blength": 56,"Clength":30},
    "color7.pptx": {"Blength": 56,"Clength":30},
    "color8.pptx": {"Blength": 56,"Clength":30}
}

def getList(relative_folder_path):
    folder_path = os.path.abspath(relative_folder_path)
    try:
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        return files
    except FileNotFoundError:
        print(f"The folder {relative_folder_path} does not exist.")
        return None

def PickPPT(style):
    base_path = os.getcwd()  # Get the current working directory
    if style == "0":
        folderpath = os.path.join(base_path, "PPT Templates", "Colors")
    elif style == "1":
        folderpath = os.path.join(base_path, "PPT Templates", "Modern")
    elif style == "2":
        folderpath = os.path.join(base_path, "PPT Templates", "Space")
    
    folderList = getList(folderpath)
    if not folderList:
        raise FileNotFoundError(f"Folder {folderpath} not found or is empty.")
    
    ppt = folderList[random.randrange(0, len(folderList))]
    print(ppt)
    return (os.path.join(folderpath, ppt), template[ppt])
