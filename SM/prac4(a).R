out=1:6;
pro=rep(1/6,6);
mean=sum(out*pro);
cat(mean,"\n")



library(stats);
mean_conn=mean(rnorm(500));
cat(mean_conn);