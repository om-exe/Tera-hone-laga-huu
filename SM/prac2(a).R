coin = 2;
dice= 6;
get_4=1;
get_h=1;
prob_4=get_4/dice;
prob_h=get_h/coin;
ans  = prob_4*prob_h;
print(paste("ans ",ans));


total=52;
red = 26;
face=12;
prob_red=red/total;
prob_face=face/total;
ans = prob_red*prob_face;
print(paste("ans is ", ans))

d = 13;
b = 26;
a = 2;
prob_d=d/total;
prob_b=a/b;
answer=prob_d*prob_b;
print(paste("ans is ",answer))


oc=6;
odd=3;
div_3=2;
prob_div_3=div_3/oc;
prob_odd=odd/oc;
ans1=prob_odd+prob_div_3-(1/oc);
print(paste("ans is ",ans1))