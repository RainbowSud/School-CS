#HW 4 Q1
Adat = c(0, -1, 2, 1, -1, 1, -1, -1, 1, -2, 0, 1, 1, 3, 0, 0)
A = matrix(Adat, nrow=4)
A
det(A)
pracma::charpoly(A)

#HW 4 Q2
Adat = c(1,0,0,0)
A=matrix(Adat,nrow=2)
A
pracma::charpoly(A)
pracma::eig(A)
eigen(A)
