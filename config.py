# -*- coding: UTF-8 -*-
class Config:


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    # 'testing': TestingConfig,
    # 'production': ProductionConfig,
    #  'heroku': HerokuConfig,
    #  'unix': UnixConfig,

    'default': DevelopmentConfig
}