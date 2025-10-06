#모듈 임포트

#환경변수 선언
asset_name = "파이썬 리듬게임"
note0 = 0
note1 = 0
note2 = 0
note3 = 0
note4 = 0
note5 = 0


#각 노트의 판정선내 위치 유무 선언
# 0 : MISS, 1 : GOOD, 2 : GREAT, 3 : PERFECT, 4 : GREAT, 5 : GOOD

#isNote = 0(노트 없음), 1(일반노트), 2(크리티컬 노트) / ago_time = int
def note(isNote):
    if isNote == 0:
        return make_note(True, False, False)
    elif isNote == 1:
        return make_note(False, True, False)
    elif isNote == 2:
        return make_note(False, False, True)
    else:
        return make_note(False, False, False)

#모든 arg는 T/F로 입력받음
def make_note(no, common, crit):
    note_text = ""
    if no == True:
        return(note_text)
    elif common == True:
        note_text = "=========="
        return(note_text)
    elif crit == True:
        note_text = "**********"
        return(note_text)
    else:
        return("!!!!!!!!!!!!!!")
    
def idiot_cls():
    print("\n" * 100)

def draw_frame(y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16, y17, y18, y19, y20):
    idiot_cls()
    print(note(y20))
    print(note(y19))
    print(note(y18))
    print(note(y17))
    print(note(y16))
    print(note(y15))
    print(note(y14))
    print(note(y13))
    print(note(y12))
    print(note(y11))
    print(note(y10))
    print(note(y9))
    print(note(y8))
    print(note(y7))
    note5 = y7
    print(note(y6))
    note4 = y6
    print("..........")
    print(note(y5))
    note3 = y5
    print(note(y4))
    note2 = y4
    print(note(y3))
    note1 = y3
    print(note(y2))
    note0 = y2
    print(note(y1))

print(asset_name)
print("엔터키를 눌러 노트를 처리하실 수 있습니다.\n계속하려면 엔터키를 누르세요.")

def chebo_hudae_renhwa():
    draw_frame(0, 0, 1, 1, 1, 2, 0, 2, 1, 2, 0, 1, 2, 0, 1, 2, 2 ,2 ,1 ,1)

chebo_hudae_renhwa()