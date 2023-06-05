// wait for the content of the window element to load, then performs the operations.
window.addEventListener('load', ()=>{

	resize(); // Resizes the canvas once the window loads
	document.addEventListener('mousedown', startPainting);
	document.addEventListener('mouseup', stopPainting);
	document.addEventListener('mousemove', sketch);
	window.addEventListener('resize', resize);
});

const canvas = document.querySelector('#canvas');

const ctx = canvas.getContext('2d');

function resize(){
  ctx.canvas.width = window.innerWidth - 50;
  ctx.canvas.height = window.innerHeight - 20;
}

// Stores the initial position of the cursor
let coord = {x:0 , y:0};

// trigger drawing
let paint = false;

// Updates the coordianates of the cursor when
// an event e is triggered to the coordinates where
// the said event is triggered.
function getPosition(event){
  coord.x = event.clientX - canvas.offsetLeft;
  coord.y = event.clientY - canvas.offsetTop;
}

function startPainting(event){
  paint = true;
  getPosition(event);
}
function stopPainting(){
  paint = false;
}

function sketch(event){
  if (!paint) return;
  ctx.beginPath();

  ctx.lineWidth = 5;
  ctx.lineCap = 'round';
  ctx.strokeStyle = 'green';

  ctx.moveTo(coord.x, coord.y);
  getPosition(event);
  ctx.lineTo(coord.x , coord.y);

  ctx.stroke();
}
