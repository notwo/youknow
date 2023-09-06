# !!!2023年内リリース予定!!!

よく使うコマンドを先に書いておく

### Django
#### マイグレーション
```Bash
# マイグレーション確認
python manage.py showmigrations

# マイグレーションファイル作成
python manage.py makemigrations

# マイグレーション実行
python manage.py migrate you_know
```

#### マイグレーションやり直し手順
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

### Git Bash (Python)
```Bash
cd ~/Desktop/work/youknow
source env1/Scripts/activate
python manage.py runserver --traceback
```

### VSCode (VueJS)
```Bash
npm run dev
```

### sqlite3
```Bash
.open ../../youknow/db.sqlite3
```
