# -*- coding: utf-8 -*-

'''
    该文件为项目主程序:
    运行该程序即可打开项目可视化界面，支持单条和批量导入新闻10类别预测
'''

import paddlehub as hub
import interface
import sys
import xlrd
import csv
import re
import pandas as pd
import numpy as np
from functools import partial
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from time import time

# 定义单条新闻文本分类函数
def Single_classification(ui):
    title = ui.lineEdit.text()  # 获取输入的新闻标题
    content = ui.textEdit.toPlainText()  # 获取输入的新闻内容

    # 新闻正文内容不能为空
    if title == '' or content == '' :
        ui.label_4.setText('无')
        ui.warn1()   # 提示补全新闻内容
    else:
        # 将新闻标题和正文直接拼接
        news = title + content
        # 去除换行符和多余空格等进行简单清洗
        process = lambda x: x.strip().replace('\n', '').replace('\r', '').replace(" ","").replace(u'\xa0', u'').replace(u'\u3000',u'').replace(u'\t',u'')
        news = process(news)

        # 格式处理
        # 创建空列表
        data = []
        list = []
        # 使用 append() 添加元素
        list.append(news)
        data.append(list)

        # 单条预测时间度量
        t1 = time()
        # 进行单条新闻文本分类预测，注意默认为CPU环境。 若已配置GPU，可设置use_gpu=True
        label = model.predict(data, max_seq_len=256, batch_size=1, use_gpu=False)
        t2 = time()
        print('单条文本分类CPU预测耗时（毫秒）：%.3f' % ((t2 - t1) * 1000.0))
        # 显示新闻分类预测结果
        ui.label_4.setText(label[0])
        # 弹窗提示分类完成
        ui.success1()
        
# 定义批量新闻文本分类函数
def Batch_classification(ui):
    excel_path = ui.lineEdit_2.text()   # 获取输入文件路径
    output_path = ui.lineEdit_3.text()  # 获取输出文件路径
    if excel_path == '':
        ui.warn2()  # 提示未选择要导入的excel新闻文件
    elif output_path == '':
        ui.warn3()  # 提示未选择分类结果文件输出路径
    else:
        # pandas读取新闻excel文件
        df = pd.read_excel(excel_path)
        # 对数据进行清洗以及将标题和内容进行拼接

        news = pd.DataFrame(columns=['news'])
        # 拼接新闻标题title和正文内容content列
        news['news'] = df["title"] + df["content"]

        # 去除换行符和多余空格等
        process1 = lambda x: x.strip().replace('\n', '').replace('\r', '').replace(" ","").replace(u'\xa0', u'').replace(u'\u3000',u'').replace(u'\t',u'')
        # 去除噪声数据
        process2 = lambda x: re.sub(u"\\(.*?\\)|\\{.*?}", "", x)
        news['news'] = news['news'].apply(process1)
        news['news'] = news['news'].apply(process2)

        # 首先将pandas读取的数据转化为array
        data_array = np.array(news)
        # 然后转化为list形式
        data_list =data_array.tolist()
        
        # 进行批量分类预测
        # 注意默认为cpu环境，若已配置GPU可设置use_gpu=True。对于批量分类，batch_size也可适当增大进行提速
        results = model.predict(data_list, max_seq_len=256, batch_size=1, use_gpu=False)

        # 将结果填充到新闻类别channelName列上
        df['channelName'] = results

        # 保存结果文件为xlsx文件
        df.to_excel(output_path, sheet_name='类别', index=False, header=True)
        ui.showresult()   # 预览显示预测完成后的excel结果文件
        # 提示批量分类完成
        ui.success2()

if __name__ == '__main__':

    # 定义要进行分类的10个类别
    label_list=['财经', '房产', '教育', '科技', '军事', '汽车', '体育', '游戏', '娱乐', '其他']
    label_map = { 
        idx: label_text for idx, label_text in enumerate(label_list)
    }

    # 加载训练好的新闻10分类模型
    model = hub.Module(
        name='ernie_tiny',
        task='seq-cls',
        load_checkpoint='../model/model.pdparams',
        label_map=label_map
    )

    # 加载GUI界面
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = interface.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    # 为按钮绑定相关功能函数完成功能添加
    # 单条新闻文本分类
    ui.pushButton.clicked.connect(partial(Single_classification, ui))
    # 批量新闻文本分类
    ui.pushButton_6.clicked.connect(partial(Batch_classification, ui))

    sys.exit(app.exec_())