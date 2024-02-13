menu = '<div class="dropdown-content"><a href="#">Link 1</a><a href="#">Link 2</a><a href="#">Link 3</a></div>'

add_signature = """
let signature = document.createElement('h1');
signature.textContent = "iyordanov";

linkContainer.appendChild(signature)
"""

dropdown_script = """
var dropdownContainer = document.createElement('div');

dropdownContainer.className = 'dropdown';

var dropdownButton = document.createElement('button');
dropdownButton.className = 'dropbtn';
dropdownButton.style.backgroundColor = 'transparent';
dropdownButton.style.color = '#d40000';
dropdownButton.style.padding = '16px';
dropdownButton.style.fontSize = '16px';
dropdownButton.style.border = 'none';
dropdownButton.style.width = 'none';
dropdownButton.textContent = 'Cheat menu';

var dropdownContent = document.createElement('div');
dropdownContent.className = 'dropdown-content';
dropdownContent.style.display = 'none';
dropdownContent.style.position = 'absolute';
dropdownContent.style.backgroundColor = 'transparent';
dropdownContent.style.minWidth = '160px';
dropdownContent.style.boxShadow = '0px 8px 16px 0px rgba(0,0,0,0.2)';
dropdownContent.style.zIndex = '1';
dropdownContent.style.width = '12vw';
dropdownContent.style.paddingTop = '1.5vh';
dropdownContent.style.paddingRight = '1vw';
dropdownContent.style.paddingBottom = '1.5vh';
dropdownContent.style.paddingLeft = '1vw';


var linkContainer = document.createElement('div');  // New div to wrap the links
linkContainer.style.display = 'flex';  // Set display to flex
linkContainer.style.flexDirection = 'column';  // Set flex direction to column

function createCheckboxWithLabel(text) {
    let label = document.createElement('label');

    let checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.style = "float: right; width: 1.5vw; height: 1.5vh; padding-bottom: 0.5vh;"

    let h1 = document.createElement('h1');
    h1.textContent = text;
    h1.style = "font-size: 20px; color: #c20000; float: left; padding-bottom: 0.5vh;"

    label.appendChild(checkbox);
    label.appendChild(h1);

    return label;
}

let checkbox1 = createCheckboxWithLabel("Auto move");
let checkbox2 = createCheckboxWithLabel("Suggestions");
let checkbox3 = createCheckboxWithLabel("Spammer");

linkContainer.appendChild(checkbox1);
linkContainer.appendChild(checkbox2);
linkContainer.appendChild(checkbox3);

dropdownContent.appendChild(linkContainer);

dropdownContainer.appendChild(dropdownButton);
dropdownContainer.appendChild(dropdownContent);


arguments[0].appendChild(dropdownContainer);

// Add event listeners for hover
let isShown = false;
dropdownButton.addEventListener('click', function() {
    if (isShown) {
        dropdownContent.style.display = 'none';
        isShown = false;
    } else {
        dropdownContent.style.display = 'block';
        isShown = true;
    }
        
});

dropdownContent.innerHTML = "<button id='okbtnxd'>ok</button>"
dropdownContent.id = "cheatMenuDropdown"
document.getElementById("okbtnxd").addEventListener("click", count);
function count() {
    console.log("NO FKING WAY!")
}
""" + add_signature
