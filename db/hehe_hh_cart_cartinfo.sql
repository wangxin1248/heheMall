create table hh_cart_cartinfo
(
    id      int auto_increment
        primary key,
    count   int not null,
    good_id int not null,
    user_id int not null,
    constraint hh_cart_cardinfo_good_id_833ad759_fk_hh_good_goodinfo_id
        foreign key (good_id) references hh_good_goodinfo (id),
    constraint hh_cart_cardinfo_user_id_ca595483_fk_hh_user_userinfo_id
        foreign key (user_id) references hh_user_userinfo (id)
);

INSERT INTO hehe.hh_cart_cartinfo (id, count, good_id, user_id) VALUES (1, 3, 1, 1);
INSERT INTO hehe.hh_cart_cartinfo (id, count, good_id, user_id) VALUES (2, 8, 5, 1);
INSERT INTO hehe.hh_cart_cartinfo (id, count, good_id, user_id) VALUES (3, 3, 4, 1);
INSERT INTO hehe.hh_cart_cartinfo (id, count, good_id, user_id) VALUES (4, 3, 3, 1);