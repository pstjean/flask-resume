drop table if exists timeline;
create table timeline (
    id integer primary key autoincrement,
    headline text not null,
    text text not null,
    asset integer not null
);

drop table if exists entries;
create table entries (
    id integer primary key autoincrement,
    startDate text not null,
    endDate text not null,
    headline text not null,
    text text not null,
    asset integer not null
);

drop table if exists asset;
create table asset (
    id integer primary key autoincrement,
    media text not null,
    credit text not null,
    caption text not null
);
