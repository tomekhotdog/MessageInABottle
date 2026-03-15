"""Phase 3: Merge enrichment data (summaries, tags) into letters.json and .md files."""

import json
from pathlib import Path

CATALOGUED = Path("catalogued")

enrichments = {
    1: {
        "summary": "A fragmentary document in which Christopher Meryng identifies a cargo mark — a red stone — apparently the closing lines of a longer commercial letter. The fragment gives no context beyond the mark itself, suggesting it is the tail end of a shipment identification record.",
        "type": "business",
        "themes": ["trade", "shipping"],
        "people_mentioned": ["Christopher Meryng"],
        "goods_mentioned": [],
        "notable": False,
    },
    2: {
        "summary": "William Gresham writes warmly from Antwerp to his cousin Ellen, coordinating the distribution of barrels of sturgeon among named friends, family members, and notably Master Cromwell and the lord of Rutland. The letter reveals a dense social network of gift-giving and mutual exchange, including venison pasties received from Roger Manyngton and Mistress Looke, and ends with a last-minute change of collection point.",
        "type": "mixed",
        "themes": ["food", "gifts", "social_networks", "shipping", "trade"],
        "people_mentioned": ["William Gresham", "Ellen", "Peter Cole", "Rowlond Schakerley", "daughter Wilson", "Master Lock", "Master Botry", "Thomas Abraham the elder", "lord of Rutland", "Thomas Wilson", "Merten Albryght", "Roger Manyngton", "Mistress Looke", "Master Cromwell", "Awdryan Johnson"],
        "goods_mentioned": ["sturgeon", "ale", "venison pasties"],
        "notable": True,
        "notable_reason": "Names Thomas Cromwell as a recipient of sturgeon, placing this merchant letter within the orbit of one of Henry VIII's most powerful ministers.",
    },
    3: {
        "summary": "William Laund, an apprentice merchant in Antwerp, writes to his master William Mery with a detailed spice price report and shipping update, while also relaying the sad news of Charles Benche's death. The letter's most human moment comes when Laund describes confronting a debtor named Steven, who wept and admitted he had been deceiving his master, prompting the apprentice to plead for patience on Steven's behalf.",
        "type": "business",
        "themes": ["spices", "trade", "financial", "debt", "shipping", "news", "health"],
        "people_mentioned": ["William Laund", "William Mery", "Charles Benche", "Steven"],
        "goods_mentioned": ["ginger", "nutmegs", "cloves", "mace", "pepper", "saffron", "currants", "cinnamon", "rice", "kerseys"],
        "notable": True,
        "notable_reason": "Combines granular commodity price intelligence with an emotionally vivid account of a debtor breaking down in tears — rare personal texture within a routine trade letter.",
    },
    4: {
        "summary": "John Copynger, a fishmonger writing from Antwerp, directs his wife on how to receive and distribute a vessel of fresh sturgeon, while urging her to manage the household, supervise the workers, and collect outstanding debts in his absence. The letter captures the dual burden placed on a merchant's wife: acting as de facto business manager at home while her husband sourced goods abroad.",
        "type": "mixed",
        "themes": ["trade", "shipping", "food", "debt", "family", "financial"],
        "people_mentioned": ["John Copynger", "Robert Paris", "Master Kemp", "Adrian Johnson"],
        "goods_mentioned": ["sturgeon", "copper buckets", "tin"],
        "notable": True,
        "notable_reason": "Illuminates the active economic role of a merchant's wife, tasked with collecting debts and overseeing workers while her husband was overseas.",
    },
    5: {
        "summary": "William Gresham sends his wife what amounts entirely to a cargo manifest, listing a wide range of haberdashery goods shipped from Antwerp, with all prices recorded in merchant cipher. The letter contains no personal greeting or news, functioning purely as an encoded commercial document.",
        "type": "business",
        "themes": ["trade", "textiles", "coded_prices", "shipping", "crafts"],
        "people_mentioned": ["William Gresham"],
        "goods_mentioned": ["painted cloths", "inkle", "ounce thread", "gold checks", "aglets", "hawk ends", "says", "razors", "bosses", "pack needles", "fine checks with gold", "bay silk", "minikin pins", "brass bells", "leather", "paper", "brown paper", "sheep bells", "sturgeon"],
        "notable": True,
        "notable_reason": "A rare surviving example of a merchant's price cipher in active use, offering direct evidence of how sixteenth-century traders concealed commercially sensitive information within family correspondence.",
    },
    6: {
        "summary": "Ryner Grover sends a brief shipping note to Edward Morton, a grocer, listing spices and confectionery dispatched via Adrian Johnson's service from Antwerp. Among the goods is a personal item — his own wearing gown — tucked into a truss alongside the commercial cargo.",
        "type": "business",
        "themes": ["spices", "trade", "shipping", "food"],
        "people_mentioned": ["Ryner Grover", "Edward Morton", "Adrian Johnson"],
        "goods_mentioned": ["mace", "succade", "orange flowers", "gown"],
        "notable": False,
    },
    7: {
        "summary": "Blase Saunders writes from Antwerp to his brother Edward, reporting on a previous letter and a gift of lute strings he had sent, and asking after their quality. He sends warm regards to his parents and siblings, asking especially for his mother's blessing, and promises to write her a proper letter soon. The letter reveals a young man living abroad who is clearly mindful of family bonds and eager to maintain them across distance.",
        "type": "personal",
        "themes": ["family", "gifts", "social_networks"],
        "people_mentioned": ["Blase Saunders", "Edward Saunders"],
        "goods_mentioned": ["lute strings"],
        "notable": True,
        "notable_reason": "A rare glimpse of a young Englishman in Antwerp maintaining tender family ties across the Channel, complete with a gift of lute strings and a request for his mother's blessing.",
    },
    8: {
        "summary": "Jan van Espen writes from Brussels to Liuken van Brussel in London, reporting that he has looked into the matter of goods belonging to Peter Nene held at Sint Joos ten Hoede. He advises Liuken to come to Brussels in person to recover the goods, and notes that Wouter in de Nobele sends greetings.",
        "type": "business",
        "themes": ["trade", "social_networks"],
        "people_mentioned": ["Jan van Espen", "Liuken van Brussel", "Peter Nene", "Wouter in de Nobele", "Machielen"],
        "goods_mentioned": [],
        "notable": False,
    },
    9: {
        "summary": "William Lawson writes from Antwerp to his master Thomas Dichfield with a detailed cargo manifest of figured cloths and textiles being shipped via Adrian Johnson, totalling nearly £89. He also relays important market intelligence: yarn price rises are pushing up cloth prices, a key merchant named Colin is gravely ill, and a trader named Andryas Sallman has obtained an imperial writ shielding him from creditors for three years.",
        "type": "business",
        "themes": ["trade", "textiles", "shipping", "financial", "debt", "health"],
        "people_mentioned": ["William Lawson", "Thomas Dichfield", "Adrian Johnson", "Colin", "Andryas Sallman"],
        "goods_mentioned": ["figured cloths", "textiles", "yarn", "paper"],
        "notable": True,
        "notable_reason": "Combines a granular cloth cargo manifest with vivid market intelligence — rising yarn costs, a bedridden merchant, and a trader hiding behind an imperial writ.",
    },
    10: {
        "summary": "Jan van Espen reports that a messenger he sent to Longuen was blocked by a siege at Grevelingen, though he later learned passage was in fact possible without declaring goods. He asks Marten to find a reliable skipper to transport money on his behalf, and closes warmly with greetings to Marten's wife and a devotional Jesus token she had requested.",
        "type": "mixed",
        "themes": ["trade", "shipping", "financial", "social_networks", "war", "religion", "gifts"],
        "people_mentioned": ["Jan van Espen", "Marten"],
        "goods_mentioned": ["Jesus token"],
        "notable": True,
        "notable_reason": "A military siege disrupting merchant courier routes combined with a devotional token sent as a personal gift — an unusually vivid blend of the political, commercial, and spiritual worlds of 1533.",
    },
    11: {
        "summary": "Christopher Fysher sends an extremely terse note from Antwerp to his master William Windleff, informing him that a firkin containing ten rounds of sturgeon is being dispatched via Adrian Johnson. The letter contains nothing beyond this bare shipment notice.",
        "type": "business",
        "themes": ["trade", "shipping", "food"],
        "people_mentioned": ["Christopher Fysher", "William Windleff", "Adrian Johnson"],
        "goods_mentioned": ["sturgeon"],
        "notable": False,
    },
    12: {
        "summary": "Edward Faerlaey writes a heartfelt and increasingly desperate letter from Antwerp to his uncle Willem, lamenting that his many previous letters have gone unanswered. He has learned through an Englishman who married his uncle's daughter that Willem is in good health, yet still has not heard from him, and begs to be remembered and helped with unspecified past matters that are likely financial.",
        "type": "personal",
        "themes": ["family", "financial", "debt", "social_networks"],
        "people_mentioned": ["Edward Faerlaey", "Willem Faerlaey"],
        "goods_mentioned": [],
        "notable": True,
        "notable_reason": "The emotional intensity of a young man pleading repeatedly to be remembered by a silent uncle makes this one of the most humanly affecting letters in the collection.",
    },
    13: {
        "summary": "William Pratt, a grocer based in Antwerp, writes to his wife with detailed business instructions covering a wide range of commodities and household matters. He directs her on selling sheep, buying quicksilver, shipping almonds, and pricing madder, while noting that pepper is exceptionally plentiful — the most in seven years. The letter reveals a busy merchant household where wife and servant together manage operations in his absence.",
        "type": "mixed",
        "themes": ["trade", "family", "food", "spices", "textiles", "financial"],
        "people_mentioned": ["William Pratt", "Edward", "Edward Mewrelle"],
        "goods_mentioned": ["sheep", "quicksilver", "almonds", "madder", "pepper", "featherbed", "comfits", "cottons", "scales", "weights"],
        "notable": True,
        "notable_reason": "A rare window into the domestic-commercial partnership of a Tudor merchant couple, with the wife acting as a capable business agent.",
    },
    14: {
        "summary": "Liesbet Raens writes from home to her husband Claes in London, updating him on family and household affairs since Easter. She reports on marriages that may affect a property deal he was interested in, gently reproaches him for forgetting to write hop prices as promised, and closes with a plea that he look after his health. A tender picture of a couple managing distance together.",
        "type": "mixed",
        "themes": ["family", "trade", "property", "health", "textiles", "social_networks", "women_writing", "financial"],
        "people_mentioned": ["Liesbet Raens", "Claes Raens", "Machiel Dammasch", "Jana Braeckaet", "Bernaet", "Andries", "Pauelus Coernelys"],
        "goods_mentioned": ["hops", "black cloth"],
        "notable": True,
        "notable_reason": "An unusually warm and personal letter from a wife to an absent merchant husband, combining domestic detail, property negotiation, and marital affection.",
    },
    15: {
        "summary": "Harry Austen writes from Antwerp to his wife in London, arranging the delivery of three small firkins of sturgeon via Adrian Johnson. He carefully allocates the contents: the largest for a business associate, the middle one to be forwarded to Coventry for her family, and the smallest for her own enjoyment.",
        "type": "personal",
        "themes": ["food", "family", "shipping", "gifts", "social_networks"],
        "people_mentioned": ["Harry Austen", "Adrian Johnson", "Master Blanke", "Master Hill", "Claes de Frise"],
        "goods_mentioned": ["sturgeon"],
        "notable": False,
    },
    16: {
        "summary": "John Blundell writes from Antwerp to John Petey, a servant of London alderman Sir Thomas Baldry, with a mix of personal errands and trade business. He asks for his gown to be dyed puce and tailored with ruffed sleeves, arranges debt repayment via an armorer, and ships half a sturgeon. He reports all goods unreasonably dear, especially mercery goods.",
        "type": "mixed",
        "themes": ["trade", "financial", "debt", "textiles", "crafts", "food", "employment", "social_networks"],
        "people_mentioned": ["John Blundell", "John Petey", "Sir Thomas Baldry", "Hanyngton", "John Bennett", "Symond Cowper", "Adrian Johnson"],
        "goods_mentioned": ["gown", "sturgeon", "mercery goods"],
        "notable": False,
    },
    17: {
        "summary": "An elderly Flemish mother, Katline Tsaseleren, writes a heartfelt letter to her son Marten, expressing her longing to see him once more before she dies. She shares modest news of the family — a brother at a mill in Woeren, a sister still unmarried — and closes with a prayer for her son's soul. Written on Ascension Day, the letter is remarkable for its emotional directness.",
        "type": "personal",
        "themes": ["family", "health", "religion", "women_writing", "social_networks"],
        "people_mentioned": ["Katline Tsaseleren", "Marten Tsaseleren", "Peter", "Marie"],
        "goods_mentioned": [],
        "notable": True,
        "notable_reason": "A deeply moving letter from an elderly mother to her absent son, offering a rare and intimate glimpse into family emotion and the fear of death in the sixteenth century.",
    },
    18: {
        "summary": "An unnamed Antwerp merchant sends a detailed cargo manifest to Wyllem van Tonghen in London, documenting a diverse shipment via Adrian Janson. The list spans luxury and everyday goods — fine yarns, Tournai textiles, tapestries, Brussels ribbons, silk thread carpets, kerseys, decorated ceramics, and hats — an unusually rich record of the range of commodities flowing between Antwerp and London.",
        "type": "business",
        "themes": ["trade", "textiles", "shipping", "crafts"],
        "people_mentioned": ["Wyllem van Tonghen", "Adrian Janson"],
        "goods_mentioned": ["yarn", "Tournai textiles", "says", "silk thread carpet", "cord", "leather", "tapestries", "Ypres doubles", "Brussels ribbons", "kerseys", "Valenciennes half ox-pieces", "crested jugs", "ewers", "hats", "wood"],
        "notable": False,
    },
    19: {
        "summary": "Dietrich Hoerner writes from Cologne to Heinrich Schelt, a Hanseatic merchant at the London Steelyard, expressing frustration that Heinrich has failed to send proper accounts. The letter details complex financial arrangements including crown repayments, currency exchange in Antwerp, and instructions to purchase woad, red cloth, and russets. Hoerner scolds Heinrich directly — 'you are in the wrong.'",
        "type": "business",
        "themes": ["trade", "financial", "debt", "textiles"],
        "people_mentioned": ["Dietrich Hoerner", "Heinrich Schelt", "Arnt Byrckman", "van Gangell"],
        "goods_mentioned": ["woad", "red cloth", "russets", "gold measures"],
        "notable": False,
    },
    20: {
        "summary": "James Bolney, a mercer writing from Antwerp, instructs his servant William Hobson on the distribution of a sturgeon, with careful instructions on how to divide and sell it. He also relays news about cloth for shirts and a linen purchase for his wife, apologising that a better sheet was sold before he could secure it.",
        "type": "mixed",
        "themes": ["trade", "food", "textiles", "family", "shipping", "social_networks"],
        "people_mentioned": ["James Bolney", "William Hobson", "Adrian Johnson", "Laurens", "Mistress Jones", "Humphrey Lewis", "Mistress Jarvis", "Robert Stockfish"],
        "goods_mentioned": ["sturgeon", "cloth", "shirts", "ells", "seams"],
        "notable": True,
        "notable_reason": "The meticulous instructions for dividing a single sturgeon between neighbours humanise the merchant world in an unusually domestic and personal way.",
    },
    21: {
        "summary": "John Dene writes from Antwerp to his brother Richard, relaying detailed trading instructions from their master. The letter covers cloth purchases, credit terms, and price negotiations on worsteds and fustians, with a confidential postscript to sell five bales of Bavernell cloth quietly before the price falls further.",
        "type": "business",
        "themes": ["trade", "textiles", "financial", "debt"],
        "people_mentioned": ["John Dene", "Richard Dene", "Richard Wilson", "Bolinger", "Master Lynch"],
        "goods_mentioned": ["cloth", "worsteds", "fustians", "Bavernell cloth"],
        "notable": True,
        "notable_reason": "The confidential postscript — buy cheap and sell quietly before prices drop — gives a rare unguarded look at insider trading practices among Tudor cloth merchants.",
    },
    22: {
        "summary": "Robert Hobbes writes to his master Robert Dene, a London grocer, providing a cargo manifest of goods shipped via Adrian Johnson from Antwerp. The shipment includes exotic pharmaceutical and medicinal commodities — gum opopanax, senna, turbith, and several unidentified substances — alongside canvas and crossbow thread.",
        "type": "business",
        "themes": ["trade", "shipping", "spices", "health", "crafts"],
        "people_mentioned": ["Robert Hobbes", "Robert Dene", "Adrian Johnson"],
        "goods_mentioned": ["gum opopanax", "nigella romana", "senna", "turbith", "canvas", "crossbow thread"],
        "notable": True,
        "notable_reason": "The cargo includes several obscure and unidentified medicinal substances, making it a rare primary source for the history of the pharmaceutical trade in Tudor England.",
    },
    23: {
        "summary": "Blase Saunders writes from Antwerp to Christopher Salway, reporting the dispatch of food goods and enquiring about lute strings he had previously sent. A personal note reveals that the man with whom Saunders had arranged lodging has recently been bereaved and can no longer host him, leaving Saunders without accommodation.",
        "type": "mixed",
        "themes": ["trade", "food", "shipping", "social_networks", "gifts"],
        "people_mentioned": ["Blase Saunders", "Christopher Salway", "William Butler", "Adrian Johnson", "Richard Ponter", "Martin Allbrook", "Master Pratt"],
        "goods_mentioned": ["sturgeon", "olives", "capers", "succade", "lute strings"],
        "notable": True,
        "notable_reason": "The lodging crisis caused by a host's bereavement illustrates the personal vulnerabilities of young men navigating life as merchant factors abroad.",
    },
    24: {
        "summary": "Stephen Bodington writes from Antwerp to his master William Mery, confessing he cannot yet repay a significant debt and reporting that the recent show day was the worst he had ever seen — not a single cloth sold. He relays intelligence from Venice on ginger supplies and warns that new shipping at Barbers Mart could devastate cloth sales for years.",
        "type": "mixed",
        "themes": ["trade", "textiles", "spices", "financial", "debt", "news", "politics"],
        "people_mentioned": ["Stephen Bodington", "William Mery", "Mistress Hall", "Harry Mylles"],
        "goods_mentioned": ["cloth", "ginger", "lead weights"],
        "notable": True,
        "notable_reason": "A cryptic reference to 'great murmuring of the death of the 2 strangers' and fears of a seven-year market collapse capture a moment of acute commercial anxiety.",
    },
    25: {
        "summary": "Jan van Espen writes a brief, warm personal note to Bernard de Bordverwerche and his wife Maeyken in London. He reports that their mutual acquaintance Willem de Vlemmick has lost dramatic weight — likely through illness — and sends affectionate greetings to 'black Peter' and the circle of embroiderers, full of playful nicknames.",
        "type": "personal",
        "themes": ["social_networks", "crafts", "health"],
        "people_mentioned": ["Jan van Espen", "Bernard de Bordverwerche", "Maeyken de Bordverwerche", "Willem de Vlemmick", "Peter"],
        "goods_mentioned": [],
        "notable": True,
        "notable_reason": "The use of affectionate nicknames such as 'little drunken cup' and the vivid description of a friend's dramatic physical transformation give this letter an unusually lively, intimate quality.",
    },
    26: {
        "summary": "Henry Brinklow writes from Antwerp to George Conyars with urgent business instructions involving a delayed £100 sterling payment, the distribution of goods between a London stand and the waterside, and a shipment including a coverlet of lilies and lawn fabric. The letter contains heavily coded mercantile notation and ends with a pointed directive to act 'secretly and with diligence.'",
        "type": "business",
        "themes": ["trade", "financial", "textiles", "shipping", "coded_prices", "debt"],
        "people_mentioned": ["Henry Brinklow", "George Conyars", "T. Brace", "Adrian Johnson", "Mistress Smyng", "Mistress Whale"],
        "goods_mentioned": ["coverlet of lilies", "lawn", "writing tablets", "gold"],
        "notable": True,
        "notable_reason": "The combination of coded notation, secrecy instructions, and a £100 delayed payment gives a vivid picture of the covert mechanics of Tudor cross-Channel trade.",
    },
    27: {
        "summary": "Katrijne Tehaselare writes from Brussels to her son Marten in a deeply emotional letter, disclosing that she has been gravely ill and feared she would never see him again. She expresses a desperate longing to see him once more before she dies and hints at a secret she has kept in her heart that she wishes to reveal in person. A postscript notes that the sister Babelken has died.",
        "type": "personal",
        "themes": ["family", "health", "women_writing", "gifts", "social_networks"],
        "people_mentioned": ["Katrijne Tehaselare", "Marten Tehaselare", "Jan Speeckaert", "Bettulen", "Lussken", "Babelken"],
        "goods_mentioned": ["tabard"],
        "notable": True,
        "notable_reason": "A dying mother dictating a farewell letter to her son, hinting at a lifelong secret never yet spoken aloud — one of the most emotionally raw surviving letters from this period.",
    },
    28: {
        "summary": "Richard Donne writes from Antwerp to his wife in London, sending trenchers, sleys, and settles via Adrian Gonson, and reporting with growing anxiety that he cannot recover money owed, fears being deceived by a servant, and has failed to sell half his nets. He urges his wife to sell what she can to raise funds before his situation becomes untenable.",
        "type": "mixed",
        "themes": ["trade", "financial", "debt", "shipping", "family", "crafts"],
        "people_mentioned": ["Richard Donne", "Adrian Gonson", "John Nundeth", "Harold", "Peter Classen", "Master Davies"],
        "goods_mentioned": ["trenchers", "sleys", "settles", "nets"],
        "notable": False,
    },
    29: {
        "summary": "Jheronnimus writes to his brother Jasper with a meticulous accounting of goods sent — hundreds of fans, handkerchiefs, cakes, and yarn — listing prices in stuivers and nobles and tracking every toll and shipping cost. He apologizes for delays caused by cash-flow problems and mentions borrowing from a friend. A brief aside that 'Hubert also sells beer' hints at the diverse small-scale commercial activities in the brothers' network.",
        "type": "business",
        "themes": ["trade", "financial", "shipping", "social_networks", "family", "debt"],
        "people_mentioned": ["Jheronnimus", "Jasper", "Peter Kalssen", "Katrin", "Merten", "Anne", "Cornelis", "Anne Banckers", "Hubert", "Knapkout"],
        "goods_mentioned": ["fans", "handkerchiefs", "cakes", "yarn", "basket"],
        "notable": False,
    },
    30: {
        "summary": "William Butler writes from Antwerp to his pregnant wife Brigit in London, sending firkins of sturgeon, olives, capers, and succade via Adrian Johnson's ship the James of Antwerp. He instructs her to open the barrel of sturgeon and succade for her gossips at her lying-in, praying God to send her well through childbirth.",
        "type": "mixed",
        "themes": ["family", "shipping", "food", "gifts", "health"],
        "people_mentioned": ["William Butler", "Brigit Butler", "Adrian Johnson", "cousin Pratt"],
        "goods_mentioned": ["sturgeon", "olives", "capers", "succade"],
        "notable": True,
        "notable_reason": "A merchant sending luxury foods home specifically for his wife's childbirth celebration, with a tender prayer for her survival — an unusually intimate window into domestic life behind Tudor commerce.",
    },
    31: {
        "summary": "Harry Maye writes from Antwerp to his master William Chamberlain, a London draper, with a detailed account of commodity purchases and current market prices across both cities. He reports shipping hops and bay salt, notes sharp price rises at Arnemuiden, and surveys the cost of iron, madder, spices, soap, and wire. His master has money lying idle but cannot find profitable investments — everything is dear abroad and cheap at home.",
        "type": "business",
        "themes": ["trade", "shipping", "spices", "textiles", "financial"],
        "people_mentioned": ["Harry Maye", "William Chamberlain", "Adrian Johnson", "John Maye"],
        "goods_mentioned": ["hops", "bay salt", "iron", "Namur iron", "madder", "latten wire", "black soap", "maces", "cloves", "pepper", "alum", "white soap", "cloth"],
        "notable": True,
        "notable_reason": "An exceptionally detailed snapshot of commodity prices across Antwerp and England in 1533, capturing the arbitrage logic of a Tudor merchant.",
    },
    32: {
        "summary": "Mercer William Colsell writes a warm and playful letter from Antwerp to his wife Kate, sending affectionate greetings to their children including a tender nickname for the youngest — 'the little pig in the basket.' He ships barrels of sturgeon, teases Kate about a past domestic disagreement, and confides that his side is giving him pain and he wishes he were home.",
        "type": "mixed",
        "themes": ["family", "shipping", "food", "health", "social_networks", "gifts"],
        "people_mentioned": ["William Colsell", "Kate Colsell", "Master FitzRamys", "Mistress FitzRamys", "Nicholas", "Master Ressener", "Master Denssy", "Master Daniell", "Adrian Johnson"],
        "goods_mentioned": ["sturgeon", "cloth", "venison"],
        "notable": True,
        "notable_reason": "The nickname 'the little pig in the basket' for his youngest child and his self-deprecating domestic teasing give the letter an unusually human and intimate quality.",
    },
    33: {
        "summary": "Factor John Westbury writes from Antwerp to his master Thomas Abraham reporting the shipment of 58 pieces of say — a lightweight cloth — graded across multiple quality tiers with individual prices from 22s to 60s per piece, totalling £95 7s.",
        "type": "business",
        "themes": ["trade", "textiles", "shipping", "financial"],
        "people_mentioned": ["John Westbury", "Thomas Abraham", "Adrian Johnson"],
        "goods_mentioned": ["say"],
        "notable": False,
    },
    34: {
        "summary": "A bare cargo note recording that John Westbery has one bale aboard Adrian Johnson's ship, with freight charged at three shillings sterling. It functions purely as a shipping label.",
        "type": "business",
        "themes": ["shipping", "trade"],
        "people_mentioned": ["John Westbery", "Adrian Johnson"],
        "goods_mentioned": [],
        "notable": False,
    },
    35: {
        "summary": "Veteran Merchant Adventurer John Smyth writes from Antwerp to John Dawes of Maldon, Essex, introducing himself on the recommendation of a mutual contact and proposing a trading partnership. He lists a remarkable range of goods already purchased speculatively — iron, pots, paving tiles, hops, salt, fustians, feather balls, flax, and sturgeon 'to make acquaintance with' — and asks Dawes to source dairy, grain, and other commodities for the return trade.",
        "type": "business",
        "themes": ["trade", "shipping", "financial", "social_networks", "food", "crafts"],
        "people_mentioned": ["John Smyth", "John Dawes", "Master Flege"],
        "goods_mentioned": ["Namur iron", "pots", "paving tiles", "hops", "bay salt", "fustians", "white salt", "feather balls", "dressed flax", "baskets", "lanterns", "bellows", "trenchers", "sturgeon", "cheeses", "butter", "mustard seed", "tallow", "bacon", "malt", "barley"],
        "notable": True,
        "notable_reason": "The sheer breadth of goods offers a vivid panorama of Anglo-Flemish import-export trade, and the note that feather balls are unknown in Scotland hints at the uneven spread of consumer goods.",
    },
    36: {
        "summary": "Hanseatic merchant Marx Meyer writes urgently from London to the Lübeck council describing a diplomatic crisis: English authorities have seized Hanseatic goods and are compelling Steelyard merchants to accept rulings without any right of reply. Meyer, detained and unable to leave England, warns that losing the Steelyard's privileges would be catastrophic — 'better to lose ten hundredweight of gold than such a privilege' — and begs the council to send a diplomatic petition.",
        "type": "mixed",
        "themes": ["politics", "diplomacy", "trade", "financial", "shipping"],
        "people_mentioned": ["Marx Meyer", "Hans Molenbeke"],
        "goods_mentioned": [],
        "notable": True,
        "notable_reason": "A first-hand account of the political pressure bearing down on the Hanseatic Steelyard in London, capturing a merchant caught between two sovereign powers and the fragility of long-established trading privileges.",
    },
}


# --- Load and update letters.json ---
with open("letters.json", "r", encoding="utf-8") as f:
    letters = json.load(f)

for letter in letters:
    lid = letter["id"]
    if lid in enrichments:
        e = enrichments[lid]
        letter["summary"] = e["summary"]
        letter["letter_type"] = e["type"]
        letter["themes"] = e["themes"]
        letter["people_mentioned"] = e["people_mentioned"]
        letter["goods_mentioned"] = e["goods_mentioned"]
        letter["notable"] = e["notable"]
        if e.get("notable_reason"):
            letter["notable_reason"] = e["notable_reason"]

with open("letters.json", "w", encoding="utf-8") as f:
    json.dump(letters, f, indent=2, ensure_ascii=False)

print(f"Updated letters.json with enrichment data for {len(enrichments)} letters")

# --- Update .md files ---
updated = 0
for lid, e in enrichments.items():
    md_path = CATALOGUED / f"letter_{lid:02d}.md"
    if not md_path.exists():
        print(f"WARNING: {md_path} not found")
        continue

    content = md_path.read_text(encoding="utf-8")

    # Build enrichment section
    themes_str = ", ".join(e["themes"])
    people_str = ", ".join(e["people_mentioned"]) if e["people_mentioned"] else "None"
    goods_str = ", ".join(e["goods_mentioned"]) if e["goods_mentioned"] else "None"
    notable_str = "Yes" if e["notable"] else "No"

    enrichment_section = f"""## Summary

{e["summary"]}

## Tags

- **Type:** {e["type"]}
- **Themes:** {themes_str}
- **People mentioned:** {people_str}
- **Goods mentioned:** {goods_str}
- **Notable:** {notable_str}"""

    if e.get("notable_reason"):
        enrichment_section += f"\n- **Why notable:** {e['notable_reason']}"

    # Insert after frontmatter header line, before ## Archival Reference or ## Transcription
    # Find the first ## heading after the title
    lines = content.split("\n")
    insert_idx = None
    for i, line in enumerate(lines):
        if line.startswith("## ") and i > 0:
            insert_idx = i
            break

    if insert_idx is not None:
        lines.insert(insert_idx, enrichment_section + "\n")
        md_path.write_text("\n".join(lines), encoding="utf-8")
        updated += 1
    else:
        print(f"WARNING: Could not find insertion point in {md_path}")

print(f"Updated {updated} .md files with enrichment sections")
