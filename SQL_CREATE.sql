CREATE TABLE IF NOT EXISTS genre (
  genre_id   SERIAL      PRIMARY KEY,
  genre_name VARCHAR(60) NOT NULL
  );

CREATE TABLE IF NOT EXISTS artist (
  artist_id   SERIAL      PRIMARY KEY,
  artist_name VARCHAR(60) NOT NULL
  );

CREATE TABLE IF NOT EXISTS album (
  album_id   SERIAL       PRIMARY KEY,
  album_name VARCHAR (60) NOT NULL,
  album_year INTEGER      NOT NULL CONSTRAINT check_album_year CHECK (album_year BETWEEN 1900 AND 9999)
  );

CREATE TABLE IF NOT EXISTS track (
  track_id       SERIAL      PRIMARY KEY,
  track_name     VARCHAR(60) NOT NULL,
  track_duration INTEGER     NOT NULL CONSTRAINT positive_duration CHECK (track_duration > 0),
  album_id       INTEGER     REFERENCES album(album_id)
  );

CREATE TABLE IF NOT EXISTS collection (
  collection_id   SERIAL      PRIMARY KEY,
  collection_name VARCHAR(60) NOT NULL,
  collection_year INTEGER     NOT NULL CONSTRAINT check_collection_year CHECK (collection_year BETWEEN 1900 AND 9999)
  );

CREATE TABLE IF NOT EXISTS artist_genre (
  artist_genre_id SERIAL  PRIMARY KEY,
  artist_id       INTEGER REFERENCES artist(artist_id),
  genre_id        INTEGER REFERENCES genre(genre_id)
  );

CREATE TABLE IF NOT EXISTS album_artist (
  album_artist_id SERIAL  PRIMARY KEY,
  album_id        INTEGER REFERENCES album(album_id),
  artist_id       INTEGER REFERENCES artist(artist_id)
  );

CREATE TABLE IF NOT EXISTS collection_track (
  collection_track_id SERIAL  PRIMARY KEY,
  collection_id       INTEGER REFERENCES collection(collection_id),
  track_id            INTEGER REFERENCES track(track_id)
  );