import os

def findInFiles():
    targetLower = 'searchValue'.lower() #what you are searching for.
    rootDir = 'C:\\Users\\Public\\Documents' #where you are searching..
    foundFiles = []

    for dirpath, dirnames, filenames in os.walk(rootDir):
        for name in filenames:
            filePath = os.path.join(dirpath, name)
            try:
                text = aqFile.ReadWholeTextFile(filePath, 22)
            except:
                Log.Warning('Skipped unreadable file: ' + filePath)
                continue

            if text and targetLower in text.lower():
                foundFiles.append(filePath)
                Log.Message('Match found: ' + filePath)

    if foundFiles:
        Log.Message('Total matches: ' + str(len(foundFiles)))
    else:
        Log.Message('No matches found in: ' + rootDir)

    return foundFiles
