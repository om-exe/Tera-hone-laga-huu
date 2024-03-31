standard probability distribution
n=5
p=1/2
q=(1-p)
mean=n*p
variance=n*p*q
sd=sqrt(variance)
cat("mean",mean,"\n")
cat("variance=",variance,"\n")
cat("standard deviation=",sd,"\n")


probability of normal distribution
x_values=2.3
prob=pnorm(x_values)
cat("prob of 2.3 in normal distribution=",prob)
