select b.title, b.board_id, r.reply_id, r.writer_id, r.contents, date_format(r.created_date, '%Y-%m-%d') created_date
from used_goods_reply r
    inner join used_goods_board b
    on r.board_id = b.board_id
where date_format(b.created_date, '%Y-%m') = '2022-10'
order by r.created_date, b.title