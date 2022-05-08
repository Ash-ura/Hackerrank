/*
Enter your query here.
*/
SELECT F1.X, F1.Y FROM FUNCTIONS F1
    INNER JOIN FUNCTIONS F2
        ON F1.X = F2.Y AND F2.X = F1.Y
    GROUP BY F1.X, F1.Y
    HAVING COUNT(F1.X) > 1 OR F1.X < F1.Y
    ORDER BY F1.X;