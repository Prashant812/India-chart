# Install all necessary packages and load the libraries into R
library(ggplot2)
library(RColorBrewer)
library(ggmap)
library(maps)
library(rgdal)
library(scales)
library(maptools)
library(gridExtra)
library(rgeos)
library(sp)

# Set working directory
states_shape <- readOGR(dsn = file.path('C:/Users/acer/Desktop/MA605/Project/Indian map', 'polbnda_ind.shp'), stringsAsFactors = F)
class(states_shape)
names(states_shape)
#print(states_shape$ID_1)
print(states_shape$nam)
plot(states_shape, main = "Administrative Map of India")