select
    attemptsubmissions.idattemptsubmission,
    attemptsubmissions.idparticipant,
    attemptsubmissions.idsession,
    q.idquery,
    idstep,
    audiofilename,
    attemptnum,
    iscorrect,
    total_time,
    recording_time,
    planning_time,
    session.idsequence as group_number,
    speakql_first,
    wt.transcript,
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
inner join attemptsubmissiontimes a2 on a.idattemptsubmission = a2.idattemptsubmission
inner join session on attemptsubmissions.idsession = session.idsession
inner join (select distinct idsequence, speakql_first from query_sequences) as qs on session.idsequence = qs.idsequence
where
    usedspeakql = 1
;