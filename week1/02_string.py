# split
# split(分隔符號)：把字串切成 list，看到分隔符號就切一刀
# split() 不放參數：用任何空白切，連續空白當成一個，頭尾空白忽略
# split(' ') 會死板地每個空格都切 → 連續空格會產生空字串，要避免
data = '2026-11-24'
log = 'ERROR   2026-11-24   檔案找不到'
data_split = data.split('-')
log_split = log.split()
print(log_split[0])

# rsplit maxsplit
# split(maxsplit=n)：最多切 n 刀，得到 n+1 塊，後面的內容保持完整
# rsplit：從右邊切，搭配 maxsplit=1 + [-1] 可以拿最後一段（副檔名、網址最後一段）
# ' '.join(s.split())：整理空白的好用招式，頭尾和中間多餘的空白一次清乾淨
command = 'add 薩爾達傳說 曠野之息'
url = 'https://example.com/games/zelda'
user_input = '   寶可夢    朱   紫  '

action,game = command.split(' ',maxsplit=1)
url_part = url.rsplit('/',maxsplit=1)
print(url_part[-1])
clean_user_input = ' '.join(user_input.split())

print(clean_user_input)

# strip 家族
title = '===== 遊戲清單 ====='
filename = 'games_backup.txt'
price = '¥5,980'
title_clean = title.strip('= ')
print(repr(title_clean))
filename_clean = filename.removesuffix('.txt')
print(repr(filename_clean))
price_clean = (price.strip('¥')).replace(',','')
print(repr(price_clean))

# in,find,count
review = '這款遊戲很好玩！畫面很漂亮，音樂也很好聽，就是價格有點貴。'
email = 'cliff@example.com'
if '貴' in review:
    print('有提到價格')
print(review.count('很'))
# email_split = email.split([0:5])
# 完全錯誤 把split跟切片搞混了
user_name = email[:email.find('@')]
# user_name = email.split('@')[0]

# startwith endwith
logs = [
    'ERROR 檔案找不到',
    'INFO 程式啟動',
    'WARNING 記憶體不足',
    'ERROR 網路連線失敗',
    'INFO 程式結束',
]
files = ['report.pdf', 'notes.md', 'photo.jpg', 'readme.md', 'data.csv']

# 用 for + startswith，只印出 ERROR 開頭的 log
for log in logs:
    if log.startswith('ERROR'):
        print(log)
# 用 for + endswith，印出所有 .md 或 .pdf 檔案（用 tuple 一次判斷）

for file in files:
    if file.endswith(('.md','.pdf')):
        print(file)

# f-string 格式化
games = [('Zelda', 7980, 0.95), ('Mario Kart', 6578, 0.88), ('Pokemon', 5980, 0.912)]
#
print(f'{" Games List ":=^28}')
for name,price,comment in games:
    price_text = f'${price:,}'
    print(f'{name:<12}{price_text:>8}{comment:>7.1%}')
# f-string 格式化：{要顯示的東西:格式}，冒號一定要有
# .2f → 小數 2 位     , → 千分位     .1% → 百分比 1 位小數
# < 靠左  > 靠右  ^ 置中，後面接寬度：{name:<12}
# 補位字元放在對齊符號前面：{"標題":=^28}（補什麼 → 怎麼對齊 → 幾格）
# 可以組合：{rate:>7.1%}（對齊 → 寬度 → 小數和類型）
# f-string 裡面的字串要用另一種引號：f'{"文字"}'
# 要黏在一起的東西先組成字串，再拿去對齊
# 中文字佔兩格寬，對齊會跑掉

# practice
print(f'{"practice":=^34}')
print(f'{' Games Prices ':=^34}')
print(f'{"Name":<14}{"Platform":<10}{"Price":>10}')
count = 0
total = 0
with open('game_prices.txt','r',encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line.startswith('#'):
            continue
        elif line == '':
            continue
        # if not line or line.startswith('#'):
        #     continue -> 可以簡寫成這樣
        name, rest = line.split(',', maxsplit=1)
        price, platform = rest.rsplit(',', maxsplit=1)
        # 分兩次切
        name = name.strip()
        price = price.strip()
        platform = platform.strip()
        # print(repr(platform))
        price_int = int(price.strip('¥').replace(',',''))
        platform_upper = platform.upper()
        # print(repr(platform_upper))
        count += 1
        total += price_int
        price_formatted = f'¥{price_int:,}'
        print(f'{name:<14}{platform_upper:<10}{price_formatted:>10}')
print(f'{"-"*34}')# practice
print(f'{"practice":=^34}')
print(f'{' Games Prices ':=^34}')
print(f'{"Name":<14}{"Platform":<10}{"Price":>10}')
count = 0
total = 0
with open('game_prices.txt','r',encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line.startswith('#'):
            continue
        elif line == '':
            continue
        # if not line or line.startswith('#'):
        #     continue -> 可以簡寫成這樣
        name, rest = line.split(',', maxsplit=1)
        price, platform = rest.rsplit(',', maxsplit=1)
        # 分兩次切
        name = name.strip()
        price = price.strip()
        platform = platform.strip()
        # print(repr(platform))
        price_int = int(price.strip('¥').replace(',',''))
        platform_upper = platform.upper()
        # print(repr(platform_upper))
        count += 1
        total += price_int
        price_formatted = f'¥{price_int:,}'
        print(f'{name:<14}{platform_upper:<10}{price_formatted:>10}')
print(f'{"-"*34}')
# print('-' * 34) 就可以了
print(f'Total: {count} games, ¥{total:,}')
print(f'Total: {count} games, ¥{total:,}')