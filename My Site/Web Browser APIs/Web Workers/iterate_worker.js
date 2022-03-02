var color = "blue";

function changeColor() {    
    color == "red" ? color = "blue" : color = "red";
    postMessage(color);
}
setInterval("changeColor()", 1000);