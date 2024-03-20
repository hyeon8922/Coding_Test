select
    I.ID
    ,N.FISH_NAME
    ,I.LENGTH
from FISH_INFO as I, FISH_NAME_INFO as N
where 1=1
    and I.FISH_TYPE = N.FISH_TYPE
    and (I.FISH_TYPE, I.LENGTH) in (
        select FISH_TYPE, max(LENGTH)
        from FISH_INFO
        group by FISH_TYPE
    )