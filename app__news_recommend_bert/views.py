from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from django.views.decorators.csrf import csrf_exempt

from operator import itemgetter
import numpy as np
import app__api.views as api
global df
df = api.df

news_sim_martrix = np.load('app__news_recommend_bert/dataset/news_sim_martrix.npy')

item_id2idx={}
for id, i in df.newsId.items():
    item_id2idx[i] = id

def home(request):
    return render(request, "app__news_recommend_bert/home.html")

@csrf_exempt
def latestnews(request):

    return JsonResponse({'latest_news': [{'id': 4867633,
   'category': 'tw_stock_news',
   'title': '資本利得+匯兌利益加持 富邦金4月大賺145.05億元 前4月獲利創同期次高',
   'content': '富邦金控 (2881-TW) 今 (9) 日公布 2022 年 4 月自結稅後純益 145.05 億元，創下歷年 4 月的歷史新高，累計今年前 4 月稅後純益 609.82 億元，為歷年同期次高紀錄，每股稅後純益為 5.17 元，續居金控每股獲利王寶座。富邦金表示，若以子公司來看，富邦人壽單 4 月及前 4 月累計稅後純益均創下同期歷史新高；台北富邦銀行前 4 月累計稅後純益亦創下同期歷史新高，成為金控獲利亮眼大功臣。此外，截至 4 月 30 日，富邦金控已取得日盛金控 58.75% 股權，而富邦金控於前 4 月認列日盛金投資收益 5.3 億元。各子公司獲利部分，金雞母富邦人壽 4 月稅後純益為 123.64 億元，累計稅後純益為 487.27 億元。RBC 超過 300%，資本水準維持良好。富邦人壽表示，4 月份國際投資市場震盪加劇，台股當月指數終以下跌 6.22% 作收，富邦人壽因應風險環境持續實現獲利並汰弱留強。債市投資方面，4 月份利率持續走高，富邦人壽的策略採擴大資金部位，待利率上升時機增加配置，提高未來整體經常性收益。在升息趨勢下，美元表現強勢，4 月份美元兌台幣升值 3%，也讓富邦人壽的單月及累月匯兌損益與避險成本，持續大幅優於去年同期，4 月底外匯價格變動準備金餘額，亦自前月 190 億元上升至逾 250 億元。外界關注的俄債問題，富邦人壽指出，截至 4 月底俄羅斯主權債的美元票息獲償付，4 月份未新增相關預期信用損失，累計前 4 月共計提新台幣 22.6 億元，未來仍將持續追蹤戰事發展與未來付息狀況。惟依據 ESG 投資原則，將不再新增俄羅斯部位，且利用機會減碼部位的原則不變。保險本業部份，富邦人壽 4 月合併初年度保費收入 (First Year Premium) 達 136 億元，合併總保費收入 (Total Premium) 達 317 億元。富邦人壽台灣初年度保費業績預估排名業界第二，單 4 月初年度保費 105.4 億，較去年同期成長 10.2%，成長動能主要來自投資型商品較去年同期成長 85.4%，表現亮眼。另一子公司台北富邦銀行 4 月稅後純益 16.88 億元，累積稅後純益 82.14 億元，較去年同期成長 21%，獲利成長主要受惠資產規模提升，台美升息帶動利差擴大，累積利息淨收益年增 11%。不過，財管收益及金融市場操作收益表現較去年同期落後，反映資本市場震盪，金融交易評價波動及財管客戶投資趨於保守謹慎，銷量較同期減少，惟 AuM 仍穩健提升。北富銀的信用卡發卡動能穩定成長，累積前 4 月信用卡發卡年成長 38%，帶動有效卡數及簽帳金額持續成長。北富銀截至 4 月底逾放比率為 0.16%，備抵呆帳覆蓋率為 769%，維持良好資產品質。富邦產險 4 月稅後純益 2.91 億元，累計稅後純益 32.44 億元，較去年同期成長 23%，來自於優異的投資績效和穩健承保業務表現。單月簽單保費 45.70 億元，較去年同期成長 18.0%，不論個人保險或企業保險皆延續上個月成長動能而有「雙位數」成長表現，其中，又以工程險因積極參與綠能保險業務讓單月簽單保費大幅成長 153.2%，同時也大幅領先市場成長；累計前 4 月簽單保費收入 189.08 億元，成長 16.2%，簽單市佔率達 25.4%，較去年同期增加 1.1%，續居市場龍頭。富邦證券 4 月稅後純益 1.58 億元，累計稅後純益 9.23 億元，較去年同期減少，今年以來台股市場震盪走跌，4 月份加權指數續破今年新低至 16,219 點，影響金融部位獲利表現，台股日均值今年累計至 4 月 3,707 億元，較去年同期下降，影響現貨及財管收入較去年同期減少。\xa0',
   'link': 'https://news.cnyes.com/news/id/4867633?exp=a',
   'photo_link': 'https://cimg.cnyes.cool/prod/news/4867633/l/48d356ff055898dbe22e4db75dcdafd6.jpg'},
  {'id': 4867627,
   'category': 'tw_stock_news',
   'title': '外資主要賣超金控股 提款台積電近44億元',
   'content': '台股今 (9) 日再度呈現股匯雙殺破底格局，加權指數終場下跌 359.28 點，收全日最低點 16048.92 點，創去年 5 月下旬以來新低，三大法人合計賣超 265.62 億元，其中，外資續賣 211.48 億元，主要賣超金控股，若以金額來看，仍是台積電遭提款近 44 億元最多。三大法人今日合計賣超 265.62 億元，其中，外資賣超 211.48 億元，自營商賣超 59.21 億元，均為連 2 賣，投信買超 5.07 億元，為連 18 買。今日遭外資賣超前 10 大標的依序為國泰永續高股息 2.2 萬張、新光金近 2.2 萬張，中鋼 2 萬餘張、台新金 1.5 萬張，元大金、長榮航在 1.4 萬張上下，富邦金和緯創均超過 1 萬張，國產和佳世達在 9000 張上下。外資買超前 10 大標的則有臺企銀 2.2 萬張，中信金 1.1 萬張，京元電子、群創和合晶在 9000 張上下，元晶逾 7500 張，兆豐金和王道銀行均逾 4800 張，漢翔和中鴻也超過 3300 張。投信方面，買超前 10 大標的有永豐金逾 4000 張，開發金和仁寶在 3500 張上下，英業達逾 3000 張，金像電、遠東新、元大金、第一金和宏碁在 2000 張上下，台泥逾 1500 張。而投信賣超前 10 大標的則有臺企銀近 6000 張，中信金 5500 張，元晶近 4000 張，智原、創惟、世界均超過 2000 張，台肥、京元電子、新光鋼均超過 1000 張，啟碁 950 張。國泰證期研究部表示，美元維持強勢、亞幣近期走弱，新台幣走勢疲軟不利資金行情推升，由於整體資金、法人和技術面仍未明顯偏多，即便指數有機會築底反彈，操作上仍不宜過度追價。元大投顧則指出，空方氣勢高漲，而在聯準會貨幣政策大致明朗以後，市場焦點轉往業績揭曉，隨著第一季季報和 4 月營收進入緊鑼密鼓最後公告階段，預料個股波動將加劇，建議投資人選股依各項數字驗證，再據復工復產復流實際情形，做為各家上市櫃公司未來展望重要參考。',
   'link': 'https://news.cnyes.com/news/id/4867627?exp=a',
   'photo_link': 'https://cimg.cnyes.cool/prod/news/4867627/l/197458ce12723f2785637d9c39a01df7.jpg'},
  {'id': 4867433,
   'category': 'tw_stock_news',
   'title': '第一金投信：台股趕底跌到近滿足點 向下撿便宜價值浮現',
   'content': '美國聯準會大動作調整利率政策，損害經濟成長在所難免，使得美股再度承壓，台股今 (9) 日再度重挫 359 點，在市場混沌轉折之際，第一金投信舉行線上記者會表示，台股目前陷入升息縮表、通脹、景氣衰退三大擔憂，過往升息經驗顯示，指數回檔約達 2 成，目前已趕底跌到近滿足點，且台股本益比已跌破 12 年低點，向下撿便宜的投資價值浮現。第一金投信投資長唐祖蔭表示，台股從萬八到今天跌到下探萬六，呈現加速趕底，短線而言，美國通膨有望逐步往下，中國五一長假陸續解封，對供應鏈將有幫助，加上台股台股本益比已經跌破 12 年來低點、至 11.68 倍，這波跌幅達 13%，以過往經驗來看，升息後的中期調整為 2 成，雖然還是有下行空間，但台股殖利率逾 4.5%，將會吸引一定資金流入，建議不要追高，往下撿便宜的投資價值浮現。而以長線來看，第一金投信則看好未來全球發展趨勢下的機會點，第一金台灣核心戰略建設基金經理人張正中表示，隨著美、中等大國角力持續深化，競爭領域不斷擴張，目前已遍及科技、通訊、綠能、基建、太空等領域，影響層面既深且廣，而在新冠疫情肆虐後，全球化更成為過去式，取而代之的是「逆全球化」，世界運作模式也逐漸從企業層級躍升至國家層級，政府政策對產業、經濟發展的影響力大為提升，未來想掌握投資趨勢，必須先鎖定國家經濟政策的主要方向。張正中指出，台灣過去一直在全球供應鏈扮演關鍵樞紐角色，如今也成為美中歐極為重視與拉攏的合作對象，政府在此趨勢中，2020 年宣示推動聚焦發展「資訊及數位、資安卓越、國防及戰略、民生及戰備、綠能及再生能源、精準健康」六大關鍵性產業，藉由發揮台灣自身優勢，同時吸納國際資源，台灣將很有機會如同當年設立「新竹科學園區」推動積體電路產業一樣，再次打造出綿延不絕的新護國神山群，激勵台灣經濟走出新格局。唐祖蔭進一步分析，台灣在全球半導體產業鏈中締造「製造第一、封測第一、IC 設計第二」不可動搖的產業地位，成為地緣政治的兵家必爭之地，因此政府在 2020 年宣示推動六大核心戰略產業，看準此商機，第一金投信因此推出台灣首檔瞄準政府核心戰略政策的台股基金「第一金台灣核心戰略建設基金」，聚焦六大核心戰略產業，包括：資訊、資安、民生、戰備國防、精準醫療、再生綠能等，預計 5 月 17 日起募集。',
   'link': 'https://news.cnyes.com/news/id/4867433?exp=a',
   'photo_link': 'https://cimg.cnyes.cool/prod/news/4867433/l/8a2a49e10c444d9ba6bf65f2f1c07580.jpg'},
  {'id': 4866985,
   'category': 'tw_stock_news',
   'title': '投資不要相信Fed鮑爾，要相信華爾街交易員！',
   'content': 'FOMC 會議是市場投資人眾所關注的焦點，但事實上 FOMC 造成的短線波動，不足以改變盤勢，因為早在 2021 Q1 開始，華爾街就在當時就推測通膨的程度，會使最遲 2022 Q3 必須升息，15 個月來 FED 都是善意的謊言，尤其鮑爾，比華爾街投行更鴿派，但最後會向專業、現實靠攏轉鷹。FOMC 決策與聲明，又是一次善意的謊言FOMC 本次決議：升息 2 碼（符合市場預期）、宣布 6 月進行第一次縮表，規模 300 億元公債 + 175 億元 MBS，9 月才會調升成 600+350 億元（前次會議紀要提及的速度）市場上在瘋狂震盪下，當日走出了狂喜行情，認為有利多，5/4 創紀錄的上漲幅度，隔日 5/4 再伴隨者更大幅的反轉下跌，就我的主觀論點來看，下跌沒有利空原因，很多新聞根本胡扯，本質就是 FOMC 會議，市場錯誤的解讀成利多，本就沒有理由是利多上漲，短線震盪後回歸華爾街的空方趨勢延續，畢竟鮑爾只是又一次安慰人心，選擇長痛非短痛，筆者認為若想顧及行情與名聲，只會在通膨議題上拖延，損失更大的歷史定位而已。如下表分析：電信、金融終於合理補跌，但還不夠「投信助漲也能助跌」! 金融股開始出現投信買、賣超同時出現，破線的停損壓力開始浮現，宛若國王的新衣，當然目前幅度還不夠，如下圖，目前價格層面，有均線支撐因此無法連跌，但預計金融指數最合理的修正幅度還有 5% 以上，破年線都不足為奇，並且目前投信只是有買有賣，還不到全面逼出資金（ETF 散戶贖回潮都還沒開始，還未有恐慌氣氛），所以整體有籌碼良性換手的跡象，但仍還須經歷最後一波主跌段的類股籌碼大搬風。結論：國際情勢與台股都相當類似，散戶投資人持續懷抱著急彈的期待、不願面對縮表，進入較低風險、較低報酬的現實，止跌就不會輕易到來。操作上，仍會建議目前延續今年至今的空方操作為主，而對於手中現股套牢的投資人，筆者建議，若資金部位不是個 3、5000 萬，其實都是很小的部位，斷然停損會比較好，接近築底必須讓手中資金愈多愈好，才能在後續佈局漲的更加快速的標的，套牢跌得愈深的股票，除非是權值股，否則通常反彈也會愈弱勢，不停損只會讓資產規模復原得更慢而已。（撰文者：永誠資產管理處研究員 范振峰）「永誠資產管理處」是全台合法擁有金管字號的證券投資顧問公司中「唯一首創資產管理的部門」20 年深耕專營台灣各大科技園區，以認真、誠信思維提供客戶服務讓努力累積財富的你，也可貼身感受理財管家的 VIP 價值沒有代理金融商品，不以商品銷售出發，減少你的財務漏洞從資產配置出發，透過「專案客製化」、「服務精緻化」、「獲利系統化」你不需犧牲時間體力，就能感受到資產提升！卓越投資研究團隊」加「頂尖財務顧問團隊」共同與客戶締造里程碑立即加入 https://line.me/R/ti/p/%40asset88598＞＞＞閱讀更多精彩文章 https://www.facebook.com/yongchengasset本公司所分析個別有價證券僅供參考，投資人應獨立判斷, 審慎評估並自負投資風險。\xa0',
   'link': 'https://news.cnyes.com/news/id/4866985?exp=a',
   'photo_link': 'https://cimg.cnyes.cool/prod/news/4866985/l/ff00fcc5011917ec5b906e61e4562014.jpg'},
  {'id': 4866975,
   'category': 'tw_stock_news',
   'title': '〈焦點股〉4月營收續攀峰、無懼中國封控 欣興股價逆勢走揚',
   'content': '受惠 ABF 載板價量齊揚，欣興 (3037-TW) 4 月營收達 111.57 億元，月增 4.46%、年增 41.83%，改寫單月新高，顯見中國封控停工對營運影響不大，激勵今 (9) 日股價逆勢走揚，盤中勁揚逾 3%，站上月線，另兩家 ABF 大廠南電 (8046-TW)、景碩 (3189-TW) 也相對抗跌。台股盤中跌勢加重，大跌近 330 點，摜破 16100 點，回測萬六，為近 1 年新低，不過，ABF 載板三雄股價相對有撐，其中欣興一度上漲超過 3%，最高來到 215.5 元，收復月線及 5 日線；南電在 400 元附近拉鋸，一度漲至 406 元；景碩午盤前也在平盤附近震盪，但賣壓隨之湧現；其他 PCB 股如金像電、志超也獲買盤力挺。欣興 4 月營收 111.57 億元，月增 4.46%、年增 41.83%，再創單月新高，累計前 4 月營收達 418.68 億元，年增 41.02%。雖然欣興昆山子公司 4 月因中國封控政策停工多日，但月底逐步復產，因此對營運影響不大，第二季在新產能開出下，可望挹注營收獲利表現。景碩 4 月營收 37.48 億元，月增 0.09%、年增 37.19%，改寫歷史新高，累計前 4 月營收 137.62 億元，年增 38.2%，續創同期新高，法人認為，中國昆山及蘇州封控對景碩營運影響不大，在產品組合優化下，將帶動毛利率及獲利同步提升。南電 4 月營收 44.35 億元，月減 14.7%，年增 7.1%，累計前 4 月營收 189.96 億元，年增 26.7%。法人指出，受惠 ABF 載板產品組合優化、記憶體 BT 載板需求升溫與有利的匯率因素，南電第二季營收可望達 160 億元、季增 1 成，毛利率也將挑戰 38%，維持買進評等。',
   'link': 'https://news.cnyes.com/news/id/4866975?exp=a',
   'photo_link': 'https://cimg.cnyes.cool/prod/news/4866975/l/d053223ff18b80853feaec3d30b90748.jpg'},
  {'id': 4866984,
   'category': 'tw_stock_news',
   'title': '【法人洞見：晶圓代工反彈時機到？】',
   'content': '指數近期走弱，先前漲多的網通、風電族群都在回檔，加上電子股接連創新低，短期內盤勢轉強機率確實不高，不過長遠來看，隨著電子族群修正幅度加大，投資價值越是浮現，尤其上週已有不少公司開始實施庫藏股，都在暗示機會藏在恐慌中。台股護國神山台積電 (2330-TW)) 先前就預估，今年整體半導體產業將成長 9%，晶圓代工市場則受惠於更多 IDM 廠和系統商使用自行研發晶片並委外代工，產業年成長高達 20%。觀察台積電 (2330-TW)) 股價表現，今年 1 月高點過後，股價已走弱一個季度，不過台積電近期獲利屢屢創高，今年第一季營收達到 175.7 億美元，毛利率更是一舉衝上 55.6%，雙雙來到歷史新高，如此優異的成績主要來自今年市場對 HPC(高效能運算)及車用電子的強勁需求，隨著股價修正超過兩成挑戰前低，外資賣超幅度明顯遞減，投信則持續在增加持股，止跌時機指日可待，應耐心等候。聯電 (2303-TW)) 今年第一季營收 634 億元，年增高達 40.02%，聯電在日前法說會給出優於同業平均成長 20% 展望，與台積電不謀而合，都看好網通、伺服器和車用需求高成長，可以抵銷消費性電子表現疲軟，為了因應科技新應用所需，近期更積極搶進 8 吋晶圓第三代半導體製造領域，預計下半年進駐廠區，我認為聯電由於進度領先同業，帶動股價近日在短線上有相對強勢的反彈，法人也都回頭買超，後續表現很值得投資人關注。同樣受投資人關注的晶圓代工大廠力積電 (6770-TW)，先前股價從上市後的 80.3 元重挫四成到 50 元附近就止跌反彈，隨著這波修正又再度來到 50 元的甜蜜價格附近，我認為在車用、5G 大趨勢帶領下，傳統製程晶片的價值也會有所提升，加上大多數晶圓代工廠在傳統的製程上並無重大擴產計劃，因此力積電有望穩中求勝，從基本面來看，力積電首季獲利營收均創新高，外資投信今年以來也都站在買方，股價表現也有領先同業打底的情況，建議可以優先關注這檔標的，一旦股價成功站穩季線，可能就是準備反彈的訊號。免費加入林鈺凱分析師頻道，最新的產業資訊、一手飆股，隨時為各位更新：股林高手林鈺凱 YOUTUBE 頻道：https://www.youtube.com/channel/UC9Pd7LN9potuHVafJCLX7Pw/featured林鈺凱分析師官方 LINE 帳號：https://line.me/R/ti/p/%40wyr8177f(ID：@win16888)林鈺凱分析師官方 TELEGRAM 頻道：https://t.me/win88888(ID：win88888)本公司所推薦分析之個別有價證券無不當之財務利益關係 以往之績效不保證未來獲利投資人應獨立判斷 審慎評估並自負投資風險',
   'link': 'https://news.cnyes.com/news/id/4866984?exp=a',
   'photo_link': 'https://cimg.cnyes.cool/prod/news/4866984/l/184927e27552679f7a297385eea4ba87.jpg'},
  {'id': 4866973,
   'category': 'tw_stock_news',
   'title': '台股陷萬六點保衛戰 財長：四因素引發震盪',
   'content': '台股盤中大跌逾 300 點，大盤指數面臨 16000 點保衛戰，財政部長兼國安基金委員會委員蘇建榮表示，台股下挫除與美股連動有關，還包括國內疫情升溫、美國升息循環與俄烏戰爭等因素有關，強調國安基金會密切緊盯股市發展。台股今 (9) 日持續大跌，包括電子、金融與傳產幾乎全盤皆墨，盤中指數一度重挫逾 300 點，蘇建榮今天出席政治大學國際金融學院揭牌典禮，也不免不了被媒體追問台股大跌國安基金的態度為何。蘇建榮會後受訪時指出，美股大跌主要是受聯準會升息所影響，進而牽動台股跟著下跌，加上國內疫情嚴峻，以及俄烏戰爭引發的通膨效應，都是影響台股走勢的原因。但蘇建榮也說，台灣有穩健的經濟基本面支撐，4 月出口預計將維持正成長格局，強調國安基金將持續關注金融市場與資金走勢，有必要時也會出手維持市場穩定。',
   'link': 'https://news.cnyes.com/news/id/4866973?exp=a',
   'photo_link': 'https://cimg.cnyes.cool/prod/news/4866973/l/b2c74279cc36107dd55a71bf61c5202d.jpg'},
  {'id': 4866947,
   'category': 'tw_stock_news',
   'title': '台灣精銳掛牌首日蜜月行情失靈 股價一度破發',
   'content': '台灣精銳 (4583-TW) 今 (9) 日上市，發行價每股 200 元，不過，在台股重挫下，影響蜜月行情，早盤一度跌破發行價、最低探至 198.5 元，盤中翻紅小漲 0.75%。台灣精銳主要產品為精密型行星式減速機、齒輪及齒排 (條)，營收 8 成以上來自半導體、面板及醫療設備產業，其他應用還包括航太、電子業及傳產等自動化設備及工具機，客服及餐旅營收占比 9.3%，由轉投資台中日月千禧酒店收入挹注。台灣精銳第一季受到原物料上漲影響，成本增加，導致毛利率下滑，不過，台灣精銳表示，台中中科后里園區三廠正準備新品，隨著中科三廠投產，透過產能效益控制成本，預估下半年毛利率可維持近 50% 水準。為反映部分成本，台灣精銳規劃也 7 月、明年 1 月，分別啟動漲價，漲幅各約 3-4%。台灣精銳第一季營收 8.61 億元，毛利率 48.7%，營益率 32.04%；稅後純益 3.67 億元，每股純益 5.03 元。',
   'link': 'https://news.cnyes.com/news/id/4866947?exp=a',
   'photo_link': 'https://cimg.cnyes.cool/prod/news/4866947/l/d909cceb5c32f1c86e1d370b76ebb103.jpg'},
  {'id': 4866844,
   'category': 'tw_stock_news',
   'title': '權證投資人一定要了解的 權證投資人看多標的－航運股',
   'content': '美國聯準會 (Fed) 如預期升息 2 碼，僅為美股帶來一日反彈，5 日在市場恐慌通膨惡化下，美股四大指數重挫，道瓊指數更是大跌逾千點。受到美股災情拖累，6 日台股盤中一度跌至最低 16,312.17 點，終場則下跌 287.92 點，以 16,408.20 點作收，跌幅 1.72%。從 6 日現股投資人看多金額前五名來看，除了與大盤連動密切的 加權指數 (TSE01-TW)，其餘進榜標的皆為航運股，包含 長榮 (2603-TW)、長榮航 (2618-TW)、陽明 (2609-TW)、裕民 (2606-TW)，其中，長榮 (2603-TW) 更以看多金額達 5,319 萬元居冠。雖然受到大陸封城影響物流供應鏈，航運族群今年度截至目前仍繳出相當亮眼的營收表現，6 日更扮演台股撐盤要角，在大盤大跌下，航運類指數仍逆勢小幅上漲。投資人如看好前述航運股標的，推薦可挑選剩餘天期 90 天以上且價內 5%~ 價外 20% 之認購權證進行布局，例如：長榮群益 1B 購 13 (069859)、長榮群益 1B 購 21 (072309)、長榮航群益 1C 購 09 (072902)、長榮航群益 1C 購 08 (072311)、陽明群益 1C 購 03 (071901)、陽明群益 1B 購 06 (070205)、裕民群益 21 購 01 (074036)、裕民群益 1A 購 01 (068026) 等。了解更多權證資訊 權民最大網',
   'link': 'https://news.cnyes.com/news/id/4866844?exp=a',
   'photo_link': 'https://cimg.cnyes.cool/prod/news/4866844/l/673d95e7a8c57ef83b39b63574f9700e.jpg'},
  {'id': 4866733,
   'category': 'tw_stock_news',
   'title': '〈台股盤前要聞〉鴻海布局智慧農業、金管會擬推數位健康證明 今日必看財經新聞',
   'content': '關注台股盤前要聞重點，鴻海近年積極布局智慧農業，中國媒體報導，旗下鴻富錦精密工業 (深圳) 成立 100% 持股公司的富士康智慧農業 (深圳)；為解決防疫保單亂象，金管會擬推出「數位健康證明」，邀集產壽險公會及業者討論相關事宜。以下是今 (9) 日必看重要財經新聞。鴻海布局智慧農業 新設立深圳子公司鴻海 (2317-TW) 集團衝刺智慧農業布局，根據中國媒體報導，鴻海旗下鴻富錦精密工業 (深圳)，成立 100% 持股公司的富士康智慧農業 (深圳)。閱讀全文...防疫保單診斷書需求暴增 金管會擬推數位健康證明保戶擠爆醫療院所要拿診斷證明，為解決防疫保單亂象，因此在衛福部建議之下，金管會擬推出「數位健康證明」，金管會昨 (8) 日晚間表示，已邀請產壽險公會及相關業者，研商解決民眾赴醫療院所申請診斷證明事宜，衛生福利部將提供數位新冠病毒健康證明查驗服務。閱讀全文...氫燃料電池需求旺 Bloom Energy 年底產能估翻倍增美國氫燃料電池製造商 Bloom Energy (BE-US) 近日公布 2022 會計年度第一季財報，執行長 K. Sridhar 電話會議中表示，受惠 SK 集團強勁訂單，激勵 Q1 營收創同期新高，隨著再生能源、儲能趨勢持續帶動市場成長，將持續擴產，預計今年底燃料電池產能將倍增。閱讀全文...國光生今年海外比重將過半 全年營收上看 20 億元創高國光生 (4142-TW) 今年營運成長動能來自海外市場，包括中國出貨單價較高的四價流感疫苗，日本、東歐、東南亞等疫苗產品也陸續出貨，今年海外營收比重將過半，有望推升全年營收衝破 20 億元，創新高。閱讀全文...南亞科：今年市況審慎樂觀 有機會逐季改善DRAM 大廠南亞科 (2408-TW) 股東會年報出爐，董事長吳嘉昭表示，今年 DRAM 市況審慎樂觀，整體產業邁向成長，從供需情況來看，預期第二季產業將延續第一季小幅修正市況，之後有機會逐季改善，但仍需觀察全球通膨、烏俄戰爭、疫情及供應鏈缺料的影響。閱讀全文...一張表掌握 15 家金控股利 總配息 2384 億破紀錄 外資將抱走逾 600 億元15 家金控股利政策全數出爐，由於去 (2021) 年獲利亮麗，15 家金控今年合計將發出 2384 億元現金股利，不但大舉高於去年的配息總額，續創歷史新高，更可望挹注台股資金活水；而外資偏愛金控股，因此可大豐收抱走超過 600 億元現金入袋。閱讀全文...不畏消費性需求轉弱 晶圓代工廠順勢擴大車用佈局隨著近來消費性電子需求轉疲，矽晶圓業者指出，在車用晶片需求持續成長下，國內各晶圓代工廠、記憶體廠，相繼調整產品組合，加速轉往車用產品腳步，順勢擴大車用版圖。閱讀全文...',
   'link': 'https://news.cnyes.com/news/id/4866733?exp=a',
   'photo_link': 'https://cimg.cnyes.cool/prod/news/4866733/l/b002eefe147eac5bac20cadbe76005b1.jpg'}]}, safe=False)
