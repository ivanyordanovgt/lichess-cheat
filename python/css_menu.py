
css_menu = """

.cheatContainer {
    width: 30vw;
    margin: 0 auto;
    font-size: calc(.7vw + .7em);
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.cheatNavbar {
    background-color: rgb(94, 0, 0);
    overflow: hidden;
    padding-left: 4.2vw;
}

.cheatNavbar a {
    float: left;
    color: white;
    padding: 14px 16px;
    text-decoration: none;
}

.cheatNavbar a:hover {
    background-color: #ddd;
    color: black;
}

.content {
}

.hidden {
    display: none;
}

#cheatBorderRight {
    border-right: 2px solid indianred;

}

.cheatSubmenu {
    background-color: rgba(0, 0, 0, 0.932);
    color: white;
    height: 45vh;
}

.cheatSubmenu h2 {
    margin: 0;
    padding: 0;
    text-align: center;
    padding-top: 1vh;
    font-size: calc(.8vw + .8em);
    font-family:cursive;
    font-weight: 100;
    color: rgba(255, 255, 255, 0.842);
}

.cheatSubmenu p {
    margin: 0;
    margin-top: 0.4vh;
    width: 10vw;
}

.cheatSubmenu .options {
    margin-left: 2vw;
    margin-top: 1.5vh;
    float: left;
}

.cheatSubmenu .inputs {
    float: right;
    margin-right: 2vw;
    margin-top: 1.3vh;
}

.cheatSubmenu .inputs select {
    width: 8vw;
    font-size: calc(.4vw + .4em);
    margin-top: 1.2vh;
    background-color: black;
    color: rgba(255, 255, 255, 0.89);
    border: none;
    border: 1px solid rgba(255, 255, 255, 0.438);
    font-family: Arial, Helvetica, sans-serif;
    font-weight: 100;
}

.cheatSubmenu .inputs select option:hover {
    background-color: wheat;
}

option {
}

.cheatSubmenu #misc p{
    padding-top: .4vh
}

.cheatSubmenu #misc select {
    margin-top: 1.3vh;
}

#misc select {
    margin-top: 2vh;
}

.cheatSubmenu .squareColor {
    margin-left: 2vw;
    margin-top: 3vh;
}

.pieceSet img {
    width: 3vw;
    background-color: rgba(128, 128, 128, 0.466);
}

.pieceSet img:hover {
    background-color: rgba(177, 174, 174, 0.781);

}

.pieceSet {
    margin-left: 5vw;
    margin-top: 2vh;
}

.colorPicker input {
    background-color: black;
    color: white;
    border: 1px solid white;
    font-size: calc(.35em + .35vw);
}

.colorInputs {
    margin-left: 11.6vw;
    margin-top: 1vh;
}

.colorPicker input::placeholder {
    color: white;
}

.colorPicker label {
    font-size: calc(.4vw + .4em);
}

.changePiecePopup {
    width: 30vw; height: 30vh; margin-top: 15vh; margin-left: 10vw;background-color: rgb(0, 0, 0); position: absolute;
}

.changePiecePopup h1 {
    color: white;
    font-size: calc(.45em + .45vw);
    margin: 0;
    text-align: center;
    margin-top: 2vh;
}

.changePiecePopup .builtIn {
    margin-left: 2vw;
    float: left;
}

.changePiecePopup select {
    font-size: calc(.35vw + .35em);
}

.changePiecePopup .builtIn h1 {
    text-align: left;
}

.changePiecePopup .builtIn label {
    color: white;
    margin: 0;
    padding: 0;
    font-size: calc(.4em + .4vw);
}

.selectedPiece {
    font-size: calc(.4em + .4vw);
}

.selectedPiece {
    text-align: left;
}

.selectedPiece p {
    color: white;
    text-align: center;
    margin: 0;
    font-size: calc(.4em + .4vw);
}

.selectedPiece img {
    background-color: rgba(128, 128, 128, 0.466);
    margin-left: 7.7vw;
    margin-top: 1vh;
    width: 3vw;
}

.selectedPiece input {
    margin-left: 5.8vw;
    width: 7vw;
}

.selectedPiece label {
    color: white;
    text-align: center;
    margin-left: 8.5vw;
}

.selectedPiece button {
    margin-left: 19.6vw;
    margin-top: 1vh;
    font-size: calc(.4vw + .4em);
    background-color: black;
    color: white;
}

.builtIn select {
    width: 7vw;
}

.changePiecePopup button:hover {
}

.changePiecePopup #closeBtn {
    background-color: indianred;
    border: none;
    position: absolute;
    float: right;
    margin-left: 28.9vw;

}

.changePiecePopup #closeBtn:hover{
    background-color: rgb(235, 128, 128);
}

#botOptions p {

   padding-top: 1.8vh;
}

#miscOptions p {
    padding-top: 2vh; 

}

.options input {
    height: 0.5vh;
    padding-top: 1px;

}

canvas {
    transition: background-color 0.5s ease;
}


"""