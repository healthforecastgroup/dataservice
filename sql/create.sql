CREATE TABLE app_user (
  user_id serial NOT NULL,
  user_name text NOT NULL,
  first_name text NOT NULL,
  last_name text NOT NULL,
  password text NOT NULL,
  email  text NOT NULL,
  privilege integer NOT NULL DEFAULT 0,
  CONSTRAINT pk_user_id PRIMARY KEY (user_id),
  CONSTRAINT unique_user_name UNIQUE(user_name)
);