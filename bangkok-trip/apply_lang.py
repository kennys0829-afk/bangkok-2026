#!/usr/bin/env python3
"""
Apply language toggle to Bangkok trip app:
1. Add lang-btn to header in index.html
2. Add CSS for lang-btn to style.css
3. Add data-zh/data-en attributes to all Chinese text elements in index.html
4. Add JS toggleLang function to app.js
"""

import re

# ==================== 1. Update style.css ====================
with open('/home/user/workspace/bangkok-trip/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

lang_css = """.lang-btn {
  margin-left: auto;
  background: rgba(255,255,255,.15);
  border: 1px solid rgba(255,255,255,.3);
  color: #fff;
  font-size: 11px; font-weight: 600;
  padding: 4px 10px;
  border-radius: 20px;
  cursor: pointer;
  transition: background .15s;
  white-space: nowrap;
}
.lang-btn:hover { background: rgba(255,255,255,.25); }

"""

css = css.replace('/* ---- BOTTOM NAV ---- */', lang_css + '/* ---- BOTTOM NAV ---- */')

with open('/home/user/workspace/bangkok-trip/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("✅ style.css updated")


# ==================== 2 & 3. Update index.html ====================
with open('/home/user/workspace/bangkok-trip/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ---- Step 1: Add lang button after header-brand div ----
old_header_end = '''    </div>
  </header>
  <!-- COUNTDOWN -->'''

new_header_end = '''    </div>
    <button class="lang-btn" id="langBtn" onclick="toggleLang()">🌐 EN</button>
  </header>
  <!-- COUNTDOWN -->'''

html = html.replace(old_header_end, new_header_end, 1)

# ---- Step 2: Add data-zh/data-en to countdown labels ----
html = html.replace(
    '<span class="cd-label">距離出發還有</span>',
    '<span class="cd-label" data-zh="距離出發還有" data-en="Departing in">距離出發還有</span>'
)
html = html.replace(
    '<span class="cd-txt">天</span>',
    '<span class="cd-txt" data-zh="天" data-en="d">天</span>'
)
html = html.replace(
    '<span class="cd-txt">時</span>',
    '<span class="cd-txt" data-zh="時" data-en="h">時</span>'
)
html = html.replace(
    '<span class="cd-txt">分</span>',
    '<span class="cd-txt" data-zh="分" data-en="m">分</span>'
)
html = html.replace(
    '<span class="cd-txt">秒</span>',
    '<span class="cd-txt" data-zh="秒" data-en="s">秒</span>'
)

# ---- Step 3: Day filter pills ----
html = html.replace(
    '<button class="day-pill active" data-day="all">全部</button>',
    '<button class="day-pill active" data-day="all" data-zh="全部" data-en="All">全部</button>'
)

# ---- Step 4: Map hint ----
html = html.replace(
    '<p>點擊地圖標記<br/>查看地點詳情</p>',
    '<p data-zh="點擊地圖標記<br/>查看地點詳情" data-en="Tap a map marker<br/>to view details">點擊地圖標記<br/>查看地點詳情</p>'
)

# ---- Step 5: Day headers ----
# Day 1
html = html.replace(
    '<div class="day-header-title">抵達曼谷・Co Limited EMsphere・JODD FAIRS 夜市</div>',
    '<div class="day-header-title" data-zh="抵達曼谷・Co Limited EMsphere・JODD FAIRS 夜市" data-en="Arrival · Co Limited EMsphere · JODD FAIRS Night Market">抵達曼谷・Co Limited EMsphere・JODD FAIRS 夜市</div>'
)
html = html.replace(
    '<div class="day-hotel-badge">🏨 SKYVIEW Hotel（入住）</div>',
    '<div class="day-hotel-badge" data-zh="🏨 SKYVIEW Hotel（入住）" data-en="🏨 SKYVIEW Hotel (Check-in)">🏨 SKYVIEW Hotel（入住）</div>'
)
html = html.replace(
    '<div class="prep-notice">⚡ 整理上網卡／eSIM · 熟習酒店→BTS 路線</div>',
    '<div class="prep-notice" data-zh="⚡ 整理上網卡／eSIM · 熟習酒店→BTS 路線" data-en="⚡ Set up SIM/eSIM · Familiarise hotel→BTS route">⚡ 整理上網卡／eSIM · 熟習酒店→BTS 路線</div>'
)

# Day 2
html = html.replace(
    '<div class="day-header-title">建興酒家・Siam 行街・After You・Nature Thai Massage・The Ledger Room</div>',
    '<div class="day-header-title" data-zh="建興酒家・Siam 行街・After You・Nature Thai Massage・The Ledger Room" data-en="Somboon Seafood · Siam Shopping · After You · Nature Thai Massage · The Ledger Room">建興酒家・Siam 行街・After You・Nature Thai Massage・The Ledger Room</div>'
)
html = html.replace(
    '<div class="day-hotel-badge">🏨 SKYVIEW Hotel</div>',
    '<div class="day-hotel-badge" data-zh="🏨 SKYVIEW Hotel" data-en="🏨 SKYVIEW Hotel">🏨 SKYVIEW Hotel</div>'
)
html = html.replace(
    '<div class="prep-notice">⚡ 提前預約 建興酒家 · Nature Thai Massage · Vanilla Sky Rooftop Bar</div>',
    '<div class="prep-notice" data-zh="⚡ 提前預約 建興酒家 · Nature Thai Massage · Vanilla Sky Rooftop Bar" data-en="⚡ Pre-book: Somboon Seafood · Nature Thai Massage · Vanilla Sky Rooftop Bar">⚡ 提前預約 建興酒家 · Nature Thai Massage · Vanilla Sky Rooftop Bar</div>'
)

# Day 3
html = html.replace(
    '<div class="day-header-title">大皇宮・Wat Pho・Wat Arun・藍旗船・ICONSIAM・水舞</div>',
    '<div class="day-header-title" data-zh="大皇宮・Wat Pho・Wat Arun・藍旗船・ICONSIAM・水舞" data-en="Grand Palace · Wat Pho · Wat Arun · Blue Flag Boat · ICONSIAM · Water Show">大皇宮・Wat Pho・Wat Arun・藍旗船・ICONSIAM・水舞</div>'
)
html = html.replace(
    '<div class="prep-notice">⚡ 著長褲（廟宇規定）· 提前預約 Kub Kao Kub Pla</div>',
    '<div class="prep-notice" data-zh="⚡ 著長褲（廟宇規定）· 提前預約 Kub Kao Kub Pla" data-en="⚡ Wear long trousers (temple rules) · Pre-book Kub Kao Kub Pla">⚡ 著長褲（廟宇規定）· 提前預約 Kub Kao Kub Pla</div>'
)

# Day 4
html = html.replace(
    '<div class="day-header-title">Roast Brunch・Thonglor・Once Upon A Thai Spa・Asiatique</div>',
    '<div class="day-header-title" data-zh="Roast Brunch・Thonglor・Once Upon A Thai Spa・Asiatique" data-en="Roast Brunch · Thonglor · Once Upon A Thai Spa · Asiatique">Roast Brunch・Thonglor・Once Upon A Thai Spa・Asiatique</div>'
)
html = html.replace(
    '<div class="prep-notice">⚡ 預約 Once Upon A Thai Spa · 著易脫服裝 · 留意叫 Grab 去夜市</div>',
    '<div class="prep-notice" data-zh="⚡ 預約 Once Upon A Thai Spa · 著易脫服裝 · 留意叫 Grab 去夜市" data-en="⚡ Book Once Upon A Thai Spa · Wear easy-to-remove clothing · Plan Grab to night market">⚡ 預約 Once Upon A Thai Spa · 著易脫服裝 · 留意叫 Grab 去夜市</div>'
)

# Day 5
html = html.replace(
    '<div class="day-header-title">酒店早餐・Em 區最後 hea・分開出發回港澳</div>',
    '<div class="day-header-title" data-zh="酒店早餐・Em 區最後 hea・分開出發回港澳" data-en="Hotel Breakfast · Last stroll in Em District · Depart separately">酒店早餐・Em 區最後 hea・分開出發回港澳</div>'
)
html = html.replace(
    '<div class="day-hotel-badge">🏨 SKYVIEW Hotel（退房）</div>',
    '<div class="day-hotel-badge" data-zh="🏨 SKYVIEW Hotel（退房）" data-en="🏨 SKYVIEW Hotel (Check-out)">🏨 SKYVIEW Hotel（退房）</div>'
)
html = html.replace(
    '<div class="prep-notice">⚡ 檢查行李 · 用清泰銖 · 預留機場時間</div>',
    '<div class="prep-notice" data-zh="⚡ 檢查行李 · 用清泰銖 · 預留機場時間" data-en="⚡ Check luggage · Spend remaining THB · Allow extra airport time">⚡ 檢查行李 · 用清泰銖 · 預留機場時間</div>'
)

# ---- Step 6: Timeline card titles ----
card_titles = [
    ('抵達 SKYVIEW Hotel', 'Arrive at SKYVIEW Hotel'),
    ('榮泰米粉湯 Rung Rueang Pork Noodle 🍜（Phrom Phong）', 'Rung Rueang Pork Noodle 🍜 (Phrom Phong)'),
    ('EmQuartier / EMsphere + Pang Cha 🧊', 'EmQuartier / EMsphere + Pang Cha 🧊'),
    ('JODD FAIRS Ratchada 夜市 🌃', 'JODD FAIRS Ratchada Night Market 🌃'),
    ('ThaiThai Massage The Signature Sukhumvit 24 💆', 'ThaiThai Massage The Signature Sukhumvit 24 💆'),
    ('前往建興酒家', 'Getting to Somboon Seafood'),
    ('建興酒家 Somboon Seafood 🦀（Siam Square One 4F）', 'Somboon Seafood 🦀 (Siam Square One 4F)'),
    ('Siam Paragon → Siam Center → CentralWorld 🛍️', 'Siam Paragon → Siam Center → CentralWorld 🛍️'),
    ('After You 甜品 🍧', 'After You Dessert 🍧'),
    ('返酒店休息 → 步行往 Nature Thai Massage', 'Back to Hotel → Walk to Nature Thai Massage'),
    ('Nature Thai Massage S24 🧖 Aromatherapy Oil', 'Nature Thai Massage S24 🧖 Aromatherapy Oil'),
    ('Co Limited EMsphere 🦀 晚餐', 'Co Limited EMsphere 🦀 Dinner'),
    ('Vanilla Sky Rooftop Bar 🌅（SKYVIEW 35F · 最頂層）', 'Vanilla Sky Rooftop Bar 🌅 (SKYVIEW 35F · Rooftop)'),
    ('The Ledger Room 🥃（SKYVIEW 32F · Whisky &amp; Cigar Lounge）', 'The Ledger Room 🥃 (SKYVIEW 32F · Whisky &amp; Cigar Lounge)'),
    ('大皇宮 + 玉佛寺 Wat Phra Kaew 👑', 'Grand Palace + Wat Phra Kaew (Temple of the Emerald Buddha) 👑'),
    ('Tha Tien 區冷氣午餐（Home Cafe Tha Tien）❄️🍛', 'Air-conditioned Lunch in Tha Tien (Home Cafe Tha Tien) ❄️🍛'),
    ('Wat Arun 黎明寺 🌅', 'Wat Arun (Temple of Dawn) 🌅'),
    ('藍旗觀光船 → ICONSIAM 🚢', 'Blue Flag Boat → ICONSIAM 🚢'),
    ('Kub Kao Kub Pla 晚餐 🍽️（ICONSIAM 5F 河景）', 'Kub Kao Kub Pla Dinner 🍽️ (ICONSIAM 5F Riverside)'),
    ('🌊 ICONSIAM 水舞表演', '🌊 ICONSIAM Water &amp; Light Show'),
    ('回 SKYVIEW Hotel ＋ 超市掃貨 / 宵夜 🏨', 'Back to SKYVIEW Hotel + Supermarket / Late Night Snacks 🏨'),
    ('Roast Coffee &amp; Eatery Brunch ☕（theCOMMONS Thonglor）', 'Roast Coffee &amp; Eatery Brunch ☕ (theCOMMONS Thonglor)'),
    ('Roast Coffee & Eatery Brunch ☕（theCOMMONS Thonglor）', 'Roast Coffee & Eatery Brunch ☕ (theCOMMONS Thonglor)'),
    ('Thonglor 行街 · 文青 Cafe / 甜品', 'Exploring Thonglor · Indie Cafés &amp; Desserts'),
    ('Once Upon A Thai Spa – Phrom Phong 💆（首選）', 'Once Upon A Thai Spa – Phrom Phong 💆 (Top Pick)'),
    ('Asiatique The Riverfront 夜市 🎡', 'Asiatique The Riverfront Night Market 🎡'),
    ('景觀晚餐：河畔浪漫二選一 🍽️', 'Riverside Dinner: Choose One 🍽️'),
    ('返 SKYVIEW Hotel 🏨', 'Back to SKYVIEW Hotel 🏨'),
    ('SKYVIEW 酒店自助早餐', 'SKYVIEW Hotel Breakfast Buffet'),
    ('Checkout + 寄存行李', 'Checkout + Store Luggage'),
    ('✈️ 分開出發回港澳', '✈️ Departing Separately'),
]

for zh, en in card_titles:
    old = f'<div class="tl-card-title">{zh}</div>'
    new = f'<div class="tl-card-title" data-zh="{zh}" data-en="{en}">{zh}</div>'
    if old in html:
        html = html.replace(old, new, 1)
    else:
        print(f"  ⚠️ NOT FOUND: tl-card-title: {zh[:30]}")

# ---- Step 7: Card descriptions ----
card_descs = [
    (
        'Klook 接送車由 BKK 機場出發，車程約 30–45 分鐘。Check-in / 寄存行李。',
        'Klook airport transfer from BKK. Journey ~30–45 min. Check in / store luggage.'
    ),
    (
        '由 SKYVIEW 步行約 5 分鐘，Soi 26 內。米芝蓮必比登，主打豬肉 / 魚蛋粉，一人一碗，唔會太飽。<br>📌 Plan B：Co Limited EMsphere GM05（粉絲焗大河蝦），如當日精神 / 肚餓可代替，否則留肚畀 Pang Cha + 夜市。',
        '5-min walk from SKYVIEW, Soi 26. Michelin Bib Gourmand — pork noodles or fish ball noodles. One bowl each, light meal.<br>📌 Plan B: Co Limited EMsphere GM05 (Glass noodles with river prawn), if you\'re hungry or feeling adventurous — otherwise save room for Pang Cha and the night market.'
    ),
    (
        '行街吹冷氣。EMsphere G/F「Pang Cha」泰式奶茶剉冰（米芝蓮推薦），兩人 share 一碗。如已 check-in 可返房小睡補眠。',
        'Browse the air-conditioned malls. Try "Pang Cha" Thai milk tea shaved ice at EMsphere G/F (Michelin-recommended) — share one between two. If already checked in, feel free to nap first.'
    ),
    (
        '由酒店步行約 3–5 分鐘到店，做 60 或 90 分鐘足部按摩，放鬆一日疲勞。',
        '3–5 min walk from hotel. 60 or 90-min foot massage — the perfect end to day one.'
    ),
    (
        'SKYVIEW → 步行 3–5 分鐘到 BTS Phrom Phong（E5）→ 搭 Sukhumvit Line 往 National Stadium 方向至 Siam 站（CEN）→ 出 BTS 閘，按指示步行約 2–3 分鐘到 Siam Square One 4 樓',
        'Walk 3–5 min from SKYVIEW to BTS Phrom Phong (E5) → Take Sukhumvit Line towards National Stadium to Siam (CEN) → Exit BTS and walk ~2–3 min to Siam Square One 4/F'
    ),
    (
        '11:30 入座避開 12:00 peak。必點：咖喱炒蟹 + 蒜蓉大蝦 / 其他蝦料理 + 炒通菜 + 飲品。建議 TableCheck 提早預約。',
        'Arrive at 11:30 to beat the 12:00 peak. Must order: curry crab + garlic prawns + stir-fried morning glory + drinks. Book ahead via TableCheck.'
    ),
    (
        'Paragon 高級品牌、超市 → Siam Center 本地潮牌 → 天橋去 CentralWorld。',
        'Paragon for luxury brands &amp; supermarket → Siam Center for local streetwear → Skywalk to CentralWorld.'
    ),
    (
        'CentralWorld 或 Siam Paragon 分店，兩人 share Kakigori + 厚多士。',
        'At CentralWorld or Siam Paragon. Share one Kakigori shaved ice + thick toast between two.'
    ),
    (
        'BTS Siam → Phrom Phong（E5），返 SKYVIEW 沖涼休息一陣，再步行前往 Nature Thai Massage Sukhumvit 24（步行數分鐘）。',
        'BTS Siam → Phrom Phong (E5). Head back to SKYVIEW for a shower and rest, then walk a few minutes to Nature Thai Massage Sukhumvit 24.'
    ),
    (
        'EMsphere GM 樓層。必點：粉絲焗蟹（Pu Ob Woonsen）。由 Nature Thai 步行返酒店方向，天橋直達 EMsphere GM 層。',
        'Located on EMsphere GM floor. Must order: Glass Noodle Baked Crab (Pu Ob Woonsen). Walk back from Nature Thai towards the hotel — the skywalk leads directly to EMsphere GM level.'
    ),
    (
        '一齊喺酒店餐廳食，唔使太早起。',
        'Enjoy breakfast together at the hotel restaurant. No rush.'
    ),
    (
        'Check-out 並將行李寄存酒店 Concierge，之後分開出發。',
        'Check out and store luggage with the hotel concierge. Then head off separately.'
    ),
]

for zh, en in card_descs:
    old = f'<div class="tl-card-desc">{zh}</div>'
    new = f'<div class="tl-card-desc" data-zh="{zh}" data-en="{en}">{zh}</div>'
    if old in html:
        html = html.replace(old, new, 1)
    else:
        print(f"  ⚠️ NOT FOUND: tl-card-desc: {zh[:50]}")

# ---- Step 8: Tags ----
tag_replacements = [
    ('<span class="tag tag-transport">交通</span>', 'Transport'),
    ('<span class="tag tag-stay">住宿</span>', 'Accommodation'),
    ('<span class="tag tag-food">餐飲</span>', 'Dining'),
    ('<span class="tag tag-activity">活動</span>', 'Activity'),
]

for old_tag, en_text in tag_replacements:
    zh_text = old_tag.split('>')[1].split('<')[0]
    new_tag = old_tag.replace(f'>{zh_text}<', f' data-zh="{zh_text}" data-en="{en_text}">{zh_text}<')
    html = html.replace(old_tag, new_tag)

# ---- Step 9: Budget lines ----
budget_lines = [
    ('💰 兩人約 THB 300–400', '💰 ~THB 300–400 for 2'),
    ('💰 Pang Cha 約 THB 150–200', '💰 Pang Cha ~THB 150–200'),
    ('💰 晚餐兩人約 THB 400–700', '💰 Dinner ~THB 400–700 for 2'),
    ('💰 THB 300–600 / 人', '💰 THB 300–600 / person'),
    ('💰 兩人約 THB 1,200–1,800', '💰 ~THB 1,200–1,800 for 2'),
    ('💰 兩人約 THB 300–500', '💰 ~THB 300–500 for 2'),
    ('💰 約 THB 1,350–1,440 / 人（GoWabi）', '💰 ~THB 1,350–1,440 / person (GoWabi)'),
    ('💰 兩人約 THB 800–1,200', '💰 ~THB 800–1,200 for 2'),
    ('💰 兩人約 THB 400–700', '💰 ~THB 400–700 for 2'),
    ('💰 兩人約 THB 600–1,000', '💰 ~THB 600–1,000 for 2'),
    ('💰 門票約 THB 500 / 人', '💰 Admission ~THB 500 / person'),
    ('💰 兩人午餐約 THB 400–700', '💰 Lunch ~THB 400–700 for 2'),
    ('💰 門票約 THB 100–200 / 人', '💰 Admission ~THB 100–200 / person'),
    ('💰 兩人約 THB 1,600–2,000', '💰 ~THB 1,600–2,000 for 2'),
    ('💰 兩人約 THB 1,000–1,100 + 10% 服務費', '💰 ~THB 1,000–1,100 for 2 + 10% service charge'),
    ('💰 約 THB 1,700–1,900 / 人', '💰 ~THB 1,700–1,900 / person'),
    ('💰 Crystal Grill House 約 THB 1,800–2,500 / 兩人 · Siam Tea Room 套餐約 THB 1,190 / 散點 THB 1,200–1,800', '💰 Crystal Grill House ~THB 1,800–2,500 for 2 · Siam Tea Room set menu ~THB 1,190 / à la carte THB 1,200–1,800'),
]

for zh, en in budget_lines:
    old = f'<div class="tl-budget">{zh}</div>'
    new = f'<div class="tl-budget" data-zh="{zh}" data-en="{en}">{zh}</div>'
    count = html.count(old)
    if count > 0:
        html = html.replace(old, new, 1)
    else:
        print(f"  ⚠️ NOT FOUND: tl-budget: {zh[:50]}")

# ---- Step 10: Book links (WhatsApp/TableCheck etc.) ----
book_links_zh_en = [
    ('📅 WhatsApp 預約 →', '📅 Book via WhatsApp →'),
    ('📅 TableCheck 預訂 →', '📅 Book via TableCheck →'),
    ('📅 LINE 預訂 →', '📅 Book via LINE →'),
]

for zh, en in book_links_zh_en:
    # Replace in tl-book-link elements
    html = html.replace(
        f'>{zh}</a>',
        f' data-zh="{zh}" data-en="{en}">{zh}</a>'
    )

# ---- Step 11: Summary/detail buttons ----
# msg-template summary elements
summary_replacements = [
    ('🚗 機場接送', '🚗 Airport Transfer'),
    ('📋 預約範本', '📋 Booking Template'),
    ('📍 行程路線', '📍 Route Guide'),
    ('🚗 Grab 落車點', '🚗 Grab Drop-off Point'),
    ('🍽️ 附近午餐選擇', '🍽️ Nearby Lunch Options'),
    ('📌 搭船備註', '📌 Ferry Notes'),
    ('🚗 Grab 上車點', '🚗 Grab Pick-up Point'),
    ('💆 按摩選擇', '💆 Massage Option'),
    ('🚦 交通情況', '🚦 Traffic Check'),
    ('🛒 超市', '🛒 Supermarket'),
]

for zh, en in summary_replacements:
    old = f'<summary style="display:inline-flex;align-items:center;">{zh}</summary>'
    new = f'<summary style="display:inline-flex;align-items:center;" data-zh="{zh}" data-en="{en}">{zh}</summary>'
    if old in html:
        html = html.replace(old, new)
    else:
        # Try without inline style
        old2 = f'<summary>{zh}</summary>'
        new2 = f'<summary data-zh="{zh}" data-en="{en}">{zh}</summary>'
        if old2 in html:
            html = html.replace(old2, new2)
        else:
            print(f"  ⚠️ NOT FOUND: summary: {zh}")

# ---- Step 12: Copy buttons ----
html = html.replace(
    '>複製</button>',
    ' data-zh="複製" data-en="Copy">複製</button>'
)
# Also the confirmed copy state text stays in JS - handled separately

# ---- Step 13: Bottom nav ----
html = html.replace(
    '<span>地圖</span>',
    '<span data-zh="地圖" data-en="Map">地圖</span>'
)
html = html.replace(
    '<span>行程</span>',
    '<span data-zh="行程" data-en="Itinerary">行程</span>'
)
html = html.replace(
    '<span>預訂</span>',
    '<span data-zh="預訂" data-en="Bookings">預訂</span>'
)
html = html.replace(
    '<span>小貼士</span>',
    '<span data-zh="小貼士" data-en="Tips">小貼士</span>'
)

# ---- Step 14: Booking section headers ----
booking_headers = [
    ('🏨 酒店預訂', '🏨 Hotel'),
    ('🍽️ 餐廳預約', '🍽️ Restaurants'),
    ('💆 按摩預約', '💆 Massage'),
    ('🛕 景點門票', '🛕 Attractions'),
    ('💰 預算總覽（HKD 估算）', '💰 Budget Overview (HKD Estimate)'),
    ('📞 快速聯絡（預約用）', '📞 Quick Contacts (for Bookings)'),
]
for zh, en in booking_headers:
    old = f'<div class="booking-section-header">{zh}</div>'
    new = f'<div class="booking-section-header" data-zh="{zh}" data-en="{en}">{zh}</div>'
    if old in html:
        html = html.replace(old, new)
    else:
        print(f"  ⚠️ NOT FOUND: booking-section-header: {zh}")

# ---- Step 15: Booking items ----
booking_item_details = [
    ('7/20–7/24（4晚）· Sukhumvit Soi 24 · 含早餐', '7/20–7/24 (4 nights) · Sukhumvit Soi 24 · Breakfast included'),
    ('Day 2 · SKYVIEW 35F · 21:00 · 2 人 · 出發前一星期預訂 · 備註要求 clear city view / panoramic seat', 'Day 2 · SKYVIEW 35F · 21:00 · 2 pax · Book 1 week ahead · Request clear city view / panoramic seat'),
    ('Day 2 · Siam Square One 4F · 午餐 11:30 · 2 人 · 出發前一星期預訂', 'Day 2 · Siam Square One 4F · Lunch 11:30 · 2 pax · Book 1 week ahead'),
    ('Day 3 · ICONSIAM 5F · 18:00–18:30 · 2 位 · 出發前一星期 LINE 預訂 · 備註要求河景 / 靠窗位', 'Day 3 · ICONSIAM 5F · 18:00–18:30 · 2 pax · Book 1 week ahead via LINE · Request river-view window seat'),
    ('Day 4 · Asiatique 河畔 · 晚餐 18:30 · 2 人 · 備註 Riverfront Table（戶外區）', 'Day 4 · Asiatique Riverside · Dinner 18:30 · 2 pax · Request Riverfront Table (outdoor)'),
    ('Day 4 · Asiatique 河畔 · 晚餐 18:30 · 2 人套餐', 'Day 4 · Asiatique Riverside · Dinner 18:30 · Set menu for 2'),
    ('Day 1 · 22:00 · 足部按摩 60–90 分 · 2 人', 'Day 1 · 22:00 · Foot massage 60–90 min · 2 pax'),
    ('Day 2 · 18:00 · Aroma Oil 90 分 · 2 人同房', 'Day 2 · 18:00 · Aroma Oil 90 min · Couple room'),
    ('Day 4 · 15:30 · Aroma Oil 90–120 分 · 2 人（首選）', 'Day 4 · 15:30 · Aroma Oil 90–120 min · 2 pax (Top Pick)'),
    ('Day 2 · 18:00 · Foot Massage with Fresh Herbal Ball · 60/90 分 · 2 人', 'Day 3 · 21:30 · Foot Massage with Fresh Herbal Ball · 60/90 min · 2 pax'),
    ('Day 3 · 現場購票 · 8:30–15:30', 'Day 3 · Buy on-site · 8:30–15:30'),
    ('Day 3 · 現場購票 · 開放至 18:30', 'Day 3 · Buy on-site · Open until 18:30'),
    ('Day 4 · 臨場決定 · 17:00–24:00', 'Day 4 · Decide on the night · 17:00–24:00'),
]

for zh, en in booking_item_details:
    old = f'<div class="booking-item-detail">{zh}</div>'
    new = f'<div class="booking-item-detail" data-zh="{zh}" data-en="{en}">{zh}</div>'
    if old in html:
        html = html.replace(old, new, 1)
    else:
        print(f"  ⚠️ NOT FOUND: booking-item-detail: {zh[:50]}")

# booking item prices
booking_prices = [
    ('兩人約 THB 400–700', '~THB 400–700 for 2'),
    ('約 THB 1,200–1,800 兩人', '~THB 1,200–1,800 for 2'),
    ('約 THB 1,600–2,000 兩人', '~THB 1,600–2,000 for 2'),
    ('散點約 THB 1,800–2,500 兩人', 'À la carte ~THB 1,800–2,500 for 2'),
    ('套餐折後約 THB 1,190 兩人', 'Set menu ~THB 1,190 for 2'),
    ('THB 300–600 / 人', 'THB 300–600 / person'),
    ('THB 1,350–1,440 / 人（GoWabi）', 'THB 1,350–1,440 / person (GoWabi)'),
    ('THB 1,700–1,900 / 人', 'THB 1,700–1,900 / person'),
    ('THB 800–1,100 / 人', 'THB 800–1,100 / person'),
]

for zh, en in booking_prices:
    old = f'<div class="booking-item-price">{zh}</div>'
    new = f'<div class="booking-item-price" data-zh="{zh}" data-en="{en}">{zh}</div>'
    if old in html:
        html = html.replace(old, new, 1)
    else:
        print(f"  ⚠️ NOT FOUND: booking-item-price: {zh[:50]}")

# booking status badges
booking_badges = [
    ('✅ 已選定', '✅ Selected'),
    ('⚠ 建議提早預訂', '⚠ Book early'),
    ('⚠ 建議預約', '⚠ Reservation recommended'),
    ('⚠ 預約指定河景位', '⚠ Reserve river-view seat'),
    ('⚠ 提前預約', '⚠ Book in advance'),
    ('⚠ 建議預訂', '⚠ Reservation recommended'),
    ('可當場訂', 'Walk-in / same-day ok'),
    ('現場即買', 'Buy on arrival'),
    ('可選', 'Optional'),
]

for zh, en in booking_badges:
    old = f'<div class="booking-status-badge'
    # Find specific badges - use text-based replacement
    for cls in ['status-selected', 'status-urgent', 'status-optional']:
        old_badge = f'<div class="booking-status-badge {cls}">{zh}</div>'
        new_badge = f'<div class="booking-status-badge {cls}" data-zh="{zh}" data-en="{en}">{zh}</div>'
        if old_badge in html:
            html = html.replace(old_badge, new_badge)

# booking names
booking_names_zh = [
    ('建興酒家 Somboon Seafood', 'Somboon Seafood'),
    ('Kub Kao Kub Pla（吃飯吃魚）', 'Kub Kao Kub Pla'),
    ('大皇宮 + 玉佛寺', 'Grand Palace + Wat Phra Kaew'),
    ('Wat Pho 臥佛寺', 'Wat Pho (Reclining Buddha)'),
    ('Asiatique Sky 摩天輪（可選）', 'Asiatique Sky Ferris Wheel (Optional)'),
]

for zh, en in booking_names_zh:
    old = f'<div class="booking-item-name">{zh}</div>'
    new = f'<div class="booking-item-name" data-zh="{zh}" data-en="{en}">{zh}</div>'
    if old in html:
        html = html.replace(old, new, 1)
    else:
        print(f"  ⚠️ NOT FOUND: booking-item-name: {zh}")

# booking notes (ul > li in hotel card)
booking_note_items = [
    ('頂層戶外泳池 + Mojjo Rooftop Bar / The Ledger Room', 'Rooftop pool + Mojjo Rooftop Bar / The Ledger Room'),
    ('近 BTS Phrom Phong（步行 3–5 分）', 'Near BTS Phrom Phong (3–5 min walk)'),
    ('旁邊 EmQuartier / EMsphere 商場', 'Next to EmQuartier / EMsphere mall'),
]

for zh, en in booking_note_items:
    old = f'<li>{zh}</li>'
    new = f'<li data-zh="{zh}" data-en="{en}">{zh}</li>'
    if old in html:
        html = html.replace(old, new, 1)
    else:
        print(f"  ⚠️ NOT FOUND: booking-note li: {zh}")

# booking detail (hotel detail)
html = html.replace(
    '<div class="booking-detail">7/20–7/24（4晚）· Sukhumvit Soi 24 · 含早餐</div>',
    '<div class="booking-detail" data-zh="7/20–7/24（4晚）· Sukhumvit Soi 24 · 含早餐" data-en="7/20–7/24 (4 nights) · Sukhumvit Soi 24 · Breakfast included">7/20–7/24（4晚）· Sukhumvit Soi 24 · 含早餐</div>'
)

# book-link texts
book_links = [
    ('TableCheck 預訂 →', 'TableCheck →'),
    ('TableCheck 預約 →', 'TableCheck →'),
    ('LINE @kubkaokubpla →', 'LINE @kubkaokubpla →'),
    ('Hungry Hub →', 'Hungry Hub →'),
    ('GoWabi →', 'GoWabi →'),
    ('LINE 預約 →', 'LINE →'),
    ('Klook 預購 →', 'Klook →'),
    ('WhatsApp 預約 →', 'WhatsApp →'),
]

for zh, en in book_links:
    old = f'<a class="book-link"'
    # more targeted - match the text
    pattern = f'>{zh}</a>'
    replacement = f' data-zh="{zh}" data-en="{en}">{zh}</a>'
    html = html.replace(pattern, replacement)

# ---- Step 16: Budget section ----
budget_labels = [
    ('你機票 HKG↔BKK', 'Your flight HKG↔BKK'),
    ('托運行李費', 'Checked baggage fee'),
    ('SKYVIEW Hotel（4晚）', 'SKYVIEW Hotel (4 nights)'),
    ('機場接送（Klook）', 'Airport transfer (Klook)'),
    ('按摩（4次）', 'Massage (4 sessions)'),
    ('餐飲（5天）', 'Dining (5 days)'),
    ('景點門票', 'Attraction tickets'),
    ('交通（Grab）', 'Transport (Grab)'),
    ('手信 / 雜費', 'Souvenirs / misc.'),
]

for zh, en in budget_labels:
    old = f'<div class="budget-label">{zh}</div>'
    new = f'<div class="budget-label" data-zh="{zh}" data-en="{en}">{zh}</div>'
    if old in html:
        html = html.replace(old, new, 1)
    else:
        print(f"  ⚠️ NOT FOUND: budget-label: {zh}")

budget_amounts = [
    ('HKD ~2,099 <span class="budget-note-inline">+托運</span>', 'HKD ~2,099 <span class="budget-note-inline" data-zh="+托運" data-en="+ baggage fee">+托運</span>'),
    ('HKD 4,600 <span class="budget-note-inline">已確認</span>', 'HKD 4,600 <span class="budget-note-inline" data-zh="已確認" data-en="Confirmed">已確認</span>'),
    ('<span class="budget-note-inline">單程</span>', '<span class="budget-note-inline" data-zh="單程" data-en="one way">單程</span>'),
]
for old, new in budget_amounts:
    if old in html:
        html = html.replace(old, new, 1)

# Budget section labels
budget_section_labels = [
    ('✈️ 機票 + 🏨 酒店', '✈️ Flights + 🏨 Hotel'),
    ('🍽️ 在地消費（兩人 THB → HKD）', '🍽️ Local expenses (2 pax THB → HKD)'),
]
for zh, en in budget_section_labels:
    old = f'<div class="budget-section-label">{zh}</div>'
    new = f'<div class="budget-section-label" data-zh="{zh}" data-en="{en}">{zh}</div>'
    if old in html:
        html = html.replace(old, new, 1)
    else:
        print(f"  ⚠️ NOT FOUND: budget-section-label: {zh}")

# Budget total
html = html.replace(
    '<div class="budget-total">合計估算：約 HKD 11,500 – 12,400<span class="budget-hkd">（你個人）</span></div>',
    '<div class="budget-total" data-zh="合計估算：約 HKD 11,500 – 12,400" data-en="Total estimate: ~HKD 11,500 – 12,400">合計估算：約 HKD 11,500 – 12,400<span class="budget-hkd" data-zh="（你個人）" data-en="(your share)">（你個人）</span></div>'
)

# Budget note
html = html.replace(
    '<p class="budget-note">* 機票 HKD 2,099（香港快運，未含托運）· 酒店 HKD 4,600 已確認 · 新增：Co Limited 晚餐 + 按摩改 4 次 + 機場接送 · THB 1 ≈ HKD 0.22</p>',
    '<p class="budget-note" data-zh="* 機票 HKD 2,099（香港快運，未含托運）· 酒店 HKD 4,600 已確認 · 新增：Co Limited 晚餐 + 按摩改 4 次 + 機場接送 · THB 1 ≈ HKD 0.22" data-en="* Flight HKD 2,099 (HK Express, excl. baggage) · Hotel HKD 4,600 confirmed · Added: Co Limited dinner + 4 massage sessions + airport transfer · THB 1 ≈ HKD 0.22">* 機票 HKD 2,099（香港快運，未含托運）· 酒店 HKD 4,600 已確認 · 新增：Co Limited 晚餐 + 按摩改 4 次 + 機場接送 · THB 1 ≈ HKD 0.22</p>'
)

# ---- Step 17: Quick contacts ----
wa_details = [
    ('LINE: @kubkaokubpla · 備註河景 / 靠窗位', 'LINE: @kubkaokubpla · Request river-view seat'),
    ('WhatsApp 預約 · Phrom Phong 分店', 'WhatsApp booking · Phrom Phong branch'),
    ('Hungry Hub / Klook 套餐預訂', 'Book via Hungry Hub / Klook'),
    ('WhatsApp +66 61 896 2459 · Day 2 18:00', 'WhatsApp +66 61 896 2459 · Day 2 18:00'),
]

for zh, en in wa_details:
    old = f'<div class="wa-detail">{zh}</div>'
    new = f'<div class="wa-detail" data-zh="{zh}" data-en="{en}">{zh}</div>'
    if old in html:
        html = html.replace(old, new, 1)
    else:
        print(f"  ⚠️ NOT FOUND: wa-detail: {zh}")

# ---- Step 18: Tips section headers ----
tip_headers = [
    ('🧳 行李清單（5日4夜）', '🧳 Packing List (5 Days 4 Nights)'),
    ('✈️ 入境 / 簽證', '✈️ Entry / Visa'),
    ('💵 換錢 &amp; 支付', '💵 Currency &amp; Payment'),
    ('🚇 BTS Rabbit Card', '🚇 BTS Rabbit Card'),
    ('🚇 交通貼士', '🚇 Transport Tips'),
    ('💆 按摩貼士', '💆 Massage Tips'),
    ('👗 廟宇著裝規定', '👗 Temple Dress Code'),
    ('☀️ 天氣 / 裝備', '☀️ Weather / Gear'),
    ('📱 必備 Apps', '📱 Essential Apps'),
    ('🆘 緊急聯絡', '🆘 Emergency Contacts'),
]

for zh, en in tip_headers:
    old = f'<span>{zh}</span><span class="tip-chevron">▼</span>'
    new = f'<span data-zh="{zh}" data-en="{en}">{zh}</span><span class="tip-chevron">▼</span>'
    if old in html:
        html = html.replace(old, new)
    else:
        print(f"  ⚠️ NOT FOUND: tip-header: {zh}")

# Also handle "💵 換錢 & 支付" without HTML entity
html = html.replace(
    '<span>💵 換錢 & 支付</span><span class="tip-chevron">▼</span>',
    '<span data-zh="💵 換錢 & 支付" data-en="💵 Currency &amp; Payment">💵 換錢 & 支付</span><span class="tip-chevron">▼</span>'
)

# ---- Step 19: Packing section labels ----
html = html.replace(
    '<div class="packing-label">🧳 23KG 托運行李</div>',
    '<div class="packing-label" data-zh="🧳 23KG 托運行李" data-en="🧳 23KG Checked Luggage">🧳 23KG 托運行李</div>'
)
html = html.replace(
    '<div class="packing-label">🎒 7KG 手提行李</div>',
    '<div class="packing-label" data-zh="🎒 7KG 手提行李" data-en="🎒 7KG Carry-on">🎒 7KG 手提行李</div>'
)

# Packing categories
packing_cats = [
    ('👕 衣物（約 2–3kg）', '👕 Clothing (~2–3kg)'),
    ('👟 鞋（約 1–1.5kg）', '👟 Shoes (~1–1.5kg)'),
    ('🧴 洗漱用品（約 0.5–1kg）', '🧴 Toiletries (~0.5–1kg)'),
    ('💻 電子設備（必帶）', '💻 Electronics (essentials)'),
    ('🪪 隨身物品（必帶）', '🪪 Personal Essentials (must-haves)'),
]

for zh, en in packing_cats:
    old = f'<span>{zh}</span><span>▶</span>'
    new = f'<span data-zh="{zh}" data-en="{en}">{zh}</span><span>▶</span>'
    if old in html:
        html = html.replace(old, new)
    else:
        print(f"  ⚠️ NOT FOUND: packing-cat: {zh}")

# Packing items (list items)
packing_items = [
    ('短袖 T-shirt × 4–5', 'Short-sleeve T-shirts × 4–5'),
    ('長褲 × 1–2（廟宇入場必備）', 'Long trousers × 1–2 (required for temples)'),
    ('短褲 × 2–3', 'Shorts × 2–3'),
    ('輕便外套 × 1（商場冷氣用）', 'Light jacket × 1 (for air-conditioned malls)'),
    ('泳褲 × 1', 'Swim shorts × 1'),
    ('內褲 × 5', 'Underwear × 5'),
    ('襪 × 3–5', 'Socks × 3–5'),
    ('速乾睡衣 × 1 套', 'Quick-dry pyjamas × 1 set'),
    ('舒適步行鞋 × 1', 'Comfortable walking shoes × 1'),
    ('拖鞋 / 涼鞋 × 1', 'Flip-flops / sandals × 1'),
    ('洗髮水 / 沐浴露（酒店有備，可不帶）', 'Shampoo / body wash (hotel provides, optional)'),
    ('洗面用品', 'Face wash'),
    ('防曬乳（面 / 身體 SPF50+，出門前打底）', 'Sunscreen (face + body SPF50+, apply before heading out)'),
    ('Biore Athlizm 防曬噴霧（補塗用，噴後用手推勻）', 'Biore Athlizm sunscreen spray (for top-ups, spread with hand after spraying)'),
    ('Nivea Men Dry 止汗 roll-on（出門前用）', 'Nivea Men Dry antiperspirant roll-on (apply before going out)'),
    ('電動鬚刨（⚠️ 放手提行李，勿托運）', 'Electric shaver (⚠️ Keep in hand luggage, do NOT check in)'),
    ('電話 + 充電器', 'Phone + charger'),
    ('行動電源（≤20000mAh）', 'Power bank (≤20000mAh)'),
    ('耳機', 'Earphones'),
    ('電動鬚刨（勿放托運）', 'Electric shaver (hand luggage only)'),
    ('萬用轉插 / 充電插頭', 'Universal adapter / charging plug'),
    ('護照（有效期 6 個月以上）', 'Passport (valid for 6+ months)'),
    ('銀包 / 信用卡 / 少量現金', 'Wallet / credit cards / some cash'),
    ('摺疊雨傘', 'Foldable umbrella'),
    ('AquaSeal 防水袋', 'AquaSeal waterproof bag'),
    ('薄外套', 'Light jacket'),
    ('紙巾 / 濕紙巾', 'Tissues / wet wipes'),
    ('常備藥物', 'Regular medication'),
]

for zh, en in packing_items:
    old = f'<li>{zh}</li>'
    new = f'<li data-zh="{zh}" data-en="{en}">{zh}</li>'
    if old in html:
        html = html.replace(old, new)
    else:
        print(f"  ⚠️ NOT FOUND: packing li: {zh}")

# Weight bars
html = html.replace(
    '<div class="pw-label">托運估算重量</div>',
    '<div class="pw-label" data-zh="托運估算重量" data-en="Estimated checked luggage weight">托運估算重量</div>'
)
html = html.replace(
    '<div class="pw-text">約 5–7kg / 23kg 上限</div>',
    '<div class="pw-text" data-zh="約 5–7kg / 23kg 上限" data-en="~5–7kg / 23kg limit">約 5–7kg / 23kg 上限</div>'
)
html = html.replace(
    '<div class="pw-label">手提估算重量</div>',
    '<div class="pw-label" data-zh="手提估算重量" data-en="Estimated carry-on weight">手提估算重量</div>'
)
html = html.replace(
    '<div class="pw-text">約 3–4kg / 7kg 上限</div>',
    '<div class="pw-text" data-zh="約 3–4kg / 7kg 上限" data-en="~3–4kg / 7kg limit">約 3–4kg / 7kg 上限</div>'
)

# ---- Step 20: Tips body content (list items) ----
tip_list_items = [
    # Entry / Visa
    ('香港特區護照（HKSAR）<strong>免簽入境</strong>，無需申請任何簽證', 'Hong Kong SAR passport holders enter <strong>visa-free</strong> — no visa required.'),
    ('最長可留 <strong>60 日</strong>，5 天旅程完全無問題', 'Maximum stay <strong>60 days</strong> — more than enough for a 5-day trip.'),
    ('護照有效期須由入境日起計 <strong>至少 6 個月</strong>', 'Passport must be valid for <strong>at least 6 months</strong> from entry date.'),
    ('建議隨身備有 <strong>回程機票截圖</strong>（移民官偶爾查問）', 'Keep a screenshot of your <strong>return flight</strong> — immigration officers occasionally ask.'),
    ('每人隨身帶備 <strong>THB 5,000</strong> 現金或可查閱資金證明（兩人 THB 10,000）', 'Carry <strong>THB 5,000</strong> cash per person (or proof of funds) — THB 10,000 for two.'),
    # Currency
    ('出發前香港先換約 <strong>THB 5,000</strong> 現金，用作門票、船票、夜市、小費等', 'Exchange around <strong>THB 5,000</strong> in Hong Kong before departure for admission tickets, ferry tickets, night markets and tips.'),
    ('市區補換首選綠色 <strong>SuperRich Thailand</strong>（Siam 區或 Terminal 21 Asok 分店），匯率比機場好；機場非必要唔換大額', 'In Bangkok, exchange at the green <strong>SuperRich Thailand</strong> (Siam area or Terminal 21 Asok branch) for better rates. Avoid large exchanges at the airport.'),
    ('餐廳、商場、按摩店大多接受<strong>信用卡（Visa / Mastercard）</strong>，盡量刷卡減少帶現金', 'Most restaurants, malls and massage shops accept <strong>credit cards (Visa/Mastercard)</strong>. Use cards where possible to minimise cash on hand.'),
    ('夜市（JODD FAIRS、Asiatique 小食攤）、寺廟門票需現金', 'Night markets (JODD FAIRS, Asiatique food stalls) and temple admission require cash.'),
    ('Grab 可預設信用卡付款，免找續', 'Grab can be set up with a credit card — no cash needed for rides.'),
    # BTS Rabbit Card
    ('在任何 BTS 站客服櫃位購買，<strong>外國人需出示護照</strong>登記', 'Buy at any BTS station service counter. <strong>Foreign visitors must show their passport.</strong>'),
    ('卡價約 <strong>THB 200</strong>（發卡費 THB 100 + 儲值 THB 100），發卡費不退', 'Card costs ~<strong>THB 200</strong> (THB 100 issuance fee + THB 100 stored value). Issuance fee is non-refundable.'),
    ('買卡時建議<strong>即時再增值 THB 300</strong>，共 THB 500 儲值，足夠整個行程使用', 'Top up an extra <strong>THB 300</strong> at purchase for a total of THB 500 stored value — enough for the whole trip.'),
    ('可 tap in / out，比逐程買票方便；之後按需要隨時增值', 'Tap in/out like an Octopus card. Top up anytime as needed.'),
    ('行程主要用途：<strong>Phrom Phong（E5）⇄ Siam（CEN）⇄ Asok（E4）</strong>', 'Main routes: <strong>Phrom Phong (E5) ⇄ Siam (CEN) ⇄ Asok (E4)</strong>'),
    ('退卡：完程去任何 BTS 客服退回餘額（THB 250 以下即時退，以上需等最多 15 日），<strong>發卡費不退</strong>', 'Refund: Visit any BTS service counter after your trip. Balances under THB 250 are refunded immediately; above THB 250 may take up to 15 days. <strong>Issuance fee is non-refundable.</strong>'),
    # Transport tips
    ('<strong>Grab</strong> 係曼谷最方便打車 App，出發前落咗佢', '<strong>Grab</strong> is Bangkok\'s most convenient ride-hailing app. Download it before you leave.'),
    ('<strong>BTS（空鐵）</strong>搭乘可買 Rabbit Card 或 Token（有找散計）', '<strong>BTS (Skytrain):</strong> use a Rabbit Card or buy a token at the machine.'),
    ('<strong>MRT</strong> 用 Token 買票，Sukhumvit 站可轉 BTS Asok', '<strong>MRT:</strong> buy tokens at the machine. Sukhumvit MRT connects to BTS Asok.'),
    ('酒店近 <strong>BTS Phrom Phong（E5）</strong>，步行 3–5 分鐘。建議經 <strong>EM District 商場</strong>入口上天橋層，可直接接駁 BTS Phrom Phong 同 EM 商場，毋需先行出馬路搵樓梯。', 'The hotel is 3–5 min walk from <strong>BTS Phrom Phong (E5)</strong>. Use the <strong>EM District mall</strong> entrance to reach the skywalk level — it connects directly to BTS Phrom Phong without going down to street level.'),
    ('去 Asiatique / ICONSIAM 晚上塞車，預多 30–45 分鐘緩衝', 'Heading to Asiatique / ICONSIAM in the evening? Allow 30–45 extra minutes for traffic.'),
    ('ICONSIAM 後備：BTS + Sathorn Pier 搭免費接駁船', 'ICONSIAM backup: BTS to Saphan Taksin + free shuttle boat from Sathorn Pier.'),
    # Massage tips
    ('GoWabi / Klook 預約比現場平，建議提前 1–2 日', 'Booking via GoWabi or Klook is cheaper than walk-in. Book 1–2 days ahead.'),
    ('唔鍾意大力：入店講 <strong>「Soft pressure please, no Thai massage」</strong>', 'Don\'t want it too firm: tell them <strong>"Soft pressure please, no Thai massage"</strong> when you arrive.'),
    ('Aroma Oil Massage 遠比泰式按摩舒服（唔痛）', 'Aroma Oil Massage is far more relaxing than traditional Thai massage — no pain.'),
    ('Two persons same room：跟店方 request，一般都可以', 'Couple room: just request it when booking — most places can accommodate.'),
    ('按摩後多飲水，幫助排毒放鬆', 'Drink plenty of water after your massage to help your body recover.'),
    # Temple dress code
    ('大皇宮、Wat Pho、Wat Arun <strong>全部強制著長褲</strong>', 'Grand Palace, Wat Pho and Wat Arun all <strong>strictly require long trousers.</strong>'),
    ('上身：有袖上衣（短袖 T-shirt ok），不可背心 / 吊帶 / 透視', 'Top: sleeved shirt (short sleeves ok). No tank tops, spaghetti straps or see-through.'),
    ('下身：長褲蓋過膝頭，不可短褲 / 破牛仔褲', 'Bottom: trousers covering the knee. No shorts or ripped jeans.'),
    ('入殿前要脫鞋，建議著容易脫鞋款式', 'Remove shoes before entering the hall. Wear slip-on friendly footwear.'),
    ('廟宇外有租借長裙服務（少少費用）', 'Sarong/wrap skirt rental is available outside the temples for a small fee.'),
    # Weather
    ('7 月係雨季，<strong>帶摺疊傘 / 輕便雨衣</strong>', 'July is rainy season — pack a <strong>foldable umbrella or lightweight rain jacket.</strong>'),
    ('氣溫約 28–35°C，高濕度，戶外易出汗', 'Temperature ~28–35°C with high humidity. Expect to sweat outdoors.'),
    ('商場冷氣猛，帶薄外套', 'Malls are heavily air-conditioned — bring a light jacket.'),
    ('必備防曬，廟宇景點日照強', 'Sunscreen is essential — temple sites are exposed to strong sun.'),
    ('帶行動電源，Grab + Google Maps 耗電', 'Bring a power bank — Grab and Google Maps drain your battery fast.'),
    # Apps
    ('<strong>Grab</strong> — 打車必備，預先設好信用卡', '<strong>Grab</strong> — essential for rides. Set up your credit card in advance.'),
    ('<strong>Google Maps</strong> — 導航 + 餐廳搜尋', '<strong>Google Maps</strong> — navigation and restaurant search.'),
    ('<strong>ThaiHand</strong> — 泰國按摩預約平台，200+ 按摩店，折扣高達 70%，可買 bulk voucher 更平，支援即時預約', '<strong>ThaiHand</strong> — Thai massage booking platform with 200+ spas. Discounts up to 70%, bulk vouchers available, supports instant booking.'),
    ('<strong>GoWabi</strong> — 按摩 / Spa 預約優惠', '<strong>GoWabi</strong> — massage and spa booking with deals.'),
    ('<strong>Klook</strong> — 景點票 + 活動', '<strong>Klook</strong> — attraction tickets and activities.'),
    ('<strong>Google Translate</strong> — 相機翻譯泰文', '<strong>Google Translate</strong> — camera translate for Thai text.'),
]

for zh, en in tip_list_items:
    old = f'<li>{zh}</li>'
    new = f'<li data-zh="{zh}" data-en="{en}">{zh}</li>'
    if old in html:
        html = html.replace(old, new, 1)
    else:
        print(f"  ⚠️ NOT FOUND: tip li: {zh[:60]}")

# TDAC highlight block
old_tdac = '''<div class="tdac-highlight">
              <strong>⚠️ TDAC 數碼入境卡（必填！）</strong><br/>
              2025年5月起所有外籍旅客入境泰國，均須於出發前 <strong>72 小時內</strong>填妥 Thailand Digital Arrival Card（TDAC），獲 QR code 後入境時出示。免費，不填有機會被拒入境。<br/>
              官方網站：<a href="https://www.thaievisa.go.th" target="_blank">thaievisa.go.th</a>
            </div>'''

new_tdac = '''<div class="tdac-highlight">
              <strong data-zh="⚠️ TDAC 數碼入境卡（必填！）" data-en="⚠️ TDAC Digital Arrival Card (MANDATORY!)">⚠️ TDAC 數碼入境卡（必填！）</strong><br/>
              <span data-zh="2025年5月起所有外籍旅客入境泰國，均須於出發前 72 小時內填妥 Thailand Digital Arrival Card（TDAC），獲 QR code 後入境時出示。免費，不填有機會被拒入境。" data-en="From May 2025, all foreign visitors must complete the Thailand Digital Arrival Card (TDAC) within 72 hours before arrival. You receive a QR code to show at immigration. Free to complete — failure to do so may result in denied entry.">2025年5月起所有外籍旅客入境泰國，均須於出發前 <strong>72 小時內</strong>填妥 Thailand Digital Arrival Card（TDAC），獲 QR code 後入境時出示。免費，不填有機會被拒入境。</span><br/>
              官方網站：<a href="https://www.thaievisa.go.th" target="_blank">thaievisa.go.th</a>
            </div>'''

if old_tdac in html:
    html = html.replace(old_tdac, new_tdac)
else:
    print("  ⚠️ NOT FOUND: TDAC highlight block")

# Emergency grid labels
html = html.replace(
    '<span class="em-label">泰國緊急（警察）</span>',
    '<span class="em-label" data-zh="泰國緊急（警察）" data-en="Thailand Emergency (Police)">泰國緊急（警察）</span>'
)
html = html.replace(
    '<span class="em-label">救護車</span>',
    '<span class="em-label" data-zh="救護車" data-en="Ambulance">救護車</span>'
)
html = html.replace(
    '<span class="em-label">旅遊警察</span>',
    '<span class="em-label" data-zh="旅遊警察" data-en="Tourist Police">旅遊警察</span>'
)
html = html.replace(
    '<span class="em-label">港人求助熱線</span>',
    '<span class="em-label" data-zh="港人求助熱線" data-en="HK Assistance Hotline">港人求助熱線</span>'
)

# Tips footer
html = html.replace(
    '<div class="tips-footer">平安順風 · ขอให้เดินทางปลอดภัย</div>',
    '<div class="tips-footer" data-zh="平安順風 · ขอให้เดินทางปลอดภัย" data-en="Safe travels · ขอให้เดินทางปลอดภัย">平安順風 · ขอให้เดินทางปลอดภัย</div>'
)

# Write back
with open('/home/user/workspace/bangkok-trip/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ index.html updated")


# ==================== 4. Update app.js ====================
with open('/home/user/workspace/bangkok-trip/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

lang_js = """
  // ---- LANGUAGE TOGGLE ----
  window._lang = 'zh';

  window.toggleLang = function() {
    window._lang = window._lang === 'zh' ? 'en' : 'zh';
    const btn = document.getElementById('langBtn');
    btn.textContent = window._lang === 'zh' ? '🌐 EN' : '🌐 中';

    // Translate all elements with data-zh / data-en
    document.querySelectorAll('[data-zh]').forEach(el => {
      const zh = el.dataset.zh;
      const en = el.dataset.en;
      if (!zh || !en) return;
      // For elements with child HTML (strong tags etc.), use innerHTML
      if (zh.includes('<') || en.includes('<')) {
        el.innerHTML = window._lang === 'en' ? en : zh;
      } else {
        el.textContent = window._lang === 'en' ? en : zh;
      }
    });

    // Update copy buttons back to correct language
    document.querySelectorAll('.copy-btn[data-zh]').forEach(btn => {
      // Copy buttons - only update if not in "copied" state
      if (btn.textContent !== '✓ Copied' && btn.textContent !== '✓ 已複製') {
        btn.textContent = window._lang === 'en' ? btn.dataset.en : btn.dataset.zh;
      }
    });

    // Update document lang
    document.documentElement.lang = window._lang === 'en' ? 'en' : 'zh-HK';

    // Update the countdown "done" message if visible
    const cdDone = document.querySelector('.cd-done');
    if (cdDone) {
      cdDone.textContent = window._lang === 'en' ? 'Time to go! ✈️ Have an amazing trip!' : '出發啦！✈️ 祈有個好旅程！';
    }

    // Update countdown unit labels that are currently live
    const unitMap = {zh: ['天','時','分','秒'], en: ['d','h','m','s']};
    const cdTxts = document.querySelectorAll('.cd-txt');
    const labels = unitMap[window._lang];
    cdTxts.forEach((el, i) => {
      if (labels[i]) el.textContent = labels[i];
    });
  };
"""

# Insert before the final closing });
# The app.js ends with:   const cdTimer = setInterval(updateCountdown, 1000);\n});
old_end = '  const cdTimer = setInterval(updateCountdown, 1000);\n});'
new_end = '  const cdTimer = setInterval(updateCountdown, 1000);\n' + lang_js + '\n});'

if old_end in js:
    js = js.replace(old_end, new_end)
    print("✅ app.js updated")
else:
    print("  ⚠️ Could not find insertion point in app.js")
    print("  Last 200 chars:", repr(js[-200:]))

with open('/home/user/workspace/bangkok-trip/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("\n🎉 All done!")
