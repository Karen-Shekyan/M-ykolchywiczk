// wait for the content of the window element to load, then performs the operations.
window.addEventListener("load", ()=>{

	resize(); // Resizes the canvas once the window loads
  resizeC();
  loadColors();
	document.addEventListener("mousedown", startPainting);
  document.addEventListener("mousedown", sketch);
  document.addEventListener("mousedown", selectColor);
	document.addEventListener("mouseup", stopPainting);
	document.addEventListener("mousemove", sketch);
	window.addEventListener("resize", resize);
  window.addEventListener("resize", resizeC);
  window.addEventListener("resize", loadColors);
});

const canvas = document.getElementById("draw");

const ctx = canvas.getContext("2d");

ctx.strokeStyle = "black";

function resize() {
  ctx.canvas.width = window.innerWidth * 0.5;
  ctx.canvas.height = window.innerHeight * 0.7;
};

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

  ctx.beginPath();

  ctx.lineWidth = 5;
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
      break;
    }
    j++;

    if (coordC.x >= 0.057 * window.innerWidth && coordC.x <= 0.057 * window.innerWidth + 0.03 * window.innerWidth && coordC.y >= i*0.043*window.innerWidth + space && coordC.y <= i*0.043*window.innerWidth + space + 0.03 * window.innerWidth) {
      ctx.strokeStyle = validColors[j];
      break;
    }
    j++
  }
}

const myImageData = ctx.getImageData(0, 0, ctx.canvas.width, ctx.canvas.height);
console.log(myImageData.data);
// ONE DIMENSIONAL LIST THAT IS width * height * 4 long
// redIndex, greenIndex, blueIndex, alphaIndex
