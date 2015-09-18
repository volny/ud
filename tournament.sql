CREATE DATABASE tournament;

CREATE TABLE players (
  id SERIAL PRIMARY KEY,
  tournament_entered INTEGER REFERENCES tournaments (id) -- HOW TO CROSS REF?
);

CREATE TABLE tournaments ( -- for multiple tournaments
  id SERIAL PRIMARY KEY,
  name TEXT,
  style TEXT,
  contestants INTEGER REFERENCES players (id) -- HOW TO CROSS REF?
);

CREATE TABLE matches (
  contestant1 INTEGER REFERENCES players (id),
  contestant2 INTEGER REFERENCES players (id),
  result INTEGER
  tournament
);

