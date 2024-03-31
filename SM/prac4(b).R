total =1:6
prob=rep(1/6,6)
mean =sum(total*prob)
variance =sum((total-mean)^2*prob)
sd=sqrt(variance)
cat("variance is=",variance,"\n")
cat("standard deviation=",sd,"\n")
