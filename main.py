from Application.BaseApplication import BaseApplication
from Libraries import matrixGui

if __name__ == '__main__':
    omatrix = matrixGui.NeoMatrixGui(15, 30, pixels)

    app = BaseApplication(omatrix)
    app.run()
