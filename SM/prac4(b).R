variance and sd of discrete and continuous prob distribution
total =1:6
prob=rep(1/6,6)
mean=sum(total*prob)
variance=sum((total-mean)^2*prob)
sd=sqrt(variance)
cat("variance is=",variance,"\n")
cat("standard deviation=",sd,"\n")



continuous prob distribution
library(stats)
random=rnorm(1000)
mean_continuous=mean(random)
var_continuous=var(random)
sd_continuous=sd(random)
cat("mean is",mean_continuous,"\n")
cat("variance is",var_continuous,"\n")
cat("sd is",sd_continuous,"\n")
