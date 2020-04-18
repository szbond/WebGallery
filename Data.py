import sqlite3
import os
class PicData:
    def __init__(self, dataPath):
        
        # 连接对象
        self.dataPath = dataPath
        self.connect = sqlite3.connect(dataPath, check_same_thread=False)
        # 游标对象
        self.cursor = self.connect.cursor()
        self.tableNames = []
        self.createTb()
        # 相对提交标志 默认提交行为
        self.comitFlag = True
        # 绝对提交标志 可以绝对阻止提交行为
        self.comitAbsu = True
        
        
        
        
        # print('create app ', self.name)
    
    def createTb(self):
        # 初始化表
        tables = self.cursor.execute("SELECT name from sqlite_master where type='table' ")
        for row in tables:
            self.tableNames.append( row[0])

        if 'TAG' not in self.tableNames:
            self.cursor.execute(
            '''CREATE TABLE TAG 
            (TAGID INTEGER PRIMARY KEY AUTOINCREMENT,
            TAGNAME TEXT UNIQUE NOT NULL);
            ''')
        if 'PIC' not in self.tableNames:
            self.cursor.execute(
            '''CREATE TABLE PIC
            (PICID INTEGER PRIMARY KEY AUTOINCREMENT,
            PICNAME TEXT UNIQUE NOT NULL,
            PICORG TEXT UNIQUE NOT NULL,
            PICPRE TEXT UNIQUE NOT NULL);
            ''')
        if 'REL' not in self.tableNames:
            self.cursor.execute(
            '''CREATE TABLE REL 
            (RELID INTEGER PRIMARY KEY AUTOINCREMENT,
            PICID INTEGER NOT NULL,
            TAGID INTEGER NOT NULL);
            ''')
    
    def exec(self, sql, values=()):
        # 数据库提交命令
        result = []
        try:
            result = self.cursor.execute(sql,values).fetchall()
        except Exception as e:
            print(e)
        if self.comitAbsu and self.comitFlag :
            self.connect.commit()
        return result
    def execSearch(self, sql, values=()):
        result = []
        try:
            result = self.cursor.execute(sql,values).fetchall()
        except Exception as e:
            print(e)
        return result

    def insertPic(self,picOrg, picPre):
        # 插入图片
        res = self.getPicId(picOrg)
        picName = os.path.basename(picOrg)
        if res:
            return res[0][0]
        else:
            sql = "INSERT into PIC(PICNAME, PICORG, PICPRE) VALUES(?, ?, ?)"
            self.exec(sql, (picName, picOrg, picPre))
            return self.cursor.lastrowid
    
    def insertTag(self, tagName):
        # 插入标签
        res = self.getTagId(tagName)
        if res:
            return res[0][0]
        else:
            sql = "INSERT into TAG(TAGNAME) VALUES(?)"
            self.exec(sql, (tagName,))
            return self.cursor.lastrowid
    
    def insertRel(self, picId, tagId):
        # 插入关系
        res = self.relExi(picId, tagId)
        if res:
            return res[0][0]
        else:
            sql = "INSERT into REL(PICID, TAGID) VALUES(?,?)"  
            self.exec(sql, (picId,tagId))
            return self.cursor.lastrowid

    '''
    def updatePic(self, picOrg, picPre, picId):
        # 更改图片
        sql = "UPDATE PIC SET PICORG=?, PICPRE=? where PICID=? "
        self.exec(sql,(picOrg, picPre, picId))

    def updateRel(self, picId, tagId, relId):
        # 更改关联
        sql = "UPDATE REL SET PICID=?, TAGID=? where RELID=? "
        self.exec(sql,(picId, tagId, relId))

    def updateTag(self, tagName, tagId):
        # 更改标签
        sql = "UPDATE TAG SET TAGNAME=? where TAGID=? "
        self.exec(sql,(tagName, tagId))
    '''

    def delPic(self, picOrg):
        # 删除图片及其关系
        self.comitFlag = False
        picId = self.getPicId(picOrg)
        tags = self.findTag(picOrg)

        
        sql = "DELETE from PIC where PICORG=?"
        self.exec(sql,(picOrg,))
        
        self.delRel("PIC", picId)
        TagIds = PicData.optim(self.exec("SELECT DISTINCT TAGID from REL"))
        delTagIds = []
        for tag in tags:
            tagId = self.getTagId(tag)
            if tagId not in TagIds:
                delTagIds.append(tag)
        delLen = len(delTagIds)

        for i in range(delLen):
            if i == delLen-1:
                self.comitFlag = True
       
            self.delTag(delTagIds[i],False)

    def delTag(self, tagName, opt = True):
        # 删除标签及其关系
        self.comitFlag = False
        tagId = self.getTagId(tagName)
        sql = "DELETE from TAG where TAGNAME=?"
        self.exec(sql,(tagName,))
        self.comitFlag = True
        if opt:  
            self.delRel("TAG", tagId)
    
    def delRel(self, tbName, target):
        sql = "DELETE from REL where " + tbName.upper() + "ID=? "
        self.exec(sql,(target,))
       
    def findOrg(self, picName):
        
        sql = "SELECT PICORG from PIC where PICNAME=?"
       
        return PicData.optim(self.execSearch(sql,(picName,)))
       


    def findTags(self, picName):
        sql = "SELECT TAGNAME FROM PIC JOIN REL JOIN TAG ON PIC.PICID=REL.PICID AND TAG.TAGID=REL.TAGID WHERE PIC.PICNAME=? "
        return PicData.optim (self.execSearch(sql,(picName,))) 
        
        

    def findPic(self, tagName):
     
        sql = "SELECT PIC.PICORG FROM PIC JOIN REL JOIN TAG ON PIC.PICID=REL.PICID AND TAG.TAGID=REL.TAGID WHERE TAG.TAGNAME=? "
        return PicData.optim( self.execSearch(sql,(tagName,)))
      
         

    @staticmethod
    def optim(result):
        res = []
        for row in result:
            res.append(row[0])
        return res

    def printTb(self, tbName):
        # 打印表
        if tbName.upper() in self.tableNames or tbName in self.tableNames:
            sql = "SELECT * from " + tbName
            table = self.execSearch(sql)
            print(table)
        else:
            print("table is not in database")

    def relExi(self, picId, tagId):
        # 联系表是否重复
        sql = "SELECT RELID from REL where TAGID=? AND PICID=? " 
        res = self.execSearch(sql,(tagId,picId))
        return res
    
    def getPicId(self, picOrg):
        picId = self.execSearch("SELECT PICID from PIC where PICORG=?",(picOrg,))
        return picId
    
    def getTagId(self, tagName):
        tagId = self.execSearch("SELECT TAGID from TAG where TAGNAME=?",(tagName,))
        return tagId
    def getPic(self, limit, offset):
        sql = "SELECT PICNAME  from PIC ORDER BY PICID LIMIT ? offset ?"
        return PicData.optim(self.execSearch(sql,(limit,offset)))
    '''
    def getTags(self, picId):
        sql = "SELECT TAGNAME  from TAG JOIN REL ON REL.TAGID=TAG.TAGID WHERE PICID = ?"
        return PicData.optim(self.execSearch(sql,(picId,)))
    '''
    def getAll(self, tbName):
        if tbName.upper() in self.tableNames or tbName in self.tableNames:
            sql = "SELECT * from " + tbName
            return self.execSearch(sql)
        else:
            return None
        
    def clearData(self):
        self.comitFlag = False
        self.exec("DELETE from PIC")
        self.exec("DELETE from TAG")
        self.exec("DELETE from REL")
        self.comitFlag = True
        self.exec("DELETE from sqlite_sequence")          

    def __del__(self):
        self.connect.close()
        
if __name__ == "__main__":
    app = PicData("C:/Users/szbon/Desktop/python/gallery/data/gallery.db")

    print(app.getPic(100, 0))
    
    
  





    












