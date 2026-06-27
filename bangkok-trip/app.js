/* =============================================
   BANGKOK 2026 — App Logic
   ============================================= */

// ---- PLACE DATA ----
const places = {
  skyview: {
    name: 'SKYVIEW Hotel Bangkok',
    type: 'hotel',
    day: [1,2,3,4,5],
    lat: 13.7295, lng: 100.5690,
    tags: ['住宿'],
    desc: 'Em District · Sukhumvit Soi 24。頂層戶外泳池 + Mojjo Rooftop Bar。全程住宿，近 BTS Phrom Phong（步行 3–5 分）。',
    budget: '',
    gmaps: 'https://www.google.com/maps/search/?api=1&query=13.7295,100.5690'
  },
  rungrueang: {
    name: '榮泰米粉湯 Rung Rueang Pork Noodle',
    type: 'food',
    day: [1],
    lat: 13.728468, lng: 100.570639,
    tags: ['Day 1 · 午餐', '餐飲'],
    desc: 'EMsphere GM Floor GM05。必點：粉絲焍大河蝦、蟹肉粉絲煜。交通：由 SKYVIEW 步行經天橋至 EMsphere，小戀電梯到 GM 樓，尋 GM05 號舖。',
    budget: '💰 兩人約 THB 800–1,500',
    gmaps: 'https://www.google.com/maps/search/?api=1&query=13.728468,100.570639'
  },
  colimited: {
    name: 'Co Limited EMsphere',
    type: 'food',
    icon: '🦀',
    lat: 13.732227, lng: 100.566378,
    tags: ['Day 2 · 晚餐', '餐飲'],
    desc: 'EMsphere GM 樓層。必點：粉絲焗蟹（Pu Ob Woonsen）。',
    budget: '💰 兩人約 THB 800–1,200',
    gmaps: 'https://www.google.com/maps/search/?api=1&query=13.732227,100.566378'
  },
  emquartier: {
    name: 'EmQuartier / EMsphere',
    type: 'activity',
    day: [1,5],
    lat: 13.732209, lng: 100.566389,
    tags: ['購物', '活動'],
    desc: 'Phrom Phong 站旁。EmQuartier 高級品牌 + 超市；EMsphere G/F 有 Pang Cha 泰式奶茶剉冰（米芝蓮推薦）。',
    budget: '💰 Pang Cha 約 THB 150–200',
    gmaps: 'https://www.google.com/maps/search/?api=1&query=13.732209,100.566389'
  },
  joddfairs: {
    name: 'JODD FAIRS Ratchada 夜市',
    type: 'food',
    day: [1],
    lat: 13.767868, lng: 100.571212,
    tags: ['Day 1 · 晚餐', '夜市'],
    desc: 'MRT Thailand Cultural Centre（BL19）4 號出口，步行 3–5 分鐘。火山豬肋骨、烤海鮮、芒果糯米。17:00–01:00。',
    budget: '💰 兩人約 THB 400–700',
    gmaps: 'https://www.google.com/maps/search/?api=1&query=13.767868,100.571212'
  },
  thaithai: {
    name: 'ThaiThai Massage The Signature Sukhumvit 24',
    type: 'activity',
    day: [1],
    lat: 13.730061, lng: 100.569435,
    tags: ['Day 1 · 按摩', '活動'],
    desc: '步行 3–5 分鐘出酒店。60 或 90 分鐘足部按摩。',
    budget: '💰 THB 300–600 / 人',
    gmaps: 'https://www.google.com/maps/search/?api=1&query=13.730061,100.569435'
  },
  somboon: {
    name: '建興酒家 Somboon Seafood',
    type: 'food',
    day: [2],
    lat: 13.744340, lng: 100.534107,
    tags: ['Day 2 · 午餐', '餐飲'],
    desc: 'Siam Square One 4F。必點：咖喱炒蟹（已拆蟹肉版本）。11:30 入座避開 peak，可 KKday 預約。',
    budget: '💰 兩人約 THB 1,200–1,800',
    gmaps: 'https://www.google.com/maps/search/?api=1&query=13.744340,100.534107'
  },
  siam: {
    name: 'Siam Paragon / Siam Center / CentralWorld',
    type: 'activity',
    day: [2],
    lat: 13.746528, lng: 100.532833,
    tags: ['Day 2 · 下午', '購物'],
    desc: 'BTS Siam 站旁。Paragon 高級品牌 + 超市 → Siam Center 本地潮牌 → 天橋去 CentralWorld。',
    budget: '',
    gmaps: 'https://www.google.com/maps/search/?api=1&query=13.746528,100.532833'
  },
  afteryou: {
    name: 'After You 甜品',
    type: 'food',
    day: [2],
    lat: 13.7458, lng: 100.5332,
    tags: ['Day 2 · 甜品', '餐飲'],
    desc: 'CentralWorld 或 Siam Paragon 分店。Kakigori + 厚多士，兩人 share 1–2 款。',
    budget: '💰 兩人約 THB 300–500',
    gmaps: 'https://www.google.com/maps/search/?api=1&query=13.7458,100.5332'
  },
  lekmassage: {
    name: 'Nature Thai Massage S24',
    type: 'activity',
    day: [2],
    lat: 13.729904, lng: 100.569586,
    tags: ['Day 2 · 按摩', '活動'],
    desc: 'Sukhumvit Soi 24，距 SKYVIEW 步行數分鐘。環境新、有 Couple Room。KKday / Klook / GoWabi 預約，90 分 Aromatherapy Oil Massage，兩人同房。',
    budget: '💰 約 THB 1,400–1,800 / 人（GoWabi）',
    gmaps: 'https://www.google.com/maps/search/?api=1&query=13.729904,100.569586'
  },
  mojjo: {
    name: 'Mojjo Rooftop Bar',
    type: 'bar',
    day: [2],
    lat: 13.7293, lng: 100.5686,
    tags: ['Day 2 · 晚上', 'Bar'],
    desc: 'SKYVIEW Hotel 頂層。俯瞰 Sukhumvit 夜景，cocktail / mocktail + finger food 宵夜。Smart casual（Tee + 長褲 ok）。',
    budget: '💰 兩人約 THB 600–1,000',
    gmaps: 'https://www.google.com/maps/search/?api=1&query=13.7293,100.5686'
  },
  grandpalace: {
    name: '大皇宮 + 玉佛寺 Wat Phra Kaew',
    type: 'activity',
    day: [3],
    lat: 13.751675, lng: 100.493039,
    tags: ['Day 3 · 上午', '景點'],
    desc: '開放 8:30–15:30，現場購票。著長褲入場。先入玉佛寺（殿內禁拍照），再行皇宮庭院。',
    budget: '💰 THB 500 / 人',
    gmaps: 'https://www.google.com/maps/search/?api=1&query=13.751675,100.493039'
  },
  watpho: {
    name: 'Wat Pho 臥佛寺',
    type: 'activity',
    day: [3],
    lat: 13.7465, lng: 100.4930,
    tags: ['Day 3 · 中午', '景點'],
    desc: '由大皇宮步行約 10–15 分鐘。46 米長臥佛，入殿前除鞋。附近有泰菜小店可食午餐。',
    budget: '💰 門票 THB 200–300 / 人',
    gmaps: 'https://www.google.com/maps/search/?api=1&query=13.7465,100.4930'
  },
  watarun: {
    name: 'Wat Arun 黎明寺',
    type: 'activity',
    day: [3],
    lat: 13.7437, lng: 100.4888,
    tags: ['Day 3 · 下午', '景點'],
    desc: 'Tha Tien Pier 搭渡輪過河（THB 4–10），船程 2–3 分鐘。逛寺廟，可行上高台睇昭披耶河景。',
    budget: '',
    gmaps: 'https://www.google.com/maps/search/?api=1&query=13.7437,100.4888'
  },
  iconsiam: {
    name: 'ICONSIAM + SOOKSIAM 水上市場',
    type: 'activity',
    day: [3],
    lat: 13.7265, lng: 100.5099,
    tags: ['Day 3 · 傍晚', '景點 / 購物'],
    desc: 'Wat Arun Pier 搭藍旗觀光船（THB 30–60），約 20–30 分鐘到 ICONSIAM Pier。GF 有 SOOKSIAM 室內水上市場，各地泰式小食。20:00 水舞表演。',
    budget: '',
    gmaps: 'https://www.google.com/maps/search/?api=1&query=13.7265,100.5099'
  },
  kubkao: {
    name: 'Kub Kao Kub Pla（吃飯吃魚）',
    type: 'food',
    day: [3],
    lat: 13.7268, lng: 100.5102,
    tags: ['Day 3 · 晚餐', '餐飲'],
    desc: 'ICONSIAM 5F 河景泰菜。需提前 1–2 週預約靠窗位。推薦：咖喱蟹肉 / 綠咖喱、椰奶湯、芒果糯米 share。',
    budget: '💰 兩人約 THB 1,600–2,000',
    gmaps: 'https://www.google.com/maps/search/?api=1&query=13.7268,100.5102'
  },
  roast: {
    name: 'Roast Coffee & Eatery',
    type: 'food',
    day: [4],
    lat: 13.735221, lng: 100.582275,
    tags: ['Day 4 · Brunch', '餐飲'],
    desc: 'theCOMMONS Thonglor，BTS Thong Lo 步行。招牌：Iced Espresso Latte。必點 The Original Roast Breakfast + Pasta。',
    budget: '💰 兩人約 THB 1,000–1,100 + 10% 服務費',
    gmaps: 'https://www.google.com/maps/search/?api=1&query=13.735221,100.582275'
  },
  thonglor: {
    name: 'Thonglor 文青區 / theCOMMONS',
    type: 'activity',
    day: [4],
    lat: 13.7270, lng: 100.5815,
    tags: ['Day 4 · 下午', '購物'],
    desc: 'BTS Thong Lo 附近。文青 cafe、設計小店、潮牌，適合慢慢 hea 行。',
    budget: '',
    gmaps: 'https://www.google.com/maps/search/?api=1&query=13.7270,100.5815'
  },
  onceupon: {
    name: 'Once Upon A Thai Spa – Phrom Phong',
    type: 'activity',
    day: [4],
    lat: 13.728107, lng: 100.572015,
    tags: ['Day 4 · 按摩', '活動'],
    desc: 'BTS Phrom Phong 附近，步行 5 分鐘。Klook / GoWabi 預約，90–120 分鐘 Aroma Oil 套餐。後備：Let\'s Relax Sukhumvit 39。',
    budget: '💰 約 THB 1,700–1,900 / 人',
    gmaps: 'https://www.google.com/maps/search/?api=1&query=13.728107,100.572015'
  },
  asiatique: {
    name: 'Asiatique The Riverfront',
    type: 'activity',
    day: [4],
    lat: 13.7094, lng: 100.5038,
    tags: ['Day 4 · 夜市', '活動'],
    desc: 'Grab 約 20–30 分鐘。Warehouse 1–2（小食）、5–7（手信）、河畔步道。Asiatique Sky 摩天輪（臨場決定）。17:00–24:00。',
    budget: '💰 摩天輪 THB 450–550 / 人（可選）',
    gmaps: 'https://www.google.com/maps/search/?api=1&query=13.7094,100.5038'
  },
  siamtearoom: {
    name: 'The Siam Tea Room at Asiatique',
    type: 'food',
    day: [4],
    lat: 13.7088, lng: 100.5032,
    tags: ['Day 4 · 晚餐', '餐飲'],
    desc: 'Asiatique 河畔泰菜餐廳。Hungry Hub / Klook 有 2 人套餐折後約 THB 1,190。建議提前預訂。',
    budget: '💰 套餐約 THB 1,190 / 散點 THB 1,200–1,800（兩人）',
    gmaps: 'https://www.google.com/maps/search/?api=1&query=13.7088,100.5032'
  }
};

// ---- MAP INIT ----
let map, activeDay = 'all';
const markers = {};

function initMap() {
  // 以 SKYVIEW Hotel 為中心，zoom 15 即可見附近街道
  map = L.map('leaflet-map', { zoomControl: false }).setView([13.7295, 100.5690], 15);
  L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
    attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors © <a href="https://carto.com/attributions">CARTO</a>',
    subdomains: 'abcd', maxZoom: 20
  }).addTo(map);
  L.control.zoom({ position: 'bottomright' }).addTo(map);

  // ★ 處安標訵2 — SKYVIEW Hotel
  const hotelIcon = L.divIcon({
    className: '',
    html: `<div class="hotel-pulse-wrap">
             <div class="hotel-pulse-ring"></div>
             <div class="hotel-pulse-dot">🏨</div>
           </div>`,
    iconSize: [44, 44],
    iconAnchor: [22, 22]
  });
  L.marker([13.7295, 100.5690], { icon: hotelIcon, zIndexOffset: 1000 })
    .addTo(map)
    .bindTooltip('🏨 SKYVIEW Hotel • 你們住這裡', {
      permanent: true, direction: 'top', offset: [0, -22],
      className: 'hotel-label-tooltip'
    });

  Object.entries(places).forEach(([id, p]) => {
    // SKYVIEW 已由金色脈衝 marker 代表，跳過獨立 marker
    if (id === 'skyview') return;
    const icon = L.divIcon({
      html: `<div class="custom-marker marker-${p.type}">${markerEmoji(p.type)}</div>`,
      className: '', iconSize: [32,32], iconAnchor: [16,16]
    });
    const m = L.marker([p.lat, p.lng], { icon })
      .addTo(map)
      .bindTooltip(p.name, { permanent: false, direction: 'top', className: 'map-tooltip' })
      .on('click', () => showDetail(id));
    markers[id] = { marker: m, days: p.day };
  });
}

function markerEmoji(type) {
  return { hotel:'🏨', food:'🍽', activity:'🌿', bar:'🍹' }[type] || '📍';
}

function filterMarkers(day) {
  Object.entries(markers).forEach(([id, obj]) => {
    if (day === 'all' || obj.days.includes(parseInt(day))) {
      obj.marker.addTo(map);
    } else {
      obj.marker.remove();
    }
  });
}

function showDetail(id) {
  const p = places[id];
  if (!p) return;
  document.getElementById('mapDetailEmpty').style.display = 'none';
  document.getElementById('mapDetailContent').style.display = 'block';
  document.getElementById('detailName').textContent = p.name;
  document.getElementById('detailTags').innerHTML = p.tags.map(t => `<span class="tag tag-${tagClass(t)}">${t}</span>`).join('');
  document.getElementById('detailDesc').textContent = p.desc;
  document.getElementById('detailBudget').textContent = p.budget;
  const btn = document.getElementById('detailGmaps');
  btn.href = p.gmaps;
  map.panTo([p.lat, p.lng]);
  // Mobile: show floating panel
  if (window.innerWidth <= 600) showMobileDetail(p);
}

function tagClass(tag) {
  if (tag.includes('餐') || tag.includes('午') || tag.includes('晚') || tag.includes('甜') || tag.includes('Brunch')) return 'food';
  if (tag.includes('活') || tag.includes('按') || tag.includes('景') || tag.includes('Bar')) return 'activity';
  if (tag.includes('交') || tag.includes('交通')) return 'transport';
  if (tag.includes('住')) return 'stay';
  return 'activity';
}

// Mobile floating panel
let mobilePanel;
function showMobileDetail(p) {
  if (mobilePanel) mobilePanel.remove();
  mobilePanel = document.createElement('div');
  mobilePanel.className = 'mobile-map-detail';
  mobilePanel.innerHTML = `
    <button onclick="this.parentElement.remove()" style="position:absolute;top:8px;right:10px;font-size:18px;color:#888">✕</button>
    <div style="font-size:15px;font-weight:700;margin-bottom:6px;padding-right:24px">${p.name}</div>
    <div style="font-size:13px;color:#555;margin-bottom:8px">${p.desc}</div>
    ${p.budget ? `<div style="font-size:12px;font-weight:600;color:#c9963c;margin-bottom:8px">${p.budget}</div>` : ''}
    <a href="${p.gmaps}" target="_blank" style="display:inline-flex;align-items:center;gap:6px;font-size:13px;font-weight:700;background:#1a5c38;color:white;border-radius:8px;padding:8px 14px">📍 Google Maps</a>
  `;
  document.querySelector('.main-area').appendChild(mobilePanel);
}


// ---- DAY FILTER ----
function setDay(day) {
  activeDay = day;
  // Update pills
  document.querySelectorAll('.day-pill').forEach(p => {
    p.classList.toggle('active', p.dataset.day === day);
  });
  // Filter itinerary
  document.querySelectorAll('.day-block').forEach(b => {
    b.classList.toggle('hidden', day !== 'all' && b.dataset.day !== day);
  });
  // Filter map markers
  filterMarkers(day);
}

// ---- ITINERARY MAP BUTTON ----
function handleMapBtn(placeId) {
  switchPanel('map');
  setTimeout(() => {
    showDetail(placeId);
    const p = places[placeId];
    if (p) map.flyTo([p.lat, p.lng], 16);
  }, 150);
}

// ---- TIPS TOGGLE ----
function toggleTip(header) {
  const body = header.nextElementSibling;
  const isOpen = body.classList.toggle('open');
  header.classList.toggle('open', isOpen);
}

// ---- PACKING TOGGLE ----
function togglePack(el) {
  const items = el.nextElementSibling;
  if (items && items.classList.contains('packing-items')) {
    items.classList.toggle('open');
    const arrow = el.querySelector('span:last-child');
    if (arrow) arrow.textContent = items.classList.contains('open') ? '▼' : '▶';
  }
}

// ---- TAB NAVIGATION (updated) ----
function switchPanel(panelId) {
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.bnav-btn').forEach(b => b.classList.remove('active'));
  const panel = document.getElementById('panel-' + panelId);
  if (panel) panel.classList.add('active');
  document.querySelector(`.bnav-btn[data-panel="${panelId}"]`)?.classList.add('active');
  if (panelId === 'map') {
    // Force layout then invalidate so Leaflet fills the container
    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        if (map) map.invalidateSize(true);
      });
    });
  }
}

// ---- INIT ----
document.addEventListener('DOMContentLoaded', () => {
  // Init map AFTER a short delay so the panel has rendered dimensions
  setTimeout(() => {
    initMap();
  }, 80);

  // Bottom nav
  document.querySelectorAll('.bnav-btn').forEach(btn => {
    btn.addEventListener('click', () => switchPanel(btn.dataset.panel));
  });

  // Day pills
  document.querySelectorAll('.day-pill').forEach(pill => {
    pill.addEventListener('click', () => setDay(pill.dataset.day));
  });

  // Map detail close
  document.getElementById('mapDetailClose')?.addEventListener('click', () => {
    document.getElementById('mapDetailContent').style.display = 'none';
    document.getElementById('mapDetailEmpty').style.display = 'flex';
  });

  // Itinerary map buttons
  document.querySelectorAll('.tl-map-btn').forEach(btn => {
    btn.addEventListener('click', () => handleMapBtn(btn.dataset.placeId));
  });

  // Overview cards
  document.querySelectorAll('.overview-card[data-goto]').forEach(card => {
    card.addEventListener('click', () => {
      switchPanel('itinerary');
      setDay(card.dataset.goto.replace('day',''));
    });
  });

  // Quick nav buttons
  document.querySelectorAll('.quick-btn[data-tab]').forEach(btn => {
    btn.addEventListener('click', () => switchPanel(btn.dataset.tab));
  });

  // ---- COUNTDOWN ----
  const target = new Date('2026-07-20T07:25:00+08:00').getTime();
  const cdDays = document.getElementById('cdDays');
  const cdHours = document.getElementById('cdHours');
  const cdMins = document.getElementById('cdMins');
  const cdSecs = document.getElementById('cdSecs');
  const bar = document.getElementById('countdownBar');

  function pad(n) { return String(n).padStart(2, '0'); }

  function updateCountdown() {
    const diff = target - Date.now();
    if (diff <= 0) {
      bar.innerHTML = '<span class="cd-done">出發啦！✈️ 祈有個好旅程！</span>';
      clearInterval(cdTimer);
      return;
    }
    const d = Math.floor(diff / 86400000);
    const h = Math.floor((diff % 86400000) / 3600000);
    const m = Math.floor((diff % 3600000) / 60000);
    const s = Math.floor((diff % 60000) / 1000);
    cdDays.textContent = d;
    cdHours.textContent = pad(h);
    cdMins.textContent = pad(m);
    cdSecs.textContent = pad(s);
  }

  updateCountdown();
  const cdTimer = setInterval(updateCountdown, 1000);

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
      // header-title has inner <span> — use innerHTML
      if (el.classList.contains('header-title')) {
        el.innerHTML = window._lang === 'en'
          ? 'Bangkok Trip · <span style="font-weight:400;opacity:.85;font-size:16px;">กรุงเทพฯ</span>'
          : '曼谷旅遊 · <span style="font-weight:400;opacity:.85;font-size:16px;">กรุงเทพฯ</span>';
        return;
      }
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

});
