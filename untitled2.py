

#linear regression with stochastic gradient descent
import numpy as np

class var():
  x=[1,2,3,4,5]
  y=[1,2,3,4,5]
  B0=0
  B1=0
  LearningRate=.01
  ErrorArr=[]

def PredictY(x):return var.B0+var.B1*x 

def ERROR(x):
  ERRORresult=PredictY(x)-var.y[var.x.index(x)]
  var.ErrorArr.append(ERRORresult)
  return ERRORresult

def BCalc(x):
  var.B0=var.B0-var.LearningRate*ERROR(x)
  var.B1=var.B1-var.LearningRate*ERROR(x)*x 
  return 

def itration(epoches):
  itr_mod=0
  for itr in range(0,epoches):
    if  itr >= len(var.x):itr_mod=1
    BCalc(var.x[itr_mod])
    itr_mod+=1
  return     


def predict(epoches,x_pred):
  itration(epoches)
  return [var.ErrorArr[len(var.ErrorArr)-1],PredictY(x_pred)]

def Start(x_pred_):
  PredArr=predict(epoches=100,x_pred=x_pred_)
  return print((PredArr[0] *PredArr[1]*-1)+PredArr[1])

if __name__=="__main__":
  Start(x_pred_=10)
