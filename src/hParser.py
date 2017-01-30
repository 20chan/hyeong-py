import re

hearts = '♥❤💕💖💗💘💙💚💛💜💝♡'
kor = '형혀항핫하흣흡흑흐'


def is_korean(ch):
    return re.search('[가-힇]', ch) is not None


def parse(code):
    code = code.replace(' ', '')
    i = 0
    while i < len(code):
        tok, ch_len, dot_len, zone = None, 0, 0, None
        end = False
        # 한글 글자 해석
        if code[i] == '형':
            tok, ch_len = '형', 1
        elif code[i] == '혀':
            ch_len = 1
            while code[i] != '엉':
                if is_korean(code[i]):
                    ch_len += 1
                i += 1
            tok = '형'
        elif code[i] == '항':
            tok, ch_len = '항', 1
        elif code[i] == '핫':
            tok, ch_len = '핫', 1
        elif code[i] == '하':
            ch_len = 1
            while code[i] not in '앗앙':
                if is_korean(code[i]):
                    ch_len += 1
                i += 1
            if code[i] == '앗':
                tok = '핫'
            else:
                tok = '항'
        elif code[i] == '흣':
            tok, ch_len = '흣', 1
        elif code[i] == '흡':
            tok, ch_len = '흡', 1
        elif code[i] == '흑':
            tok, ch_len = '흑', 1
        elif code[i] == '흐':
            ch_len = 1
            while code[i] not in '읏읍윽':
                if is_korean(code[i]):
                    ch_len += 1
                i += 1
            if code[i] == '읏':
                tok = '흣'
            elif code[i] == '읍':
                tok = '흡'
            else:
                tok = '흑'
        i += 1
        # 말줄임표 해석
        if not end:
            while i < len(code):
                if code[i] in kor:
                    end = True
                    i -= 1
                    break
                if code[i] in hearts + '!?':
                    break
                if code[i] == '.':
                    dot_len += 1
                elif code[i] in '…⋯⋮':
                    dot_len += 3
                i += 1
        # 하트 구역 해석
        if not end:
            last = i
            while last < len(code) and code[last] not in kor:
                last += 1
            zone = ''.join([o for o in code[i:last] if o in hearts + '?!'])
            if len(zone) == 0:
                zone = None
            i = last
        i += 1
        yield tok, ch_len, dot_len, zone


if __name__ == '__main__':
    assert list(parse('흐...읍')) == [('흡', 2, 0, None)]
    assert list(parse('혀일이삼사오육앙앗읏읍엉')) == [('형', 12, 0, None)]
    assert list(parse('혀일....이삼사오육앙♥앗?!읏♡읍...엉')) == [('형', 12, 0, None)]
    assert list(parse('하흐읏앗앙')) == [('핫', 4, 0, None)]
    assert list(parse('하앗. … ⋯ ⋮')) == [('핫', 2, 10, None)]
    assert list(parse('혀읏......잠....하앙....혀엉. .....')) == [('형', 7, 6, None)]
    assert list(parse('하아앗.. . ? ♥ ! 💖')) == [('핫', 3, 3, '?♥!💖')]
    assert list(parse('혀엉...♥?!♡')) == [('형', 2, 3, '♥?!♡')]
