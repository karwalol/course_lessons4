#   сложность O(N*M) -> O(N**2)

#def strcounter(s):
#    print(set(s))           #set() - множество (структура данных с неупорядоченными уникальными значениями)
#    for sym in set(s):
#        count = 0
#        for sub_sym in s:
#            if sym == sub_sym:
#                count += 1
#        print(sym, '-', count)
#
#strcounter('aaabbcd')

def strcounter(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    for sym, count in syms_counter.items():
        print(sym, count)

strcounter('aaaaaaaabbbbbbbbccccccddddd')