# -*- coding: utf-8 -*-
import os


class DevelopmentConfig:
    # Flask
    DEBUG = False

    #ClearDB
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8mb4'.format(**{
        'user': os.getenv('DB_USER', '[DBユーザ]'),
        'password': os.getenv('DB_PASSWORD', '[DBパスワード]'),
        'host': os.getenv('DB_HOST', '[DBホスト]'),
        'database': os.getenv('DB_DATABASE', '[データベース名]')
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

Config = DevelopmentConfig


#LINEチャンネル設定
Channel_access_token = '[チャンネルアクセストークン]'

Channel_secret = '[チャンネルシークレット]'

