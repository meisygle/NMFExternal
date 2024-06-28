###!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import scipy.sparse as sps
from sklearn.decomposition import NMF
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from scipy.spatial.distance import squareform
from scipy.cluster import hierarchy  

def externalpredict(train_file,test_file):
    tol = 1e-3    
    alpha_W = 0.01
    alpha_H = 0.01
    l1_ratio = 0.1
    max_iter = int(1e+6)
    
    X = pd.read_excel(train_file, header = 0, index_col = 0)
    colnames = X.columns
    rownames = X.index
    n_components = len(colnames)        

    
    X_pred = pd.read_excel(test_file, header = 0, index_col = 0)
    colnames_pred = X_pred.columns
    rownames_pred = X_pred.index
    
  
    model = NMF(n_components = n_components, init = 'nndsvd', random_state = 159,beta_loss = 'frobenius', tol = tol, verbose = True, alpha_W = alpha_W, alpha_H =alpha_H, l1_ratio = l1_ratio,max_iter = max_iter)
    W = model.fit_transform(X)
    H = model.components_

    #external test or predict procedure
    test = model.transform(X_pred)        
    Y = np.dot(test,H)
    YF = pd.DataFrame(Y)
    YF.columns = colnames_pred
    YF.index = rownames_pred    

    excel_file = ".\\%s.predict.xlsx" % test_file
    YF.to_excel(excel_file)  
    
    #cas studies: predict missing values in X    
    #test = model.transform(X)   # using the external test or predict procedure, re-mapping X into the reduced space as test matrix    
    #Y = np.dot(test,H)
    
    Y = np.dot(W,H) # or, X = WH
    YF = pd.DataFrame(Y)
    YF.columns = colnames_pred
    YF.index = rownames_pred    

    excel_file = ".\\X.predict.xlsx"
    YF.to_excel(excel_file)     

        
if __name__ == "__main__":
    train_file = '.\\S1.xlsx'
    test_file = '.\\S2.xlsx'
    externalpredict(train_file,test_file)
    print('finished')
            

            
    
    
            
