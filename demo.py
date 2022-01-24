# 导入所需包
import paddle
import paddlehub as hub

if __name__ == '__main__':

    # 定义要进行新闻10分类的内容数据：新闻标题title + 新闻正文body
    # 新闻标题title：
    title = "新总督致力提高加拿大公立教育质量"
    # 新闻正文body：
    body = "滑铁卢大学校长约翰斯顿先生于10月1日担任加拿大总督职务。约翰斯顿先生还曾任麦吉尔大学长，并曾在多伦多大学、女王大学和西安大略大学担任教学职位。"

    # 定义要进行分类的10个类别
    label_list=['财经', '房产', '教育', '科技', '军事', '汽车', '体育', '游戏', '娱乐', '其他']
    label_map = { 
        idx: label_text for idx, label_text in enumerate(label_list)
    }

    # 加载训练好的模型
    model = hub.Module(
        name='ernie_tiny',
        task='seq-cls',
        num_classes=10,    # 分类类别为10
        load_checkpoint='./model/model.pdparams',  # 加载微调训练好的模型权重,注意此处路径一定要注意设置对！
        label_map=label_map
    )

    # 拼接新闻标题和正文内容
    data = title + body

    # 对数据进行简单清洗和格式处理
    process = lambda x: x.strip().replace('\n', '').replace('\r', '').replace(" ","").replace(u'\t',u'')
    data = process(data)
    newslist = []
    list = []
    list.append(data)
    newslist.append(list)

    # 新闻长文本10分类模型预测
    # 默认为cpu环境，若已配置gpu环境可设置use_gpu=True
    label = model.predict(newslist, max_seq_len=256, batch_size=1, use_gpu=False)

    # 输出结果
    print('新闻标题: {} \n 新闻正文: {} \n 新闻类别: {} '.format(title, body, label[0]))