-- Sum of planning time for all attempts (tot_pt) and total time for all attempts (tot_tt):
WITH tpt AS (
	select ats.idparticipant, ats.idsession, ats.idstep, sum(atst.planning_time) as tot_pt, sum(atst.total_time) as tot_tt
	from attemptsubmissiontimes atst
	natural join attemptsubmissions ats
	where ats.idparticipant >= 1 and ats.idparticipant <= 20
    and atst.planning_time > 0
	group by ats.idparticipant, ats.idsession, ats.idstep
),

-- Planning time for first attempt:
fpt AS (
    select ats.idparticipant, ats.idsession, ats.idstep, max(atst.planning_time) as first_pt
    from attemptsubmissiontimes atst
    natural join attemptsubmissions ats
    where ats.idparticipant >= 1 and ats.idparticipant <= 20
        and ats.attemptnum = 1
	group by ats.idparticipant, ats.idsession, ats.idstep
)

SELECT 
	ats.idparticipant, ats.idsession, ats.idattemptsubmission, ats.idquery, ats.idstep, attemptnum,
	total_time, recording_time, planning_time, tot_pt, first_pt, tot_tt, s.idsequence as groupnum, 
	step, speakql_first, language, ispractice, atc.iscorrect as correct, ats.usedspeakql,
    q.complexity, q.normalized, q.is_complex, q.num_mods, q.num_joins, q.num_funcs, q.num_proj, q.num_tables, q.num_selections
FROM speakql_study.attemptscommitted atc
NATURAL JOIN speakql_study.attemptsubmissions ats
NATURAL JOIN speakql_study.attemptsubmissiontimes atst
NATURAL JOIN session s
JOIN tpt on tpt.idparticipant = ats.idparticipant AND tpt.idsession = ats.idsession AND tpt.idstep = ats.idstep
JOIN fpt on fpt.idparticipant = ats.idparticipant AND fpt.idsession = ats.idsession AND fpt.idstep = ats.idstep
JOIN speakql_study.query_sequences qs ON s.idsequence = qs.idsequence AND qs.step = ats.idstep
JOIN queries AS q ON ats.idquery = q.idquery
JOIN participants on ats.idparticipant = participants.idparticipant
WHERE 
	(iscorrect = 1 OR (iscorrect = 0 AND attemptnum = 3)) 
	and participants.username like '%participant%'
	and transcript <> "SKIP"
    and attemptnum <= 3
ORDER BY ats.idstep, ats.attemptnum