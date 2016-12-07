from poi import POI
import csv
import math
pois=[]

class POIManager(object):
  def __init__(self):
    self.pois = []
    self.odp=[]
  
  def get_all_poi(self):
    with open('pois.txt', 'r') as plik:
      punkty=csv.reader(plik,delimiter=' ')
      for kol in punkty:
        poi=POI(kol[0],kol[1],kol[2:])
        self.pois.append(poi)
    return self.pois
  
  def add_poi(self,POI):
    self.pois.append(POI)
    pass
    
  def get_poi_near(self,x,y,r):
    self.x=x
    self.y=y
    self.r=r
    for a in self.pois:
      if math.sqrt((float(a.x)-float(self.x))**2+(float(a.y)-float(self.y))**2)<float(r):
        self.odp.append(a)
    return self.odp

