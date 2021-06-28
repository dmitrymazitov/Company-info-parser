from view import View
from model import Model 

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.main()

    def onButtonClick(self, caption):
        if caption == 'Search':
            self.view.cleanFrame()
            pullValue = self.view.getEntryValue()
            result = self.model.action(pullValue)
            val = self.model.treatResult(result)
            self.view.makeLabel(val)
        else:
            self.view.cleanEntry()
        
if __name__ == "__main__":
    controller = Controller()
    controller.main()
