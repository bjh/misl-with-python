import eyeD3
from eyeD3 import TagException

class Tags(object):
    def update_image(self, cover, directory, name):
        #print "updating: %s" % name
        mp3 = directory + '/' + name
        image = directory + '/' + cover
        
        # print "%s %s" % (mp3, image)
        
        tag = eyeD3.Tag()
        tag.link(mp3)
        
        images = tag.getImages()

        if len(images) == 0:
            try:
                tag.addImage(0x03, image)
                tag.update(eyeD3.ID3_V2_3)
                images = tag.getImages()
            except TagException, e:
                print e

