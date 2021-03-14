CREATE TABLE Collections
(
  collection_id INT NOT NULL,
  collection VARCHAR(255) NOT NULL,
  PRIMARY KEY (collection_id)
);

CREATE TABLE Genre
(
  genre_id INT NOT NULL,
  genre_name VARCHAR(50) NOT NULL,
  PRIMARY KEY (genre_id)
);

CREATE TABLE IMDB
(
  imdb_id VARCHAR(20) NOT NULL,
  average_rating FLOAT NOT NULL,
  num_votes INT NOT NULL,
  PRIMARY KEY (imdb_id)
);

CREATE TABLE Movies
(
  budget INT NOT NULL,
  id INT NOT NULL,
  overview VARCHAR(1000) NOT NULL,
  popularity FLOAT NOT NULL,
  release_date DATE NOT NULL,
  revenue INT NOT NULL,
  runtime INT NOT NULL,
  tagline VARCHAR(255) NOT NULL,
  title VARCHAR(500) NOT NULL,
  is_adult VARCHAR(5) NOT NULL,
  adjusted_revenue INT NOT NULL,
  adjusted_budget INT NOT NULL,
  num_of_tickets_sold INT NOT NULL,
  imdb_id VARCHAR(20) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (imdb_id) REFERENCES IMDB(imdb_id)
);

CREATE TABLE Production_Companies
(
  prodcompany_id INT NOT NULL,
  prodcompany_name VARCHAR(225) NOT NULL,
  PRIMARY KEY (prodcompany_id)
);

CREATE TABLE Production_Countries
(
  prodcountry_iso CHAR(2) NOT NULL,
  prodcountry_name VARCHAR(50) NOT NULL,
  PRIMARY KEY (prodcountry_iso)
);

CREATE TABLE Actor
(
  actor_id INT NOT NULL,
  actor_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (actor_id)
);

CREATE TABLE Movie_Actor
(
  id INT NOT NULL,
  actor_id INT NOT NULL,
  PRIMARY KEY (id, actor_id),
  FOREIGN KEY (id) REFERENCES Movies(id),
  FOREIGN KEY (actor_id) REFERENCES Actor(actor_id)
);

CREATE TABLE Director
(
  director_id INT NOT NULL,
  director_name VARCHAR(225) NOT NULL,
  PRIMARY KEY (director_id)
);

CREATE TABLE Movie_Director
(
  director_id INT NOT NULL,
  id INT NOT NULL,
  PRIMARY KEY (director_id, id),
  FOREIGN KEY (director_id) REFERENCES Director(director_id),
  FOREIGN KEY (id) REFERENCES Movies(id)
);

CREATE TABLE Critic
(
  critic_score INT NOT NULL,
  id INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (id) REFERENCES Movies(id)
);

CREATE TABLE Movie_Collections
(
  collection_id INT NOT NULL,
  id INT NOT NULL,
  PRIMARY KEY (collection_id, id),
  FOREIGN KEY (collection_id) REFERENCES Collections(collection_id),
  FOREIGN KEY (id) REFERENCES Movies(id)
);

CREATE TABLE Movie_Genre
(
  genre_id INT NOT NULL,
  id INT NOT NULL,
  PRIMARY KEY (genre_id, id),
  FOREIGN KEY (genre_id) REFERENCES Genre(genre_id),
  FOREIGN KEY (id) REFERENCES Movies(id)
);

CREATE TABLE Movie_ProdCompany
(
  prodcompany_id INT NOT NULL,
  id INT NOT NULL,
  PRIMARY KEY (prodcompany_id, id),
  FOREIGN KEY (prodcompany_id) REFERENCES Production_Companies(prodcompany_id),
  FOREIGN KEY (id) REFERENCES Movies(id)
);

CREATE TABLE Movie_ProdCountry
(
  prodcountry_iso CHAR(2) NOT NULL,
  id INT NOT NULL,
  PRIMARY KEY (prodcountry_iso, id),
  FOREIGN KEY (prodcountry_iso) REFERENCES Production_Countries(prodcountry_iso),
  FOREIGN KEY (id) REFERENCES Movies(id)
);