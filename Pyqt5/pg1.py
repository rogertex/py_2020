import pyqtgraph as pg
import pandas as pd
import sys

import pyqtgraph as pg
import pandas as pd
import sys


# 读取数据
df = pd.read_csv("D:\VS\Pyqt5\000001.csv",encoding='gb2312').sort_values("日期")
data = df['收盘价'].tolist()

pg.plot(data,title="A股收盘价历史走势|州的先生zmister.com")
if __name__ == '__main__':
    pg.QtGui.QApplication.exec_()