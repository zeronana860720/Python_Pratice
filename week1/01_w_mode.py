# with open('test.txt','w', encoding='utf-8') as f:
#     pass
#     # pass：什麼都不做的佔位符
#     # Python 靠縮排決定區塊，區塊不能是空的（註解不算），所以要放 pass
#
#     # 實驗結果：'w' 在 open() 的瞬間就清空檔案，不用等 write()
#     # → 好習慣：先準備好資料，確定沒問題再 open(..., 'w')
#     # f.write('第二次')
# with open('test.txt','w',encoding='utf-8') as f:
#     # w:自動建立 清空後再寫
#     f.write('第一次')
with open('test.txt','a',encoding='utf-8') as f:
    # a:自動建立 接在最後面寫
    # 'a' 模式（append）：檔案不存在就自動建立，存在就接在最後面寫，不會清空舊內容
    # 跟 'w' 的差別：'w' 會清空，'a' 不會
    # 用途：記錄 log、新增資料
    f.write('第二次')

games = ['薩爾達傳說', '瑪利歐賽車', '寶可夢']
with open('test.txt','w',encoding='utf-8') as f:
    for game in games:
        f.write(f'{game}\n')

# join
# 練習1
# 要用什麼連接寫在前面
print(' | '.join(games))
# 練習2
print('-'.join(games))
prompt = '請推薦以下內容的作品:\n-'+'\n-'.join(games)
print(prompt)

# 練習3
scores = [90,85,77]
print('/'.join(str(scores)))
print('/'.join(str(s)for s in scores))

# 練習4
# 加編號
lines = '\n'.join(f'{i}. {g}'for i, g in enumerate(games,start=1))
print(lines)
prompt = f'我玩過的遊戲:\n{lines}'
print(prompt)

# join：分隔符號.join(list)，用分隔符號把字串黏起來
# 分隔符號只放「中間」，頭尾不會加
# list 裡只能放字串，數字要先 str(s) for s in ...
# str(整個list) 會變成一個字串，join 會把它拆成一個一個字元 → 錯
# 組 prompt 的常見寫法：'\n'.join(f'...' for ... in ...)

with open('test.txt','w',encoding='utf-8') as f:
    for g in games:
        print(g, file=f)
# print(..., file=f)：把 print 的輸出改寫到檔案裡
# 會自動換行（write 不會），也可以直接放數字

new_game = input('請輸入要增加的遊戲： ').strip()
with open('games.txt','r',encoding='utf-8') as f:
    games = f.read().splitlines()
if not new_game:
    print('沒有輸入遊戲名稱')
# elif new_game.strip()=='':
#     print('請輸入遊戲名稱')
# 在input端就strip()就可以少判斷一個
elif new_game.strip() in games:
    print('遊戲以存在')
else:
    with open('games.txt','a',encoding='utf-8') as f:
        print(new_game, file=f)
    print(f'已新增{new_game}')
    print('目前的遊戲清單:')
    with open('games.txt', 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, start=1):
            print(f'{i}. {line.strip()}')



