from quart import Quart
from app.config import Config


def create_app(config_obj=Config) -> Quart:
    app = Quart(__name__)
    app.config.from_object(config_obj)

    @app.route('/')
    async def index():
        return {"message": "Hello world"}
    
    return app
