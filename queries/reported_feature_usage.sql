with

participants as (select * from participants
where username like 'participant%' and username not like '%18%'
order by idparticipant),

reported_feature_usage as (
    select idparticipant, used_synonyms, used_ordering, used_natural_func, used_unbundle, used_mod_order
    from survey_answers
),

max_session as(
    select idparticipant, idsequence, max(idsession) as idsession from session
    where idsequence like '%group%'
    group by idparticipant, idsequence
),

max_submission as(
    select * from attemptsubmissions
    where idattemptsubmission in (
        select idsession, idquery, idstep from (select idsession, idquery, idstep, max(attemptnum)
        from attemptsubmissions group by idsession, idquery, idstep) as a
    )
)

select * from participants
left join reported_feature_usage on participants.idparticipant = reported_feature_usage.idparticipant
join max_session on max_session.idparticipant = participants.idparticipant
join max_submission
    on max_submission.idparticipant = participants.idparticipant
         and max_submission.idsession = max_session.idsession
join attemptscommitted a on max_submission.idattemptsubmission = a.idattemptsubmission
where
    transcript <> 'SKIP'
    and attemptnum <= 3
order by participants.idparticipant
;