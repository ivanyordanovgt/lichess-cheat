
DETECT_MOVE_JS = """

const squares = document.getElementsByClassName("last-move");

if (squares.length > 1) {
    console.log("Move is:", squares[1]["cgKey"]+squares[0]["cgKey"]);
    let square1Pos = extractNumbers(squares[1].style.transform)
    let square0Pos = extractNumbers(squares[0].style.transform)
    
    console.log(square0Pos, square1Pos)
    console.log()
    
}

function extractNumbers(str) {
    let regex = /(\d+(\.\d+)?)/g;
    let matches = str.match(regex);
    return matches.map(num => parseFloat(num));
}

"""

RETURN_BOARD_JS = """
function getSquare(x, y, containerWidth, containerHeight) {
    const squareSize = containerWidth / 8;
    const rank = 8 - Math.floor(y / squareSize);
    const file = Math.floor(x / squareSize);
    return 'abcdefgh'.charAt(file) + rank;
}

function extractNumbers(transformString) {
    const regex = /(\d+(\.\d+)?)/g;
    return transformString.match(regex).map(num => parseFloat(num));
}


function chessBoardToFEN(board)
{
    let result = "";
    for(let y = 0; y < board.length; y++)
    {
        let empty = 0;
        for(let x = 0; x < board[y].length; x++)
        {
            let c = board[y][x][0];  // Fixed
            if(c == 'w' || c == 'b') {
                if(empty > 0)
                {
                    result += empty.toString();
                    empty = 0;
                }
                if(c == 'w')
                {
                    result += board[y][x][1].toUpperCase();  // Fixed
                } else {
                    result += board[y][x][1].toLowerCase();  // Fixed
                }                
            } else {
                empty += 1;
            }
        }
        if(empty > 0)   // Fixed
        {
            result += empty.toString();
        }
        if(y < board.length - 1)  // Added to eliminate last '/'
        {
          result += '/';
        }
    }
    const botColor = window['botCurrentColor'];
    const botToTurn = window['botToTurn'];
    let colorToPlay = "";
    
    colorToPlay = (botToTurn) ? botColor : (botColor === "w" ? "b" : "w");
    
    result += ` ${colorToPlay} KQkq - 0 1`;
    return result;
}


function createFEN() {
    const pieces = {
        pawn: document.getElementsByClassName("pawn"),
        rook: document.getElementsByClassName("rook"),
        knight: document.getElementsByClassName("knight"),
        bishop: document.getElementsByClassName("bishop"),
        queen: document.getElementsByClassName("queen"),
        king: document.getElementsByClassName("king")
    };
    
    const cgContainer = document.getElementsByTagName('cg-container')[0];
    if (!cgContainer) return 'Error: cg-container not found';

    const containerWidth = cgContainer.offsetWidth;
    const containerHeight = cgContainer.offsetHeight;
    let board = new Array(8).fill(null).map(() => new Array(8).fill('.'));
    for (let [pieceKey, pieceRefs] of Object.entries(pieces)) {
        console.log(pieceRefs, "PIECE REFS")
        for (let pieceRef of pieceRefs) {
            if (!pieceRef.style.transform) {
                continue;
            }
            let pieceTransformValue = extractNumbers(`${pieceRef.style.transform}`);
            let [c, r] = [Math.ceil(pieceTransformValue[0]/74.4), Math.ceil(pieceTransformValue[1]/74.4)]
            const pieceName = pieceRef.classList.value.split(" ")
            let currentName = '';
            // Example: black rook, white bishop
            // Ghost pieces are when your holding a piece and it is in the air.
            if (pieceName.includes("ghost")) {
                pieceName.shift();
            }
            
            if (pieceName[1] === 'knight') {
                pieceName[1] = 'night';
            }
            
            let [f, l] = [pieceName[0][0], pieceName[1][0]]; // piece name is ["black", "rook"]
            
            if (f === "b") {
                l = l.toLowerCase();    
            } else {
                l = l.toUpperCase();
            }
            
            currentName = pieceName[1][0]
            board[r][c] = `${l}`
        
        }
    }
    
    
    // Convert the board array to FEN
    return board;
}

// Usage
console.log(createFEN())
return createFEN();

"""

SUGGEST_MOVE_JS = """


const cgBoard = document.getElementsByTagName("cg-board")[0];
function chessMoveToIndices(chessMove) {
  // Validate input format
  if (chessMove.length !== 4) {
    throw new Error("Invalid chess move format. Expected format: 'e2e4'.");
  }

  // Extract source and destination squares
  const sourceSquare = chessMove.slice(0, 2);
  const destSquare = chessMove.slice(2);

  // Convert algebraic notation to row and column indices
  const files = 'abcdefgh';
  const col1 = files.indexOf(sourceSquare[0]);
  const row1 = 8 - parseInt(sourceSquare[1], 10);
  const col2 = files.indexOf(destSquare[0]);
  const row2 = 8 - parseInt(destSquare[1], 10);

  return [row1, col1, row2, col2];
}

const moveToSuggest = window['moveToSuggest'];

if (moveToSuggest) {
    let [r1, c1, r2, c2] = chessMoveToIndices(moveToSuggest);
    console.log(r1, c1, r2, c2, 'rows and cols')

    const suggestColor = window['suggestColor'];
    window['drawChessBoard'](r1, c1, r2, c2, suggestColor)
    
   
    
}
"""
