from poi import POI
import csv
pois=[]

class POIManager(object):
  def __init__(self):
    self.pois = []
  
  def get_all_poi(self):
    with open('pois.txt', 'r') as plik:
      punkty=csv.reader(plik,delimiter=' ')
      for kol in punkty:
        poi=POI(kol[0],kol[1],kol[2:])
        self.pois.append(poi)
    return self.pois
  
  def add_poi(self,poi):
    pass
    
  def get_poi_near(self,x,y,r):
    pass
