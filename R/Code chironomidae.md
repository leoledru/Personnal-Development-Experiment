# Analyse statistiques multivariées et analyse spatiale de données sous R
## Évaluation de la qualité écologique du lac d'Annecy à l'aide du caractère bioindicateur des Chironomidae

oceane.guillor@etu.univ-smb.fr
# EN EDITION!

# Keywords

* [ACP](##ACP)
* **[RDA](##RDA)**
* **[AnOVa](#anova)** 
* **[indice de Moran](#indice de Moran)** 
* **indice de simpson** 
* **betadiversité** 
* **mise en forme** 
* **graphs**


## Sommaire

* [Sommaire](#Sommaire)
* [Chargement de données spatiales] (#Chargement de données spatiales)
    * 

Liste des fonctions utilisées
[read.delim] (#read.delim)
[head]

# Le code

On commence par définir le répertoire dans lequel on veut travailler
'setwd("~/Recherche/Neo/Feder CEN/Annecy/Annecy/subfossils")'

Appel des packages nécessaires pour le code




## Chargement de données spatiales
### Faire apparaître la batymétrie du lac

Charger le fichier contenant les valeurs de bathy
Arguments: header permet de définir si le document possède une entête (valeur=T pour true ou F), dec permet de définir si la décimale est un point ou une virgule dans le document
'bat<-read.delim("bathyannecy.txt",header=T,dec=",")'
Voir les premières lignes du dataframe créé
'head(bat)'

Transformer le tableau en données spatiales (raster) et les afficher 
'library(sp)
a <- SpatialPixelsDataFrame(points = bat[c("X", "Y")],data=bat)

library(adehabitatMA)
contour <- getcontour(a[,1])'

library(raster)
coordinates(bat) <- ~ X + Y
gridded(bat) <- TRUE
bathy<- raster(bat) '

'Altitude de la surface du lac
surf_alt <- 447
bathy <-  surf_alt-bathy
bathy[bathy <= 0] <- NA

library(RColorBrewer)
colors<-colorRampPalette(brewer.pal(9,"Blues"))(20)

op <- par(mfrow=c(1,1),mar = c(2,2,1,1) + 0.5,mgp = c(1, 0, 0))
plot(bathy,col = colors)
plot(contour,add=T)
scalebar(4000,xy=click(),type='bar',divs=4,cex=.5)

library(prettymapr)
addnortharrow(lwd=1,scale=.5)



# Load sites and wave
caps<-read.delim("caps.txt",header=T,dec=",")
head(caps)


# Convert coordinates from degres to decimal
library(spaa)

Ydec<-matrix(NA,nrow=nrow(caps),ncol=1)
Xdec<-matrix(NA,nrow=nrow(caps),ncol=1)
for (i in 1:nrow(caps)){
  Ydec[i,1]<-deg2dec(caps[i,2],caps[i,3],0)
  Xdec[i,1]<-deg2dec(caps[i,4],caps[i,5],0)
}

pts<-data.frame(Xdec,Ydec)

library(sp)
library(rgdal)
coordinates(pts)<-c("Xdec","Ydec")
class(pts) 
proj4string(pts) <- CRS("+init=epsg:4326") #epsg4326 = WGS84
ptsL <- spTransform(pts, CRS("+init=epsg:27572"))# transformation des points en Lambert II



#Corrections
ptsL@coords[1,1]<-ptsL@coords[1,1]+150
ptsL@coords[2,1]<-ptsL@coords[2,1]-150
ptsL@coords[3,1]<-ptsL@coords[3,1]+150
ptsL@coords[5,1]<-ptsL@coords[5,1]-100;ptsL@coords[5,2]<-ptsL@coords[5,2]+50
ptsL@coords[6,1]<-ptsL@coords[6,1]+50
ptsL@coords[7,1]<-ptsL@coords[7,1]+50
ptsL@coords[8,1]<-ptsL@coords[8,1]+50;ptsL@coords[8,2]<-ptsL@coords[8,2]-1500
ptsL@coords[9,1]<-ptsL@coords[9,1]+50
ptsL@coords[10,2]<-ptsL@coords[10,2]+100
ptsL@coords[11,1]<-ptsL@coords[11,1]-100
ptsL@coords[12,1]<-ptsL@coords[12,1]-100
ptsL@coords[13,1]<-ptsL@coords[13,1]+50
# 14/15 deux prel?vements tr?s proche mais 14 ds cale rocheuse et 15 ds chara
#Controle police
ptsL@coords[14,2]<-ptsL@coords[14,2]+50
ptsL@coords[15,2]<-ptsL@coords[15,2]+50
ptsL@coords[17,2]<-ptsL@coords[17,2]-50
ptsL@coords[18,2]<-ptsL@coords[18,2]-50
ptsL@coords[19,1]<-ptsL@coords[19,1]+1400
ptsL@coords[20,2]<-ptsL@coords[20,2]-1900
ptsL@coords[25,1]<-ptsL@coords[25,1]-50
ptsL@coords[26,2]<-ptsL@coords[26,2]-50
ptsL@coords[27,1]<-ptsL@coords[27,1]-50
ptsL@coords[28,1]<-ptsL@coords[28,1]-50


points(ptsL,pch=19,col="red",cex=.8)
text(ptsL@coords-200,paste("S",seq(from=1,to=nrow(caps),by=1),sep=""),cex=.5)

# Inter-site distance
library(spaa)
dist <- list(matrix(NA, ncol=1, nrow=nrow(caps)-1))
for(i in 1:(nrow(caps)-1))
{
  dist[i]<-geodist(pts@coords[i,1],pts@coords[i,2],pts@coords[i+1,1],pts@coords[i+1,2])
}
dist #Distance des sites entre eux 

hist(unlist(dist[-which.max(dist)]), las=1 ,ylab="Fr?quence",xlab="Distance inter-sites",nclass=10,col="bisque", main = "Distance inter-sites en fonction de la fr?quence") 



# Variables

#wave energy
wave<-read.delim("wave.txt",header=T,dec=",")
head(wave)

plot(wave[,2]~wave[,3], main = "Energie des vagues", col = "darkgreen")
abline(0,1)


op <- par(mfrow=c(1,1),mar = c(2,2,1,1) + 0.5,mgp = c(1, 0, 0))
colors<-colorRampPalette(brewer.pal(9,"Blues"))(20)
plot(bathy,col = colors)
plot(contour,add=T)
scalebar(4000,xy=click(),type='bar',divs=4,cex=.5)# cliquer sur l'endroit ou on veut l'?chelle dans la fig.

library(prettymapr)
addnortharrow(lwd=1,scale=.5)

colors<-colorRampPalette(c("blue","violet","red"))(240)
coul<-seq(from=range(wave[,2]*1000)[1],to=range(wave[,2]*1000)[2],length.out = 240)

cc<-matrix(NA,nrow=1,ncol=28)
for(i in 1:28){
  cc[1,i]<-which.min(abs(coul-wave[i,2]*1000))
}

points(wave[,4:5],pch=19,col=colors[cc],cex=2)
text(ptsL@coords-200,paste("S",seq(from=1,to=nrow(caps),by=1),sep=""),cex=.5)


source("colorbar.R")
color.bar(colorRampPalette(c("blue","violet","red"))(240),-1)



library(splancs)
library(pgirmess)

Rayon<-200
slope<-matrix(NA,ncol=1,nrow=28)
for (i in 1:nrow(ptsL@coords)){
  point<-ptsL@coords[i,]
  circ<-polycirc(Rayon,pts=c(point[1],point[2]),nbr=100);colnames(circ)<-c("x","y")
  bb<-bath[,1:2];colnames(bb)<-c("x","y")
  site<-inout(bb,circ)
  ss<-which(site==TRUE)
  theraster = rasterFromXYZ(bath[ss,]) 
  crs(theraster) = "+init=epsg:27572" 
  slope_asp = terrain(theraster, opt=c('slope', 'aspect'), unit='degrees', neighbors=8)
  slope[i,1]<-slope_asp@data@max[1]
}
slope
plot(theraster) 


op <- par(mfrow=c(1,1),mar = c(2,2,1,1) + 0.5,mgp = c(1, 0, 0))
colors<-colorRampPalette(brewer.pal(9,"Blues"))(20)
plot(bathy,col = colors)
plot(contour,add=T)
scalebar(4000,xy=click(),type='bar',divs=4,cex=.5)# cliquer sur l'endroit ou on veut l'?chelle dans la fig.

library(prettymapr)
addnortharrow(lwd=1,scale=.5)

colors<-colorRampPalette(c("blue","violet","red"))(240)
coul<-seq(from=range(slope)[1],to=range(slope)[2],length.out = 240)

cc<-matrix(NA,nrow=1,ncol=28)
for(i in 1:28){
  cc[1,i]<-which.min(abs(coul-slope[i]))
}

points(ptsL@coords,pch=19,col=colors[cc],cex=2)
text(ptsL@coords-200,paste("S",seq(from=1,to=nrow(caps),by=1),sep=""),cex=.5)



occ_litto<-c(2,1,2,1,2,1,2,1,3,3,2,1,3,2,2,1,2,2,2,3,2,2,2,1,1,2,2,2)

var<-data.frame(caps[,1],slope,wave[,2]*1000,occ_litto,ptsL@coords);colnames(var)<-c("site","slope","wave","occ_litto", "Xdec","Ydec")
var
var<-var[-c(2,4,6,28),]




##########################################
#Load chiro data
chiro<-read.delim("chiro_annecy.txt",header=T,dec=",")
head(chiro)
str(chiro)

rownames(chiro)<-chiro[,1]
chiro
chiro<-chiro[,2:ncol(chiro)]
chiro

totalcount<-rowSums(chiro)
totalcount
sum(totalcount)

chiro2<-chiro[,1:ncol(chiro)-1]
chiro2

#Inspect taxa and site attributes

op <- par(mfrow=c(1,2),mar = c(2,2,1,1) + 0.5,mgp = c(1, 0.2, 0))
barplot(sort(colSums(chiro2),decreasing=T),las=2,cex.axis=.7,col="lightblue",
        ylab="Total counts of chironomid HC",cex.lab=.7,cex.names =.5,tck=-.01)
barplot(sort(log10(colSums(chiro2)),decreasing=T),las=2,cex.axis=.7,
        xpd=F, ylab="Total counts of chironomid HC",cex.lab=.7,cex.names =.5,tck=-.01,col="lightblue")
barplot(sort(rowSums(chiro2),decreasing=T),las=2,cex.axis=.7,
        xpd=F, ylab="Total counts of chironomid HC",cex.lab=.7,cex.names =.5,tck=-.01,col="lightblue")


mean(rowSums(chiro2))
sd(rowSums(chiro2))



#Delete species having less than 5 HC found over all sites
ncol(chiro2)
chiro2<-chiro2[,-c(which(colSums(chiro2)<10))]
ncol(chiro2)

#Delete sites with less than 40 HC 
nrow(chiro2)

deleted_lines<-which(rowSums(chiro2)<40)

chiro2<-chiro2[-c(deleted_lines),]
nrow(chiro2) # reste 24/28 sous esp

sum(colSums(chiro2))


# Transform to %
library(vegan)
chirop<-decostand(chiro2, method = "total", Margin = 1 ) 
rowSums(chirop) #on v?rifie que ?a fait 100% partout



###### Multivariate analysis
library(ade4)
acp <- dudi.pca(chirop)
op <- par(mfrow=c(1,1),mar = c(2,2,1,1),mgp = c(1, 0.3, 0))
scatter(acp)
op <- par(mfrow=c(1,2),mar = c(2,2,1,1),mgp = c(1, 0.3, 0))
s.corcircle(acp$co)
s.label(acp$li)

inertia.dudi(acp)# % variance explained by axes



# Which species are the most influencial on PCA axes
op <- par(mfrow=c(1,2),mar = c(2,4,1,1),mgp = c(1, 0.3, 0))
#Axis1
barplot(sort(scores(acp,display="sp")[,1],decreasing=T),las=2,cex.axis=.7,
        ylab="Species contribution to PCA axis1",cex.lab=.7,cex.names =.5,tck=-.01,,col="lightblue")

#Axis2
barplot(sort(scores(acp,display="sp")[,2],decreasing=T),las=2,cex.axis=.7,
        ylab="Species contribution to PCA axis2",cex.lab=.7,cex.names =.5,tck=-.01,col="lightblue")


# RDA
wave = wave[-c(2, 4, 6, 28),]
slope = slope[-c(2, 4, 6, 28),]
occ_litto=  occ_litto[-c(2, 4, 6, 28)]




mod1 <- rda(chirop ~ var$slope+var$wave+var$occ_litto)#pas le m?me nombre de variable 28 (Var & wave) et 24 (chirop)
anova(mod1)
anova(rda(chirop ~ var$slope+var$wave+var$occ_litto),by="terms",permut=9999)

mod1 <- rda(chirop ~ var$Xdec+var$Ydec)
anova(mod1)
summary(mod1)

anova(rda(chirop ~ var$Xdec+var$Ydec),by="terms",permut=9999)

op <- par(mfrow=c(1,2),mar = c(2,2,1,1),mgp = c(1, 0.3, 0))
plot(mod1, dis=c("sites"))
plot(mod1, dis=c("species","cn"))
plot(mod1)





######################################################
# Assess spatial autocorrelation of taxa

ncol(chirop)

library(pgirmess)

op <- par(mfrow=c(4,4),mar = c(2,2,1,1),mgp = c(.7, 0.1, 0))
for (i in 1:15){
  if(length(which(chirop[,i]>0))<8){
    plot(0,0,main=colnames(chirop)[i])
  }else{
     cor <- correlog(coords=var[,5:6]/1000, z=chirop[,i], method="Moran",nbclass=20)
    plot(cor,main=colnames(chirop)[i],tck=-.015,las=1,cex=.8,cex.lab=.5,ylim=c(-1,1))
  }
   
}



#################
# Diversity metrics

library(iNEXT)
dat<-data.frame(t(chiro2))
dat[1:5,1:10]

DIV<-iNEXT(dat, q=0, datatype="abundance",se=TRUE, conf=0.95, nboot=999)

ggiNEXT(DIV)

# Extract the results
metrics<-data.frame(DIV$AsyEst[,c(1,2,4)])
div<-data.frame(metrics[metrics$Diversity=="Species richness",][,c(1,3)],metrics[metrics$Diversity=="Simpson diversity",][,3])
colnames(div)<-c("site","rich","simpson")
div

# Comparison simpson / richness
op<-par(mfrow=c(1,1),mar=c(2,2,1,1)+0.5,mgp=c(1,0.3,0))
plot(div[,2]~div[,3],xlab="Simpson",ylab="Richness",las=1,cex.axis=.7,pch=19,cex=.7,cex.lab=.7,tck=-.01,ylim=c(5,30))
summary(lm(div[,2]~div[,3]))
abline(lm(div[,2]~div[,3]))



# Richness and divesity analysis
# main variation along X and limited interactions for richness


anova(lm(div[,2]~var$slope+var$wave+var$occ_litto))
anova(lm(div[,2]~var$occ_litto+var$slope+var$wave))

anova(lm(div[,2]~var$occ_litto))
plot(div[,2]~var$occ_litto,xlab="Anthropisation",ylab="Richness",las=1,col="red",cex.axis=.7,pch=19,cex=1,cex.lab=.7,tck=-.01,ylim=c(5,30))
summary(lm(div[,2]~var$occ_litto))
abline(lm(div[,2]~var$occ_litto),lwd=2,col="red")


anova(lm(div[,2]~var$slope))
anova(lm(div[,2]~var$Xdec+var$Ydec))

summary(lm(div[,2]~var$occ_litto))

anova(lm(div[,3]~var$slope+var$wave+var$occ_litto))
anova(lm(div[,3]~var$Xdec+var$Ydec))

summary(lm(div[,3]~var$Xdec+var$Ydec))



# Plotting results on map
#Map diversity index

pts2<-data.frame(var$Xdec,var$Ydec);colnames(pts2)<-c("Xdec","Ydec")

library(sp)
coordinates(pts2)<-c("Xdec","Ydec")
class(pts2) 
proj4string(pts2) <- CRS("+init=epsg:27572") #epsg4326 = WGS84
ptsL <- spTransform(pts, CRS("+init=epsg:27572"))# transformation des points en Lambert II


op <- par(mfrow=c(1,2),mar = c(2,2,1,1) + 0.5,mgp = c(1, 0, 0))
colors<-colorRampPalette(brewer.pal(9,"Blues"))(20)
plot(bathy,col = colors)
plot(contour,add=T)
scalebar(2000,xy=c(896000,2098000),type='bar',divs=4,cex=.5)# cliquer sur l'endroit ou on veut l'?chelle dans la fig.
addnortharrow(lwd=1,scale=.5)

points(pts2,pch=19,col="red",cex=div[,2]/10)
legend("bottomleft",c("30","20","10","5"),pt.cex=c(30/10,20/10,10/10,5/10),pch=19,col="red")

plot(bathy,col = colors)
plot(contour,add=T)
scalebar(2000,xy=c(896000,2098000),type='bar',divs=4,cex=.5)# cliquer sur l'endroit ou on veut l'?chelle dans la fig.
addnortharrow(lwd=1,scale=.5)

points(ptsL,pch=19,col="green",cex=(div[,3]/5))
legend("bottomleft",c("11","8","5","2"),pt.cex=c(11/5,8/5,5/5,2/5),pch=19,col="green")







#####################################

########## Betadiv

# Legendre and De Caceres (2013, ELE)
# Copy paste the function because the loading using "source" do not work
source("betadiv.R")
library(vegan)

beta<-beta.div(chirop, method="none", sqrt.D=FALSE, 
               samp=FALSE, nperm=999, save.D=FALSE, clock=TRUE)

str(beta)

SCBD  <- sort(beta$SCBD, decreasing=TRUE) 
barplot(SCBD,las=2,cex.axis=.7,
        ylab="SCBD",cex.lab=.7,cex.names =.5,tck=-.01,col="purple")


# Assess the relationhsip between SCBD and the species abundance
#chiro2 or chiroh
plot(beta$SCBD~colMeans(chirop),pch=19,las=1,tck=-.01,col="purple",ylim=c(0,0.25))


# Assess significance
mod<-lm(beta$SCBD~colMeans(chirop))
anova(mod)
summary(mod)
abline(mod,lwd=2,col="purple")
text(beta$SCBD~colMeans(chirop),labels=names(colMeans(chirop)))

op <- par(mfrow=c(1,3),mar = c(2,2,1,1) + 0.5,mgp = c(1, 0, 0))
plot(chirop$Chironomus~beta$LCBD,xlim=c(0,0.2),ylim=c(-0.01,0.5),las=1,pch=19)
anova(lm(chirop$Chironomus~beta$LCBD))
abline(lm(chirop$Chironomus~beta$LCBD))
plot(chirop$Procladius~beta$LCBD,xlim=c(0,0.2),ylim=c(-0.01,0.5),las=1,pch=19)
anova(lm(chirop$Procladius~beta$LCBD))
abline(lm(chirop$Procladius~beta$LCBD))
plot(chirop$Psectrocladius~beta$LCBD,xlim=c(0,0.2),ylim=c(-0.01,0.5),las=1,pch=19)
anova(lm(chirop$Psectrocladius~beta$LCBD))
abline(lm(chirop$Psectrocladius~beta$LCBD))

op <- par(mfrow=c(1,1),mar = c(2,2,1,1) + 0.5,mgp = c(1, 0, 0))
barplot(sort(beta$LCBD,decreasing=T),las=2,cex.axis=1,
        ylab="SCBD",cex.lab=.7,cex.names =1,tck=-.01,col="purple")


op <- par(mfrow=c(1,2),mar = c(2,2,1,1) + 0.5,mgp = c(1, 0, 0))
colors<-colorRampPalette(brewer.pal(9,"Blues"))(20)
plot(bathy,col = colors)
plot(contour,add=T)
scalebar(2000,xy=c(896000,2098000),type='bar',divs=4,cex=.5)# cliquer sur l'endroit ou on veut l'?chelle dans la fig.
addnortharrow(lwd=1,scale=.5)

points(ptsL,pch=19,col="purple",cex=beta$LCBD*25)
legend("bottomleft",c("0.15","0.10","0.05","0.01"),pt.cex=c(0.15*25,0.10*25,0.05*25,0.01*25),pch=19,col="purple",cex=.5)



anova(lm(beta$LCBD~var$slope+var$wave+var$occ_litto))
anova(lm(beta$LCBD~var$Xdec+var$Ydec))




########
hist(as.matrix(chirop))

colors<-colorRampPalette(brewer.pal(9,"Blues"))(20)

op <- par(mfrow=c(5,3),mar = c(2,2,1,1) + 0.5,mgp = c(1, 0, 0))
for (i in 1:ncol(chirop)){
  plot(bathy,col = colors,main=names(chirop)[i])
  plot(contour,add=T)
  scalebar(2000,xy=c(896000,2098000),type='bar',divs=4,cex=.1)
  addnortharrow(lwd=1,scale=.5)
  
  points(ptsL,pch=19,col="orange",cex=chirop[,i]*2)
  legend("bottomleft",c("0.5","0.3","0.2","0.1","0.05"),pt.cex=c(0.5*2,0.3*2,0.2*2,0.1*2,0.05*2),pch=19,col="orange",cex=.5)
}



op <- par(mfrow=c(2,5),mar = c(2,2,1,1) + 0.5,mgp = c(1, 0, 0))
for (i in c(8,6,10,3,11,5,7,1,9,17)){
  plot(bathy,col = colors,main=names(chirop)[i])
  plot(contour,add=T)
  scalebar(2000,xy=c(896000,2098000),type='bar',divs=4,cex=.5)
  addnortharrow(lwd=1,scale=.2)
  
  points(ptsL,pch=19,col="orange",cex=chirop[,i]*10)
  legend("bottomleft",c("0.5","0.3","0.2","0.1","0.05"),pt.cex=c(0.5*10,0.3*10,0.2*10,0.1*10,0.05*10),pch=19,col="orange")
}

'



