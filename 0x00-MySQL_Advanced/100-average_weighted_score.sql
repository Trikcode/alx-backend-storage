-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser 
-- that computes and store the average weighted score for a student.

-- Requirements:

-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (you can assume user_id is linked to an existing users)

DELIMITER ||
CREATE PROCEDURE ComputerAverageScoreForUser (user_id INT)
BEGIN DECLARE w_avg_Score FLOAT;

SET w_avg_score = (
   SELECT SUM(score * weight) / SUM(weight)
FROM users AS user 
JOIN corrections AS corr ON user.id=corr.user_id
JOIN projects AS proj ON corr.project_id=proj.id 
WHERE user.id=user_id); UPDATE users

SET average_score = w_avg_score
WHERE id=user_id;
END ||
DELIMITER ;
