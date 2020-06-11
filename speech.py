from eave import Doc, Note, Api, PP, QP, BP



def img(src, w=''):
	if not src.startswith('http:'):
		# src = 'https://raw.githubusercontent.com/taojy123/openapi_speech/master/assets/' + src
		src = 'assets/' + src
	if w:
		return f'<img src="{src}" width="{w}">'
	return f'![avatar]({src})'



doc = Doc(title='OpenAPI 在 Django 项目中的应用 ', host='speech.tslow.cn', version='2020-06-14')


note = Note(title='开场小互动')
note.content = f"""
#### 大家一般使用什么工具写接口文档?
1. Swagger(openapi) <br><br> {img('swagger_logo.png', 200)} <br>
2. RAML <br><br>  {img('raml_logo.png', 200)} <br>
3. API Blueprint <br><br>  {img('apiblueprint_logo.jpg', 200)} <br>
4. 其他工具 <br><br>  {img('other_tools.jpg', 200)} <br>
5. 啥都不需要，用手写就行 <br><br>  {img('hand.png', 200)} <br>
"""
doc.add_note(note)


note = Note(title='今天我们话题，接口文档')
note.content = f"""
#### 说程序员最痛恨的 4 件事情
1. 写注释
2. 写文档
3. 别人不写注释
4. 别人不写文档
<br><br>

- 谁写文档: `后端工程师`
- 写给谁看: `前端工程师`

#### 青铜玩家的文档
{img('api_doc.png', 600)}
<br><br>

#### 其实我们可以有更高一点的追求
{img('snowboard_example.png', 700)}
{img('redoc-demo.png', 800)}
1. 界面美观
2. 多端浏览
3. 方便维护
<br><br><br>
"""
doc.add_note(note)


note = Note(title='')
note.content = f"""
##### 编写文档对于每一个普通的开发人员来说，可能算是一种 “负担”
##### 但是在**前后端分离**大势所趋的今天
##### 能够编写一份**可读性高**、**方便传阅交流**的接口文档已成为每一位**后端开发者**的必备技能
##### 如果能有个工具来**自动**干这件事那就更棒了!
"""
doc.add_note(note)


api = Api()
api.title = 'Swagger'
api.url = '写完代码后就能同步产出成品文档'
api.description = """
**解决痛点:**

随着时间推移，不断修改接口实现的时候都必须同步修改接口文档，而文档与代码又处于两个不同的媒介，除非有严格的管理机制，不然很容易导致不一致现象。
"""
api.tips = f"""

{img('swagger_ui_example.png', 800)}


#### 被很多著名的框架都直接或间接的支持
1. Java 领域，著名的 `spring-swagger`，后更名为 `springfox`
2. django-rest-framework 搭配 `drf_yasg` 或 `coreapi`
3. `FastAPI` 更是完美的原生支持，可一键生成 swagger 风格文档
4. ...
"""
doc.add_api(api)


api = Api(method='POST')
api.title = 'OpenAPI'
api.url = '从 swagger2 到 openapi3'
api.description = """
##### OpenAPI 是规范
##### Swagger 是实现规范的工具
"""
api.tips = f"""
#### 与其他主流工具的对比
1. `OpenAPI`: 根据规范编写出 `yaml` 或 `json` 文件，然后使用 `swagger`、`redoc` 等渲染出成品文档
2. `RAML`: 根据规范编写出 `raml` 文件，然后使用 `raml2html` 等渲染出成品文档
3. `API Blueprint`: 根据规范编写出 `markdown` 文件，然后使用 `aglio`、`snowboard` 等渲染出成品文档


openapi
drf
"""
doc.add_api(api)



doc.build('speech.html', 'zh')

