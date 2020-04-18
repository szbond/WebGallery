from PIL import Image
import os
fileDir = os.path.dirname(os.path.abspath(__file__))
class Picture:
    def __init__(self):
        self.orgin = ""
        self.name = ""
        self.prev = ""
        self.tags = []
        self.image = Image.new("RGB",(200, 200))

    def thumPic(self):
        if os.path.exists(self.orgin):
            w, h = self.image.size
            new_w = w
            new_h = h
            if (w >= 256):
                rot = 256 / w
                new_h = h * rot
                new_w = w * rot
            self.image.thumbnail((new_w,new_h))
            self.image.save(self.prev, "jpeg")
        else:
            print("file not exists")

    def changeCont(self, orgPath ,thumb = True, thumbPath = fileDir):
        self.orgin = os.path.normpath(orgPath)
        self.name = os.path.basename(orgPath)
        self.prev = os.path.join(thumbPath,self.name)
        self.image = Image.open(self.orgin)
        if self.image.mode == "P":
            self.image = self.image.convert("RGB")
        if thumb:
            self.thumPic()


    def updateData(self,database):
        if os.path.exists(self.orgin):
            picId = database.insertPic(self.orgin, self.prev)
            for tag in self.tags:
                tagId = database.insertTag(tag)
                database.insertRel(picId, tagId)
if __name__ == "__main__":

    pic = Picture()
    pic.changeCont("C:/Users/szbon/Desktop/python/gallery/image/org/test.jpg", thumbPath="C:/Users/szbon/Desktop/python/gallery/image/pre")
