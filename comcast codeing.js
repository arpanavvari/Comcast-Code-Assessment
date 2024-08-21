function isCovered(ranges, left, right) {
    for (let i = left; i <= right; i++) {
        let covered = false;
        for (let [start, end] of ranges) {
            if (start <= i && i <= end) {
                covered = true;
                break;
            }
        }
        if (!covered) {
            return false;
        }
    }
    return true;
}

// Example 1
const ranges1 = [[1, 2], [3, 4], [5, 6]];
const left1 = 2;
const right1 = 5;
const output1 = isCovered(ranges1, left1, right1);
console.log(output1);  // Output: true

// Example 2
const ranges2 = [[1, 10], [10, 20]];
const left2 = 21;
const right2 = 21;
const output2 = isCovered(ranges2, left2, right2);
console.log(output2);  // Output: false
