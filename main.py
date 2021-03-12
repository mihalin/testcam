from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/')
async def start(request):
    return web.Response(text="""
    <html>
    <head>
    <meta charset="UTF-8">
    </head>
    <body>
    <a href="/test1">Пример 1, через форму</a>
    <br>
    <a href="/test2">Пример 2, через WebRTC</a>
    </body>
    </html>
    """, content_type="html")


@routes.get("/test1")
async def test1(request):
    """
    Просто через форму
    :param request:
    :return:
    """
    return web.Response(text="""
    <html>
    <head></head>
    <body>
    <form action='/foo' method='POST'>
    <input type="file" accept="image/*;capture=camera">
    <br><br>
    <input type='submit'>
    </form>
    </body>
    </html>
    """, content_type="html")


@routes.post("/foo")
async def post(request):
    return web.Response(text="ok")


@routes.get("/test2")
async def test2(request):
    """
    WebRTS с сайта https://github.com/mdn/samples-server/tree/master/s/webrtc-capturestill
    https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Taking_still_photos
    :param request:
    :return:
    """
    with open("static/webrts/index.html", "r") as page:
        return web.Response(text=page.read(), content_type="html")


routes.static("/static", "static")

if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)
