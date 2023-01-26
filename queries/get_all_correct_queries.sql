WITH tpt AS (
	select ats.idparticipant, ats.idsession, ats.idstep, sum(atst.planning_time) as tot_pt, sum(atst.total_time) as tot_tt
	from attemptsubmissiontimes atst
	natural join attemptsubmissions ats
	group by ats.idparticipant, ats.idsession, ats.idstep
    having tot_pt > 0
),
fpt AS (
	select ats.idparticipant, ats.idsession, ats.idstep, max(atst.planning_time) as fpt
	from attemptsubmissiontimes atst
	natural join attemptsubmissions ats
--	where ats.attemptnum = 1
	group by ats.idparticipant, ats.idsession, ats.idstep
    having fpt > 0
),

used AS (
select
    fu.filename,
    CASE when used_synonyms = 'True' THEN 1 ELSE 0 END as used_synonyms,
    CASE when used_expression_ordering = 'True' THEN 1 ELSE 0 END as used_expression_ordering,
    CASE when used_mod_ordering = 'True' THEN 1 ELSE 0 END as used_mod_ordering,
    CASE when used_natural_functions = 'True' THEN 1 ELSE 0 END as used_natural_functions,
    CASE when used_unbundling = 'True' THEN 1 ELSE 0 END as used_unbundling,
    CASE when has_min_kws = 'True' THEN 1 ELSE 0 END as has_min_kws
FROM feature_usage fu
)

SELECT 
-- Join parameters:
	sp.idparticipant, sp.idsession, sp.idattemptsubmission, sp.idquery,
    
-- Time Notations:
-- tt: total time
-- rt: recording time
-- pt: planning time (planning time for last attempt)
-- fpt: first planning time (planning time for first attempt)
-- tpt: total planning time (planning time for all attempts)
-- tt_all: sum of total time of all attempts (includes planning and recording of each attempt)

    sp.tt_speakql, sp.rt_speakql, sp.pt_speakql, sp.fpt_speakql, sp.tpt_speakql, sp.tt_all_speakql, 
    sp.step as step_speakql, sp.attemptnum_speakql, correct_speakql,

    sq.tt_sql, sq.rt_sql, sq.pt_sql, sq.fpt_sql, tpt_sql, sq.tt_all_sql, 
    sq.step as step_sql, sq.attemptnum_sql, correct_sql,

-- Difference Calculations
    (sp.tt_speakql - sq.tt_sql) as tt_diff,
    (sp.tt_speakql - sq.tt_sql) / ((sp.tt_speakql + sq.tt_sql) / 2) as tt_perc_diff,

    (sp.fpt_speakql - sq.fpt_sql) as fpt_diff,
    (sp.fpt_speakql - sq.fpt_sql) / ((sp.fpt_speakql + sq.fpt_sql) / 2) as fpt_perc_diff,

    (sp.tpt_speakql - sq.tpt_sql) as tpt_diff,
    (sp.tpt_speakql - sq.tpt_sql) / ((sp.tpt_speakql + sq.tpt_sql) / 2) as tpt_perc_diff,

    (sp.rt_speakql - sq.rt_sql) as rt_diff,
    (sp.rt_speakql - sq.rt_sql) / ((sp.rt_speakql + sq.rt_sql) / 2) as rt_perc_diff,

    sp.attemptnum_speakql - sq.attemptnum_sql as attemptnum_diff,
    
    sp.idsequence, sp.speakql_first, sp.ispractice,
-- Query properties and features used:
    q.complexity, q.normalized, q.is_complex, q.num_mods, q.num_joins, 
    q.num_funcs, q.num_proj, q.num_tables, q.num_selections,
    q.synonym as synonyms_possible,
    sp.used_synonyms,
    q.exp_ordering as expression_ordering_possible,
    sp.used_expression_ordering,
    q.mod_ordering as mod_ordering_possible,
    sp.used_mod_ordering,
    q.natural_functions as natural_functions_possible,
    sp.used_natural_functions,
    q.unbundle_join as unbundling_possible,
    sp.used_unbundling,
    
-- Participant properties:
	sr.experience as participant_experience, sr.self_rating as participant_self_rating
FROM (
    SELECT 
        ats.idparticipant, ats.idsession, ats.idattemptsubmission, ats.idquery, attemptnum as attemptnum_speakql,
        total_time as tt_speakql, recording_time as rt_speakql, planning_time as pt_speakql, tot_pt as tpt_speakql, tot_tt as tt_all_speakql, fpt as fpt_speakql, s.idsequence, 
        step, speakql_first, language, ispractice, atc.iscorrect as correct_speakql,
        used.used_unbundling, used.used_natural_functions, used.used_mod_ordering, used.used_expression_ordering,
        used.used_synonyms
    FROM speakql_study.attemptscommitted atc
    NATURAL JOIN speakql_study.attemptsubmissions ats
    NATURAL JOIN speakql_study.attemptsubmissiontimes atst
    NATURAL JOIN session s
    JOIN tpt on tpt.idparticipant = ats.idparticipant AND tpt.idsession = ats.idsession AND tpt.idstep = ats.idstep
    JOIN fpt on fpt.idparticipant = ats.idparticipant AND fpt.idsession = ats.idsession AND fpt.idstep = ats.idstep
    JOIN speakql_study.query_sequences qs ON s.idsequence = qs.idsequence AND qs.step = ats.idstep
    JOIN used ON ats.audiofilename = used.filename
    WHERE 
		(iscorrect = 1 OR (iscorrect = 0 AND attemptnum = 3)) 
--        and ats.idparticipant >= 1 
--        and ats.idparticipant <= 20 
        and language = 'speakql'
        and transcript <> "SKIP"
    ORDER BY ats.idstep, ats.attemptnum
) as sp JOIN (
    SELECT 
		ats.idparticipant, ats.idsession, ats.idattemptsubmission, ats.idquery, ats.attemptnum as attemptnum_sql,
		total_time as tt_sql, recording_time as rt_sql, planning_time as pt_sql, tot_pt as tpt_sql, tot_tt as tt_all_sql, fpt as fpt_sql, s.idsequence, 
		step, speakql_first, language, ispractice, atc.iscorrect as correct_sql
    FROM speakql_study.attemptscommitted atc
    NATURAL JOIN speakql_study.attemptsubmissions ats
    NATURAL JOIN speakql_study.attemptsubmissiontimes atst
    NATURAL JOIN session s
	JOIN tpt on tpt.idparticipant = ats.idparticipant AND tpt.idsession = ats.idsession AND tpt.idstep = ats.idstep
    JOIN fpt on fpt.idparticipant = ats.idparticipant AND fpt.idsession = ats.idsession AND fpt.idstep = ats.idstep
    JOIN speakql_study.query_sequences qs ON s.idsequence = qs.idsequence AND qs.step = ats.idstep
    WHERE 
		(iscorrect = 1 OR (iscorrect = 0 AND attemptnum = 3))
        and language = 'sql'
        and transcript <> 'SKIP'
    ORDER BY ats.idstep, ats.attemptnum
) as sq ON 
    sp.idparticipant = sq.idparticipant 
    AND sp.idsession = sq.idsession
    AND sp.idquery = sq.idquery
JOIN participants on sp.idparticipant = participants.idparticipant
JOIN queries AS q ON sq.idquery = q.idquery
LEFT JOIN survey_ratings sr on sr.idparticipant = sp.idparticipant
WHERE attemptnum_speakql <= 3 and attemptnum_sql <= 3
and participants.username like '%participant%'