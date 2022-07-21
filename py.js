const MOVES = {
    "U": {
        "o": [0, 0, 0, 0],
        "p1": [0, 1, 2],
        "p2": [1, 2, 0],
        "c": 0
    },
    "R": {
        "o": [4, 1, 1, 1],
        "p1": [1, 3, 4],
        "p2": [3, 4, 1],
        "c": 1
    },
    "L": {
        "o": [3, 1, 0, 1],
        "p1": [0, 5, 3],
        "p2": [5, 3, 0],
        "c": 2
    },
    "B": {
        "o": [5, 1, 2, 1],
        "p1": [2, 4, 5],
        "p2": [4, 5, 2],
        "c": 3
    }
};

const SOLVED_VS = [
    {
        "centers": [0, 1, 2],
        "edges": [[0, 1], [0, 3], [1, 3]],
    },
    {
        "centers": [0, 1, 3],
        "edges": [[1, 2], [1, 4], [2, 4]],
    },
    {
        "centers": [0, 2, 3],
        "edges": [[0, 2], [0, 5], [2, 5]],
    },
    {
        "centers": [1, 2, 3],
        "edges": [[3, 4], [3, 5], [4, 5]],
    }
];

class Pyraminx {
    // Edges. UL RU LB FD RD LB. 'p' is permutation, 'o' is orientation.
    constructor() {
    this.e =  [
    {"p": 0, "o": 0},
    {"p": 1, "o": 0},
    {"p": 2, "o": 0},
    {"p": 3, "o": 0},
    {"p": 4, "o": 0},
    {"p": 5, "o": 0},
    ];
    // Centers. 0 solved, 1 CW, 2CCW
    this.c =  [0, 0, 0, 0];
    }
    changeOri(a) {
        this.e[a[0]].o = (this.e[a[0]].o + a[1]) % 2;
        this.e[a[2]].o = (this.e[a[2]].o + a[3]) % 2;
        return;
    }
    threeCycle(a, b) {
        [this.e[a[0]], this.e[a[1]], this.e[a[2]]] = 
        [this.e[b[0]], this.e[b[1]], this.e[b[2]]];
        return;
    }
    twistCenter(index) {
        this.c[index] = (this.c[index] + 1) % 3;
        return;
    }
    doMove(move) {
        if (move in MOVES) {
            move = MOVES[move]
            this.changeOri(move.o);
            this.threeCycle(move.p1, move.p2);
            this.twistCenter(move.c);
        }
        return;
    }
    applyMoves(moves) {
        for (let i = 0; i < moves.length; i++) {
            this.doMove(moves[i][0]);
            if (moves[i].length > 1) {
                // Lazy way of doing ccw turn by doing cw x 2
                this.doMove(moves[i][0]);
            }
        }
        return;
    }
    isSolvedEdge(index) {
        if (this.e[index].p === index && this.e[index].o === 0) {
            return true;
        } else {
            return false;
        }
    }
    isSolvedV() {
        if (this.c.filter(x => x !== 0).length > 1) {
            return false;
        }
        for (let i = 0; i < SOLVED_VS.length; i++) {
            let v = SOLVED_VS[i];
            let vc = v['centers'];
            if ((this.c[vc[0]] + this.c[vc[1]] + this.c[vc[2]]) == 0) {
                let ve = v['edges']
                for (let j = 0; j < ve.length; j++) {
                    if (this.isSolvedEdge(ve[j][0])
                    && this.isSolvedEdge(ve[j][1])) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
}

function genPossibleSolutions(n) {
    const moves = ["U", "U'", "R", "R'", "L", "L'", "B", "B'"]
    let s = moves.map(function (x) {return [x];});
    if (n === 1) {
        return s;
    }
    for (let z = 0; z < n - 1; z++) {
        for (let i = 0; i < s.length; i++) {
            temp = s[i].slice()
            for (let j = 0; j < moves.length; j++) {
                this_move = moves[j].charAt(0)
                last_move = temp[temp.length - 1].charAt(0)
                if (this_move != last_move) {
                    t = temp.slice();
                    t.push(moves[j]);
                    s[i].push(t);
                }
            }
            s[i].splice(0, temp.length);
        }
        s = s.flat();
    }
    return s;
}

function checkSolvedV(scramble, solution) {
    let py = new Pyraminx();
    py.applyMoves(scramble);
    py.applyMoves(solution);
    if (py.isSolvedV()) {
        return true
    }
    else {
        return false
    }
}

function solutionsForDepth(scramble, n) {
    let possible = genPossibleSolutions(n);
    let solutions = [];
    let solved = new Pyraminx();

    for (let i = 0; i < possible.length; i++) {
        if (checkSolvedV(scramble, possible[i])) {
            solutions.push(possible[i]);
        }
    }
    return solutions;
}

function genSolutions(scramble, n) {
    solutions = []
    for (let i = 0; i < n + 1; i++) {
        sol_i = solutionsForDepth(scramble, i);
        for (let j = 0; j < sol_i.length; j++) {
            solutions.push(sol_i[j]);
        }
    }
    return solutions;
}

function main(scramble, n) {
    scramble = scramble.split(' ');
    solutions = genSolutions(scramble, n);
    sln_strs = solutions.map(function(x) {return x.join(" ");});
    return sln_strs;
}
