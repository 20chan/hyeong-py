hearts = '♥❤💕💖💗💘💙💚💛💜💝'


def parse(code):
    i = 0
    while i < len(code):
        tok, ch_len, dot_len = None, 0, 0
        end = False
        # 한글 글자 해석
        if code[i] == '형':
            tok, ch_len = '형', 1
        elif code[i] == '혀':
            ch_len = 1
            while code[i] != '엉':
                i, ch_len = i + 1, ch_len + 1
            tok = '형'
        elif code[i] == '항':
            tok, ch_len = '항', 1
        elif code[i] == '핫':
            tok, ch_len = '핫', 1
        elif code[i] == '하':
            ch_len = 1
            while code[i] not in '앗앙':
                i, ch_len = i + 1, ch_len + 1
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
                i, ch_len = i + 1, ch_len + 1
            if code[i] == '읏':
                tok = '흣'
            elif code[i] == '읍':
                tok = '흡'
            else:
                tok = '윽'
        i += 1
        # 말줄임표 해석
        if not end:
            while i < len(code):
                if code[i] in '형혀항핫하흣흡흑흐':
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
            pass
        i += 1
        yield tok, ch_len, dot_len

print(list(parse('혀어어엉.....하앗..흡흐아아읏')))
