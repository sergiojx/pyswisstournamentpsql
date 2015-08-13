#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect();
    c = conn.cursor();
    c.execute("DELETE FROM matches;")
    conn.commit();
    conn.close();



def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect();
    c = conn.cursor();
    c.execute("DELETE FROM players;")
    conn.commit();
    conn.close();


def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect();
    c = conn.cursor();
    c.execute("select count(*) as cn from players;");
    row = c.fetchall()
    cnt = row[0][0];
    conn.commit();
    conn.close();
    return cnt;


def registerPlayer(name):
    """Adds a player to the tournament database.
   
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect();
    c = conn.cursor();
    c.execute("insert into players (name) values (%s)", (bleach.clean(name,strip = True),))
    conn.commit();
    conn.close();


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect();
    c = conn.cursor();
    c.execute("SELECT * FROM STANDINGS;");
    rows = c.fetchall()
    conn.commit();
    conn.close();
    return rows;


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect();
    c = conn.cursor();
    c.execute("insert into matches (p1,p2,winner) values (%s,%s,%s)", (winner,loser,winner));
    conn.commit();
    conn.close();
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    pairsLst = []
    p_idx = 0;
    p_namex = 1;
    p_wonx = 2;
    p_playedx = 3;
    playerStandingsLst = playerStandings()
    n = len(playerStandingsLst);
    i = iter(playerStandingsLst)
    c = 0
    while(n >= 2):
        player1 = i.next()
        player2 = i.next()
        pairsLst.append((player1[p_idx],player1[p_namex],player2[p_idx],player2[p_namex])); 
        n = n - 2;
        c = c + 1;
    if n == 1:
        print("There is an odd number of players");
    return pairsLst;

        



