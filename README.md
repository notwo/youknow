記法は[基本的な書き方とフォーマットの構文](https://docs.github.com/ja/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)に従う
___

sqliteを開く
sqlite-tools-win32-x86-3420000/sqlite3.exeで以下を実行
.open "C:/Users/07k11/Desktop/work/youknow/db.sqlite3"

# DBの確認方法
## sqlite
### Win
1. sqlite-tools-をダウンロード
1. 解凍したフォルダに入っているsqlite3.exeを実行

### Mac
TBD

## postgresql
### Win
TBD

### Mac
TBD

___

以下、あとで切り抜く

# DB操作のコマンド
select等の基本的な構文の使い方はmysqlと変わらない

## sqlite3
```text
ファイルを開く
.open db.sqlite3

テーブルの一覧を表示
.tables

スキーマを確認
.schema <テーブル名>

終了する
.exit
```

## postgresql
```text
TBD
```
