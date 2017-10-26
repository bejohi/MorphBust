import os
import imghdr 

def import_image(imagepath)
    if os.path.isfile(imagepath) = False
        print("File "+ imagepath + " does not exist. Terminating.")
        sys.exit(1)
    if not imghdr.what(imagepath) in ("'png'", "'jpeg'")
        print("File "+ imagepath + "is not a valid image file. Terminating.")
        sys.exit(1)
     
    
