from fastapi.middleware.cors import CORSMiddleware


def configure_cors(app):

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "https://api-portafolio-ia.onrender.com",
            "https://ezequieel-dev.vercel.app/",
            "*"
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )