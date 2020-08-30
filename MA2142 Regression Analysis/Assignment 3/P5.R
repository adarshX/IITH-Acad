## Importing libraries
library(readxl)
library(car)
library(lmridge)
library(olsrr) 

## Reading Data
Data<-read_excel('Data.xlsx')
Oct<-as.data.frame(Data) #octane data
X <- as.matrix(Data) #regressors


## Splitting data
n_rows = nrow(Oct) 
split_size = floor(0.6 * n_rows ) #training data is 60%
split1 = sample(seq_len(n_rows) , size = split_size)
train_split <- Oct[split1 , ]
valid_split <- Oct[-split1,] #validation data set
X_v <- as.matrix(valid_split) #regressors
p = 4 
n = dim(valid_split)[1]

## column-wise data
colnames(valid_split)
x1 <- valid_split$A1
x2 <- valid_split$A2
x3 <- valid_split$A3
x4 <- valid_split$A4
y_actual <-valid_split$B

## Initial lm1el
lm1 <- lm(y_actual ~ x1 + x2 + x3 + x4)
res<-rstudent(lm1)
fy<-fitted(lm1)
plot(fy,res)
qqnorm(residuals(lm1))


## outlier analysis

index <- vector()
#leverages 
lev<-lm.influence(lm1)$hat
levthres <- (2*5)/33   ## 2 * (p+1)/n --> p = 4 ,n = 33
check <- lev > levthres
i = 0
for (val in check)
{ i = i + 1
  if (val == TRUE)
  {index <- c(index , i)}
}

# COOK'S Distance (should be less than 1)
cd<-cooks.distance(lm1)
check <- cd > 1
i = 0
for (val in check)
{ i = i + 1
  if (val == TRUE)
  {index <- c(index , i)}
}

#DFBETA --> The cut-off value for DFBETAs is 2/sqrt(n) or observations with a value greater than 1.00 
dfb<-dfbeta(lm1)
dfb_limit <- 2/sqrt(33)
check <- dfb > dfb_limit
i = 0
for (val in check)
{ i = i + 1
  if (val == TRUE)
  {index <- c(index , i)}
}

#DFFITS
dfft<-dffits(lm1)
dfft_lim <- (2 * sqrt(p+1))/(n-p-1)
check <- dfft > dfft_lim
i = 0
for (val in check)
{ i = i + 1
  if (val == TRUE)
  {index <- c(index , i)}
}

#COVRATIO
covr<-covratio(lm1)

index <- unique(index)
index <- sort(index)
clean_data <- X_v[-index,]
plot(clean_data)

#data and model after outliers removal
x1 <- clean_data[,1]
x2 <- clean_data[,2]
x3 <- clean_data[,3]
x4 <- clean_data[,4]
y_actual <- clean_data[,5]
lm2 <- lm(y_actual ~ x1 + x2 + x3 + x4)
summary(lm2)
plot(lm2)


## Ridge analsyis
mod <-lmridge( y_actual ~ x1 + x2 + x3 + x4 , data = valid_split, K = seq(0, 0.05, 0.005))
# Multicollineairty
vif(mod)
plot(mod, type = "vif")

# Ridge trace plot
plot(mod, type = "ridge")

## Residual analysis
model1<-lm(y_actual ~ x1 + x2 + x3 + x4)
summary(model1)

residuals_p<-residuals(model1)
plot(residuals_p)

# Studentized residuals
rstandardized<-rstandard(model1)
plot(rstandardized)

# R-Student residuals
rstudent<-rstudent(model1)
plot(rstudent)

# PRESS residuals
press_res <- residuals(model1)/(1-lm.influence(model1)$hat)
plot(press_res)

## Residual Techniques and Transformation
# weighted least squares
wts1 <- 1/fitted(lm(abs(residuals(model1)) ~ fitted(model1)))^2
Weight_mod<-lm(y_actual ~ x1 + x2 + x3 + x4, weights = wts1)

wres<-rstudent(Weight_mod)
wfy<-fitted(Weight_mod)
plot(wfy,wres)

# Box-Cox transformation
lambda<-boxCox(y_actual ~ x1 + x2 + x3 + x4, family="yjPower", plotit = TRUE)
ind<-which(lambda$y == max(lambda$y))
lambda.max<-lambda$x[ind]
y.tr<-bcPower(y_actual, lambda = lambda.max)
mod3<-lm(y.tr~x1 + x2 + x3 + x4)
summary(mod3)
res3<-rstandard(mod3)
fy3<-fitted(mod3)
plot(fy3,res3)

## Model statistics
mallow_CP <- ols_mallows_cp(mod3, lm2) 


## step-wise model selection
ols_step_all_possible(lm2)
ols_step_forward_p(lm2,prem = 0.05)
ols_step_backward_p(lm2,prem = 0.05)
ols_step_both_p(lm2, details = TRUE)
ols_step_backward_aic(lm2,details = TRUE)
ols_step_forward_aic(lm2,details = TRUE)

# AIC ,BIC

AIC1<-AIC(lm(y_actual~x1  ))
AIC2<-AIC(lm(y_actual~x2  ))
AIC3<-AIC(lm(y_actual~x3  ))
AIC4<-AIC(lm(y_actual~x2  ))

AIC12<-AIC(lm(y_actual~x1+x2  ))
AIC13<-AIC(lm(y_actual~x1+x3  ))
AIC14<-AIC(lm(y_actual~x1+x4  ))
AIC23<-AIC(lm(y_actual~x2+x3  ))
AIC24<-AIC(lm(y_actual~x2+x4  ))
AIC34<-AIC(lm(y_actual~x3+x4  ))



AIC123<-AIC(lm(y_actual~x1+x2+x3  ))
AIC124<-AIC(lm(y_actual~x1+x2+x4  ))
AIC134<-AIC(lm(y_actual~x1+x3+x4  ))
AIC234<-AIC(lm(y_actual~x2+x3+x4  ))

AIC1234<-AIC(lm(y_actual~x1+x2+x3+x4  ))

AIC_Vals<-c(AIC1, AIC2, AIC3, AIC4, AIC12, AIC13, AIC14, AIC23, AIC24, AIC34, AIC123, AIC124, AIC134, AIC234, AIC1234)

BIC1<-BIC(lm(y_actual~x1  ))
BIC2<-BIC(lm(y_actual~x2  ))
BIC3<-BIC(lm(y_actual~x3  ))
BIC4<-BIC(lm(y_actual~x2  ))

BIC12<-BIC(lm(y_actual~x1+x2  ))
BIC13<-BIC(lm(y_actual~x1+x3  ))
BIC14<-BIC(lm(y_actual~x1+x4  ))
BIC23<-BIC(lm(y_actual~x2+x3  ))
BIC24<-BIC(lm(y_actual~x2+x4  ))
BIC34<-BIC(lm(y_actual~x3+x4  ))

BIC123<-BIC(lm(y_actual~x1+x2+x3  ))
BIC124<-BIC(lm(y_actual~x1+x2+x4  ))
BIC134<-BIC(lm(y_actual~x1+x3+x4  ))
BIC234<-BIC(lm(y_actual~x2+x3+x4  ))

BIC1234<-BIC(lm(y_actual~x1+x2+x3+x4  ))

BIC_Vals<-c(BIC1, BIC2, BIC3, BIC4, BIC12, BIC13, BIC14, BIC23, BIC24, BIC34, BIC123, BIC124, BIC134, BIC234, BIC1234)

name<-c("1","2","3","4","12","13","14","23","24","34","123","124","134","234","1234")
AIC_BIC<-data.frame(name, AIC_Vals, BIC_Vals)

AIC_BIC


