from tensorflow.contrib.learn.python.learn.datasets.mnist import *
seed(1234567890)
bat_num=10
m=read_data_sets('../MNIST-data/')
x,y=m.train.next_batch(bat_num)# read bat_num images & labels
#shape(x)  #(10, 784)
#shape(y)  #(10,)
affect_ratio = 0.05 # should be in (0,1)

mat=rand(784,784)
for i,j in muloop(shape(mat)):
    if mat[i,j]<affect_ratio:
        mat[i,j]=-1
    elif mat[i,j]>(1-affect_ratio):
        mat[i,j]=1
    else:
        mat[i,j]=0

for idx in range(bat_num):
    print(idx)
    x_ =x[idx]
    xdm=dot(x_ , mat)
    xdm=dot(xdm, mat)
    xdm=dot(xdm, mat)

    pcolormesh(equally_divide(xdm, 28));
    savefig('%d_is_%d.jpg'%(idx,y[idx]))
