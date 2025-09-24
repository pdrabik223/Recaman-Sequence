// This file is intentionally left blank.

const numbers = [
    0,
    1,
    3,
    6,
    2,
    7,
    13,
    20,
    12,
    21,
    11,
    22,
    10,
    23,
    9,
    24,
    8,
    25,
    43,
    62,
    42,
    63,
    41,
    18,
    42,
    17,
    43,
    16,
    44,
    15,
    45,
    14,
    46,
    79,
    113,
    78,
    114,
    77,
    39,
    78,
    38,
    79,
    37,
    80,
    36,
    81,
    35,
    82,
    34,
    83,
    33,
    84,
    32,
    85,
    31,
    86,
    30,
    87,
    29,
    88,
    28,
    89,
    27,
    90,
    26,
    91,
    157,
    224,
    156,
    225,
    155
]

window.addEventListener("load", (event) => {
    generate_drawing("80");
});
 
function generate_drawing(number_of_iterations) {

    var no_iterations = parseInt(number_of_iterations);

    const boundary = document.getElementById("canvas_bounder");
    const canvas = document.getElementById("main_canvas");

    const { width, height } = boundary.getBoundingClientRect();

    canvas.style.width = width
    canvas.style.height = height

    const ctx = canvas.getContext("2d");

    ctx.beginPath();
    ctx.moveTo(0, height);
    ctx.lineTo(width, 0);
    ctx.lineWidth = 1;
    ctx.lineCap = "round";
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(95, 45, 80, 0.0, 0.5 * Math.PI, true);
    //X POS; Y POS; RADIUS;     
    ctx.stroke();
}