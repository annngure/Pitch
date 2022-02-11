def create_app(config_name):

    from .auth import auth as auth-blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')