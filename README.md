# RacingRanking
A ranking system for (sim)racing based on [Elo rating system](https://en.wikipedia.org/wiki/Elo_rating_system).

## Preamble
Being an active simracer playing [Assetto Corsa Competizione](https://www.assettocorsa.it/competizione/) I was lucky to find a great league which offers cleaner races and a ranking. This is [Low Fuel Motorsport](https://lowfuelmotorsport.com/).

In the current season LFM is using a ranking system for rating the drivers according to their results. This leads to drivers racing with opponents close to their level, which in turn offers a much better experience.

This ranking system is based on the Elo ranking system, but the exact details are not shared by the LFM team.

Having driven a few dozen races in LFM, I noticed that the rating gain/loss after each race, takes little account of the driver's initial ranking (their skill) and much more of the position the finish. This has as a result that a driver's rating change is more influenced by where they are in the grid (one of the higher or lower rated drivers) and less by their result compared to their skill.

## My proposal
RacingRanking is a simple rating system that handles a race as a chess tournament between all participants. A driver that ends up in a better placement than another, is considered a winner (score: 1-0) in the match between them. All drivers have their expected "wins" calculated (because of their initial ranking and the ranking of their opponents). Their actual "wins" is calculated by their final placement. This system also make sure that the total rating change happening across the grid is zero.

The result of this ranking system is that the rating change is more dependent on the expected position the driver should get because of their initial rating (skill).

## An example
This example compares the rating change of the current system used by LFM and RacingRanking. It is base on the result of race [#24071](https://lowfuelmotorsport.com/events/60/race/24071) in the 25min sprint races in LFM (Coach Dave Series).

Using K factor: 6
Results:

|   Position |   Rating |   Current LMF Rating Change |   Proposed Rating Change |
|------------|----------|-----------------------------|--------------------------|
|          1 |     1991 |                          86 |                       32 |
|          2 |     1943 |                          78 |                       31 |
|          3 |     2186 |                          60 |                        2 |
|          4 |     1590 |                          74 |                       68 |
|          5 |     1606 |                          64 |                       60 |
|          6 |     1697 |                          50 |                       41 |
|          7 |     1649 |                          43 |                       42 |
|          8 |     1755 |                          29 |                       21 |
|          9 |     1831 |                          17 |                        4 |
|         10 |     1950 |                           3 |                      -18 |
|         11 |     1695 |                           3 |                       12 |
|         12 |     1663 |                          -5 |                        9 |
|         13 |     1885 |                         -23 |                      -28 |
|         14 |     2073 |                         -40 |                      -56 |
|         15 |     1722 |                         -35 |                      -17 |
|         16 |     1647 |                         -42 |                      -12 |
|         17 |     1570 |                         -48 |                       -8 |
|         18 |     2068 |                         -77 |                      -80 |
|         19 |     1607 |                         -68 |                      -25 |
|         20 |     1696 |                         -82 |                      -43 |
|         21 |     1589 |                         -86 |                      -35 |

Let's note some big differences:
* Driver in place #3 doesn't really get a lot of points with the proposed system as they are the top driver in split. Place #3 is not a big achievement for them.
* Driver in place #17 doesn't really lose a lot of points as he is the lowest rated river in the grid and is expected to be placed low.

There are other more subtle differences, but I think by now are getting the point.

## If you want to test by yourself
There are dependencies, I am not so experienced to explain, so I would recommend installing [Anaconda](https://www.anaconda.com/) and then run the python file with `python ranking.py`. You can change the number of the race (race_id) and the split (split_id) to test any race you want. Just try to choose races with 8+ drivers as these only are ranked in LFM.
