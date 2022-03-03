% Logistic function f(x;m,b)=1/(1+exp(-mx+b))
%[ valor]=logisticf(x,m,b)

function [ valor]=logisticf(x,m,b)

valor=1./(1.+exp(-m*x+b));