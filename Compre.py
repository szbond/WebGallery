
import os
import Data
import Pic

fileDir = os.path.dirname(os.path.abspath(__file__))
class Compre:
    def __init__(self):
        
        self.database = Data.PicData(os.path.join(fileDir, "data", "gallery.db"))
        # 文件目录列表
        self.dirList = []
        # 缓存
        self.picData = []
        # 读取位置
        self.page = 0
        # 三元组
        self.walkList = []

        self.thumbPath = os.path.join(os.path.dirname(__file__),"static/images/thumb")
    def addDir(self, picPath):
        picPath = os.path.normpath(picPath)
        # 添加图片目录
        if os.path.exists(picPath) and not self.dirExi(picPath):
            self.dirList.append(picPath)
            self.walkList.append(os.walk(picPath))
        else:
            print("path not exists or already addup: ",picPath)

    def dirExi(self, picPath):
        for index, path in enumerate(self.dirList):
            # 路径为列表路径的子路径
            if path in picPath:
                # 判读目标路径是否为对象目录的子路径
                return True
            if picPath in path:
                # 判断对象路径是否是目标路径子目录
                # 是，则删除对象路径， 添加遍历结果
                self.dirList.remove(path)
                self.walkList[index] = (os.walk(picPath))
                return False
 
    def updateData(self, addup=False, clearup=False):
        
        if addup:
            self.addPicData()
        
        # 提交缓存数据
        relList = []
        if not self.picData:
            return
        
        for pic in self.picData:
            if len(pic[0]) != 2:
                continue
            picId = self.database.insertPic(pic[0][0], pic[0][1])
            if len(pic) < 2:
                continue
            for tag in pic[1]:
                tagId = self.database.insertTag(tag)
                relList.append((picId, tagId))
        for rel in relList:
            self.database.insertRel(rel[0], rel[1])
        # 清空缓存
        if clearup:
            self.picData = []

    def addPicData(self):
        pic = Pic.Picture()
        for walkPath in self.walkList:
            for root, dirs, files in walkPath:
                for name in files:
                    pic.changeCont(os.path.join(root, name),thumbPath=self.thumbPath)             
                    self.picData.append([(pic.orgin, pic.prev), pic.tags])
        del pic

    def readPage(self, limit=10, cleanPage = False):
        if cleanPage:
            self.page = 0
        
        pics = self.database.getPic(limit, self.page)
        self.page += limit
        picsDit = {}
        picsOrg = {}
        for pic in pics:
            picsOrg[pic[0]] = pic[1]
            picsDit[pic[0]] = self.database.findTags(pic[0])
        return (picsDit, picsOrg)
    def subTags(self, pic, tags):
        if (not pic) or (not tags):
            return None
        relList = []
        picId = self.database.getPicId(pic, True)[0][0]
        
        for tag in tags:
            
            tagId = self.database.insertTag(tag)
       
            relList.append((picId, tagId))
        for rel in relList:
            self.database.insertRel(rel[0], rel[1])
            # self.database.insertRel(rel[0], rel[1])
    def cleanThumb(self):

        if not os.path.exists(self.thumbPath):
            return
        thumbPic = os.listdir(self.thumbPath)
        for pic in thumbPic:
            if not self.database.findOrg(pic):    
                os.remove(os.path.join(self.thumbPath, pic))
        orgs = self.database.getAll("pic")

        for org in orgs:
            if org[1] not in thumbPic:
                pic = Pic.Picture()
                pic.changeCont(org[2], thumbPath=self.thumbPath)

if __name__ == "__main__":  
    comp = Compre()
    print(comp.readPage())