
create table Users(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL, pass_hash TEXT NOT NULL, salt TEXT NOT NULL);
create table Books(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL);
create table LoanInfo(id INTEGER PRIMARY KEY AUTOINCREMENT,user_id INTEGER NOT NULL, book_id INTEGER NOT NULL);
insert into Users(name,pass_hash,salt) values('test','dd4305f6988d048711eb52f0c3fe8c9b3d1f5ff394f83bbb78ece99345ae793ef7cee8098ad990c6be1fbff2bcbc2e92c16ed111a951b64948352d19468eb464','1444806337.4782078');
insert into Books(name) values('ModernC++Design');
insert into Books(name) values('EffectiveC++');
