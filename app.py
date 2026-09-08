import logging

from setup import create_app

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = create_app()


def main() -> None:
    
    @app.route("/")
    def root():
        return "Hello world"


main()   