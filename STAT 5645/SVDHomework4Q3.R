library(imager)
#Original Image
image <- load.image("waterfall.jpg")
image <- grayscale(image)
plot(image, main = "Original Image", axes=FALSE)

SVDValues <- svd(scale(image))
#SVDValues has values for U, D, and V. Since we're showing the original Matrix
#as M = UDVt, thus using the number of singular values and multiplying them across
#should accurately estimate this image according to the required rank

#SVD Rank 1 
R1approx <- SVDValues$u[,1] %*% as.matrix(SVDValues$d[1]) %*% t(SVDValues$v[,1]) 
plot(as.cimg(R1approx, dim=dim(image)), main = "Rank 1 Approximation", axes = FALSE,)
#by the Young-Eckart Theorem, we know the error is the K+1th singular value, thus 
R1error <- SVDValues$d[2]

#SVD Rank 2 
R2approx <- SVDValues$u[,1:2] %*% diag(SVDValues$d[1:2]) %*% t(SVDValues$v[,1:2]) 
plot(as.cimg(R2approx, dim=dim(image)), main = "Rank 2 Approximation", axes = FALSE)
#by the Young-Eckart Theorem, we know the error is the K+1th singular value, thus 
R2error <- SVDValues$d[3]

#SVD Rank 3 
R3approx <- SVDValues$u[,1:3] %*% diag(SVDValues$d[1:3]) %*% t(SVDValues$v[,1:3]) 
plot(as.cimg(R3approx, dim=dim(image)), main = "Rank 3 Approximation", axes = FALSE)
#by the Young-Eckart Theorem, we know the error is the K+1th singular value, thus 
R3error <- SVDValues$d[4]

#SVD Rank 4 
R4approx <- SVDValues$u[,1:4] %*% diag(SVDValues$d[1:4]) %*% t(SVDValues$v[,1:4]) 
plot(as.cimg(R4approx, dim=dim(image)), main = "Rank 4 Approximation", axes = FALSE)
#by the Young-Eckart Theorem, we know the error is the K+1th singular value, thus 
R4error <- SVDValues$d[5]

#SVD Rank 5 
R5approx <- SVDValues$u[,1:5] %*% diag(SVDValues$d[1:5]) %*% t(SVDValues$v[,1:5]) 
plot(as.cimg(R5approx, dim=dim(image)), main = "Rank 5 Approximation", axes = FALSE)
#by the Young-Eckart Theorem, we know the error is the K+1th singular value, thus 
R5error <- SVDValues$d[6]

#plotting all singular values 
plot(SVDValues$d, main = "Singular Values Plotted")
#seems like after 50 it drops off hard, gonna check rank
R50error <- SVDValues$d[51]
R100error <- SVDValues$d[101]
R200error <- SVDValues$d[201]
R300error <- SVDValues$d[301]

R50approx <- SVDValues$u[,1:50] %*% diag(SVDValues$d[1:50]) %*% t(SVDValues$v[,1:50]) 
plot(as.cimg(R50approx, dim=dim(image)), main = "Rank 50 Approximation", axes = FALSE)

R100approx <- SVDValues$u[,1:100] %*% diag(SVDValues$d[1:100]) %*% t(SVDValues$v[,1:100]) 
plot(as.cimg(R100approx, dim=dim(image)), main = "Rank 100 Approximation", axes = FALSE)
