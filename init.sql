CREATE TABLE IF NOT EXISTS todo(
    t_name TEXT PRIMARY KEY NOT NULL,
    t_status BOOLEAN NOT NULL,
    updated_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now')),
    create_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now'))
);

-- --Create
-- INSERT INTO todo (t_name, t_status) VALUES ('Jump', 1);
-- INSERT INTO todo (t_name, t_status) VALUES ('Crouch', 0);
-- --Read
-- SELECT * FROM todo;
-- --Update
-- UPDATE todo SET t_status = 1 WHERE t_name = 'Jump';
-- --Delete
-- DELETE FROM todo WHERE t_name = 'Jump';