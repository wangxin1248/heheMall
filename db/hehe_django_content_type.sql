create table django_content_type
(
    id        int auto_increment
        primary key,
    app_label varchar(100) not null,
    model     varchar(100) not null,
    constraint django_content_type_app_label_model_76bd3d3b_uniq
        unique (app_label, model)
);

INSERT INTO hehe.django_content_type (id, app_label, model) VALUES (1, 'admin', 'logentry');
INSERT INTO hehe.django_content_type (id, app_label, model) VALUES (3, 'auth', 'group');
INSERT INTO hehe.django_content_type (id, app_label, model) VALUES (2, 'auth', 'permission');
INSERT INTO hehe.django_content_type (id, app_label, model) VALUES (4, 'auth', 'user');
INSERT INTO hehe.django_content_type (id, app_label, model) VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO hehe.django_content_type (id, app_label, model) VALUES (10, 'hh_cart', 'cartinfo');
INSERT INTO hehe.django_content_type (id, app_label, model) VALUES (8, 'hh_good', 'goodinfo');
INSERT INTO hehe.django_content_type (id, app_label, model) VALUES (9, 'hh_good', 'typeinfo');
INSERT INTO hehe.django_content_type (id, app_label, model) VALUES (7, 'hh_user', 'userinfo');
INSERT INTO hehe.django_content_type (id, app_label, model) VALUES (6, 'sessions', 'session');