# 概要
知識整理アプリ「youknow」のAPI部分

バージョン1.0.0リリース済み

# API Doc
- [仕様書ダウンロード](https://you-know-j3fh.onrender.com/api/schema)
- [仕様書](https://you-know-j3fh.onrender.com/api/docs/)
- [Redoc](https://you-know-j3fh.onrender.com/api/redoc/)

# 構成
PaaSを用いているためインフラの構成は割愛

## DB
- 開発環境=> SQLite3
- 本番環境=> PostgreSQL

# 開発用コマンド
<details>
<summary>ここをクリック</summary>

## サーバ起動(Windows)
```Bash
cd ~/Desktop/work/youknow
source env1/Scripts/activate
python manage.py runserver --traceback
```

## Django
### ルーティング確認
```Bash
python manage.py show_urls
```

### マイグレーション
```Bash
# マイグレーション確認
python manage.py showmigrations

# マイグレーションファイル作成
python manage.py makemigrations

# マイグレーション実行
python manage.py migrate you_know
```

### マイグレーションやり直し手順
```Bash
.open ../../youknow/db.sqlite3
drop table <テーブル名>;
select * from django_migrations;
delete from django_migrations where id=<id>;
select * from django_migrations;
.tables

# マイグレーション実行前に戻ったか見る
python manage.py showmigrations you_know

# 不要なマイグレーションファイル削除
rm you_know/migrations/~~.py

# マイグレーションやり直し
python manage.py makemigrations
python manage.py migrate you_know
```

## sqlite3
sqlite-tools-win32-x86-3420000を用いる
```Bash
.open ../../youknow/db.sqlite3

.mode column
.header on

.tables
```

</details>

# 運用
<details>
<summary>ここをクリック</summary>

## デプロイ
[render.com](render.com)へデプロイする(GitHub連携済)

mainブランチにマージされた際に自動でデプロイされる

</details>

# 今後の方針
残りのissuesに従って、合間合間に実装を進める

単体テストも随時追加予定
