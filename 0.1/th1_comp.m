clear all
x=csvread('comp.csv');
v1=x(:,1);
v2=x(:,4);
v3=x(:,7);
v4=x(:,10);
t=x(:,13);
plot(t,v1,t,v2,t,v3,t,v4);