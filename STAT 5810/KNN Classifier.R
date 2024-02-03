library(class)
library(ggplot2)

#Import Data
data_seed <- read.delim("data_seed.dat", header = FALSE, sep ='\t')
#First 7 Cols are seed dimensions, last col is seed type, goal is to 
#predict seed type based on seed dimensions given.

Manual_Split_KNN <- function (split_ratio, k_values) {
  #Split data into train and test data 
  split <- sample.split(data_seed, SplitRatio = split_ratio)
  train_set <- subset(data_seed, split == "TRUE")
  test_set <- subset(data_seed, split == "FALSE")
  train_values <- scale(train_set[, 1:7])
  test_values <- scale(test_set[, 1:7])

  results <- sapply(k_values, function(k) {
    classifier_knn <- knn(train = train_values,
                          test = test_values,
                          cl =  train_set$V8,
                          k = k)
    1 - mean(classifier_knn != test_set$V8)
  })
  
  result_df <- data.frame(K = k_values, Results = results)
  
  ggplot(result_df, aes(x = K, y = Results)) +
    geom_line(color = "gray", size = 1) +
    geom_point(color = "black", size = 2) +
    labs(title = "Accuracy of guesses based on K value",
         x = "Number of Neighbors checked (K)",
         y = "Accuracy") +
    theme_minimal() 
}

#Doing K-fold CV and getting MSE

K_Fold_KNN <- function(num_folds, k_values) {
  set.seed(sample(1:1000000000,1))
  train_control <- trainControl(method = "cv",
                                number = num_folds)
  
  model <- train(V8~.,
                 data = data_seed,
                 tuneGrid = expand.grid(k = k_values),
                 trControl = train_control,
                 method = "knn")
  plot(model, main = "K-Fold-CV")
}

K_Fold_KNN(5, 1:50)
Manual_Split_KNN(0.7, 1:50)

#https://github.com/RainbowSud?tab=repositories