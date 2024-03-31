total =1:6
prob=rep(1/6,6)
mean =(total)
variance =((total-mean)*2*prob)
SD=sqrt(variance)
cat("Standard variance is ",SD,"\n")
cat("variance is ",variance,"\n")