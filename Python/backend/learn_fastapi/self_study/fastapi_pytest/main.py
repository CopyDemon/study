from fastapi import FastAPI
from .router import Router


class App:
    def __init__(self):
        self.app = FastAPI()

        Router(self.app)

    def getApp(self):
        return self.app
