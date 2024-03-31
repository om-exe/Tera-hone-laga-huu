prob mass function

out=1:6
prob=rep(1/6,6)
pmf=function(x){
if(x%in% out){
return(prob[out==x])
}
else{
return(0)
}
}
for(i in out){
cat(i,"------",pmf(i),"\n")
}


box=1:10
prob=rep(1/10,10)
pmf=function(x){
if(x%in% box){
return(prob[box==x])
}
else{
return(0)
}
}
for(i in box){
cat(i,"------",pmf(i),"\n")
}
