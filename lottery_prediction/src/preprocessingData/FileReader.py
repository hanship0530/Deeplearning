import csv, os
import numpy as np

if os.name == 'nt':
    dir = os.path.abspath('..\\..')
    file_path = os.path.abspath(os.path.join(dir, 'data\\lotto_input.csv'))
else:
    dir = os.path.abspath('../../..')
    file_path = os.path.abspath(os.path.join(dir, 'data/lotto_input.csv'))
with open(os.path.abspath(os.path.join(dir, 'data\\lotto_input.csv')),'r') as inputFile:
    inputReader = csv.reader(inputFile)

    with open(os.path.abspath(os.path.join(dir, 'data\\lotto_inputExtension.csv')),'w',newline='') as inputExtensionFile:
        inputExtensionWriter = csv.writer(inputExtensionFile, delimiter=',',
                                          quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for inputRow in inputReader:
            inputExtensionRow = np.zeros(47)
            inputExtensionRow = inputExtensionRow.astype('int32')
            inputExtensionRow[0] = int(inputRow[0])
            inputExtensionRow[int(inputRow[1])] = inputRow[1]
            inputExtensionRow[int(inputRow[2])] = inputRow[2]
            inputExtensionRow[int(inputRow[3])] = inputRow[3]
            inputExtensionRow[int(inputRow[4])] = inputRow[4]
            inputExtensionRow[int(inputRow[5])] = inputRow[5]
            inputExtensionRow[int(inputRow[6])] = inputRow[6]
            inputExtensionWriter.writerow(inputExtensionRow)
    inputExtensionFile.close()
inputFile.close()
