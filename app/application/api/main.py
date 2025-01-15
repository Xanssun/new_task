from application.api.v1.handlers import router
from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(
        title = 'Microservice',
        docs_url = '/api/docs',
        description = 'api for applications',
        debug = True,
    )

    app.include_router(router, prefix='/api/v1')

    return app
