/* FINAL BUT CANT SUBMIT */	
	
SELECT 
    con.contest_id, 
    con.hacker_id, 
    con.name, 
    SUM(ss.ts) AS sts, 
    SUM(ss.tas) AS stas, 
    SUM(vs.tv) AS stv, 
    SUM(vs.tuv) AS stuv
    
    FROM Contests AS con
    
    LEFT OUTER JOIN Colleges AS col
        ON col.contest_id = con.contest_id
    
    LEFT OUTER JOIN Challenges as ch
        ON ch.college_id = col.college_id
    
    LEFT OUTER JOIN (
        SELECT challenge_id, SUM(total_submissions) AS ts, SUM(total_accepted_submissions) AS tas
            FROM Submission_Stats
            GROUP BY challenge_id
    ) AS ss
        ON ss.challenge_id = ch.challenge_id
        
    LEFT OUTER JOIN (
        SELECT challenge_id, SUM(total_views) AS tv, SUM(total_unique_views) AS tuv
            FROM View_Stats
            GROUP BY challenge_id
    ) AS vs
        ON vs.challenge_id = ch.challenge_id
        
    GROUP BY 
        con.contest_id, 
        con.hacker_id, 
        con.name
        
    HAVING 
        (sts + stas + stv + stuv) != 0
        
    ORDER BY con.contest_id;