SELECT
    students.student_id,
    students.student_name,
    subject.subject_name,
    COUNT(Examination.subject_name) as attended_exams
From Students students
JOIN Subjects subject
LEFT JOIN Examinations Examination
ON students.student_id = Examination.student_id
AND subject.subject_name = Examination.subject_name
GROUP BY students.student_id, subject.subject_name
ORDER BY student_id ASC, subject_name ASC