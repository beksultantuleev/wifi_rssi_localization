heads <-  c("mac", "chanel", "rssi", "ssid", "grid")
data <- wifif

 
colnames(data) <- heads
summary(data)
data$grid = as.factor(data$grid)
summary(data$grid)
data$chanel = NULL


library(tidyr)
wide_data <- spread(data=data, mac, rssi)
View(wide_data)
