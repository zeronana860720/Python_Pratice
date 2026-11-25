ranking = []
ranking.append('Zelda')
ranking.append('Mario')
ranking.insert(0,'Elden Ring')
ranking.extend(['Pokemon','Kirby'])
print(ranking)
print(len(ranking))

# append(x)：加在最後面，x 整個當成一個元素
# insert(i, x)：插在第 i 個位置，後面的往後擠
# extend(list)：把 list 裡的元素一個一個加進來
# append(list) 會變成 list 裡面有 list → 要加多個元素用 extend
# list 是可變的：方法會直接改原本的 list，回傳 None，不要寫 games = games.append(...)

ranking = ['Elden Ring', 'Zelda', 'Mario', 'Pokemon', 'Kirby']
last = ranking.pop()
print(f'已移除:{last}')
ranking.remove('Mario')
del ranking[0]
if 'Tetris' in ranking:
    ranking.remove('Tetris')
else:
    print('Tetris 不在排行榜內')
print(ranking)

scores = [95, 88, 76, 92, 85, 70, 99, 81]
text = 'Python AI Engineer'
print(scores[:3])
print(scores[-2:])
print(scores[::-1])
print(scores[::2])
text_part = text.split()[1]
print(text_part)
text_reverse = text[::-1]
print(text_reverse)

# 切片 [開始:結束:間隔]，不包含結束位置
# [:n] 前 n 個、[-n:] 最後 n 個、[:-1] 除了最後一個
# [::2] 每 2 個拿一個、[::-1] 反轉（字串也可以）
# [:] 複製一份新的 list
# 切片超出範圍不會報錯，索引超出會報錯

# .sort()
# 直接修改原本的list
# sorted() 回傳一個新的

scores = [85, 92, 76, 99, 88]
new_scores = sorted(scores)
print(new_scores)
print(scores)
# print(f'最高分{new_scores[-3:]}') -> 錯了 順序錯了
print(f'最高分{sorted(scores,reverse=True)[:3]}')
# 或是用原本的結果再反轉
# print(f'最高分{new_scores[-3:][::-1]}')
scores.sort(reverse=True)
print(scores)
print(scores.sort())
#  因為沒有回傳值-> none

players = ['Cliff', 'Kai', 'Ami', 'Ken']
scores = [88, 95, 72, 90]
for player,score in zip(players,scores):
    print(f'{player}: {score}')

for i,(player,score) in enumerate(zip(players,scores),start=1):
    print(f'{i}. {player} - {score}分')

players.pop()

for i,(player,score) in enumerate(zip(players,scores),start=1):
    print(f'{i}. {player} - {score}分')


# zip(a, b)：把兩個 list 同位置的元素配對成 tuple，像拉鍊
# for x, y in zip(a, b)：直接解包
# 長度不同時以最短的為準，多的會被默默丟掉（不會報錯）
# 要看內容要用 list(zip(...))
# 搭配 enumerate：for i, (x, y) in enumerate(zip(a, b))，裡面要加括號

# 今日份practice
games = ['Zelda', 'Mario Kart', 'Pokemon', 'Kirby', 'Tetris']
scores = [92, 85, 88, 79, 95]
games.append('Elden Ring')
scores.append(97)
kirby_index = games.index('Kirby')
del games[kirby_index]
del scores[kirby_index]
pairs = list(zip(scores,games))
#  分數要在前面才會排序
print(pairs)
ranking = sorted(pairs, reverse=True)
# 高到低所以要reverse
print(ranking)

print(f'{" Game Ranking TOP 3 ":=^28}')
top3 = ranking[:3]
for i,(score,game) in enumerate(top3,start=1):
    print(f'{i}. {game:<18}{score:>5}')
print('-'*28)
total = sum(scores)
avg = total / len(scores)
print(f'平均分數：{avg:.1f}')
