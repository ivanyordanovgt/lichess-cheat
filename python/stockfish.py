import chess
import chess.engine

# stockfish_path = 'stockfish_engine/stockfish.exe'
# engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
#
# board = chess.Board()
#
# while not board.is_game_over():
#     print(board)
#     if board.turn:  # Your move
#         user_move = input("Your move: ")
#         board.push_san(user_move)
#     else:  # Stockfish's move
#         result = engine.play(board, chess.engine.Limit(time=0.1))
#         board.push(result.move)

print("HI?")


class Stockfish:

    def __init__(self, stockfish_color):
        self.stockfish_path = 'stockfish_engine/stockfish.exe'
        self.engine = chess.engine.SimpleEngine.popen_uci(self.stockfish_path)
        self.board = chess.Board()
        self.stockfish_color = stockfish_color
        self.engine.configure({"Skill Level": 1})
        if stockfish_color == 'white':
            self.board_to_move = True
        else:
            self.board_to_move = False
        self.start_count = 0

    def move(self, player_move=None):
        try:
            current_stockfish_move = None
            moves_result = []
            if self.board_to_move:
                result = self.engine.play(self.board, chess.engine.Limit(time=1, depth=12))
                self.board.push(result.move)
                moves_result.append(result.move)
                print('stockfish moved!', result.move.uci())
                self.board_to_move = False
                print('returning ', result.move.uci())
                return [result.move.uci()]
            if player_move:
                if isinstance(player_move, str):
                    if player_move == 'h8h8' or player_move == 'h8e8' or player_move == 'e8h8':
                        player_move = 'e8g8'
                    self.board.push_san(player_move)
                    moves_result.append(player_move)
                    self.board_to_move = True
                    print('pushed move', player_move)
            if len(moves_result) == 0:
                return [[]]

            return moves_result
        except:
            return None
    @staticmethod
    def set_board_from_matrix(board_matrix):
        # Create a new empty board
        board = chess.Board(None)  # None to start with an empty board

        # Define a mapping from piece symbols to their corresponding piece types in the chess library
        piece_map = {
            'r': chess.ROOK, 'n': chess.KNIGHT, 'b': chess.BISHOP,
            'q': chess.QUEEN, 'k': chess.KING, 'p': chess.PAWN,
            'R': chess.ROOK, 'N': chess.KNIGHT, 'B': chess.BISHOP,
            'Q': chess.QUEEN, 'K': chess.KING, 'P': chess.PAWN,
        }

        # Iterate over each row in the matrix
        for y, row in enumerate(board_matrix):
            # Iterate over each piece symbol in the row
            for x, char in enumerate(row):
                if char in piece_map:
                    # Determine the color based on the case of the character
                    color = chess.WHITE if char.isupper() else chess.BLACK

                    # Create the piece
                    piece = chess.Piece(piece_map[char], color)

                    # Calculate the square index
                    square = chess.square(x, 7 - y)  # 7 - y because the board starts with 0 at the top

                    # Place the piece on the board
                    board.set_piece_at(square, piece)

        return board

stockfish_engine = Stockfish("white")
stockfish_engine.move()
print(stockfish_engine.board.fen())
print(stockfish_engine.board)
