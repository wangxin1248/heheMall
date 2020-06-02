create table hh_user_userinfo
(
    id          int auto_increment
        primary key,
    u_name      varchar(10)  not null,
    u_pwd       varchar(40)  not null,
    u_phone     varchar(11)  not null,
    u_email     varchar(30)  not null,
    u_real_name varchar(10)  not null,
    u_addr      varchar(100) not null,
    u_code      varchar(6)   not null
);

INSERT INTO hehe.hh_user_userinfo (id, u_name, u_pwd, u_phone, u_email, u_real_name, u_addr, u_code) VALUES (1, 'test0001', '3426f1585a8f489f72ad109aa7adc54bce99da95', '11111111111', 'test@test.com', '王鑫', '陕西省西安市长安区西北工业大学', '111111');