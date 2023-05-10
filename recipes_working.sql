-- SELECT * FROM users;
-- INSERT INTO recipes(name, description, instructions, under_30, user_id)
-- VALUES('Chicken Alfredo','Pasta with Alredo Sauce', 'Boil Pasta, Add Sauce and Enjoy', 1, 1); 
SELECT * FROM recipes
LEFT JOIN users ON users.id = recipes.user_id;
