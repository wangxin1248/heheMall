create table auth_user
(
    id           int auto_increment
        primary key,
    password     varchar(128) not null,
    last_login   datetime(6)  null,
    is_superuser tinyint(1)   not null,
    username     varchar(150) not null,
    first_name   varchar(30)  not null,
    last_name    varchar(150) not null,
    email        varchar(254) not null,
    is_staff     tinyint(1)   not null,
    is_active    tinyint(1)   not null,
    date_joined  datetime(6)  not null,
    constraint username
        unique (username)
);

INSERT INTO hehe.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (1, 'pbkdf2_sha256$150000$96ZBnlQEVmYK$5TmeWmnoNFsLe8nfodJqQAWW5NpK1rpVi5AmYzsc0Fw=', '2020-04-25 15:20:18.656433000', 1, 'admin', '', '', 'test@abc.com', 1, 1, '2020-04-25 14:03:59.830939000');