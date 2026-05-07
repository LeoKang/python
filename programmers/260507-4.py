function solution(numbers) {
    const Num_str = {
        one: 1,
        two: 2,
        three: 3,
        four: 4,
        five: 5,
        six: 6,
        seven: 7,
        eight: 8,
        nine: 9,
        zero: 0,
    };

    for (let word in Num_str) {
    numbers = numbers.replaceAll(word, Num_str[word]);
}

    return Number(numbers);
}

# 1. ------------------------------------------

arrstr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def solution(numbers):
    answer = numbers
    for i in arrstr:
        answer = answer.replace(i, str(arrstr.index(i)))
    return int(answer)

number1 = "onetwothreefourfivesixseveneightnine"
number2 = "onefourzerosixseven"
print(solution(number1))
print(solution(number2))