#select only first floor
first_floor <- dataset[dataset$Zonename == "1st Floor East Corridor",]

#replace str null to NA
first_floor <- data.frame(lapply(first_floor, function(x) {gsub("null", 0, x)}))

#remove NA columns
#first_floor <- first_floor[,colSums(is.na(first_floor))<nrow(first_floor)]

library(dplyr)
#select specific columns from initial dataset
final_df <- first_floor %>% select(15:45, 3, 4) 

library( taRifx )
final_df <- japply( final_df, which(sapply(final_df, class)=="character"), as.numeric )

final_df$grid <- paste(final_df$Position.X, final_df$Position.Y, sep = "-")
View(final_df)
final_df$grid <- as.factor(final_df$grid)

final_df <- final_df %>% select(1:31, length(final_df)) 

library(rpart)
decision_tree_model <- rpart(grid~., data = final_df)
decision_tree_model
prediction_decision_train <-predict(decision_tree_model, final_df, type = 'class') 
mean(prediction_decision_train==final_df$grid)
library(rpart.plot)
prp(decision_tree_model)
# summary(final_df)
# library(ggfortify)
# k_means_clust <- kmeans(final_df[-(22:24)], 10, nstart = 25)
# autoplot(k_means_clust, final_df, frame=T)
