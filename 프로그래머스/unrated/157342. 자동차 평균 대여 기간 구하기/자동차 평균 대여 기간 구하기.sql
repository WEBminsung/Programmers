select car_id , round(avg(date_gap),1) as average_duration
	from 
		(select car_id , datediff(end_date,start_date)+1 as date_gap
			from
				car_rental_company_rental_history) as tmp_table
	group by 
		car_id
	having
		average_duration >= 7
        -- car_id < 3
	order by
		average_duration desc ,car_id desc;