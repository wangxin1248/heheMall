create table auth_permission
(
    id              int auto_increment
        primary key,
    name            varchar(255) not null,
    content_type_id int          not null,
    codename        varchar(100) not null,
    constraint auth_permission_content_type_id_codename_01ab375a_uniq
        unique (content_type_id, codename),
    constraint auth_permission_content_type_id_2f476e4b_fk_django_co
        foreign key (content_type_id) references django_content_type (id)
);

INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (25, 'Can add user info', 7, 'add_userinfo');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (26, 'Can change user info', 7, 'change_userinfo');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (27, 'Can delete user info', 7, 'delete_userinfo');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (28, 'Can view user info', 7, 'view_userinfo');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (29, 'Can add good info', 8, 'add_goodinfo');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (30, 'Can change good info', 8, 'change_goodinfo');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (31, 'Can delete good info', 8, 'delete_goodinfo');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (32, 'Can view good info', 8, 'view_goodinfo');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (33, 'Can add type info', 9, 'add_typeinfo');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (34, 'Can change type info', 9, 'change_typeinfo');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (35, 'Can delete type info', 9, 'delete_typeinfo');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (36, 'Can view type info', 9, 'view_typeinfo');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (37, 'Can add card info', 10, 'add_cardinfo');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (38, 'Can change card info', 10, 'change_cardinfo');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (39, 'Can delete card info', 10, 'delete_cardinfo');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (40, 'Can view card info', 10, 'view_cardinfo');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (41, 'Can add cart info', 10, 'add_cartinfo');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (42, 'Can change cart info', 10, 'change_cartinfo');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (43, 'Can delete cart info', 10, 'delete_cartinfo');
INSERT INTO hehe.auth_permission (id, name, content_type_id, codename) VALUES (44, 'Can view cart info', 10, 'view_cartinfo');