const fs = require('fs');

fs.open("./input.txt", "r", (err, fd) => {
    if (err) throw err;
    let input = fs.readFileSync(fd, "utf8");
    let lines = input.split("\n");
    let dimensions = lines.map(line => line.split("x").map(Number));
    let wrappingPaper = 0;
    let ribbon = 0;
    dimensions.forEach(dimensions => {
        let [l, w, h] = dimensions;
        let [a, b, c] = [l * w, w * h, h * l];
        let [d, e, f] = [l + w, w + h, h + l];
        wrappingPaper += 2 * a + 2 * b + 2 * c + Math.min(a, b, c);
        ribbon += 2*(Math.min(d, e, f)) + (l * w * h);
    }
    );
    console.log(wrappingPaper);
    console.log(ribbon);
    }
)
