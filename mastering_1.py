import os
from PIL import Image
import glob

where = input("where: ")
# curs = r'C:\Users\User\Desktop\python\master\original'
extension = r'\Python_master'
dst_dir = where + extension
os.makedirs(dst_dir, exist_ok=True)
stars = r'\*'
globus = where + stars

files = glob.glob(globus)

for f in files:
    if f.endswith((".jpg", ".jpeg", ".JPG")):
        roots, ext = os.path.splitext(f)
        basename = os.path.basename(roots)
        img = Image.open(f)
        img_resize = img.resize((500, 790), Image.BICUBIC)
        img_resize.save(os.path.join(dst_dir, basename + '_master' + ext), quality=95)


