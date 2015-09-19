__author__ = 'yuri'
import os
import sys
from PIL import Image

config = {
    'big': (2000, 0),
    'middle': (1200, 0),
    'small': (600, 0)
}


class ImageResize(object):
    def __init__(self, folder=None):
        self.main_dir = folder or os.getcwd()
        self.walk_throw()

    def walk_throw(self, recursive=False):
        """
        :rtype : object
        """
        if recursive:
            os.path.walk(self.main_dir, _file_handler, [])
        else:
            _file_handler('',self.main_dir,os.listdir(self.main_dir))


def _file_handler(arg, dir, f_names):
    for file in f_names:
        print file
        if file.endswith('.jpg') or file.endswith('.JPG') and not file.startswith('.'):
            try:
                im = Image.open(os.path.join(dir, file))
                for image_size_name, image_size in config.iteritems():
                    if not os.path.isdir(os.path.join(dir, image_size_name)):
                        os.makedirs(os.path.join(dir, image_size_name))
                    print "resizing image...{}".format(file)
                    print im.size
                    r_width, r_height = im.size
                    print r_width,r_height
                    print "ratio {} , new width {}, new height {}".format(
                        float(r_height) / float(r_width),
                        image_size[0],
                        float(r_height) / float(r_width)  * image_size[0]
                    )
                    im_re = im.resize((image_size[0], int(float(r_height) / float(r_width) * image_size[0])), Image.ANTIALIAS)
                    im_re.save(os.path.join(dir, image_size_name, file))
            except:
                print "file not worked"
                pass



if __name__ == "__main__":
    ImageResize(sys.argv[1])
