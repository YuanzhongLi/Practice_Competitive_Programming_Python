SELECT A1.player_id, A1.device_id
FROM (Activity A1 INNER JOIN (
        SELECT player_id, MIN(event_date) As event_date
        FROM Activity
        GROUP BY player_id
    ) A2 ON A1.player_id = A2.player_id AND A1.event_date = A2.event_date
)
