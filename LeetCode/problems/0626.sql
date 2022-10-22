SELECT (
    CASE
        WHEN MOD(s1.id, 2) != 0 AND seat_counts.counts != id THEN id + 1
        WHEN MOD(s1.id, 2) != 0 AND seat_counts.counts = id THEN id
        ELSE id - 1
    END
) AS id, s1.student
FROM Seat s1, (
    SELECT COUNT(*) AS counts
    FROM seat
) AS seat_counts
ORDER BY id ASC
