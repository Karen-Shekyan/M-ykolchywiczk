//import { io } from "https://cdn.socket.io/4.4.1/socket.io.esm.min.js";
var socket = io();

uName = sessionStorage.getItem("uName");
rCode = sessionStorage.getItem("rCode");
waitList = sessionStorage.getItem("rooms");

console.log(uName,rCode)

// wait for the content of the window element to load, then performs the operations.
window.addEventListener("load", ()=>{
	resize(); // Resizes the canvas once the window loads
  resizeC();
  loadColors();

	ctx.fillStyle = "white";
  ctx.rect(0, 0, 750, 480);

	document.addEventListener("mousedown", startPainting);
  document.addEventListener("mousedown", sketch);
  document.addEventListener("mousedown", selectColor);
	document.addEventListener("mouseup", stopPainting);
	document.addEventListener("mousemove", sketch);
	window.addEventListener("resize", resize);
  window.addEventListener("resize", resizeC);
  window.addEventListener("resize", loadColors);

	socket.emit("reconnect", rCode);
	console.log(rCode);

  var waitListSplit = waitList.split(',');

  var playersHTML = "<tr><th>&nbsp;&nbsp;&nbsp;#&nbsp;&nbsp;&nbsp;&nbsp;</th><th>Player&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th></tr>";
  for (var i = 0; i < waitListSplit.length; i++) {
    playersHTML += "<tr> <td><center>" + (i + 1) + "</center></td><td>" + waitListSplit[i] + "</td></tr>";
  }
  document.getElementById("players").innerHTML = playersHTML;
});

const canvas = document.getElementById("draw");

const ctx = canvas.getContext("2d");

ctx.strokeStyle = "black";

function resize() {
// create a temporary canvas obj to cache the pixel data //
  let temp_cnvs = document.createElement('canvas');
  let temp_ctx = temp_cnvs.getContext('2d');
// set it to the new width & height and draw the current canvas data into it //
  temp_cnvs.width = ctx.canvas.width;
  temp_cnvs.height = ctx.canvas.height;
  temp_ctx.fillStyle = "white";  // the original canvas's background color
  temp_ctx.fillRect(0, 0, ctx.canvas.width, ctx.canvas.height);
  temp_ctx.drawImage(canvas, 0, 0);
// resize & clear the original canvas and copy back in the cached pixel data //
  ctx.canvas.width = 750;
  ctx.canvas.height = 480;
  ctx.drawImage(temp_cnvs, 0, 0);
}

// Stores the initial position of the cursor
let coord = {x:0 , y:0};

// trigger drawing
let paint = false;

// Updates the coordianates of the cursor when
// an event e is triggered to the coordinates where
// the said event is triggered.
function getPosition(event) {
  coord.x = event.clientX - canvas.offsetLeft;
  coord.y = event.clientY - canvas.offsetTop;
}

function startPainting(event) {
  paint = true;
  getPosition(event);
}

function stopPainting() {
  paint = false;
}

function sketch(event) {
  if (!paint) {
    return;
  }

  if (ctx.lineWidth != 20) {
    ctx.lineWidth = 5;
  }

  ctx.beginPath();

  ctx.lineCap = "round";

  ctx.moveTo(coord.x, coord.y);
  getPosition(event);
  ctx.lineTo(coord.x , coord.y);

  ctx.stroke();
}

///////////////////////////
// Over-engineering Zone //
///////////////////////////

const color = document.getElementById("colors");
const clr = color.getContext("2d");

let coordC = {x:0 , y:0};

function getPositionC(event) {
  coordC.x = event.clientX - color.offsetLeft;
  coordC.y = event.clientY - color.offsetTop;
}

function resizeC() {
  clr.canvas.width = window.innerWidth * 0.1;
  clr.canvas.height = window.innerHeight * 0.7;
}

const validColors = ["white", "", "red", "blue", "purple", "yellow", "grey", "black", "orange", "pink", "green", "cyan", "brown", "magenta"]

function loadColors() {
  const space = 0.013 * window.innerWidth;
  let j = 0;

  for (let i = 0; i < 7; i++) {
    clr.beginPath();
    clr.fillStyle = validColors[j];
    j++;
    clr.rect(space, i*0.043*window.innerWidth + space, 0.03 * window.innerWidth, 0.03 * window.innerWidth);
    clr.fill();
    clr.stroke();

    clr.beginPath();
    if (j == 1) {
      clr.fillStyle = "white"
    } else {
      clr.fillStyle = validColors[j];
    }
    j++;
    clr.rect(0.057 * window.innerWidth, i*0.043*window.innerWidth + space, 0.03 * window.innerWidth, 0.03 * window.innerWidth);
    clr.fill();
    clr.stroke();
  }
}

function selectColor(event) {
  getPositionC(event);
  const space = 0.013 * window.innerWidth;
  let j = 0;

  for (let i = 0; i < 7; i++) {
    if (coordC.x >= space && coordC.x <= space + 0.03 * window.innerWidth && coordC.y >= i*0.043*window.innerWidth + space && coordC.y <= i*0.043*window.innerWidth + space + 0.03 * window.innerWidth) {
      ctx.strokeStyle = validColors[j];

      if (j == 0) {
        ctx.lineWidth = 20;
      } else {
        ctx.lineWidth = 5;
      }

      break;
    }
    j++;

    if (coordC.x >= 0.057 * window.innerWidth && coordC.x <= 0.057 * window.innerWidth + 0.03 * window.innerWidth && coordC.y >= i*0.043*window.innerWidth + space && coordC.y <= i*0.043*window.innerWidth + space + 0.03 * window.innerWidth) {
      if (j == 1) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
      } else {
        ctx.strokeStyle = validColors[j];
        ctx.lineWidth = 5;
      }
      break;
    }
    j++
  }
}
// REMOVED METHOD HERE
