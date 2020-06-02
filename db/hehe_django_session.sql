create table django_session
(
    session_key  varchar(40) not null
        primary key,
    session_data longtext    not null,
    expire_date  datetime(6) not null
);

create index django_session_expire_date_a5c62663
    on django_session (expire_date);

INSERT INTO hehe.django_session (session_key, session_data, expire_date) VALUES ('3owh242d8xbwdau97fxnaa7b6vq8w2a9', 'MDkyYjIxZGMyMTVlN2Q0MzdmYTYzMDlhNTcyYjg2MzQ1M2Q5ZGE1YTp7InVzZXJfaWQiOjEsInVzZXJfbmFtZSI6InRlc3QwMDAxIiwiY291bnQiOjR9', '2020-06-12 08:52:41.694709000');
INSERT INTO hehe.django_session (session_key, session_data, expire_date) VALUES ('mif74kr6pqh50fiz9wjk9tiopkrmca46', 'YTliNGVjMGUyNTIxMTM0ZTU3YjQ3MjkyMzZhZGZkODFiNGI5MmY4Yzp7InVzZXJfaWQiOjEsInVzZXJfbmFtZSI6InRlc3QwMDAxIn0=', '2020-04-16 10:27:43.386114000');