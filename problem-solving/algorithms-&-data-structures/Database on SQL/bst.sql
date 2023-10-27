/*
A query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node:

    Root: If node is root node.
    Leaf: If node is leaf node.
    Inner: If node is neither root nor leaf node.
Enter your query here.
*/

SELECT CASE WHEN P is Null THEN CONCAT(N, " Root")
            WHEN N IN(SELECT DISTINCT P FROM BST) THEN CONCAT(N, " Inner") 
            ELSE CONCAT(N, " Leaf")
        END AS node FROM BST ORDER BY N;
  
  
/*
Sample Input:

            BST table
        ________________________
        |   N       |   P       |
        |-----------|-----------|
        | 1         | 2         |
        | 3         | 2         |
        | 6         | 8         |
        | 9         | 8         |
        | 2         | 5         |
        | 8         | 5         |
        | 5         | Null      |
        |___________|___________|
        
Sample Output:
                1 Leaf
                2 Inner
                3 Leaf
                5 Root
                6 Leaf
                8 Inner
                9 Leaf
*/