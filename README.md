# Local Chat Messenger

## 概要
このプログラムはPythonのソケット通信とfakerパッケージを使用して、クライアントサーバ間で情報をやりとりするシンプルなアプリケーションです。
サーバーは、クライアントからメッセージを受け取るとfakerで返答を生成して、クライアントに送り返します。

## 使い方

プログラムを以下の形式で実行してください。

1. ターミナルでserver.pyを立ち上げます
```bash
$ python server.py
```
2. 別のターミナルでclient.pyを立ち上げる
```bash
$ python client.py
```
&nbsp;

### Fakerのインストール方法
**Ubuntu**
```bash
UbuntuにFakerをインストール
$ sudo apt update
$ pip install faker
```
#### 使用技術
<p style="display: inline">
<img src="https://img.shields.io/badge/-Linux-212121.svg?logo=linux&style=popout">
<img src="https://img.shields.io/badge/-Python-FFC107.svg?logo=python&style=popout">
</p>

&nbsp;

## 環境構築
### 開発環境
| OS・言語・ライブラリ | バージョン |
| :------- | :------ |
| Ubuntu | 22.04.4 LTS |
| Python | 3.10.12 |

&nbsp;
