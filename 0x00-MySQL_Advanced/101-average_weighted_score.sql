-- ComputeAverageWeightedScoreForUsers
-- This stored procedure computes and stores the average weighted score for all students.
-- Parameters: None
-- Returns: None

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id_cursor CURSOR FOR
        SELECT id FROM users;
    
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id INT;
    
    DECLARE total_score DECIMAL(10,2);
    DECLARE total_weight DECIMAL(10,2);
    DECLARE average_weighted_score DECIMAL(10,2);
    
    -- Declare handler for cursor operations
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    OPEN user_id_cursor;
    
    user_loop: LOOP
        FETCH user_id_cursor INTO user_id;
        
        IF done THEN
            LEAVE user_loop;
        END IF;
        
        -- Calculate total_score and total_weight for the user
        SELECT 
            SUM(score * weight) INTO total_score,
            SUM(weight) INTO total_weight
        FROM 
            scores
        WHERE 
            user_id = user_id;

        -- Calculate the average weighted score
        IF total_weight > 0 THEN
            SET average_weighted_score = total_score / total_weight;
        ELSE
            SET average_weighted_score = 0;
        END IF;

        -- Store the average weighted score for the user
        INSERT INTO average_weighted_scores (user_id, score) VALUES (user_id, average_weighted_score);
        
    END LOOP user_loop;
    
    CLOSE user_id_cursor;
    
END;
//

DELIMITER ;

