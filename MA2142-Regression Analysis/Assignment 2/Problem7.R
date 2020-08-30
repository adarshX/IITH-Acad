## importing data from excel file
data_model <- read.csv("data.csv")

## storing column wise data
x1 <- data_model$x1
x2 <- data_model$x2
x3 <- data_model$x3
x4 <- data_model$x4
x5 <- data_model$x5
y_actual <- data_model$y

#Applying multiple linear regression
multiple_linear_reg <- lm(y_actual ~ x1 + x2 + x3 + x4 + x5 )
summary(multiple_linear_reg)


# coefficients of variables 
intercept <- 2.85473
x1_coeff <-  -0.29047
x2_coeff <-   0.20572
x3_coeff <-   0.45444
x4_coeff <-   -0.59419
x5_coeff <-   0.00464 

## final equation
y_pred = intercept + x1_coeff * x1 +  x2_coeff * x2 +   x3_coeff * x3 +  x4_coeff * x4 +  x5_coeff * x5
print("Predicted y values by the model : ")
print(y_pred)

