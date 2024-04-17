# lavender
Lavender thrives in poor soil。



主要解决部分历史数据库的字段不同而导致的分析问题。

工作目标：
1.查找数据库中表的关联关系，尤其是字段类型、字段长度的不一致，从而解决相关可能导致的数据库sql性能的不一致。
2.查找数据库表中数据字段的处理，主要处理相关主表或者数据内容不一致的情况，从而解决较大项目中，某些字段扩充了主表字段，但是部分程序没有开展相关调整而导致的问题。



第一步工作思路：
1. 第一步先开展数据库中的表、字段的分析
2. 读取多个库用相同名称字段名开展不同表的比较，并对比相关类型与长度
3. 
我真是个鱼唇的人。。。
基于 select * from information_schema.COLUMNS 就可以开展相关工作了。

我来打脸自己这个鱼唇的人吧

`
select
    tbs.TABLE_SCHEMA,
    tbs.TABLE_NAME,
    tbs.COLUMN_NAME,
    tbs.DATA_TYPE,
    tbs.CHARACTER_SET_NAME,
    tbs.COLLATION_NAME,
    tbs.COLUMN_TYPE,
    tbs.COLUMN_COMMENT,
    fdsid.cnt
from
    information_schema.COLUMNS tbs ,
(
    SELECT column_name,	count(1) cnt
    FROM
    (
        select DISTINCT column_name,data_type
        from
        information_schema.COLUMNS
    )tbl
    group by
        column_name
    HAVING
    c   nt>1
) fdsid
where
    tbs.column_name = fdsid.column_name
order by
    column_name,	data_type ,	TABLE_SCHEMA ,	TABLE_NAME
;
`

`

select *
from
    information_schema.COLUMNS;

`




第二步工作思路
1. 第二步结合数据库和程序源代码分析相关数据库表字段的处理
 








