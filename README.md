# グラブルTwitter救援検索ツール on Command Line

コマンドラインで動くグラブルTwitter救援検索ツール．

## 概要  
指定したマルチバトルの救援依頼ツイートを取得し，参戦IDを自動でクリップボードにコピーします．  
IDをコピーするためのクリック動作が不要なため，同種の<strong>Webアプリよりクリック1回分早い</strong>です．

## 必要なもの
+ Python3.x

## 準備

### Consumer Keyの取得

### ライブラリのインストール
```
pip install requests_oauthlib
```

## 使用方法

```
python search.py enemy_level enemy_name
```
### 例

```
python search.py 75 シュヴァリエ・マグナ
```
+ 取得したツイートがコマンドラインに表示され，同時に参戦IDがクリップボードにコピーされます．
+ 終了するときは`Ctrl+C`を押してください．


## その他
+ 日本語のみの対応です．
+ 2018年6月20日にUser StreamsなどいくつかのAPIが廃止になるという[アナウンス](https://blog.twitter.com/developer/ja_jp/topics/tools/2017/aaa.html)がありましたが，このツールが使用しているPublic Streamsは存続すると思われます．