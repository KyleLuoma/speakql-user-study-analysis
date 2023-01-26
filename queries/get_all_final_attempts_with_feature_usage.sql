-- Sum of planning time for all attempts (tot_pt) and total time for all attempts (tot_tt):
WITH tpt AS (
	select ats.idparticipant, ats.idsession, ats.idstep, ats.idquery, ats.usedspeakql,
	       max(ats.attemptnum), sum(atst.planning_time) as tot_pt, sum(atst.total_time) as tot_tt
	from attemptsubmissiontimes atst
	natural join attemptsubmissions ats
    where atst.planning_time > 0
	group by ats.idparticipant, ats.idsession, ats.idstep, ats.idquery, ats.usedspeakql
),

-- Planning time for first attempt:
fpt AS (
    select ats.idparticipant, ats.idsession, ats.idstep, ats.idquery, ats.usedspeakql,
           max(atst.planning_time) as first_pt
    from attemptsubmissiontimes atst
    natural join attemptsubmissions ats
    join participants on ats.idparticipant
    where ats.attemptnum = 1
	group by ats.idparticipant, ats.idsession, ats.idstep, ats.idquery, ats.attemptnum, ats.usedspeakql
),

-- Feature usage
used AS (
select
    attemptsubmissions.idattemptsubmission,
    idparticipant,
    idsession,
    q.idquery,
    idstep,
    audiofilename,
    wt.transcript as whisper_transcript,
    q.synonym as synonyms_possible,
    CASE when used_synonyms = 'True' THEN 1 ELSE 0 END as used_synonyms,
    q.exp_ordering as expression_ordering_possible,
    CASE when used_expression_ordering = 'True' THEN 1 ELSE 0 END as used_expression_ordering,
    q.mod_ordering as mod_ordering_possible,
    CASE when used_mod_ordering = 'True' THEN 1 ELSE 0 END as used_mod_ordering,
    q.natural_functions as natural_functions_possible,
    CASE when used_natural_functions = 'True' THEN 1 ELSE 0 END as used_natural_functions,
    q.unbundle_join as unbundling_possible,
    CASE when used_unbundling = 'True' THEN 1 ELSE 0 END as used_unbundling,
    CASE when has_min_kws = 'True' THEN 1 ELSE 0 END as has_min_kws
from attemptsubmissions
inner join attemptscommitted a on attemptsubmissions.idattemptsubmission = a.idattemptsubmission
inner join whisper_transcripts wt on attemptsubmissions.audiofilename = wt.filename
inner join feature_usage fu on wt.filename = fu.filename
inner join queries q on q.idquery = attemptsubmissions.idquery
where
    usedspeakql = 1
    and (iscorrect = 1 OR (iscorrect = 0 AND attemptnum = 3))
)

SELECT 
	ats.idparticipant, ats.idsession, ats.idattemptsubmission, ats.idquery, ats.idstep, ats.attemptnum,
	atst.total_time, atst.recording_time, atst.planning_time, tpt.tot_pt, fpt.first_pt, tpt.tot_tt,
	s.idsequence as groupnum,
	step, speakql_first, language, ispractice, atc.iscorrect as correct, ats.usedspeakql,
    q.complexity, q.normalized, q.is_complex, q.num_mods, q.num_joins, q.num_funcs, q.num_proj, q.num_tables, q.num_selections,
    used.used_unbundling, used.unbundling_possible, used.used_natural_functions, used.natural_functions_possible,
    used.used_mod_ordering, used.mod_ordering_possible, used.used_expression_ordering, used.expression_ordering_possible,
    used.used_synonyms, used.synonyms_possible
FROM speakql_study.attemptscommitted atc
NATURAL JOIN speakql_study.attemptsubmissions ats
NATURAL JOIN speakql_study.attemptsubmissiontimes atst
NATURAL JOIN session s
JOIN tpt on tpt.idparticipant = ats.idparticipant AND tpt.idsession = ats.idsession AND tpt.idstep = ats.idstep
JOIN fpt on fpt.idparticipant = ats.idparticipant AND fpt.idsession = ats.idsession AND fpt.idstep = ats.idstep
JOIN speakql_study.query_sequences qs ON s.idsequence = qs.idsequence AND qs.step = ats.idstep
JOIN queries AS q ON ats.idquery = q.idquery
JOIN participants on ats.idparticipant = participants.idparticipant
LEFT JOIN used on used.audiofilename = ats.audiofilename
WHERE
	(iscorrect = 1 OR (iscorrect = 0 AND ats.attemptnum = 3))
	and participants.username like '%participant%'
	and transcript <> "SKIP"
    and ats.attemptnum <= 3
ORDER BY ats.idstep, ats.attemptnum