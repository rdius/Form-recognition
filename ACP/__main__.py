from pyfaces import pyfaces

import sys,time
import os

if __name__ == "__main__":
    try:
        start = time.time()
        argsnum=len(sys.argv)
        print "args:",argsnum
        if(argsnum<1):
            print "Veuillez revoir la syntaxe d'execution "
            sys.exit(2) 
	path_test = "att_faces/test/"
    	Dataset_test = []
	for i in os.listdir(path_test):
        	Dataset_test.append(os.path.join(path_test, i))
        path_train='att_faces/train/'
        egfaces=int(8)
        thrshld=float(10)
	vrai = 0
	for i in range(len(Dataset_test)):
		pyf=pyfaces.PyFaces(Dataset_test[i],path_train,egfaces,thrshld)
		nom_image_test = Dataset_test[i].split("/")[2]
		
		nom_image_train = pyf.get_image()
		if nom_image_train.split("-")[0] == nom_image_test.split("-")[0]:
			vrai = vrai + 1
		end = time.time()
	print 'Performance :', vrai/2, '%'
	print 'temps de calcul est :',(end-start),'secs'

    except Exception,detail:
        print detail.args
        print " Erreur d'execution "



