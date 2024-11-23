# pinnekjott
... like [Stockfish](https://en.wikipedia.org/wiki/Stockfish_(chess)) for
[Patchwork](https://boardgamegeek.com/boardgame/163412/patchwork)!

## general idea

The general idea is to create an engine that simulates a Patchwork game, and to implement a 
[minimax algorithm](https://en.wikipedia.org/wiki/Minimax) to determine the best moves and piece placements.

Player boards are represented as 9-bit integer arrays (i.e. as [*bitboards*](https://en.wikipedia.org/wiki/Bitboard)).

This is an extremely unfinished project.

## importing pieces

`~/piece_importer/` is a code generation tool used to import your own custom pieces into the `GamePieces` class, if 
you want. To run it, run `cd /piece_importer/` and `npm start`.