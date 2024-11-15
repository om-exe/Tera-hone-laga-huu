import matplotlib.pyplot as plt
# 90
# x = 2+4j
# z=1j
# plt.scatter(x.real , x.imag ,color = 'red')
# c = x*z
# plt.scatter(c.real,c.imag,color ='blue')
# plt.show()

# # 180
# x = 2+4j
# plt.scatter(x.real,x.imag,color ='yellow')
# plt.scatter(-1*x.real,-1*x.imag,color='pink')
# plt.show()



# # 270
# x = 2+4j
# z=-1j
# plt.scatter(x.real , x.imag ,color = 'black')
# c = x*z
# plt.scatter(c.real,c.imag,color ='green')
# plt.show()


# scaling 1/2,1/3,2

x = 2+4j
scale = 0.5
scale1 = 0.33
scale2=2
plt.scatter(x.real,x.imag,color='red')
c = scale*x
d=scale1*x
e=scale2*x
plt.scatter(c.real,c.imag,color='green')
plt.scatter(d.real,d.imag,color = 'black')
plt.scatter(e.real,e.imag,color = 'black')
plt.show()