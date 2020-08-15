import numpy as np
import os, csv, sys

np.random.seed(42)
np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(formatter={'float': lambda x: 'float: ' + str(x)})
class CrossMatrix1:
    counts = 0
    train_x = 0
    train_y = 0
    test_x = 0
    data = []

    '''
    Initialization Variables
    def __init__(self, counts):
        self.counts = counts - 1
        self.train_x = np.zeros((int(counts)-1, 45, 45, 3))
        self.train_y = np.zeros((int(counts)-1, 45))
        self.test_x = np.zeros((1, 45, 45, 3))
    '''

    def splitTrain(self):
        if os.name == 'nt':
            path = os.path.abspath('..\\..\\..')
            file_path = os.path.abspath(os.path.join(path,'data\\lotto_input.csv'))
        else:
            path = os.path.abspath('../../..')
            file_path = os.path.abspath(os.path.join(path, 'data/lotto_input.csv'))
        with open(file_path, 'r') as input:
            self.data = list(csv.reader(input))
            self.data = self.data[::-1]
        input.close()

        #Initial class variables
        self.counts = int(self.data[-1][0])
        self.train_x = np.zeros((self.counts - 1, 45, 45, 3)).astype('int32')
        self.train_y = np.zeros((self.counts - 1, 45)).astype('int32')
        self.test_x = np.zeros((1, 45, 45, 3)).astype('int32')

        #make train data
        self.makeTrain(self.data)
        self.makePredictData(self.data[-1][1:7])

        print("Sample print")
        print("CrossMatrix1 Channel 1 Sample:")
        print(np.array_str(self.train_x[202][:,:,0], max_line_width=1000000))
        print("CrossMatrix1 Channel 2 Sample:")
        print(np.array_str(self.train_x[202][:,:,1], max_line_width=1000000))
        print("CrossMatrix1 Channel 3 Sample:")
        print(np.array_str(self.train_x[202][:,:,2], max_line_width=1000000))
        return self.train_x, self.train_y, self.test_x

    def makeTrain(self, data):
        index_x = 0
        index_y = 0
        for row in data[:-1]:
            index_x = self.makeTrainX(index_x, list(row[1:7]))

        for row in data[1:]:
            index_y = self.makeTrainY(index_y, list(row[1:7]))

    def makeTrainX(self, index_x, lottoNumbers):
        for number in lottoNumbers:
            self.train_x[index_x][int(number) - 1,int(number) - 1,1] = number

            for axis in range(0,45):
                self.train_x[index_x][int(number) - 1,axis,2] = number
                self.train_x[index_x][axis,int(number) - 1,2] = number

            for axis in range(int(number) - 1, 45):
                self.train_x[index_x][int(number) - 1,axis,0] = number
                self.train_x[index_x][axis,int(number) - 1,0] = number
        index_x = index_x + 1
        return index_x

    def makeTrainY(self, index_y, lottoNumbers):
        for number in lottoNumbers:
            self.train_y[index_y][int(number) - 1] = 1
        index_y = index_y + 1

        return index_y

    def makePredictData(self, lottoNumbers):
        for number in lottoNumbers:
            self.test_x[0][int(number) - 1][int(number) - 1][1] = number

            for axis in range(int(number) - 1, 45):
                self.test_x[0][int(number) - 1][axis][0] = number
                self.test_x[0][axis][int(number) - 1][0] = number

            for axis in range(0, 45):
                self.test_x[0][int(number) - 1][axis][2] = number
                self.test_x[0][axis][int(number) - 1][2] = number

    def getFinanceData(self):
        if os.name == 'nt':
            path = os.path.abspath('..\\..\\..')
            file_path = os.path.abspath(os.path.join(path,'data\\financeData'))
        else:
            path = os.path.abspath('../../..')
            file_path = os.path.abspath(os.path.join(path, 'data/financeData'))
        yData = open(file_path,'r').read().split('\n')
        return yData
