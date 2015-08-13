-- Create and connect to tournament data base
CREATE DATABASE tournament;
\c tournament;

-- Create players table with columns id and name. Set id as primary key 
CREATE TABLE players ( 	id SERIAL primary key,
						name TEXT
                     );
-- Create matches table with columns p1 for first player id, p2 for second player id,
-- and winner for winner player id. Set p1 and p2 as foreig key
CREATE TABLE matches(
						p1 INTEGER references players(id),
						p2 INTEGER references players(id),
						winner INTEGER references players(id),
						primary key (p1,p2,winner )
					);
-- view for getting player played match  quantity. Not used
CREATE VIEW PLAYED as
	select players.id, 
			players.name, 
			count(matches.winner) as played  
		from players left join matches 
			on matches.p1 = players.id or matches.p2 = players.id group by players.id order by played; 

-- view for getting player won match quantity. Not used
CREATE VIEW WON as
	select players.id,
	 		players.name,
	  		count(matches.winner) as won 
	   from players left join matches
	   	 on matches.winner = players.id group by players.id order by won desc; 
-- view for getting player's played and won math quantity information.
-- This is done by a left join of played and won requests.
CREATE VIEW STANDINGS as 
	select p.id, 
			p.name,
			w.won,
			p.played
		from 
			(select players.id,
					 players.name,
					 count(matches.winner) as played
				from players left join matches on matches.p1 = players.id or matches.p2 = players.id group by players.id) as p,
			(select players.id,
					players.name,
					count(matches.winner) as won
				from players left join matches on matches.winner = players.id group by players.id) as w where p.id = w.id order by won desc;





