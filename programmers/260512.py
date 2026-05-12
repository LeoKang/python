#프로그래머스-코딩테스트연습-코딩테스트입문-모스부호(1)

def solution(letter):
    morse_sign = [".-","-...","-.-.","-..",".","..-.","--.","....",
    "..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...",
    "-","..-","...-",".--","-..-","-.--","--.."]

    answer = ''
    for code in letter.split():
        idx = morse_sign.index(code)
        answer += chr(ord('a') + idx)
        
    return answer

# 2. ------------------------------------

def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
    return ''.join(morse[i] for i in letter.split())


# 1. ------------------------------------
morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}

def solution(letter):
    answer = ''
    lst = letter.split()
    for i in lst:
        answer += morse.get(i)

    return answer

print(solution(".... . .-.. .-.. ---"))
print(solution(".--. -.-- - .... --- -."))



# def solution(letter):
#     answer = ''

#     inp = letter.split()
#     for i in inp:
#         answer += morse.get(i)

#     return answer

# print(solution(".... . .-.. .-.. ---"))
# print(solution(".--. -.-- - .... --- -."))