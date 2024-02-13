
JS = """

function extractNumbers(transformString) {
    const regex = /(\d+(\.\d+)?)/g;
    return transformString.match(regex).map(num => parseFloat(num));
}

const nameElement = document.getElementsByTagName("name")[0];
const messageElement = document.getElementsByClassName("message")[0]
const whiteKingSquareElement = document.getElementsByClassName("white king")[0];
const kwdbElements = document.getElementsByTagName("kwdb");
let playerColor = '';

if (!window?.gameStarted) {
    let [c, r] = extractNumbers(whiteKingSquareElement.style.transform);
    if (r > 150) {
        window.botCurrentColor = "w"
    } else {
        window.botCurrentColor = "b"
    }
}

if (window?.botCurrentColor === "w") {
    if (messageElement) {
        window['botToTurn'] = true;
    } else window['botToTurn']=kwdbElements.length % 2 === 0;
    
} else if (window?.botCurrentColor === "b") {
    window['botToTurn'] = kwdbElements.length % 2 !== 0;
}

if (nameElement) {
    nameElement.textContent = `Bot to move: ${window['botToTurn']}`;
}
"""