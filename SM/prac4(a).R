mean of discrete and continuous prob distribution
out=1:6;
pro=rep(1/6,6);
mean=sum(out*pro);
cat("mean is","\n")


mean of continuous prob distribution (standard normal)
library(stats);
mean_conn=mean(rnorm(500));
cat(mean_conn)
