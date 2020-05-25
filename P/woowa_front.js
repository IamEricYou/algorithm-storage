function solution(arr) {
    var answer = -1;
    var temp =  JSON.parse(JSON.stringify( arr ));
    var comp_array = new Array();

    var count = 1
    var comp_value = arr[0];
    var how_many = 0;

    while(true){
        if(temp[0] == 1 && temp.length == 1) {
            break;
        }

        comp_array = JSON.parse(JSON.stringify( temp ));
        temp = new Array();
        for(var i = 1; i <= comp_array.length; i++) {
            if(comp_value == comp_array[i]) {
                count += 1;
            } else {
                comp_value = comp_array[i]
                temp.push(count);
                count = 1
            }
        }
        comp_value = temp[0];
        console.log(temp);
        how_many += 1;
    }

    answer = how_many;
    return answer
}

function sortingword(arr) {
    var a = "hello";
    var b = a.split("").sort().join("");
    var c = a.sort();
    console.log(b);
    return 1;
}

function temp(id, money) {
    this.id = id;
    this.money = money;

    function getId() {
        return this.id;
    }
}

arr = [1, 1, 3, 3, 2, 2, 4, 5, 1, 1, 1, 3, 3, 3];
// arr = [2];
// console.log(solution(arr));
// console.log(sortingword("hi"));

var a = 1;
var b = Number(a);