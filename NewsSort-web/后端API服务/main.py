# 项目运行：
# cmd下运行：uvicorn main:app --reload
# main对应当前主文件名main.py，app对应创建的FastAPI实例， --reload代表当修改后重新加载

from asyncio.windows_events import NULL
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import paddlehub as hub

# 定义要进行分类的10个类别
label_list=['财经', '房产', '教育', '科技', '军事', '汽车', '体育', '游戏', '娱乐', '其他']
label_map = { 
    idx: label_text for idx, label_text in enumerate(label_list)
}

# 加载训练好的模型
model = hub.Module(
    name='ernie_tiny',
    task='seq-cls',
    load_checkpoint='../../model/model.pdparams',  # 注意模型加载路径要设置正确！
    label_map=label_map
    )

# 创建一个 FastAPI「实例」
app = FastAPI()

# 设置允许跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 定义请求体数据类型，新闻标题title + 新闻正文body
class News(BaseModel):
    title: str
    body: str

# 定义API接口/newssort, 请求方法为post方法，发送数据格式为json，包含新闻标题'title'+新闻正文'body'
# 定义路径操作装饰器：POST方法 + API路径
@app.post("/newssort/", status_code=200)
# 定义路径操作函数，当接口被访问将调用该函数
async def NewsClassification(news: News):
    try:
        # 拼接接收的新闻标题和正文内容
        data = news.title + news.body

        if data == NULL:
            # 定义返回结果格式
            results = {"message": "error",  "reason": '请求数据内容为空，请检察数据格式'}
            return results

        # 对数据进行简单清洗
        process = lambda x: x.strip().replace('\n', '').replace('\r', '').replace(" ","").replace(u'\t',u'')
        data = process(data)

        # 处理数据格式
        newslist = []
        list = []
        list.append(data)
        newslist.append(list)

        # 新闻10分类预测，默认为cpu环境，若已配置gpu环境可设置use_gpu=True
        label = model.predict(newslist, max_seq_len=256, batch_size=1, use_gpu=False)

        # 定义返回结果格式
        results = {"message": "success", "label": label[0], "title": news.title, "context": news.body}
        return results

    # 异常捕获
    except Exception as e:
        print(e)
        raise HTTPException(status_code=503, detail="请求失败，服务器异常！  异常原因：" + e)
