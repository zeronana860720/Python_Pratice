from collections import Counter

scores = {
    'Zelda': 92,
    'Mario Kart': 85,
    'Pokemon': 88
}
print(scores['Zelda'])
scores['Elden Ring'] = 97
scores['Mario Kart'] = 87

print(scores)
print(len(scores))

# dict：{key: value}，用 key 取值，像字典用單字查解釋
# d[key] = value：key 不存在就新增，存在就覆蓋
# d[不存在的key] → KeyError
# key 不能重複、必須是不可變的（字串、數字、tuple），list 不行
# dict 的格式跟 JSON 一樣，之後串 AI API 會一直用到

# 安全取值 -> get()

# in -> 判斷key 存不存在, 不檢查value

stock = {'Zelda': 3, 'Mario': 0, 'Pokemon': 5}
print(stock.get('Kirby',0))
if 'Mario' in stock:
    print(stock['Mario'])
    if stock['Mario'] == 0:
        stock.pop('Mario')
        print('已下架： Mario')

sales = ['Zelda', 'Pokemon', 'Zelda', 'Kirby', 'Zelda', 'Pokemon']
count = {}
for sale in sales:
    count[sale] = count.get(sale,0) +1

print(count)

# get(key)：找不到回傳 None；get(key, 預設值)：找不到回傳預設值，不會報錯
# in：只檢查 key，不檢查 value
# del d[key] / d.pop(key)：刪除，pop 會回傳 value，pop(key, None) 找不到不報錯
# 計數器模式：count[x] = count.get(x, 0) + 1


# 遍歷 keys()、values()、items()

scores = {'Zelda': 92, 'Mario Kart': 87, 'Pokemon': 88, 'Elden Ring': 97, 'Kirby': 79}
for game, score in scores.items():
    print(f'{game}: {score}')

sum_scores = sum(scores.values())
avg_scores = sum_scores/len(scores)
print(f'{avg_scores:.1f}')
high_scores = {game: score for game, score in scores.items() if score >= 90 }
print(high_scores)
highest_score = max(scores.values())
for game, score in scores.items():
    if score == highest_score:
        print(f'{game}: {score}')

# set : 不會有重複元素的容器

# 把 cliff_games 去重，印出 Cliff 有幾款不同的遊戲
# 找出兩個人都有的遊戲
# 找出 Kai 有、Cliff 沒有的遊戲（Cliff 可以跟 Kai 借～）
# 兩個人的遊戲合起來總共有幾款（不重複）？

cliff_games = ['Zelda', 'Mario', 'Pokemon', 'Zelda', 'Kirby']
kai_games = ['Mario', 'Elden Ring', 'Pokemon', 'Tetris']

cliff_unique = set(cliff_games)
kai_unique = set(kai_games)
print(len(cliff_unique))

print(kai_unique & cliff_unique)
print(kai_unique - cliff_unique)
print(len(cliff_unique | kai_unique))

# set：不會有重複元素的容器，沒有順序，不能用 [0] 取值
# 空的 set 要用 set()，{} 是空的 dict
# set(list)：去重
# set 和 dict 的 in 是 O(1)，超快；list 的 in 是 O(n)
# & 交集、| 聯集、- 差集

# 內建函式 Counter
platforms = ['Switch', 'PS5', 'Switch', 'PC', 'Switch', 'PS5', 'PC', 'Switch', 'Xbox']
review = 'good fun good graphics bad price good story fun'
# 用 Counter 統計 platforms，印出結果
# 印出最多人使用的前 2 名平台
# 印出 'Mobile' 的數量（不能報錯）
# 統計 review 裡每個單字出現幾次，印出最常出現的單字
# （提示：要先把句子切成單字，前天學過的～）

count = Counter(platforms)
print(count)
print(count.most_common(2))
print(count['Mobile'])
clean_review = review.split()
print(clean_review)
count_review = Counter(clean_review)
print(count_review)
word ,count = count_review.most_common(1)[0]
print(f'{word}: {count}')

# from collections import Counter：從標準函式庫拿出 Counter
# Counter(list)：一行統計每個元素出現幾次，結果是一個 dict
# 取不存在的 key 回傳 0，不會報錯
# most_common(n)：前 n 名，回傳 [(元素, 次數), ...]
# word, times = c.most_common(1)[0]：拿出第一名

# practice
prices = {}
platforms = []
with open('game_prices.txt','r',encoding='utf-8') as f:
    for line in f :
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        name, rest = line.split(',',maxsplit=1)
        price, platform = rest.rsplit(',',maxsplit=1)
        name = name.strip()
        price_int = int(price.strip().strip('¥').replace(',',''))
        platform = platform.strip().upper()
        prices[name] = price_int
        platforms.append(platform)

print(prices)
print(platforms)

count_games= Counter(platforms)
# print(count_games)
print('平台統計: ')
for platform, count in count_games.items():
    print(f'{platform}: {count} 款')

# 最貴的遊戲
highest_price = max(prices.values())
for game, price in prices.items():
    if price == highest_price:
        print(f'{game}: ¥{price:,}')

# 查找系統
# search_game = input('請輸入要查詢的遊戲:').strip()
# if search_game in prices.keys():
#     print(f'{search_game}: ¥{prices[search_game]:,}')
#     # 查了兩次
# else:
#     print(f'找不到{search_game}')

#   寫法二：只查找一次
# price = prices.get(search_game)
# if price is not None:
#     print(f'{search_game}：¥{price:,}')
# else:
#     print(f'找不到 {search_game}')\

# 不分大小寫
search_game = input('請輸入要查詢的遊戲：').strip()
found = False

for game, price in prices.items():
    if game.lower() == search_game.lower():
        print(f'{game}: ¥{price:,}')
        found = True
        break
if not found:
    print(f'找不到{search_game}')
