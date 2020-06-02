create table django_migrations
(
    id      int auto_increment
        primary key,
    app     varchar(255) not null,
    name    varchar(255) not null,
    applied datetime(6)  not null
);

INSERT INTO hehe.django_migrations (id, app, name, applied) VALUES (1, 'contenttypes', '0001_initial', '2020-04-02 10:27:02.954213000');
INSERT INTO hehe.django_migrations (id, app, name, applied) VALUES (2, 'auth', '0001_initial', '2020-04-02 10:27:03.418485000');
INSERT INTO hehe.django_migrations (id, app, name, applied) VALUES (3, 'admin', '0001_initial', '2020-04-02 10:27:05.261339000');
INSERT INTO hehe.django_migrations (id, app, name, applied) VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2020-04-02 10:27:05.663653000');
INSERT INTO hehe.django_migrations (id, app, name, applied) VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2020-04-02 10:27:05.688001000');
INSERT INTO hehe.django_migrations (id, app, name, applied) VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2020-04-02 10:27:06.004804000');
INSERT INTO hehe.django_migrations (id, app, name, applied) VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2020-04-02 10:27:06.208140000');
INSERT INTO hehe.django_migrations (id, app, name, applied) VALUES (8, 'auth', '0003_alter_user_email_max_length', '2020-04-02 10:27:06.406622000');
INSERT INTO hehe.django_migrations (id, app, name, applied) VALUES (9, 'auth', '0004_alter_user_username_opts', '2020-04-02 10:27:06.424501000');
INSERT INTO hehe.django_migrations (id, app, name, applied) VALUES (10, 'auth', '0005_alter_user_last_login_null', '2020-04-02 10:27:06.565459000');
INSERT INTO hehe.django_migrations (id, app, name, applied) VALUES (11, 'auth', '0006_require_contenttypes_0002', '2020-04-02 10:27:06.576004000');
INSERT INTO hehe.django_migrations (id, app, name, applied) VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2020-04-02 10:27:06.595623000');
INSERT INTO hehe.django_migrations (id, app, name, applied) VALUES (13, 'auth', '0008_alter_user_username_max_length', '2020-04-02 10:27:06.796192000');
INSERT INTO hehe.django_migrations (id, app, name, applied) VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2020-04-02 10:27:07.001559000');
INSERT INTO hehe.django_migrations (id, app, name, applied) VALUES (15, 'auth', '0010_alter_group_name_max_length', '2020-04-02 10:27:07.228974000');
INSERT INTO hehe.django_migrations (id, app, name, applied) VALUES (16, 'auth', '0011_update_proxy_permissions', '2020-04-02 10:27:07.245638000');
INSERT INTO hehe.django_migrations (id, app, name, applied) VALUES (17, 'hh_user', '0001_initial', '2020-04-02 10:27:07.331213000');
INSERT INTO hehe.django_migrations (id, app, name, applied) VALUES (18, 'sessions', '0001_initial', '2020-04-02 10:27:07.406953000');
INSERT INTO hehe.django_migrations (id, app, name, applied) VALUES (19, 'hh_good', '0001_initial', '2020-04-25 13:37:33.522460000');
INSERT INTO hehe.django_migrations (id, app, name, applied) VALUES (20, 'hh_good', '0002_goodinfo_g_click', '2020-04-25 13:57:37.031292000');
INSERT INTO hehe.django_migrations (id, app, name, applied) VALUES (21, 'hh_good', '0003_goodinfo_g_unit', '2020-05-07 13:14:50.239037000');
INSERT INTO hehe.django_migrations (id, app, name, applied) VALUES (22, 'hh_cart', '0001_initial', '2020-05-17 12:26:18.043274000');
INSERT INTO hehe.django_migrations (id, app, name, applied) VALUES (23, 'hh_cart', '0002_auto_20200517_2039', '2020-05-17 12:39:04.352475000');