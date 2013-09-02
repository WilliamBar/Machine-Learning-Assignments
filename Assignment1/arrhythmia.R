library("foreign")
library("randomForest")

arr <- read.arff("arrhythmia.arff")

prox <- rfImpute(arr[-280],arr$class)

rough <- na.roughfix(arr)

roughRF <- randomForest( x=rough[-280],y=rough$class, ntree=1000, importance=TRUE)

proximityRF <-  randomForest( x=prox,y=rough$class, ntree=1000, importance=TRUE)

varImpPlot(roughRF)

plot(roughRF)

plot(proximityRF)

varImpPlot(proximityRF)
