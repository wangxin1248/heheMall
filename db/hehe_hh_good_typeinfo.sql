create table hh_good_typeinfo
(
    id        int auto_increment
        primary key,
    t_title   varchar(20) not null,
    is_delete tinyint(1)  not null
);

INSERT INTO hehe.hh_good_typeinfo (id, t_title, is_delete) VALUES (1, '新鲜水果', 0);
INSERT INTO hehe.hh_good_typeinfo (id, t_title, is_delete) VALUES (2, '海鲜水产', 0);
INSERT INTO hehe.hh_good_typeinfo (id, t_title, is_delete) VALUES (3, '猪牛羊肉', 0);
INSERT INTO hehe.hh_good_typeinfo (id, t_title, is_delete) VALUES (4, '禽类蛋品', 0);
INSERT INTO hehe.hh_good_typeinfo (id, t_title, is_delete) VALUES (5, '新鲜蔬菜', 0);
INSERT INTO hehe.hh_good_typeinfo (id, t_title, is_delete) VALUES (6, '速冻食品', 0);