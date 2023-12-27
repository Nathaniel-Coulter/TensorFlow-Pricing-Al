# install.packages("derivmkts")

library(derivmkts)



coupon <- 60; mat <- 3; freq <- 1; principal <- 1000; yield <- 0.056;

price <- bondpv(coupon, mat, yield, principal, freq) 

price

bondpv(coupon, mat, yield, principal, freq)

bondyield(coupon, mat, price=price, principal, freq) 

duration(price, coupon, mat, principal, freq, modified=FALSE)

duration(price, coupon, mat, principal, freq, modified=TRUE)

convexity(price, coupon, mat, principal, freq)