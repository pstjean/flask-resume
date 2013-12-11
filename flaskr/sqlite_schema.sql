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


CREATE TABLE entries (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    headline VARCHAR(255) NOT NULL,
    text TEXT NOT NULL,
    asset INTEGER NOT NULL,
    FOREIGN KEY (asset) REFERENCES asset(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE timeline (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    headline VARCHAR(255) NOT NULL,
    text TEXT NOT NULL,
    asset INTEGER NOT NULL,
    FOREIGN KEY (asset) REFERENCES asset(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE asset (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    media VARCHAR(255) NOT NULL,
    credit VARCHAR(255) NOT NULL,
    caption TEXT NOT NULL
);
