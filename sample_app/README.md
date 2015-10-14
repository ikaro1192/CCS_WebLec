#本貸出システム

##要求

if log_in:
    本一覧が見れる(/index)
    自分が借りていない場合かつその本が借りられていない場合本一覧から借りれる
    借りている場合はその旨表示・返却button
else:
    ログイン

## URL

* /
* /login
* /logout
* /borrow/<book_id>
* /return



#DB

##ユーザ情報
create table Users(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL, pass TEXT NOT NULL);

create table Users(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL, pass_hash TEXT NOT NULL, salt TEXT NOT NULL);

## 図書情報
create table Books(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL);

## 貸出情報
create table LoanInfo(id INTEGER PRIMARY KEY AUTOINCREMENT,user_id INTEGER NOT NULL, book_id INTEGER NOT NULL);


#学べること
ルーティング
テンプレート
ログインの処理(セッション)
DB

#課題
ユーザページの実装(貸出履歴)
新規ユーザ登録ページ
adminページ(本の追加・削除)の実装
