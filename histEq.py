from tensorflow.contrib.learn.python.learn.datasets.mnist import *

if_1hot = False
# mnist = load_mnist()
mnist = read_data_sets("../MNIST-data/", one_hot=if_1hot)
x = mnist.train.images
y = mnist.train.labels

idx = 0

if if_1hot:
    print('the above figure is of number:', list(y[idx]).index(1))
else:
    print('the above figure is of number:', y[idx])
print()
'''
z = x[idx]
for i,j in muloop([28,28]):
    print('%0.3f'%z[i*28+j], end=' ')
    if j>=27: print()
'''

z_=map(int, map(round, z*256))
his=histogram(z_, bins=256)[0]/(28.0*28.0)
cdf=zeros(len(his)+1)
for i in range(len(cdf)): cdf[i] = sum(his[0:i])

print()
for i,j in muloop([28,28]):
    print('%3d'%z_[i*28+j],end=' ')
    if j>=27: print()

sk=uint8(256*cdf)
Z = zeros(28*28)
for i in range(28):
    for j in range(28):
        Z[i*28+j] = sk[z_[i*28+j]]

print()
for i,j in muloop([28,28]):
    print('%3d'%Z[i*28+j],end=' ')
    if j>=27: print()
