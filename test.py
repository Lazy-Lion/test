import itertools
ns = itertools.count(1)  # count()创建一个无限自然数迭代器，只能按ctrl + c 停止,不能直接在sublime3 运行，会让sublime3 失去响应，应在命令行中运行
ns = itertools.takewhile(lambda x : 10 < x, ns)
for n in ns:
	print(n)


CREATE OR REPLACE TRIGGER TR_ORG_UPDATE    --TR_ORG_UPDATE 表示触发器的名字
AFTER update OF FLONGNUMBER        --FLONGNUMBER  更新哪个字段
ON T_BD_ORG
FOR EACH ROW
BEGIN
 DBMS_OUTPUT.PUT_LINE('旧的flongnumber值是'||:old.FLONGNUMBER
                  ||'、新的flongnumber值是'||:new.FLONGNUMBER);       --  输出值
 UPDATE usr1.t_bc_housepower h SET h.flongnumber=:new.FLONGNUMBER WHERE H.FKCURRORGID = :new.FID;
 UPDATE usr2.t_bc_housepower h  SET h.flongnumber=:new.FLONGNUMBER WHERE H.FKCURRORGID = :new.FID;
 UPDATE usr3.t_bc_housepower h SET h.flongnumber=:new.FLONGNUMBER WHERE H.FKCURRORGID = :new.FID;
END;
