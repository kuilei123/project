"""
应用配置文件
"""

#基础配置文件
class BaseConfig:
    DEBUG=False
    SECRET_KEY='IPUUGJHVGNBKVCFFXTCC'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#开发环境
class DevelopConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:123@127.0.0.1:3306/bj1910'

#生产环境（线上）
class ProductConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@127.0.0.1:3306/bj1910'

config={
    'default':BaseConfig,
    'develop':DevelopConfig,
    'production':ProductConfig
}