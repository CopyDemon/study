-- 强制断开所有连接到数据库的用户
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'browser_bookmark'
  AND pid <> pg_backend_pid();

-- 删除数据库
DROP DATABASE browser_bookmark;