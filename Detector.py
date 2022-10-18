# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 13:01:41 2021

@author: idea
"""

from pyod.models.lof import LOF
from pyod.models.pca import PCA
import pandas as pd
import numpy as np

class detection_algorithm():
    def __init__(self):
        self.lof = LOF()
        self.pca = PCA()
        self.zero_column = [0,5,10,15]

    def load_dataset_(self, filename):
        pd_file = pd.read_csv(filename, header=None)
        pd_file = np.array(pd_file)
        pd_file = np.delete(pd_file, self.zero_column, axis=1)
        return pd_file

    def load_dataset(self,filename):
        pd_file = pd.read_csv(filename, header=None)
        pd_file = np.array(pd_file)
        pd_file = np.delete(pd_file, self.zero_column, axis=1)
        return pd_file

    def load_test_dataset(self, filename):
        pd_file = pd.read_csv(filename, index_col=0)
        dataset = np.array(pd_file)
        labels = dataset[:,-1]
        dataset = np.delete(dataset, 16, axis=1)
        # print(dataset.shape)
        # print(dataset[:5,:])
        return dataset, labels
    
    def cut_dataset(self, dataset):
        tmp_dataset = np.delete(dataset, self.zero_column, axis=1)
        return tmp_dataset

    def train(self, file_train):
        '''训练函数，需要训练数据集 '''
        train_set = self.load_dataset(file_train)
        #print("shape of train_set: ",train_set.shape)

        #print("start training lof sub-model...")
        self.lof.fit(train_set)
        
        #print("start training pca sub-mode...")
        self.pca.fit(train_set)
        
        #print("Training stage success!!!")

        
    def test(self, file_test):
        '''测试函数，需要测试数据集'''
        test_set, labels = self.load_test_dataset(file_test)
        test_set_cut = self.cut_dataset(test_set)

        scores_l = self.lof.decision_function(test_set_cut)
        scores_p = self.pca.decision_function(test_set_cut)
        # 将两个异常打分相加
        scores = scores_l + scores_p
        # 计算3 sigma 阈值
        mean = np.mean(scores)
        std = np.std(scores)
        t3 = mean + 3 * std
        t_3 = mean - 3 * std

        abnormal_count = 0
        normal_count = 0
        
        print("输出检测异常的数据：")
        
        correct_predict_count = 0
        for index in range(len(labels)):
            real_label = labels[index]
            predict_label = -1
            if scores[index] > t3 or scores[index] < t_3:
                predict_label = 1
                print("异常数据：", test_set[index])
                print("预测标签：", predict_label, "实际标签：", labels[index])
                
            else:
                predict_label = 0
                
            if real_label == predict_label:
                correct_predict_count += 1
        
        
        print("检测正确率：",correct_predict_count / len(labels))
        return scores
    
    
if __name__ == '__main__':
    model = detection_algorithm() #模型创建
    model.train("./train_set.csv") # 模型训练
    model.test("./test_set.csv") # 模型测试
    
