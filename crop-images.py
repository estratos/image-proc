# Estratos Electronics SAS de CV
#
#  Crop images script to create a 512 x 512 pix image from capture directories
#
#

from PIL import Image
import os.path, sys
path = "/home/nvidia/work/Model-Train-Data/reflectorModel/"



imageW=512
imageH=512
coordX=384
coordY=104

def renameFiles(path, basefilename, depth=1):
    # Once we hit depth, just return (base case)
    if depth < 0: return
	
    # Make sure that a path was supplied and it is not a symbolic link
    if os.path.isdir(path) and not os.path.islink(path):
        ind = 1

        # Loop through each file in the start directory and create a fullpath
        for file in os.listdir(path):
            fullpath = path + os.path.sep + file

            # Again we don't want to follow symbolic links
            if not os.path.islink(fullpath):

                # If it is a directory, recursively call this function 
                # giving that path and reducing the depth.
                if os.path.isdir(fullpath):
                    renameFiles(fullpath, basefilename, depth - 1)
                else:
                    # Find the extension (if available) and rebuild file name 
                    # using the directory, new base filename, index and the old extension.
                    extension = os.path.splitext(fullpath)[1]
                    os.rename(fullpath, os.path.dirname(fullpath) + os.path.sep + basefilename + "_" + str(ind) + extension)
                    ind += 1
    return

def cropDir(inpath,outpath):
    dirs = os.listdir(inpath)
    for item in dirs:
        fullpath = os.path.join(inpath,item)
        if os.path.isfile(fullpath):
            im = Image.open(fullpath)
            f, e = os.path.splitext(fullpath)
            imCrop = im.crop((coordX,coordY,coordX+imageW,coordY+imageH))
            print (os.path.basename(fullpath))
            file = os.path.basename(fullpath)
            imCrop.save(outpath+file , quality=100)


    return
def createDir():
	try:
    		os.mkdir(path)
	except OSError:
    		print ("Creation of the directory %s failed" % path)
	else:
    		print ("Successfully created the directory %s " % path)

currentpath = os.getcwd()
print ("The current working directory is %s" % currentpath)
cropDir(path+"train/def-01/","outdir/train/def-01/")
cropDir(path+"train/def-02/","outdir/train/def-02/")
cropDir(path+"train/def-03/","outdir/train/def-03/")
cropDir(path+"test/def-01/","outdir/test/def-01/")
cropDir(path+"test/def-02/","outdir/test/def-02/")
cropDir(path+"test/def-03/","outdir/test/def-03/")
cropDir(path+"val/def-01/","outdir/val/def-01/")
cropDir(path+"val/def-02/","outdir/val/def-02/")
cropDir(path+"val/def-03/","outdir/val/def-03/")
cropDir(path+"train/good/","outdir/train/good/")
cropDir(path+"val/good/","outdir/val/good/")
cropDir(path+"test/good/","outdir/test/good/")

