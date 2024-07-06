--Задание 2
--1 select longest track, check+, work+
SELECT track_name, track_duration
FROM   track
WHERE  track_duration =
(
SELECT MAX(track_duration) FROM track
);

--2 select track longest 3.5 min, check+, work+
SELECT track_name
FROM   track
WHERE  track_duration >= 210;

--3 select collections 2018 - 2020, check+, work+
SELECT collection_name
FROM   collection
WHERE  collection_year BETWEEN 2018 AND 2020;

--4 select artist with singe word name, check+, work+
SELECT artist_name
FROM   artist
WHERE  artist_name NOT LIKE '% %';

--5 select track with 'my' in track name, check+, work+
SELECT track_name
FROM   track
WHERE  track_name LIKE '%my%';

--Задание 3
--6 select number of artists in each genre, check+, work+
SELECT   genre_name, COUNT(artist_id) as count
FROM     genre        AS g
JOIN     artist_genre AS ag ON g.genre_id = ag.genre_id
GROUP BY genre_name;

--7 select track number from albums 2019 - 2020, check+, work+
SELECT   album_name, album_year, COUNT(track_id) AS count
FROM     album AS a
JOIN     track AS t ON a.album_id = t.album_id
WHERE    album_year BETWEEN 2019 AND 2020
GROUP BY album_name, album_year;

--8 select aver track duration for each album, check+, work+
SELECT   album_name, AVG(track_duration) AS aver_track_duration
FROM     album AS a
JOIN     track AS t ON a.album_id = t.album_id
GROUP BY album_name;

--9 select artist name who did not release album in 2020, check+, work+, corrected
SELECT   artist_name
FROM     artist
WHERE    artist_name !=
(
SELECT   artist_name
FROM     artist       AS a
JOIN     album_artist AS aa ON a.artist_id = aa.artist_id
JOIN     album              ON aa.album_id = album.album_id
WHERE    album_year = 2020
);

--10 select collections with artist name NOFX, check+, work+
SELECT collection_name
FROM   collection       AS c
JOIN   collection_track AS ct ON c.collection_id = ct.collection_id
JOIN   track            AS t  ON ct.track_id = t.track_id
JOIN   album            AS a  ON t.album_id = a.album_id
JOIN   album_artist     AS aa ON a.album_id = aa.album_id
JOIN   artist                 ON aa.artist_id = artist.artist_id
WHERE  artist_name = 'NOFX';

--Задание 4
--11 album name with more than one genre artist, check+, work+, corrected
SELECT   album_name
FROM     album        AS a
JOIN     album_artist AS aa ON a.album_id = aa.album_id
JOIN     artist             ON aa.artist_id = artist.artist_id
JOIN     artist_genre AS ag ON artist.artist_id = ag.artist_id
JOIN     genre        AS g  ON ag.genre_id = g.genre_id
GROUP BY album_name
HAVING COUNT(DISTINCT genre_name) > 1;

--12 select track name which is not in any collections, check+, work+
SELECT    track_name
FROM      track            AS t
LEFT JOIN collection_track AS ct ON t.track_id = ct.track_id
WHERE     ct.track_id IS NULL;

--13 select artist wrote most short track, check+, work+
SELECT artist_name, track_name, track_duration
FROM   artist       AS a
JOIN   album_artist AS aa ON a.artist_id = aa.artist_id
JOIN   album              ON aa.album_id = album.album_id
JOIN   track        AS t  ON album.album_id = t.album_id
WHERE  track_duration = (SELECT MIN(track_duration) FROM track);

--14 select album name with less tracks in it check+, work+, corrected
SELECT album_name
FROM album AS a
JOIN     track AS t ON a.album_id = t.album_id
GROUP BY album_name
HAVING COUNT(track_name) =
(
    SELECT   COUNT(track_name) AS count
    FROM     album AS a
    JOIN     track AS t ON a.album_id = t.album_id
    GROUP BY album_name
    ORDER BY count ASC
    LIMIT 1
);