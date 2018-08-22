import  sys
from string import split
from os.path import basename
import eigenfaces
class PyFaces:
    def __init__(self,testimg,imgsdir,egfnum,thrsh):
        self.testimg=testimg
        self.imgsdir=imgsdir
        self.threshold=thrsh
        self.egfnum=egfnum 
	self.matchfile=''    
        parts = split(basename(testimg),'.')
        extn=parts[len(parts) - 1]
        print "mise en correspondance:",self.testimg," avec toutes les ",extn," images d'apprentissage:",imgsdir        
        self.facet= eigenfaces.FaceRec()
        self.egfnum=self.set_selected_eigenfaces_count(self.egfnum,extn)
        #print "nombre de Eingenfaces:",self.egfnum
        self.facet.checkCache(self.imgsdir,extn,self.imgnamelist,self.egfnum,self.threshold)
        mindist,matchfile=self.facet.findmatchingimage(self.testimg,self.egfnum,self.threshold)
        if mindist < 1e-10:
            mindist=0
        if not matchfile:
            print "NOMATCH! try higher threshold"
        else:
            print "Reconnaissance :"+matchfile+" dist :"+str(mindist)
            
    def set_selected_eigenfaces_count(self,selected_eigenfaces_count,ext):        
        #call eigenfaces.parsefolder() and get imagenamelist        
        self.imgnamelist=self.facet.parsefolder(self.imgsdir,ext)                    
        numimgs=len(self.imgnamelist)        
        if(selected_eigenfaces_count >= numimgs  or selected_eigenfaces_count == 0):
            selected_eigenfaces_count=numimgs/2    
        return selected_eigenfaces_count
        
    def get_image(self):
	mindist,matchfile=self.facet.findmatchingimage(self.testimg,self.egfnum,self.threshold)
	nom_image = matchfile.split("/")[2]
	return nom_image
        
