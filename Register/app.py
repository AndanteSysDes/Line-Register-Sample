# -*- coding: utf-8 -*-
from flask import Flask
from .database import init_db, db
from .models import Message
from .config import Channel_access_token, Channel_secret

#ログ出力用(printはWinコマンドプロンプトで日本語が文字化けする)
from pprint import pprint

#LINEbot
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


def create_app():
    app = Flask(__name__)
    app.config.from_object('Register.config.Config')

    init_db(app)

    #LINE環境設定
    line_bot_api = LineBotApi(Channel_access_token)
    handler = WebhookHandler(Channel_secret)

    @app.route('/callback', methods=['POST'])
    def callback():
        signature = request.headers['X-Line-Signature']
        body = request.get_data(as_text=True)
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)
        return 'OK'

    #メッセージイベントのハンドラーを追加
    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(event):

        #LINEのユーザーIDを取得
        user_id = event.source.user_id

        #送られてきたメッセージをテキストとして取得
        input_msg = event.message.text

        #DBに保存
        message = Message(
            line_user_id = user_id,
            message = input_msg
        )
        db.session.add(message)
        db.session.commit()
        print('メッセージ登録：{}'.format(message))

        #返答はオウム返し
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=input_msg))


    return app


app = create_app()
