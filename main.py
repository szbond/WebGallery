
import Compre
import os
if __name__ == "__main__":
    comp = Compre.Compre()
    comp.addDir("D:/参考/MALE MODEL/total/2020011811")
    '''
    comp.database.clearData()
    comp.updateData(True, True)
    '''
    
    # print(comp.dirList)
    # print(comp.walkList)
    # print(comp.picData)
    print(comp.readPage(10))
    # comp.cleanThumb("C:/Users/szbon/Desktop/python/gallery/image/pre")
    
    