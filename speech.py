from eave import Doc, Note, Api, PP, QP, BP



def img(src):
	return f'![avatar]({src})'



doc = Doc(title='OpenAPI 在 Django 项目中的应用 ', host='speech.tslow.cn', version='2020-06-14')




note1 = Note()
note.title = '今天的话题相对轻松，接口文档'
note.content = """
为什么轻松，因为只是文档而已吗，有手就能写，我上我也行
"""


note2 = Note()
note.title = '弹幕小互动'
note.content = """
## 大家一般使用什么工具写接口文档?

1. Swagger(openapi)
2. RAML
3. API Blueprint
4. 啥都不需要，用手写就行
"""





doc.build('speech.html')

