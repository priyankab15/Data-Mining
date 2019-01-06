import numpy
import scipy
import matplotlib.pyplot as plt
from scipy import stats
scores = numpy.array([114, 100, 104, 89, 102, 91, 114, 114, 103, 105,
108, 130, 120, 132, 111, 128, 118, 119, 86, 72, 111, 103, 74, 112, 107,
103, 98, 96, 112, 112, 93])
xmean = scipy.mean(scores)
sigma = scipy.std(scores)

print((xmean, sigma ))
n = scipy.size(scores)

print(xmean, xmean - 2.576*sigma /scipy.sqrt(n), xmean + 2.576*sigma / scipy.sqrt(n))
plt.stem(scores)
plt.show()

result=scipy.stats.bayes_mvs(scores)
help(scipy.stats.bayes_mvs)
print(result[0])

print('#',50*"-")
# -----------------------
import scipy.stats
help(scipy.stats)
help(scipy.stats.bayes_mvs)
help(scipy.stats.kurtosis)
numpy.info('random')
print('#',50*"-")
# -----------------------
import scipy.misc
img=scipy.misc.ascent()
plt.imshow(img)
plt.show()
print(img[0:3,0:7])
print(img)
img=scipy.misc.face()
plt.imshow(img)
plt.show()
print(img[0:3,0:7])
print(img)
print('#',50*"-")
# -----------------------
import scipy.ndimage
import numpy as np
text = scipy.ndimage.imread('image.png')
text = np.mean(text.astype(float)/255,-1)*2-1
letterE = text[37:53,275:291]
corr = scipy.ndimage.correlate(text,letterE)
eLocations = (corr >= 0.95 * corr.max())
CorrLocIndex = np.where(eLocations==True)
x=CorrLocIndex[1]
print(x)
y=CorrLocIndex[0]
print(y)
thefig=plt.figure()
plt.subplot(211)
plt.imshow(text, cmap=plt.cm.gray, interpolation='nearest')
plt.subplot(212)
plt.imshow(text, cmap=plt.cm.gray, interpolation='nearest')
plt.autoscale(False)
plt.plot(x,y,'wo',markersize=10)
plt.axis('off')
plt.show()
print('#',50*"-")
# -----------------------
A = numpy.array([1,2,3])
print(A)
B = A[::-1].copy()
B[0]=123
print(B)
C = A + B
C = A - B
dotProduct1 = numpy.dot(A, B)
print(dotProduct1)
Product = (A* B)
print(Product)
dotProduct2 = (A* B).sum()
print(dotProduct2)
crossProduct = numpy.cross(A,B)
print(crossProduct)
print('#',50*"-")
# -----------------------
import scipy.sparse
A=numpy.matrix("1,2,3;4,5,6")
print(A)
A=numpy.matrix([[1,2,3],[4,5,6]])
print(A)
A=numpy.matrix([ [0,10,0,0,0], [0,0,20,0,0], [0,0,0,30,0],
                     [0,0,0,0,40], [0,0,0,0,0] ])
print(A)
print(A[0,1],A[1,2],A[2,3],A[3,4])
rows=numpy.array([0,1,2,3])
cols=numpy.array([1,2,3,4])
vals=numpy.array([10,20,30,40])
A=scipy.sparse.coo_matrix( (vals,(rows,cols)) )
print(A)
print(A.todense())
B=numpy.mat(numpy.ones((3,3)))
W=numpy.mat(numpy.zeros((3,3)))
print(numpy.bmat('B,W;W,B'))
a=numpy.array([[1,2],[3,4]]); print(a)
print(a*a)
v = numpy.dot(a,a); print(v)
print('#',50*"-")
# -----------------------
import scipy.linalg
a=numpy.arange(5)
A=numpy.mat(a)
print(a.shape, A.shape, a.transpose().shape, A.transpose().shape)

A=scipy.linalg.hadamard(8)
zero_sum_rows = (numpy.sum(A,0)==0)
B=A[zero_sum_rows,:]
print(B[0:3,:])

mu=1/numpy.sqrt(2)
A=numpy.matrix([[mu,0,mu],[0,1,0],[mu,0,-mu]])
B=scipy.linalg.kron(A,A)

a=numpy.arange(0,2*numpy.pi,1.6)
A = scipy.linalg.toeplitz(a)
print (A)

print (numpy.exp(A))
print (scipy.linalg.expm(A))
print('#',50*"-")
# -----------------------
from scipy.linalg import svd

plt.rcParams['figure.figsize'] = (12.0, 8.0)
img=scipy.misc.ascent()
U,s,Vh=svd(img)
A = numpy.dot( U[:,0:32], numpy.dot( numpy.diag(s[0:32]), Vh[0:32,:]))
plt.subplot(121,aspect='equal');
plt.gray()
plt.imshow(img)
plt.subplot(122,aspect='equal');
plt.imshow(A)
plt.show()

A=numpy.mat(numpy.eye(3,k=1))
print(A)

b=numpy.mat(numpy.arange(3) + 1).T
print(b)

xinfo=scipy.linalg.lstsq(A,b)
print (xinfo[0].T)
print('#',50*"-")
# -----------------------
import scipy.interpolate
x=scipy.linspace(-1,1,10)
xn=scipy.linspace(-1,1,1000)
y=scipy.sin(x)
polynomial=scipy.interpolate.lagrange(x, scipy.sin(x))
plt.plot(xn,polynomial(xn),x,y,'or')
plt.show()

x=numpy.array([0,0,1,1,2,2])
y=numpy.array([0,0,1,0,2,0])
interp=scipy.interpolate.KroghInterpolator(x,y)
xn=numpy.linspace(0,2,20)
plt.plot(x,y,'o',xn,interp(xn),'r')
plt.show()
print('#',50*"-")
# -----------------------