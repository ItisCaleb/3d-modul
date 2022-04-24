var canva = document.getElementById("maps");
var ctx = canva.getContext("2d");
var graph = [
    [-50, -50, -15],
    [50, -50, -15],
    [-50, 50, -15],
    [50, 50, -15],
    [-50, -50, 15],
    [50, -50, 15],
    [-50, 50, 15],
    [50, 50, 15],
    [-100, 0, 0],
    [100, 0, 0],
    [0, -100, 0],
    [0, 100, 0],
    [0, 0, -100],
    [0, 0, 100]
];
var line = [
    [1, 2],
    [0, 3],
    [0, 3],
    [1, 2],
    [6, 5],
    [4, 7],
    [4, 7],
    [6, 5],
    [9],
    [8],
    [11],
    [10],
    [13],
    [12],
];
var path_point = [
    [-10, -10, -15],
    [-10, -20, -15],
    [-20, -30, -15],
    [-20, -10, -15],
    [-20, -40, 15]
];
var path_line = [
    [1],
    [0, 2],
    [1, 4],
    [],
    [2]
];
var ori_graph = [];
var ori_path = [];
var look = [0, -1000, 0];
var move = 1;
var theta = 0;
var alpha = 0;
var show = [];
var path_show = [];
var mouse_last = [0, 0];

function getMousePos(canvas, evt) {
    var rect = canvas.getBoundingClientRect();
    return {
        x: evt.clientX - rect.left,
        y: evt.clientY - rect.top
    };
}

function angle_of_vision(point, watcher) {
    var vec = [point[0] - watcher[0], point[1] - watcher[1], point[2] - watcher[2]]
    var k = watcher[1] / vec[1] * -1;
    var ret = [0, 0, 0];
    // console.log(vec, " ", k, " ", ret)
    for (let i = 0; i < 3; i++) {
        ret[i] = watcher[i] + vec[i] * k;
    }
    //console.log(ret);
    return ret;

}

function show_up() {
    for (let i = 0; i < show.length; i++) {
        ctx.beginPath();
        ctx.arc(origin[0] + show[i][0], origin[1] + show[i][2], 1, 0, 2 * Math.PI);
        ctx.fillStyle = "#000000";
        ctx.fill();
        ctx.stroke();
    }
    for (let i = 0; i < line.length; i++) {
        for (let j = 0; j < line[i].length; j++) {
            ctx.beginPath();
            ctx.moveTo(origin[0] + show[i][0], origin[1] + show[i][2]);
            ctx.lineTo(origin[0] + show[line[i][j]][0], origin[1] + show[line[i][j]][2]);
            ctx.strokeStyle = "#000000";
            ctx.stroke();
        }

    }

    for (let i = 0; i < path_show.length; i++) {
        ctx.beginPath();
        ctx.arc(origin[0] + path_show[i][0], origin[1] + path_show[i][2], 1, 0, 2 * Math.PI);
        ctx.fillStyle = "#0000AA";
        ctx.fill();
        ctx.stroke();
    }
    for (let i = 0; i < path_line.length; i++) {
        for (let j = 0; j < path_line[i].length; j++) {
            ctx.beginPath();
            ctx.moveTo(origin[0] + path_show[i][0], origin[1] + path_show[i][2]);
            ctx.lineTo(origin[0] + path_show[path_line[i][j]][0], origin[1] + path_show[path_line[i][j]][2]);
            ctx.strokeStyle = "#AA0000";
            ctx.stroke();
        }

    }
}
var origin = [540, 360]
for (let i = 0; i < graph.length; i++) {
    // console.log(graph[i])
    show.push(angle_of_vision(graph[i], look));
    ori_graph.push(graph[i]);
}
for (let i = 0; i < path_point.length; i++) {
    path_show.push(angle_of_vision(path_point[i], look));
    ori_path.push(path_point[i]);
}

show_up();

var delta_x = 0,
    delta_y = 0;
var press = 0;

function Update() {
    ctx.clearRect(0, 0, 1080, 720);
    theta = (delta_x * -1) * Math.PI / 120
    alpha = (delta_y * -1) * Math.PI / 240
    var x = 0,
        y = 0,
        z = 0;
    for (let i = 0; i < graph.length; i++) {
        x = graph[i][0]
        y = graph[i][1]
        z = graph[i][2]
        x = Math.cos(theta) * graph[i][0] - Math.sin(theta) * graph[i][1]
        y = Math.sin(theta) * graph[i][0] + Math.cos(theta) * graph[i][1]
        graph[i] = [x, y, z]
        y = Math.cos(alpha) * graph[i][1] - Math.sin(alpha) * graph[i][2]
        z = Math.sin(alpha) * graph[i][1] + Math.cos(alpha) * graph[i][2]
        graph[i] = [x, y, z]
        x *= move
        y *= move
        z *= move
        show[i] = angle_of_vision([x, y, z], look)
    }
    for (let i = 0; i < path_point.length; i++) {
        x = path_point[i][0]
        y = path_point[i][1]
        z = path_point[i][2]
        x = Math.cos(theta) * path_point[i][0] - Math.sin(theta) * path_point[i][1]
        y = Math.sin(theta) * path_point[i][0] + Math.cos(theta) * path_point[i][1]
        path_point[i] = [x, y, z]
        y = Math.cos(alpha) * path_point[i][1] - Math.sin(alpha) * path_point[i][2]
        z = Math.sin(alpha) * path_point[i][1] + Math.cos(alpha) * path_point[i][2]
        path_point[i] = [x, y, z]
        x *= move
        y *= move
        z *= move
        path_show[i] = angle_of_vision([x, y, z], look)
    }
    show_up();
    theta = 0;
    alpha = 0;
    delta_x = 0;
    delta_y = 0;
}

function reset() {
    move = 1;
    mouse_last = [0, 0];
    theta = 0;
    alpha = 0;
    delta_x = 0;
    delta_y = 0;
    graph = [];
    path_point = [];
    for (let i = 0; i < ori_graph.length; i++) {
        // console.log(graph[i])
        graph.push(ori_graph[i]);
    }
    for (let i = 0; i < ori_path.length; i++) {
        path_point.push(ori_path[i]);
    }
    Update();
}

function syncDelay(milliseconds) {
    var start = new Date().getTime();
    var end = 0;
    while ((end - start) < milliseconds) {
        end = new Date().getTime();
    }
}

function resize(evt) {
    evt.preventDefault();
    move += -0.001 * evt.deltaY;
    move = Math.min(10, move);
    move = Math.max(0, move);
    console.log("move", move);
    Update();
}

function draw(evt) {
    document.onmousedown = function(e) {
        press = 1;
    }
    if (press) {
        var mouse_now = [getMousePos(canva, evt).x, getMousePos(canva, evt).y];
        // console.log("x", mouse_now[0], mouse_last[0]);
        // console.log("y", mouse_now[1], mouse_last[1]);
        delta_x = mouse_now[0] - mouse_last[0];
        delta_y = mouse_now[1] - mouse_last[1];
        mouse_last = mouse_now;
        Update()
    } else {
        mouse_last = [getMousePos(canva, evt).x, getMousePos(canva, evt).y];
    }
    document.onmouseup = function(e) {
        press = 0;
    }
}

document.addEventListener('drag', draw)