from eave import Doc, Note, Api, PP, QP, BP


def img(src, w=0):
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
<br><br><br><br>
"""
doc.add_note(note)


note = Note(title='开始今天我们话题，接口文档')
note.content = f"""
- 谁写文档: `后端工程师`
- 写给谁看: `前端工程师`
<br><br>

#### 说程序员最痛恨的 4 件事情
1. 写注释
2. 写文档
3. 别人不写注释
4. 别人不写文档
<br><br>

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


note = Note(title='小结一下')
note.content = f"""
##### 编写文档对于每一个普通的开发人员来说，可能算是一种 “负担”
##### 但是在**前后端分离**大势所趋的今天
##### 能够编写一份**可读性高**、**方便传阅交流**的接口文档已成为每一位**后端开发者**的必备技能
##### 如果能有个工具来**自动**干这件事那就更棒了!
"""
doc.add_note(note)


api = Api()
api.title = 'Swagger'
api.url = '/写完代码/就能同步产出成品文档'
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
api.url = '/从 swagger2 /到 openapi3'
api.description = """
##### OpenAPI 是规范
##### Swagger 是实现规范的工具
"""
api.response_description = f"""
#### 各其他主流工具的对比
1. `OpenAPI`: 根据规范编写出 `yaml` 或 `json` 文件，然后使用 `Swagger`、`ReDoc` 等渲染出成品文档
2. `RAML`: 根据规范编写出 `raml` 文件，然后使用 `raml2html` 等渲染出成品文档
3. `API Blueprint`: 根据规范编写出 `markdown` 文件，然后使用 `Aglio`、`snowboard` 等渲染出成品文档

#### 规范简介

{img('2to3.png')}

参考: https://stuff.rdme.io/swagger2to3

```
# OpenAPI 规范版本号
openapi: 3.0.3

# API 元数据信息
info:

# 服务器连接信息
servers:

# API 的分组标签
tags:

# 声明 API 使用的安全机制
security:

# 对所提供的 API 有效的路径和操作
paths:

# 一个包含多种纲要的元素，可重复使用组件
components:

# 附加文档
externalDocs:
```

#### info 部分
```
info:
  title:  xx开放平台接口文档                    # 应用的名称
  description: |                          
    简短的描述信息，支持 markdown 语法。 | 表示换行，< 表示忽略换行。
  version: "1.0.0"                            # API 文档的版本信息
  termsOfService: 'http://swagger.io/terms/'  # 指向服务条款的 URL 地址
  contact:                                    # 所开放的 API 的联系人信息
    name: API Support                           # 人或组织的名称
    url: http://www.example.com/support         # 指向联系人信息的 URL 地址
    email: apiteam@swagger.io                   # 人或组织的 email 地址
  license:                                    # 所开放的 API 的证书信息。
    name: Apache 2.0
    url: 'http://www.apache.org/licenses/LICENSE-2.0.html'
```

#### servers 部分
```
servers:  
  - url: https://development.server.com/v1
    description: 开发服务器
  - url: https://{{subdomain}}.site.com/{{version}}
    description: 生产服务器
    variables:
      subdomain:
        default: production
      version:
        enum:
          - v1
          - v2
        default: v2
```

#### tags 部分
```
tags: 
  - name: store
    description: 宠物商店
  - name: user
    description: 用户操作相关
  - name: pet
    description: 与宠物相关的接口
    externalDocs:
      description: 外部文档
      url: 'http://pet.docs.io'
```

#### security 部分
```
BasicAuth:
  type: http
  scheme: basic

JWT:
  type: http
  scheme: bearer
  bearerFormat: jwt

APIKey:
  type: apiKey
  name: api_key
  in: header
```

#### paths 部分
```
# 对所提供的 API 有效的路径和操作
paths:
  /pet/{{petId}}:
    get:
      tags:
        - pet
      summary: 简要总结，描述此路径内包含的所有操作。
      description: 详细说明，用于描述此路径包含的所有操作。
      operationId: getPetById      # 此操作的唯一标识符
      parameters:                 # 参数列表
        - name: petId
          in: path
          description: 路径参数，宠物 ID。
          required: true
          schema:
            type: integer
            format: int64
      responses:                  # 接口响应内容
        '200':
          description: 操作成功
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                    format: int64
                  category:
                    type: object
                    properties:
                      id:
                        type: integer
                        format: int64
                      name:
                        type: string
                  name:
                    type: string
                    example: doggie
                  photoUrls:
                    type: array
                    items:
                      type: string
                  tags:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                          format: int64
                        name:
                          type: string
                  status:
                    type: string
                    description: 宠物在商店的状态
                    enum:
                      - available
                      - pending
                      - sold
        '400':
          description: 无效的 id
        '404':
          description: 找不到指定的资源
      security:             # 作用于此操作的安全机制
        - APIKey: []         # 可以声明一个空数组来变相的移除顶层的安全声明
```

#### components 部分
```
components:
  schemas:
 
  responses:
  
  parameters:
  
  examples:
    
  requestBodies:
  
  headers:
    
  securitySchemes:
  
  links:
  
  callbacks:
```

#### 上例使用 components 优化
```
paths:
  '/pet/{{petId}}':
    get:
      tags:
        - pet
      summary: 简要总结，描述此路径内包含的所有操作
      description: 详细说明，用于描述此路径包含的所有操作
      operationId: getPetById      # 此操作的唯一标识符
      parameters:                  # 参数列表
        - name: petId
          in: path
          description: pet ID
          required: true
          schema:
            type: integer
            format: int64
      responses:                  # 响应列表
        '200':
          description: 操作成功
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Pet'
        '400':
          description: 无效的 id
        '404':
          description: 找不到指定的资源
      security:             # 作用于此操作的安全机制
        - api_key: []         # 可以声明一个空数组来变相的移除顶层的安全声明

components:
  schemas:
    Pet:
      type: object
      properties:
        id:
          type: integer
          format: int64
        category:
          $ref: '#/components/schemas/Category'
        name:
          type: string
          example: doggie
        photoUrls:
          type: array
          items:
            type: string
        tags:
          type: array
          items:
            $ref: '#/components/schemas/Tag'
        status:
          type: string
          description: 宠物在商店的状态
          enum:
            - available
            - pending
            - sold
    Category:
      type: object
      properties:
        id:
          type: integer
          format: int64
        name:
          type: string
    Tag:
      type: object
      properties:
        id:
          type: integer
          format: int64
        name:
          type: string
```

#### POST 传参的例子
```
paths:
  /pet:
    post:
      tags:
        - pet
      summary: 向商店中添加新的宠物
      operationId: addPet
      requestBody:    # 请求体
        description: 需要被添加进商店的 Pet 对象
        required: true # 请求体是否被包含在请求中，默认值 false
        content:      # 请求体的内容
          application/json:
            schema:
              $ref: '#/components/schemas/Pet'
```
参考: https://www.jianshu.com/p/5365ef83252a

""" + """
#### 生成文档:
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Swagger</title>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="//unpkg.com/swagger-ui-dist@3/swagger-ui.css" />
  </head>
  <body>
    <div id="swagger-ui"></div>
    <script src="//unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js"></script>
    <script>
    const ui = SwaggerUIBundle({
        url: "{% url openapi_url %}",
        dom_id: '#swagger-ui',
        presets: [
          SwaggerUIBundle.presets.apis,
          SwaggerUIBundle.SwaggerUIStandalonePreset
        ],
        layout: "BaseLayout"
      })
    </script>
  </body>
</html>
```
```
<!DOCTYPE html>
<html>
  <head>
    <title>ReDoc</title>
    <!-- needed for adaptive design -->
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,700|Roboto:300,400,700" rel="stylesheet">
    <!-- ReDoc doesn't change outer page styles -->
    <style>
      body {
        margin: 0;
        padding: 0;
      }
    </style>
  </head>
  <body>
    <redoc spec-url='{% url openapi_url %}'></redoc>
    <script src="https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"> </script>
  </body>
</html>
```

"""
doc.add_api(api)


api = Api(method='PUT')
api.title = 'Django REST framework'
api.url = '/3.9 版本开始/官方支持 openapi3'
api.response_description = """
"""
api.tips = f"""
"""
doc.add_api(api)




doc.build('speech.html', 'zh')

