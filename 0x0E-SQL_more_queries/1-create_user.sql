-- Create a new user with root priveleges
CREATE USER IF NOT EXISTS user_0d_1@localhost;
SET PASSWORD FOR user_0d_1@localhost = 'user_0d_1pwd';
GRANT ALL PRIVELEGES ON * . * TO user_0d_1@localhost;
FLUSH PRIVELEGES;
