```
add 2 line in my.cnf:
vi /etc/my.cnf
  innodb_force_recovery = 6
  innodb_purge_threads = 1

description:
innodb_force_recovery可以设置为1-6,大的数字包含前面所有数字的影响。 具体数字对应的含义： 1-----(SRVFORCEIGNORECORRUPT):忽略检查到的corrupt页。 2-----(SRVFORCENOBACKGROUND):阻止主线程的运行，如主线程需要执行full purge操作，会导致crash。 3-----(SRVFORCENOTRXUNDO):不执行事务回滚操作。 4-----(SRVFORCENOIBUFMERGE):不执行插入缓冲的合并操作。 5-----(SRVFORCENOUNDOLOGSCAN):不查看重做日志，InnoDB存储引擎会将未提交的事务视为已提交。 6-----(SRVFORCENOLOG_REDO):不执行前滚的操作。
```
