create table django_admin_log
(
    id              int auto_increment
        primary key,
    action_time     datetime(6)       not null,
    object_id       longtext          null,
    object_repr     varchar(200)      not null,
    action_flag     smallint unsigned not null,
    change_message  longtext          not null,
    content_type_id int               null,
    user_id         int               not null,
    constraint django_admin_log_content_type_id_c4bce8eb_fk_django_co
        foreign key (content_type_id) references django_content_type (id),
    constraint django_admin_log_user_id_c564eba6_fk_auth_user_id
        foreign key (user_id) references auth_user (id)
);

INSERT INTO hehe.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (1, '2020-04-25 14:14:25.488802000', '1', 'TypeInfo object (1)', 1, '[{"added": {}}]', 9, 1);
INSERT INTO hehe.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (2, '2020-04-25 14:14:41.106347000', '2', 'TypeInfo object (2)', 1, '[{"added": {}}]', 9, 1);
INSERT INTO hehe.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (3, '2020-04-25 14:14:57.285123000', '3', 'TypeInfo object (3)', 1, '[{"added": {}}]', 9, 1);
INSERT INTO hehe.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (4, '2020-04-25 14:15:09.286490000', '4', 'TypeInfo object (4)', 1, '[{"added": {}}]', 9, 1);
INSERT INTO hehe.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (5, '2020-04-25 14:15:18.731884000', '5', 'TypeInfo object (5)', 1, '[{"added": {}}]', 9, 1);
INSERT INTO hehe.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (6, '2020-04-25 14:15:33.377474000', '6', 'TypeInfo object (6)', 1, '[{"added": {}}]', 9, 1);
INSERT INTO hehe.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (7, '2020-04-25 15:28:11.859623000', '1', '柠檬', 1, '[{"added": {}}]', 8, 1);
INSERT INTO hehe.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (8, '2020-04-25 15:29:41.484196000', '2', '红提', 1, '[{"added": {}}]', 8, 1);
INSERT INTO hehe.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (9, '2020-04-25 15:31:08.690638000', '3', '草莓', 1, '[{"added": {}}]', 8, 1);
INSERT INTO hehe.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (10, '2020-04-25 15:32:00.990298000', '4', '黄杏', 1, '[{"added": {}}]', 8, 1);
INSERT INTO hehe.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (11, '2020-04-25 15:33:21.118405000', '5', '香蕉', 1, '[{"added": {}}]', 8, 1);
INSERT INTO hehe.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (12, '2020-04-25 15:34:15.338979000', '6', '大虾', 1, '[{"added": {}}]', 8, 1);
INSERT INTO hehe.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (13, '2020-04-25 15:35:01.062612000', '7', '扇贝', 1, '[{"added": {}}]', 8, 1);
INSERT INTO hehe.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (14, '2020-04-25 15:36:40.672626000', '8', '猪肉', 1, '[{"added": {}}]', 8, 1);