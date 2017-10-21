
#Define students names and scores and passwords

s1 = ("Mary", 86, 'pyclass1');

s2 = ("Peter", 83, 'pyclass2');

s3 = ("John", 79, 'pyclass3');

s4 = ("James", 75, 'pyclass4');

s5 = ("Jane", 70, 'pyclass5');


#initialize students dictionary 
sDic = {};

#index
sDic["2016001"] = s1; #tuple # value값 #index #s[0], s[1], s[3] #value가 tuple이다
sDic["2016002"] = s2;
sDic["2016003"] = s3;
sDic["2016004"] = s4;
sDic["2016005"] = s5;

#password and score output
n = input("학번을 입력하세요:  \n");
if n in sDic:
    pw = input("비밀번호를 입력하세요: \n")
    if pw == sDic[n][2]:
        x=(sDic[n][1])
        if int(x) >= 90:
            print(sDic[n][0],'님의 성적은 A입니다')
        elif int(x) >= 80:
            print(sDic[n][0],'님의 성적은 B입니다')
        elif int(x) >= 70:
            print(sDic[n][0],'님의 성적은 C입니다')
        else:
            print(sDic[n][0],'님의 성적은 D입니다')
    else:
        print('비밀번호가 다릅니다')
else:
    print('존재하지 않는 학번입니다.')