-- ComputeAverageWeightedScoreForUser
-- This stored procedure computes and stores the average weighted score for a student identified by the provided user_id.
-- Parameters:
--   - user_id: The ID of the student (linked to an existing record in the 'users' table).
-- Returns: None

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN p_user_id INT
)
BEGIN
    DECLARE total_score DECIMAL(10,2);
    DECLARE total_weight DECIMAL(10,2);
    DECLARE average_weighted_score DECIMAL(10,2);

    SELECT 
        SUM(score * weight) INTO total_score,
        SUM(weight) INTO total_weight
    FROM 
        scores
    WHERE 
        user_id = p_user_id;

    IF total_weight > 0 THEN
        SET average_weighted_score = total_score / total_weight;
    ELSE
        SET average_weighted_score = 0;
    END IF;

    INSERT INTO average_weighted_scores (user_id, score) VALUES (p_user_id, average_weighted_score);
    
END;
//

DELIMITER ;

