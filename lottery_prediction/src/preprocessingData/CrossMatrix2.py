'''
    This is for LSTM Cross Matrix
'''
import numpy as np
import csv, os
np.random.seed(42)


class CrossMatrix2:
    # Class Variable
    counts = 0
    train_x = 0
    train_y = 0
    test_x = 0
    dimension = 45
    data = []
    data2 = []
    '''
        def __init__(self, counts):
            self.counts = counts - 1
            self.train_x = np.zeros((int(counts)-1, 1, 45))
            self.train_y = np.zeros((int(counts)-1, 45))
            self.test_x = np.zeros((1, 1, 45))
    '''
    def splitTrain(self, mode = 1):
        if os.name == 'nt':
            path = os.path.abspath('..\\..\\..')
            file_path = os.path.abspath(os.path.join(path,'data\\lotto_inputExtension.csv'))
            file_path2 = os.path.abspath(os.path.join(path,'data\\lotto_input.csv'))
        else:
            path = os.path.abspath('../../..')
            file_path = os.path.abspath(os.path.join(path, 'data/lotto_inputExtension.csv'))
            file_path2 = os.path.abspath(os.path.join(path, 'data/lotto_input.csv'))

        with open(file_path, 'r') as input:
            self.data = list(csv.reader(input))
            self.data = self.data[::-1]
        input.close()

        with open(file_path2, 'r') as input:
            self.data2 = list(csv.reader(input))
            self.data2 = self.data2[::-1]
        input.close()

        if(mode == 2):
            self.dimension = 6

        #Initialize Class Variables
        self.counts = int(self.data[-1][0])
        self.train_x = np.zeros((self.counts-1, 1, self.dimension)).astype('int32')
        self.train_y = np.zeros((self.counts-1, 45)).astype('int32')
        self.test_x = np.zeros((1, 1, self.dimension)).astype('int32')

        if(mode == 1):
            self.makeTrain(self.data)
        if(mode == 2):
            self.makeTrain2(self.data, self.data2)

        print("Sample print")
        print(np.array_str(self.train_x[202][0], max_line_width=1000000))

        return self.train_x, self.train_y, self.test_x

    def makeTrain(self, data):
        index_x = 0
        index_y = 0
        for row in data[:-1]:
            self.train_x[index_x][0] = list(row[1:46])
            index_x = index_x + 1

        for row in data[1:]:
            self.train_y[index_y] = [1 if int(x) > 0 else 0 for x in row[1:46]]
            index_y = index_y + 1

        self.test_x[0][0] = list(data[-1][1:46])

    def makeTrain2(self, data, data2):
        index_x = 0
        index_y = 0
        for row in data2[:-1]:
            self.train_x[index_x][0] = list(row[1:7])
            index_x = index_x + 1

        for row in data[1:]:
            self.train_y[index_y] = [1 if int(x) > 0 else 0 for x in row[1:46]]
            index_y = index_y + 1

        self.test_x[0][0] = list(data[-1][1:7])