import reflex as rx

class ReflexaidemoConfig(rx.Config):
    pass

config = ReflexaidemoConfig(
    app_name="ReflexAIDemo",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)