library(lpSolve)
library(quadprog)
library(pracma)

f.obj <- c(1, 3, 2)
f.con <- matrix(c(1,1,1,1,0,0), nrow=2, byrow=TRUE)
f.dir <- c(">=", ">=")
f.rhs <- c(15,2)
lp("min", f.obj, f.con, f.dir, f.rhs)$solution
lp("min", f.obj, f.con, f.dir, f.rhs, compute.sens=TRUE)$duals



#Solving Linear Primal Program
f.obj <- c(-5, -3)
f.con <- matrix(c(2,2,2,-4,-2,1,0,-1,0,1), nrow=5, byrow=TRUE)
f.dir <- c("<=","<=","<=","<=","<=")
f.rhs <- c(33,8,5,-1,8)
lp("min", f.obj, f.con, f.dir, f.rhs)$solution
#Solving Linear Dual Program
lp("max", -f.obj, f.con, f.dir, f.rhs, compute.sens=TRUE)$duals

x1=2.1666666
x2=0.3333333
x3=0
x4=0
x5=0

sol = -33*x1-8*x2-5*x3+x4-8*x5
sol

#Solving Quadratic Primal Program
Dmat <- matrix(c(2,1,1,4), nrow=2, byrow=TRUE)
dvec <- c(5,3)
Amat <- t(matrix(c(1,0,-1,0,0,1,0,-1), nrow=4, byrow=TRUE))
bvec <- c(1,1,1,1)

solve.QP(Dmat, dvec, -Amat, -bvec)







b <- c(1, -2, 10, -1, -1)
P <- (b %*% solve(t(b)%*%b)%*%t(b))
proj <- 107*(P %*% c(1,2,3,4,5))

y <- c(1,2,3,4,5)
Py <- P%*%y
yPy <- y - Py
distance <- sqrt(t(yPy)%*%yPy)
