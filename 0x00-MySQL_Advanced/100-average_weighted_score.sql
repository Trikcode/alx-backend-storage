-- creates a stored procedure ComputeAverageWeightedScoreForUser that computes
-- and store the average weighted score for a student.
-- TODO: implement weighted average based on https://www.wikihow.com/Calculate-Weighted-Average

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(
	IN user_id int
)
BEGIN
   UPDATE users
   SET overall_score = (SELECT AVG(score)
    FROM corrections
	WHERE corrections.user_id=user_id
	GROUP BY corrections.user_id )
    WHERE id=user_id;
END //
DELIMITER;
