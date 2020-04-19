import Compre
class Pages:
    def __init__(self, comp):
        # 链接
        self.comp = comp

        # 每页字典 {页码=>{图片名=>[标签, ], }, }
        self.pages = {}

        # 每加载一页加一
        self.pagesCount = 1

        # 图片原址
        self.pagePicOrg = {}

        # 每页图片数
        self.eachPage = 10

        # 加载页数限制
        self.allPages = 5

        # 每加载多页，数据库前后图片序号
        # self.picPoint=[0,0]

        # 初始化
        # self.loadPages()

        #当前页码
        self.currentPage = 1
    
    def loadPages(self, eachPage = 10, allPages = 5 ):
        # 一次载入多个页面放入内存
        # self.picPoint[0] = self.comp.page

        pageKeys = self.pages.keys()
        while True:
            
            # 列表为空跳出循环
            if not allPages:
                break  
            page = self.comp.readPage(eachPage)
            if not page[0]:
                break
            print("add up : ", self.pagesCount)
                # {页码=>{图片名=>[标签, ], }, }
            self.pages[self.pagesCount] = page[0]
                # 原图地址 图片名 => 原地址
            self.pagePicOrg.update(page[1])
            self.pagesCount += 1
            allPages -= 1
            
        # self.picPoint[1] = self.comp.page
    def loadMore(self, morePage):
        # 加载第morePage页的前2项与后三项
        self.comp.page =(morePage - 2)*self.eachPage
        self.pagesCount = morePage -2
        
        self.loadPages()

    def cleanPages(self):
        self.comp.page = 0
        self.pages = {}
        self.pagesCount = 1
if __name__ == "__main__":
   pass

    