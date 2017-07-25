from tensorflow.contrib.learn.python.learn.datasets.mnist import *
seed(1234567890)
bat_num=10
m=read_data_sets('../MNIST-data/', reshape=False)
x,y=m.train.next_batch(bat_num)# read bat_num images & labels
#shape(x) # (bat_num, 28, 28, 1)
#shape(y) # (bat_num,)
#print(y)

lmat=rand(28,28)
rmat=rand(28,28)

for idx in range(bat_num):
    x_=zeros([28,28])

    for i in range(28):
        for j in range(28):
            x_[i,j] = x[idx,i,j,0]

    print(y[idx])
    for i,j in muloop([28,28]):
        print('%.1f'%x_[i,j], end='')
        if j>=27: print()

    X_=dot(lmat, dot(x_,rmat))/50

    for i,j in muloop([28,28]):
        print('%.3f'%X_[i,j], end=' ')
        if j>=27: print()

    max(flatten(X_)) # 36.2865215

    X = X_+0.5*x_

    pcolormesh(X)
    savefig('%d-th_is_%d.jpg'%(idx,y[idx]))
