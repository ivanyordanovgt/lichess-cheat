
JS = """

const pieceImages = window['editedChessPhotos']

for (let key of Object.keys(pieceImages)) {
    const figuresData = pieceImages[key];
    const changedData = Object.entries(figuresData)
    
    for (let [pieceName, pieceImgUrl] of changedData) {
            console.log(pieceName, pieceImgUrl, 'cool ig')
            
            const pieceElements = document.getElementsByClassName(`${key} ${pieceName}`)
            
            for (let piece of pieceElements) {
                piece.style.backgroundImage = `url(${pieceImgUrl})`
            }
    }   
    const pieces = document.getElementsByClassName(key)
}


"""