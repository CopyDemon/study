class Router:
    def __init__(self, app):
        self.app = app

        @self.app.get("/")
        async def read_main():
            return {"msg": "Hello World"}
