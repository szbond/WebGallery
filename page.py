import Compre
class Pages:
    def __init__(self, comp):
        self.comp = comp
        self.pages = []
        self.allTags = []
    def loadPages(self, eachPage = 10, allPages = 100 ):
        while True:
            
            page = self.comp.readPage(eachPage)
            if(not allPages) or (not page) :
                break 
            self.pages.append(page)
            allPages -= 1
            

    def cleanPages(self):
        self.comp.page = 0
        self.pages = []
if __name__ == "__main__":
    comp = Compre.Compre()
    pages = Pages(comp)

    # pages.loadPages(2)
    # print(pages.pages)
    # pages.cleanPages()
    # print(pages.pages)
    pages.loadPages(3,5)
    print(pages.pages)


    