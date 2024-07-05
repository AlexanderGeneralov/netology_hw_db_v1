 INSERT INTO artist (artist_name)
      VALUES
      ('Tom Delonge'),
      ('Avril Lavigne'),
      ('Slipknot'),
      ('NOFX');

 INSERT INTO genre (genre_name)
      VALUES
      ('Rock'),
      ('Pop'),
      ('Punk');

 INSERT INTO album (album_name, album_year)
      VALUES
      ('The Best',    2018),
      ('Love Sux',    2019),
      ('First Album', 2020);

INSERT INTO track (track_name, track_duration, album_id)
     VALUES
     ('my_track1', 100, 1),
     ('track2',    200, 1),
     ('my_track3', 300, 2),
     ('track4',    400, 2),
     ('my_track5', 500, 3),
     ('track6',    600, 3);

INSERT INTO collection (collection_name, collection_year)
     VALUES
     ('collection1', 2021),
     ('collection2', 2020),
     ('collection3', 2020);

INSERT INTO artist_genre (artist_id, genre_id)
     VALUES
     (1, 1),
     (2, 2),
     (3, 3),
     (4, 3),
     (1, 2);

INSERT INTO album_artist (album_id, artist_id)
     VALUES
     (1, 1),
     (2, 2),
     (3, 3),
     (1, 4),
     (2, 1);

INSERT INTO collection_track (collection_id, track_id)
     VALUES
     (1, 1),
     (2, 2),
     (3, 3),
     (1, 4),
     (2, 5),
     (3, 1);