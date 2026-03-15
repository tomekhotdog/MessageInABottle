"""Phase 3: Merge enrichment data (summaries, tags) into documents.json and doc .md files."""

import json
from pathlib import Path

CATALOGUED = Path("catalogued")

enrichments = {
    37: {
        "summary": "Formal examination conducted before the Lübeck council on 25 September 1533, recording separate depositions from Adrian Johnson (skipper of Antwerp) and Hinrik Kron (Lübeck captain) regarding the capture of Johnson's ship off the south coast of England on 19 August 1533. Johnson describes being boarded after a warning shot, the transfer of goods due to the ship taking on water, and the surrender of money hidden in his sleeve; Kron largely corroborates the seizure while defending his actions as a salvage. The document is authenticated by the notary Nicolaus Clone and later certified as a true copy by Michael Petri, notary of the diocese of Schwerin.",
        "type": "deposition",
        "themes": ["piracy", "legal_proceedings", "maritime", "testimony", "goods_seizure", "notarial", "financial"],
        "people_mentioned": ["Adrian Johnson", "Hinrik Kron", "Hinrik Kerchrinck", "Herman Schute", "Johan Wilmessen", "Johann Hu\u00dfer", "Nicolaus Clone", "Michael Petri"],
        "goods_mentioned": [],
        "notable": True,
        "notable_reason": "Provides direct eyewitness testimony from both the victim and the privateer captain, including the specific detail of gold coins (31 English gold angels and 4 double ducats) hidden in the skipper's sleeve, giving rare insight into the mechanics of a 16th-century maritime seizure.",
    },
    38: {
        "summary": "A Latin translation of the same depositions recorded in Doc 37, produced by the notary Michael Petri and certified as agreeing in substance with the Low German original. It preserves the same testimony from Adrian Johnson and Hinrik Kron regarding the capture off England on 19 August 1533, with the ship named \"to the East\" explicitly identified. The document adds the formal Latin notarial apparatus and specifies the vessel type as a \"hoy.\"",
        "type": "deposition",
        "themes": ["piracy", "legal_proceedings", "maritime", "testimony", "goods_seizure", "notarial", "financial"],
        "people_mentioned": ["Adrian Johnson", "Hinrik Kron", "Hinrik Kerckrinck", "Hermann Schute", "Johann Wilemessen", "Johann Huster", "Nicolaus Clone", "Michael Petri"],
        "goods_mentioned": [],
        "notable": True,
        "notable_reason": "Identifies the ship by name (\"to the East\") and demonstrates the administrative practice of producing bilingual notarial records, reflecting the multilingual documentary culture of Hanseatic legal proceedings.",
    },
    39: {
        "summary": "A second Latin copy of the depositions of Adrian Johnson and Hinrik Kron, closely paralleling Doc 38 but bearing a misdated year of 1534 instead of 1533 and attested by a slightly different notarial hand (Nicholaus Clove rather than Nicolaus Clone). It records the same testimony about the seizure off England, the transfer of goods, and the money counted from the skipper's sleeve. The copy was likewise certified by Michael Petri as matching the original.",
        "type": "deposition",
        "themes": ["piracy", "legal_proceedings", "maritime", "testimony", "goods_seizure", "notarial", "financial"],
        "people_mentioned": ["Adrian Johnson", "Henrik Croen", "Henrik Karckrinck", "Hermann Schute", "Johann Wilmessen", "Johann Husser", "Nicholaus Clove", "Michael Petri"],
        "goods_mentioned": [],
        "notable": True,
        "notable_reason": "Contains a notable scribal misdating (1534 instead of 1533) that has documentary significance for establishing the archival history and copying sequence of these legal records.",
    },
    40: {
        "summary": "A schedule in Middle English listing the cargoes loaded aboard Adrian Johnson's ship by a range of named London and Antwerp merchants, compiled around September 1533 as a record of losses following the seizure. The document enumerates goods from at least 26 different merchants including textiles (camlets, says, fustians, worsted, Hollands), spices (pepper, cinnamon, mace), foodstuffs (currants, sturgeon, Seville oil, succade), hardware (knives, awl blades, candlesticks), and miscellaneous wares (hops, haberdashery, gum arabic, dragon's blood). Several merchants note they deliberately used false names or omitted their names from the ship's book for fear of Scottish vessels intercepting the cargo.",
        "type": "schedule",
        "themes": ["trade", "cargo", "goods_seizure", "compensation", "maritime", "textile_trade", "spice_trade", "food_trade", "financial", "personal_property"],
        "people_mentioned": ["William Lok", "Peter Welsser", "Robert Meredyth", "William Mery", "John Proctor", "John Westbery", "Harry Bechar", "John Popam", "John Ambrose", "Thomas Dichffyld", "Richard Travea", "William Chamberlayne", "Harry Austen", "John Edwards", "Robert Reynolds", "Robert Dene", "Richard Doune", "Thomas Marston", "Matthew Dale", "Cornelis Williamson", "Richard Wilson", "William Gresham", "Nicholas Tycheborn", "Thomas Brown", "William Ristlayn", "Robert Laurens", "William Cowsett", "Edward Morton", "Adrian Johnson"],
        "goods_mentioned": ["camlets", "says", "currants", "pepper", "cinnamon", "hops", "inkle thread", "quartering says", "hats", "checks", "girdling says", "knives", "awl blades", "haberdashery", "writing paper", "bellows", "Hollands linen", "sturgeon", "kettle bonds", "hemp", "gum", "gum arabic", "dragon's blood", "lapis", "turpeth", "trenchers", "Saint Thomas worsted", "Osnabr\u00fcck fustians", "mace", "succade", "Seville oil", "capers", "olives", "sugar", "iron wire", "breastplates", "backplates", "harness-skins", "shirts", "napkins", "diaper linen", "carpets", "featherbed", "apparel"],
        "notable": True,
        "notable_reason": "Exceptionally rich source listing named London merchants with individual valuations and merchant marks, revealing Anglo-Antwerp trade networks and the use of false consignment names to evade Scottish privateers; one of the most commercially detailed documents in the case.",
    },
    41: {
        "summary": "An authenticated inventory compiled on 13 and 15 September 1533 by Lübeck councillors Nicolaus Bardewick and Herman Schute, recording 119 separate items unloaded from Hinrik Kron's bogarde and received into custody at Lübeck after the seizure of Adrian Johnson's ship. The inventory lists bales, casks, sacks, chests, and loose items including pepper, cinnamon, silk, linen, haberdashery, sugar, stoneware, brass wire, iron wire, and personal effects, with each item identified by merchant mark. The document is attested by the notary Nicolaus Clone.",
        "type": "inventory",
        "themes": ["legal_proceedings", "cargo", "goods_seizure", "maritime", "notarial", "trade", "textile_trade", "spice_trade"],
        "people_mentioned": ["Nicolaus Bardewick", "Herman Schute", "Hinrik Kron", "Adrian Johnson", "Hans Vaget", "Peter vom Hagen", "Nicolaus Clone"],
        "goods_mentioned": ["Louvain cloth", "says", "sugar", "bread", "white silk", "pepper", "cinnamon", "linen", "haberdashery", "stoneware jugs", "brass wire", "brass buckets", "canvas", "iron wire", "iron band", "linen cloth", "gowns", "twine", "blankets", "feather coverlet", "leather bag", "bole pigment", "cords"],
        "notable": True,
        "notable_reason": "Provides the official Lübeck custodial record of all 119 seized items with merchant marks, serving as the definitive evidentiary inventory for subsequent restitution proceedings and allowing cross-referencing with the English merchants' loss schedule in Doc 40.",
    },
    42: {
        "summary": "A second version of the same Lübeck inventory (cf. Doc 41), compiled over the same two sessions on 13 and 15 September 1533 and authenticated by the notary Nicolaus Klon, recording goods transferred from Hinrik Kron's bogarde following the seizure of Adrian Johnson's ship. The list closely mirrors Doc 41 in content but shows minor differences in item numbering, descriptions, and merchant mark numbering, indicating it is a parallel or duplicate record rather than a direct copy. It is witnessed by Hans Vaget and Peter Hagenow.",
        "type": "inventory",
        "themes": ["legal_proceedings", "cargo", "goods_seizure", "maritime", "notarial", "trade", "textile_trade", "spice_trade"],
        "people_mentioned": ["Nicolaus Bardewick", "Herman Schute", "Adrian Johnson", "Hinrik Kron", "Hans Vaget", "Peter Hagenow", "Nicolaus Klon"],
        "goods_mentioned": ["Louvain cloth", "says", "sugar", "bread", "haberdashery", "stoneware jugs", "pepper", "cinnamon", "linen", "brass wire", "brass buckets", "canvas", "iron wire", "iron banding", "gowns", "linen cloth", "twine", "blankets", "feather coverlet", "leather bag", "bole pigment", "cords", "Louvain bindings"],
        "notable": True,
        "notable_reason": "As a parallel inventory to Doc 41 with divergent merchant mark numbering and minor descriptive variants, it has significant value for establishing the authenticity and transmission of the evidentiary record, and for identifying discrepancies that may have been relevant to disputed claims.",
    },
    43: {
        "summary": "William Mery, a grocer, records the goods he shipped aboard Adrian Johnson's vessel: pepper, currants, and cinnamon. He notes he received only half his cinnamon (18 of 36 lb.) and provides itemised valuations in Flemish money totalling £118 4s 9d.",
        "type": "schedule",
        "themes": ["trade", "cargo", "goods_seizure", "spice_trade", "food_trade", "maritime"],
        "people_mentioned": ["William Mery", "Adrian Johnson"],
        "goods_mentioned": ["pepper", "currants", "cinnamon"],
        "notable": False,
    },
    44: {
        "summary": "An inventory drawn up in Lübeck in October 1533, in the presence of William Ashe acting as attorney for the English merchants who lost goods, recording packages and items inspected by mark. The document is witnessed by Heinrich Kordes and Tyle Lutguwe and written by Nicolaus Klone.",
        "type": "inventory",
        "themes": ["cargo", "goods_seizure", "legal_proceedings", "maritime", "notarial"],
        "people_mentioned": ["William Ashe", "Heinrich Kordes", "Tyle Lutguwe", "Nicolaus Klone"],
        "goods_mentioned": ["cloth", "canvas"],
        "notable": False,
    },
    45: {
        "summary": "A list of English merchants and their goods aboard Adrian Johnson's ship, including Robert Dene, John Edward, Jürgen Conink, Heinrich Brinklave, and Randall Atkinson. Cargoes include hops, cloth, canvas, apothecary wares, and porcelain vessels, with merchant marks used to identify packages.",
        "type": "schedule",
        "themes": ["trade", "cargo", "goods_seizure", "maritime", "textile_trade"],
        "people_mentioned": ["Robert Dene", "John Edward", "J\u00fcrgen Conink", "Heinrich Brinklave", "Randall Atkinson", "Adrian Johnson"],
        "goods_mentioned": ["hops", "cloth", "canvas", "porcelain vessels", "apothecary wares"],
        "notable": False,
    },
    46: {
        "summary": "A certification letter from the council of Bergen op Zoom to the council of Lübeck, dated 24 February 1534, attesting that 37 English merchants appointed Richard Plompton as their legal representative in place of Thomas Gigges, who fell ill, to present letters from Henry VIII and recover goods seized from Adrian Johnson's ship. The document is authenticated by notary Michael Petri.",
        "type": "certificate",
        "themes": ["legal_proceedings", "diplomacy", "restitution", "goods_seizure", "maritime", "notarial"],
        "people_mentioned": ["Richard Plunthon", "Richard Plompton", "Thomas Gigges", "Henry VIII", "C. de Mera", "Michael Petri", "Adrian Johansen"],
        "goods_mentioned": [],
        "notable": True,
        "notable_reason": "Documents Henry VIII's direct diplomatic intervention on behalf of the English merchants, and records the appointment of a substitute attorney when the original envoy fell ill, making it a key link in the legal chain for restitution.",
    },
    47: {
        "summary": "On 1 April 1534 in Lübeck, councillors Hermann Schute and Gottke Engelstede formally returned 30 or more itemised packages of seized goods to Richard Plunthon, acting as attorney for the English merchants. The detailed list covers textiles, spices, personal property, and household goods belonging to named merchants and their wives, notarised by Michael Petri.",
        "type": "legal_instrument",
        "themes": ["restitution", "legal_proceedings", "cargo", "goods_seizure", "maritime", "textile_trade", "spice_trade", "notarial", "personal_property"],
        "people_mentioned": ["Hermann Schute", "Gottke Engelstede", "Richard Plunthon", "Michael Petri", "John Westborre", "Robert Meredy", "John Edward", "John Gerholt", "Richard Wilson", "John Practor", "Henry Augustin", "William Lock", "William Colsell", "William Grossen", "Robert Laurence", "Anthony Serene", "Richard Osborne", "Henry Beger", "Nicholas Tysborne", "Edward Morton", "Robert Reinholt", "William Bateman", "William Mery", "Robert Den", "Thomas Distfelt", "Ralph Warinthun", "Thomas Bruns", "Augustin Hindt", "John Martyn", "John Pappham", "Maryn Capella", "Heinrich Warnboke", "Jasper van Dalen"],
        "goods_mentioned": ["say cloth", "cloth", "porcelain wares", "cypress-wood chests", "sardonyx cloth", "rumbi", "Holland linen", "camlet", "pepper", "yarn", "mace", "canvas", "hemp", "kettle-hooks", "Ulm sardonyx", "cinnamon", "buckram", "silk", "sugarloaves", "linen cloth", "haberdashery", "frieze coats", "red stones", "leaves"],
        "notable": True,
        "notable_reason": "The most comprehensive itemised record of restitution in the case, listing over 30 individual consignments with owners, valuations, and goods, making it the central evidential document for the entire seizure and recovery of cargo.",
    },
    48: {
        "summary": "A formal notarial instrument dated 9 April 1534, in which Richard Plunthon publicly confesses before the Lübeck council to having received back all seized goods on behalf of the English merchants, swears an oath that the goods belong to English subjects and not Lübeck's enemies, and issues a full and perpetual acquittance releasing the council of Lübeck from any further legal claims arising from the seizure. The document is drawn up by notary Michael Petri and witnessed by Hermann Iserhell and Conrad Kock.",
        "type": "legal_instrument",
        "themes": ["restitution", "legal_proceedings", "goods_seizure", "maritime", "notarial", "diplomacy", "compensation", "financial"],
        "people_mentioned": ["Richard Plunthon", "Charles V", "Adrian Johansen", "Tilemann Tegetmeyger", "Joachim Gerkens", "Hermann Schuten", "Godehard Engelsteden", "Michael Petri", "John Westborri", "Robert Meredy", "John Eduart", "John Gerholt", "Richard Wilsun", "John Practor", "Henry Augustin", "William Lock", "William Kolsel", "William Grossen", "Robert Laurentii", "Anthony Sehrene", "Richard Ausborne", "Henry Betzer", "Nicholas Tisborne", "Edward Morthon", "Robert Reygenholt", "William Bateman", "Robert Meri", "Robert Dene", "Thomas Distfelt", "Ralph Warinthun", "Thomas Bruns", "Augustin Hindt", "John Martini", "John Pappham", "Maryn Capella", "William Cassellin", "Hamnoth Hammekottes", "Hermann Iserhell", "Conrad Kock"],
        "goods_mentioned": ["pepper", "mace", "cinnamon", "hemp", "canvas", "linen cloth", "thread", "silk", "sugarloaves", "oil", "rape oil", "hops", "rumbi", "cloth", "furs", "garments", "kettles", "dyestuffs", "haberdashery"],
        "notable": True,
        "notable_reason": "The definitive legal closure document for the entire case: a sworn public instrument before the Lübeck council in which the English attorney formally acquits Lübeck of all liability, referencing Emperor Charles V's reign and employing full notarial Latin formulae, making it the most legally significant document in the collection.",
    },
    49: {
        "summary": "A notarial instrument dated 9 April 1534 in which Richard Plunthon, acting as attorney for English merchants, formally acknowledges before the Lübeck council that he has received back a large collection of goods seized from Adrian Johnson's hoy in August 1533. The document lists 35 numbered items belonging to named English merchants and includes a full sworn quitclaim releasing Lübeck from all further liability for the seizure. It was drawn up by notary Michael Petri and is described as a copy checked against the original.",
        "type": "legal_instrument",
        "themes": ["trade", "piracy", "legal_proceedings", "cargo", "compensation", "maritime", "goods_seizure", "restitution", "notarial", "testimony", "textile_trade", "spice_trade", "food_trade", "personal_property"],
        "people_mentioned": ["Richard Plunthon", "Charles V", "John Westborri", "Robert Meredi", "John Edward", "John Gherholt", "Richard Wilsun", "John Practor", "Henry Augustyn", "William Lock", "William Kolsel", "Robert Laurentii", "Anthony Serene", "Richard Ousborne", "Henry Betzer", "Nicholas Tysborne", "Edward Morton", "Reynenholt", "William Bateman", "Robert Meri", "Robert Dene", "Thomas Dystfelt", "Augustine Hindt", "Rodolph Warynthun", "Thomas Bruns", "John Martini", "John Pappham", "Maryn Capella", "William Cassellyn", "Hammot Hammetrottes", "Hermann Schuten", "Godhard Engelsteden", "Joachim Gherkens", "Hermann Iserahel", "Conrad Kock", "Michael Petri"],
        "goods_mentioned": ["bales of says", "bales of arras cloth", "dry cask of miscellaneous merchandise", "chest of cypress goods", "bales of sardock cloth", "pepper", "yarn", "mace", "camlots", "sturgeon", "linen cloth", "raw silk", "coarse linen canvas (kannefust)", "cinnamon", "hemp", "rape oil", "olive oil", "hops", "sugar loaves", "red stones", "dyestuff leaves", "iron fittings for cauldrons", "garments", "chests", "letters"],
        "notable": True,
        "notable_reason": "The most detailed surviving Latin quitclaim for goods from Adrian Johnson's hoy, listing 35 individual items with named English merchant owners, quantities, values in Flemish pounds and sterling, and a complete sworn release — a key primary source for the cargo composition and the legal resolution of the seizure.",
    },
    50: {
        "summary": "A document title entry in Low German recording that Richard Plunthon acknowledged receiving from Lübeck councillor Tyle Thegetmeyger, by order of the council, one great vat of oil and eight pipes of oil belonging to William Cassellyn, plus fifteen small tuns of rape oil and three sacks of hops belonging to Homont Hametrettes of London. No full text survives beyond the title.",
        "type": "receipt",
        "themes": ["trade", "legal_proceedings", "cargo", "restitution", "goods_seizure", "maritime", "food_trade"],
        "people_mentioned": ["Richard Plunthon", "Tyle Thegetmeyger", "William Cassellyn", "Homont Hametrettes"],
        "goods_mentioned": ["olive oil", "rape oil", "hops"],
        "notable": False,
    },
    51: {
        "summary": "A Low German translation of three separate quitclaim instruments — for Anthonius Oberomiza (Venetian), Martinus de Federigo (Venetian, represented by Oberomiza), and Richard Plunthon (for numerous English merchants) — prepared for the Lübeck council and recording the restitution of goods seized from Adrian Johnson's hoy. It provides itemised inventories with merchant marks, cloth types, weights and values, and notes that Oberomiza received a cash settlement for goods that sank with the ship. The document was attested throughout by notary Michael Petri.",
        "type": "legal_instrument",
        "themes": ["trade", "piracy", "legal_proceedings", "cargo", "compensation", "maritime", "diplomacy", "goods_seizure", "restitution", "notarial", "testimony", "textile_trade", "spice_trade", "food_trade", "personal_property", "financial"],
        "people_mentioned": ["Anthonius Oberomiza", "Martinus de Federigo", "Richard Plunthon", "Clawes Bardewick", "Hermen Schute", "Michael Petri", "Laurens Wellmes", "Hermen Mollers", "Ghert Falcken", "Hinrick Cordes", "Johan Westborre", "Rubbert Meredi", "Johan Eduwarth", "Johan Gerholt", "Richard Wilsun", "Johan Practor", "Hinrick Augustyn", "Wilhelm Lock", "Wilhelm Colsen", "Wilhelm Grosshen", "Anthonio Serene", "Rubbert Laurens", "Richard Au\u00dfborne", "Hinrick Beger", "Nicolaus Tisborne", "Eduwartus Mortson", "Rubbert Reyneholt", "Wilhelm Bateman", "Wilhelm Meri", "Rubbert Den", "Thomas Bruns", "Augustin Hindt", "Raff Warynthun", "Johan Martins", "Johan Pappham", "Maryn Capella", "Nicolaus Tysborne", "Wilhelm Cassellen", "Hamont Hammetrottes", "Gotken Engelsteden", "Albert Clever", "Thyle Thegetmeyger", "Hinrick Warmbake", "Jasper van Dalen", "Henry VIII"],
        "goods_mentioned": ["says", "arras cloth", "cypress goods", "sardock cloth", "camlots", "sturgeon", "linen cloth (louwent)", "pepper", "yarn", "mace", "kannefast canvas", "hemp", "kettle-bands", "Ulm sardock", "cinnamon", "frieze cloth", "red stones", "dyestuff leaves", "silk", "haberdashery", "sugar loaves", "olive oil", "rape oil", "hops", "stone pots", "tin pots", "bells", "mirrors", "holy figure", "platters", "candlesticks", "basins", "compasses", "hammers", "tongs"],
        "notable": True,
        "notable_reason": "The most comprehensive single document in the collection, consolidating the quitclaims of all three claimant parties — two Venetian merchants and a representative of English merchants — with full itemised inventories and merchant marks; it also uniquely records that some of Oberomiza's goods sank with the ship and were settled by a cash payment, illustrating the full range of mechanisms used to resolve the seizure.",
    },
    52: {
        "summary": "A notarial instrument drawn up in London on 3 February 1533/34 by public notary Edward Barbour, in which the Venetian merchant Martinus de Federigo formally appoints his fellow Venetian Anthonius Oberomiza as his attorney with full powers to recover a bale of raw silk (weighing 164 pounds) and a small bundle of two dozen handkerchiefs seized from Adrian Johnson's vessel by Lübeck pirates. The document grants Oberomiza sweeping legal authority including the power to sue, compound, and issue quitclaims on de Federigo's behalf.",
        "type": "legal_instrument",
        "themes": ["trade", "piracy", "legal_proceedings", "cargo", "goods_seizure", "restitution", "notarial", "maritime", "textile_trade", "personal_property"],
        "people_mentioned": ["Martinus de Frederigo", "Anthonium Obromiza", "Edward Barbour", "John Anthonio Negro", "Hieronimo de Mezi", "Adrian Johnson"],
        "goods_mentioned": ["raw silk (Talanna)", "handkerchiefs"],
        "notable": True,
        "notable_reason": "One of the few documents explicitly describing Lübeck's agents as \"sea-pirates\" (maris piratos) rather than the more neutral \"privateers,\" and the only instrument establishing the formal legal chain of authority by which a Venetian merchant pursued restitution through English notarial channels; it also identifies the precise cargo value (£70 sterling) and weight of the silk.",
    },
    53: {
        "summary": "A certificate of authentication issued by Christopher Ascue, knight and mayor of London, on 4 February 1533/34, attesting to the good standing and apostolic authority of notary Edward Barbour and validating the notarial instrument of appointment (Doc 52) attached to it. The document requests that all parties give full faith to the instrument wherever it is presented.",
        "type": "certificate",
        "themes": ["legal_proceedings", "notarial", "diplomacy", "restitution"],
        "people_mentioned": ["Christopher Ascue", "Edward Barboure", "Michael Petri", "Henry VIII"],
        "goods_mentioned": [],
        "notable": True,
        "notable_reason": "Provides direct evidence of the involvement of London civic authorities in authenticating documents for use in continental legal proceedings; the mayoral seal and the explicit invocation of Henry VIII's regnal year also make this a useful diplomatic and administrative source linking English royal government to the restitution process.",
    },
    54: {
        "summary": "A Low German quitclaim instrument dated 12 March 1534 in Lübeck, in which Anthonius Oberomiza, Venetian merchant resident in London, acknowledges before Lübeck councillors Clawes Bardewick and Hermen Schute the return of his goods seized from Adrian Johnson's hoy. He swears the goods belong to him alone and not to any Hollander or ally of Lübeck's enemies; for items that sank with the ship or were otherwise unrecoverable, he accepted a cash settlement paid by councillors Gotken Engelsteden and Albert Clever, and issued a full perpetual quitclaim to Lübeck.",
        "type": "legal_instrument",
        "themes": ["trade", "piracy", "legal_proceedings", "cargo", "compensation", "maritime", "goods_seizure", "restitution", "notarial", "testimony", "financial", "personal_property"],
        "people_mentioned": ["Anthonius Oberomiza", "Clawes Bardewick", "Hermen Schute", "Michael Petri", "Hinrick Cordes", "Laurens Wilmers", "Hermen Mollers", "Gerth Falcken", "Gotken Engelsteden", "Albert Clever", "Adrian Johnson"],
        "goods_mentioned": ["stone pots", "tin pots", "bells", "mirrors", "holy figure", "platters", "candlesticks", "basins", "compasses", "hammers", "tongs"],
        "notable": True,
        "notable_reason": "The only document to record a cash settlement for goods that physically sank with the ship, illustrating that restitution extended beyond recoverable goods to financial compensation; the eclectic inventory of small metalwares and household objects (pots, bells, mirrors, candlesticks, compasses, hammers) is also distinctive and throws light on the range of goods being traded through Antwerp in 1533.",
    },
    55: {
        "summary": "A notarial quitclaim recorded in Lübeck in March 1534, documenting the return of one bale of silk to Anthonius Oberomiza acting as procurator for Martin de Federigo, a Venetian merchant resident in London, whose goods had been seized from Adrian Johansen's hoy. Upon receipt of the bale, Oberomiza formally released the council and citizens of Lübeck from all further claims in the matter.",
        "type": "legal_instrument",
        "themes": ["trade", "piracy", "legal_proceedings", "cargo", "restitution", "maritime", "notarial", "goods_seizure", "testimony"],
        "people_mentioned": ["Anthonius Oberomiza", "Martin de Federigo", "Claus Bardewick", "Hermann Schute", "Michael Petri", "Hinrick Cordes", "Laurens Wilmes", "Herman Moller", "Ghert Falcken", "Adrian Johansen"],
        "goods_mentioned": ["bale of silk"],
        "notable": False,
    },
    56: {
        "summary": "A detailed notarial instrument drawn up by Michael Petri on 31 March 1534, recording the full settlement between Anthonius Oberomiza (a Venetian merchant based in London) and the Lübeck council for goods seized from Adrian Johansen's hoy by Lübeck mercenary soldiers in August 1533. The instrument records both the return of specific seized goods and a supplementary cash payment of 25 Rhenish florins for items lost or missing, along with a comprehensive quitclaim and oath never to pursue further claims.",
        "type": "legal_instrument",
        "themes": ["trade", "piracy", "legal_proceedings", "cargo", "restitution", "maritime", "notarial", "goods_seizure", "compensation", "financial", "testimony"],
        "people_mentioned": ["Anthonius Oberomiza", "Martin de Federigo", "Charles V", "Henry VIII", "Godehard Engelstede", "Albert Clever", "Nicholas Bardewick", "Hermann Schute", "Michael Petri", "Johannes Proth", "Joachim Sevelt", "Johannes Vorhorde", "Thomas Dusterhusen", "Simon Schulren", "Adrian Johansen"],
        "goods_mentioned": ["raw silk (Talanna)", "stoneware jugs", "tin cups", "small bells", "campanellas", "mirrors", "tin dishes", "candlesticks", "silk bristle brushes", "iron rings", "iron hammers", "iron tongs"],
        "notable": True,
        "notable_reason": "Exceptionally detailed inventory of seized goods combined with a cash compensation settlement; explicitly acknowledges that Lübeck's mercenary soldiers acted without the council's consent, and invokes the authority of both Emperor Charles V and King Henry VIII of England in the diplomatic resolution.",
    },
    57: {
        "summary": "A Latin copy of the same notarial instrument as Doc 56, drawn up by Michael Petri and covering the identical settlement between Anthonius Oberomiza and the Lübeck council, with the same inventory of goods and 25 Rhenish florin compensation payment. The document notes that this copy was personally compared and collated against the original by the notary, and differs from Doc 56 in that it was written in Michael Petri's own hand rather than by another.",
        "type": "legal_instrument",
        "themes": ["trade", "piracy", "legal_proceedings", "cargo", "restitution", "maritime", "notarial", "goods_seizure", "compensation", "financial", "testimony"],
        "people_mentioned": ["Anthonius Oberomiza", "Martin de Federigo", "Charles V", "Henry VIII", "Godehard Engelstede", "Albert Clever", "Nicholas Bardewick", "Hermann Schute", "Michael Petri", "Johannes Proth", "Joachim Sevelt", "Johannes Vorhorde", "Thomas Dusterhusen", "Simon Schulren", "Adrian Johansen"],
        "goods_mentioned": ["raw silk (Talanna)", "stoneware jugs", "tin cups", "small bells", "campanellas", "mirrors", "tin dishes", "candlesticks", "silk bristle brushes", "iron rings", "iron hammers", "iron tongs"],
        "notable": True,
        "notable_reason": "Latin copy of the same settlement instrument as Doc 56, certified by the notary as matching the original; the existence of both a Low German and a Latin copy underscores the document's legal importance and the multinational parties involved.",
    },
    58: {
        "summary": "A letter of October 1533 from the Burgomaster and Council of Cologne to the Council of Lübeck, introducing Jacob van Mulheim as the authorised plenipotentiary of six named Cologne merchants whose goods were aboard Adrian Johansen's ship and had ended up in Lübeck. Cologne requests Lübeck's cooperation in releasing the goods to their agent, appealing to Hanseatic solidarity and mutual goodwill.",
        "type": "letter",
        "themes": ["trade", "legal_proceedings", "cargo", "maritime", "diplomacy", "goods_seizure", "restitution"],
        "people_mentioned": ["Jacob van Mulheim", "Johann Campman", "Peter Heynebach", "Hermann Suyderman", "Dirk Horner", "Peter Slootkenn", "Johann Borner", "Adrian Janssoon"],
        "goods_mentioned": [],
        "notable": True,
        "notable_reason": "Demonstrates the diplomatic and institutional dimension of the case, showing Cologne formally invoking Hanseatic League solidarity to secure restitution for its merchants; one of the few documents in this set originating from a city authority rather than from Lübeck itself.",
    },
    59: {
        "summary": "A notarial inventory dated 19 October 1533 listing eight packages of goods belonging to Hanseatic merchants of the Cologne Third that were found aboard Adrian Johansen's ship, drawn up at Lübeck in the presence of councillors Nicholas Bardewick and Hermann Schute and facilitated by Henning Kulemeiger, secretary of the London Steelyard. Goods are identified by merchant marks and include fustian cloth, brass wire, silk, haberdashery, and saws.",
        "type": "inventory",
        "themes": ["trade", "cargo", "legal_proceedings", "maritime", "goods_seizure", "notarial", "textile_trade"],
        "people_mentioned": ["Nicholas Bardewick", "Hermann Schute", "Henning Kulemeiger", "Hinrick Kordes", "Tyle Lutguwe", "Nicholas Klone", "Adrian Johansen"],
        "goods_mentioned": ["Osnabr\u00fcck fustian", "brass wire", "silk", "haberdashery goods", "saws"],
        "notable": True,
        "notable_reason": "Provides a concrete itemised record of Hanseatic merchant goods seized from the ship, with reference to the London Steelyard's involvement in the recovery process, illustrating the transnational commercial networks disrupted by the privateering action.",
    },
    60: {
        "summary": "A brief notarial record from 20 October 1533, documenting the opening and inspection of a single cask found in Adrian Johansen's ship at Lübeck, which was found to contain paper-wrapped bundles and a small linen purse with money. The cask was then resealed and authenticated with a merchant mark, with the proceedings attested by three citizen witnesses and notary Nicholas Klone.",
        "type": "inventory",
        "themes": ["trade", "cargo", "legal_proceedings", "maritime", "goods_seizure", "notarial", "financial", "personal_property"],
        "people_mentioned": ["Henning Kulemeier", "Nicholas Bardewick", "Hermann Schute", "Marcus Luthmar", "Sivert Kock", "Claus Haselouwe", "Nicholas Klone", "Peter Slotkyn"],
        "goods_mentioned": ["linen purse", "money"],
        "notable": True,
        "notable_reason": "The discovery of a linen purse containing money inside a sealed cask is a rare detail of personal or liquid assets being transported alongside commercial cargo, and the careful resealing and authentication of the cask reflects the council's procedural diligence in preserving merchant property.",
    },
    61: {
        "summary": "A notarially authenticated inventory, drawn up in November 1533, of goods belonging to several Cologne merchants that were unloaded from Adrian Johnson's seized ship and stored in a Lübeck warehouse. The document records specific items including silk, woolen cloth, glassware, copper wire, currency (sun-crowns and angel-nobles), and personal effects, with each lot identified by a merchant's mark.",
        "type": "inventory",
        "themes": ["trade", "piracy", "legal_proceedings", "cargo", "goods_seizure", "maritime", "notarial", "financial", "personal_property"],
        "people_mentioned": ["Jacob von der Mulln", "Nicolas Bardewick", "Hermann Schute", "Nicholas Klne", "Johann Borne", "Johann Kamman", "Dirick Horner", "Peter Sclotzke", "Peter Heinebach", "Hermen Suderman", "Albert Kleve", "Adrian Johanssen", "Hinrick Krons"],
        "goods_mentioned": ["silk bundles", "sardoc (woolen cloth)", "glassware", "slaughter-cloth", "copper wire", "sun-crowns (\u00e9cu au soleil)", "angel-nobles (English gold coins)"],
        "notable": True,
        "notable_reason": "Unique record of gold coins (both French sun-crowns and English angel-nobles) found hidden within a linen parcel among seized cargo, providing rare evidence of specie being smuggled or transported aboard merchant vessels.",
    },
    62: {
        "summary": "An undated letter from an unnamed Cologne merchant to Johann Borne requesting him, upon arriving in Lübeck, to press for the return of a tun of personal clothing and goods belonging to a young merchant recently settled in England. The letter provides a detailed itemized list of the clothing contents of the tun and promises a gratuity for success.",
        "type": "letter",
        "themes": ["goods_seizure", "restitution", "personal_property", "textile_trade", "diplomacy"],
        "people_mentioned": ["Johann Borne", "Johan Borne"],
        "goods_mentioned": ["taffeta English underskirt", "black worsted doublet", "black sardonet doublet", "black hose", "cotton camlet collar", "black leather collar", "black pelts", "shirts", "shoes", "wooden kitchen pots", "books", "fine cloths"],
        "notable": False,
    },
    63: {
        "summary": "A brief receipt dated 27 September 1533, recording that Heinrich Houwide, a citizen of Bremen, received eleven bales of goods and two bales of almonds from the seized cargo of Adrian Johnson's ship, with the release authorized by the Lübeck council and witnessed by councillors Bardewick and Schute. The almonds were received on behalf of a merchant named Albert Kreien.",
        "type": "receipt",
        "themes": ["goods_seizure", "restitution", "cargo", "legal_proceedings", "food_trade", "maritime"],
        "people_mentioned": ["Hinrick Houwide", "Nicolaus Bardewick", "Hermen Schuten", "Albert Kreien", "Hinrick Kordes", "Tyle Lutzouwe", "Nicolaus Klone"],
        "goods_mentioned": ["bales (unspecified contents)", "almonds"],
        "notable": False,
    },
    64: {
        "summary": "A letter from Hieronymus Molhusen of Lübeck to councillor Hermann Schute, seeking assistance in recovering goods belonging to Roleff Vos (a Hanse-born merchant from Deventer) and an unnamed merchant from Wesel, both seized from Adrian Johnson's ship. Molhusen holds powers of attorney for both men and notes that a Cologne representative has already retrieved some goods, prompting urgency regarding the remaining lots.",
        "type": "letter",
        "themes": ["goods_seizure", "restitution", "legal_proceedings", "trade", "maritime", "diplomacy", "textile_trade"],
        "people_mentioned": ["Hieronymus Molhusen", "Harmen Schute", "Roleff Vos", "Marcus Meyger", "Hynrick im Wynckel"],
        "goods_mentioned": ["Bruges satin", "dry cask contents (unspecified)", "chest contents (unspecified)"],
        "notable": True,
        "notable_reason": "Explicitly names Lübeck's privateers as the agents of seizure and references the broader network of legal powers of attorney and merchant representatives operating across London, Lübeck, and Cologne to recover goods, illustrating the transnational legal mechanisms mobilized in response to the seizure.",
    },
    65: {
        "summary": "A memorandum dated 1 June 1534 recording that Lübeck councillor Hermann Schute, acting on the council's behalf, handed over a merchandise cask and a chest of goods belonging to Richard Engelbarth (a Hanseatic merchant in England) to Master Johan Vorhorde, who was accompanying the Lübeck ambassadors to the English king. Vorhorde formally undertook to deliver the goods to Engelbarth.",
        "type": "memorandum",
        "themes": ["restitution", "diplomacy", "trade", "maritime", "legal_proceedings"],
        "people_mentioned": ["Hermann Schute", "Johan Vorhorde", "Gerth Odingborg", "Hans van Elphram", "Richard Engelbarth"],
        "goods_mentioned": ["dry merchandise cask", "chest/bale (contents unspecified)"],
        "notable": True,
        "notable_reason": "Directly links the restitution of seized goods to a formal diplomatic embassy sent by Lübeck to the English crown, demonstrating that the recovery of individual merchants' property was folded into high-level state diplomacy.",
    },
    66: {
        "summary": "A notarial deposition made on 20 September 1533 in London before notary John Devereux, in which five London merchants and citizens — Robert Pagiet, Thomas Gale, Robert Wilford, Ralph Foxley, and William Wilford — individually swore on oath to the precise contents of their goods loaded aboard the ship Christopher of Moros bound for Galicia in August 1533, prior to its capture. The deposition meticulously records the colors, lengths, and markings of numerous woolen cloths, and also reveals that the merchants had taken out customs cockets in a false name out of fear of Scottish raiders.",
        "type": "deposition",
        "themes": ["trade", "legal_proceedings", "cargo", "goods_seizure", "testimony", "notarial", "maritime", "textile_trade", "financial"],
        "people_mentioned": ["Robert Pagiet", "Thomas Gale", "Robert Wilford", "Ralph Foxley", "William Wilford", "Johannes Shewards (Shewars/Sewars)", "Geoffrey Vaughan", "John Joyce", "Richard Gryg", "John Devereux"],
        "goods_mentioned": ["linen packs", "woolen cloths (blue", "violet", "vesset", "red", "muster", "green medley", "russet", "plunket", "tawny", "medley)", "Northern dozens", "puke cloth", "russet cloth", "buckram wrapper", "bargelot"],
        "notable": True,
        "notable_reason": "The deponents openly admit to fraudulent customs documentation (cockets issued in a false name to avoid Scottish ships), providing rare direct evidence of merchants deliberately falsifying official records — a legally significant admission embedded within an otherwise routine sworn deposition.",
    },
    67: {
        "summary": "A brief inventory, signed by Lübeck councillor Hans Sengesaken and dated 2 November 1533, listing goods from the captured Spanish ship Christopher de Moria currently in custody of Kort Meyneken in Hamburg's inner harbor. Two identical copies were produced, one for Lübeck and one to accompany the secretary of the London Hanseatic Kontor.",
        "type": "inventory",
        "themes": ["piracy", "cargo", "goods_seizure", "maritime", "legal_proceedings", "trade"],
        "people_mentioned": ["Hans Sengesaken (Senghstake/Segestaken)", "Henning Kulemeyer", "Kort Meyneken"],
        "goods_mentioned": ["saws", "tin vessels", "flax", "basket", "chests"],
        "notable": False,
    },
    68: {
        "summary": "An undated itemized inventory of personal goods found in chests belonging to the Spanish mariners of the Christopher de Moria, organized by letter-labeled lots and currently held by Korth Meyken in Hamburg. The contents are predominantly clothing, textiles, personal effects, and tin tableware, with some navigation instruments (charts and compasses) included, and one section attributed to a named individual, Reymar Otten.",
        "type": "inventory",
        "themes": ["cargo", "goods_seizure", "maritime", "personal_property", "textile_trade"],
        "people_mentioned": ["Korth Meyken", "Reymar Otten"],
        "goods_mentioned": ["English woolen cloth", "knotted sleeves", "English cloak", "shirts", "grey English cloth", "tin saltcellars", "compasses", "pelt cloth", "ruddock cloth", "grey coats", "hose", "beret", "Spanish caps", "Castilian leather pouches", "tin jugs", "sea charts", "gold-decorated items", "grey cloaks", "doublets", "Scottish cloth", "tin wash-basins", "tin bowls", "brass candlesticks", "brass mortar", "plush cloth", "damask cloth", "red English cloth", "white English cloth", "Spanish bows", "saws", "mirrors", "bonnets", "ruffs"],
        "notable": True,
        "notable_reason": "The inventory of Spanish mariners' personal chest contents is unusually granular, preserving details of individual sailors' clothing and possessions including navigation equipment (charts, compasses) and Spanish bows, offering rare insight into the material culture of 16th-century Iberian maritime crews.",
    },
    69: {
        "summary": "A notarial instrument dated 7 April 1534 in Hamburg recording the settlement between Spanish merchants and the Lübeck council for goods seized from the Spanish carvel Christopher in the summer of 1533 off the English coast. The Spanish plenipotentiaries Alphonsus de Sancto Joan and Joan de Lusis acknowledge full receipt of compensation totalling 1,230 marks Lübeck currency for the ship's sale, plus 100 marks for personal goods, and a further sum covering cloth, hides, flax, tin vessels, oil, and salt. All claims against Lübeck are declared satisfied.",
        "type": "legal_instrument",
        "themes": ["trade", "piracy", "legal_proceedings", "cargo", "compensation", "maritime", "diplomacy", "restitution", "notarial", "goods_seizure"],
        "people_mentioned": ["Johannes Kloth alias Platen", "Johannes Hulpp", "Alphonsus de Sancto Johan", "Joan de Lusis", "Albert de Astudillo", "Ferdinand de Verdese", "Johannes de Arabiano", "Joannes de Bewariis", "Johannes Hoper", "Joachim Gherkens", "Johannes de Lennepen", "Jodocus Burhorne", "Sebastianus de Winthen", "Michael Petri"],
        "goods_mentioned": ["bales of cloth", "hides", "flax", "tin vessels", "clothing", "Lisbon oil", "Brouage salt"],
        "notable": True,
        "notable_reason": "This is the formal settlement document closing all Spanish claims against Lübeck for the 1533 seizure, providing an itemised record of compensation and functioning as a comprehensive legal release — a key instrument in the entire case.",
    },
    70: {
        "summary": "A receipt document in which the Spanish shipmaster Johannes de Lusis and procurator Alphonsus de Sancto Joan, acting also on behalf of Joan Bewariis of Muros, acknowledge receiving compensation from Lübeck proconsul Joachim Gherkens at the Hamburg proceedings for goods seized from the ship Christophorus. The document is fragmentary, breaking off mid-sentence before specifying the full sum or goods list.",
        "type": "receipt",
        "themes": ["trade", "piracy", "legal_proceedings", "compensation", "maritime", "restitution", "goods_seizure"],
        "people_mentioned": ["Johannes de Lusis", "Alphonsus de Sancto Joan", "Joan Bewariis", "Joachim Gherkens", "Johannes de Lennepen"],
        "goods_mentioned": [],
        "notable": False,
    },
    71: {
        "summary": "A continuation fragment and then a separate receipt in which Alphonsus de Sancto Joan, acting as procurator for Albert de Astudilla, Ferdinand de Verdese, and Johannes de Arabiano, acknowledges receipt in Hamburg of specific seized goods — 79 bales of cloth, flax, hides, tin vessels, chests with clothing, casks of Lisbon oil, and Brouage salt — from Lübeck representatives Joachim Gherkens and Johannes de Lennepen. He declares all claims satisfied and seals the quitclaim with his own signet, attested by notary Michael Petri.",
        "type": "receipt",
        "themes": ["trade", "piracy", "legal_proceedings", "cargo", "compensation", "maritime", "restitution", "notarial", "goods_seizure"],
        "people_mentioned": ["Johannes de Lennepen", "Joan de Lusis", "Alphonsus de Sancto Joan", "Albert de Astudilla", "Ferdinand de Verdese", "Johannes de Arabiano", "Joachim Gherkens", "Michael Petri"],
        "goods_mentioned": ["bales of cloth", "flax", "hides", "tin vessels", "clothing", "Lisbon oil", "Brouage salt"],
        "notable": False,
    },
    72: {
        "summary": "A notarial instrument drawn up by London notary John Devereux on 20 September 1533, recording sworn depositions by Thomas Cole and Simon Briganden, both London merchant tailors, regarding cloth they had loaded onto the Spanish ship Maria de Gatalope in July 1533. Each deponent provides an extremely detailed inventory of their bales — specifying cloth type, colour, and yardage for every piece — and both admit they had the bills of lading written in foreign names solely out of fear of Scottish warships.",
        "type": "deposition",
        "themes": ["trade", "legal_proceedings", "cargo", "maritime", "testimony", "goods_seizure", "textile_trade", "notarial"],
        "people_mentioned": ["Thomas Cole", "Simon Briganden", "John Devereux", "Johannes de Calegio", "Francis Maswelle", "Peter de Berevey", "John Banckes", "Ralph Foxley"],
        "goods_mentioned": ["woollen cloths", "cotton wrappings", "green cloth", "visset cloth", "red cloth", "horseflesh cloth", "russet cloth", "tawny cloth", "blue cloth", "musterdevillers", "violet cloth", "yellow cloth", "plunket cloth", "medley cloth", "kennet cloth", "silk girdles"],
        "notable": True,
        "notable_reason": "This document provides an exceptionally granular itemised inventory of individual cloth pieces with colours, yardages, and merchant marks, and contains the notable admission that bills of lading were falsified under foreign names to avoid Scottish privateers — shedding light on routine deceptive practices in 1530s English maritime trade.",
    },
    73: {
        "summary": "A Middle Low German translation of sworn depositions by ten London merchants and factors — including John Hampton, Humphrey Knight, Thomas Blanke, Thomas Cole, Simon Briganden, Robert Pagiet, Thomas Gale, Robert Wilfordt, Ralph Voxley, and William Wilfordt — each itemising goods they had loaded onto vessels seized by Lübeck warships in 1533. The goods range from woollen cloth (described in minute detail by colour, length, and merchant mark) to salt, salt fish, silk girdles, flax, and personal cash. Several deponents admit to falsifying bills of lading under foreign names to evade Scottish warships.",
        "type": "deposition",
        "themes": ["trade", "piracy", "legal_proceedings", "cargo", "maritime", "testimony", "goods_seizure", "textile_trade", "food_trade", "financial", "notarial"],
        "people_mentioned": ["John Hampton", "Johannes Bryngborne", "Johannes Williamson", "Humphrey Knight", "Thomas Wakeham", "Adrian van Sterree", "Thomas Blanke", "Gilbert Pervissche", "Thomas Cole", "Francis Maswelle", "Simon Briganden", "Robert Pagiet", "Thomas Gale", "Robert Wilfordt", "Ralph Voxley", "William Wilfordt", "Ralph Foxley", "Geoffrey Vaughan", "Johannes de Calegio", "Johannes Shewars", "Johannes Sewars"],
        "goods_mentioned": ["brown salt", "castle stones", "salt fish", "silk girdles", "woollen cloth", "cotton wrappings", "flax", "short cloths", "statute bloody cloth", "Northern dozens", "puke cloth", "russet cloth", "buckram", "baize", "cash money"],
        "notable": True,
        "notable_reason": "This is the most comprehensive witness compilation in the collection, aggregating ten separate sworn testimonies with minute cloth inventories (colours, yardages, individual merchant marks) and covering multiple seized vessels; it also independently corroborates the practice of bill-of-lading fraud to avoid Scottish warships.",
    },
    74: {
        "summary": "An indenture dated 2 November 1533, drawn up in Hamburg in the presence of Lübeck mayor Johann Sengestake and Gosslick Remmynctotes, recording a storage agreement between the Lübeck council and Mathias van Ryne for safekeeping the seized Spanish goods. It specifies a quarterly fee structure — 4 shillings per large pack, 2 shillings per small pack, per dicker of hides, and for the flax bundle — and stipulates that Ryne must hold the goods exclusively on Lübeck's authority until further order.",
        "type": "legal_instrument",
        "themes": ["trade", "legal_proceedings", "cargo", "compensation", "maritime", "goods_seizure", "notarial"],
        "people_mentioned": ["Johann Hoper", "Johann Segestaken", "Gosslick Remmynctotes", "Mathias van Ryne"],
        "goods_mentioned": ["bales of cloth", "hides", "flax"],
        "notable": True,
        "notable_reason": "This is the earliest-dated document in the batch (November 1533) and provides rare administrative detail on the immediate custody arrangements for seized goods, including a formal fee schedule — illuminating the logistical and financial mechanics of goods seizure and storage by a privateer-sponsoring city.",
    },
    75: {
        "summary": "Johann Hoper, acting under orders from the Lübeck council, inventories packs of cloth and ox hides held in custody by Mathias van Ryne in Hamburg. The goods, taken by Lübeck privateers from a Spanish ship, are itemised by merchant's mark and include 80 packs of cloth (large and small) and 48 deckers of salted ox hides. The document records the goods pending redistribution once conditions allow sailing.",
        "type": "inventory",
        "themes": ["trade", "piracy", "goods_seizure", "cargo", "maritime", "legal_proceedings", "textile_trade"],
        "people_mentioned": ["Johann Hoper", "Hans Sengestaken", "Goslick Rennerelickrath", "Mathias van Ryne"],
        "goods_mentioned": ["cloth (large packs)", "cloth (small packs)", "salted ox hides"],
        "notable": False,
    },
    76: {
        "summary": "Johann Hoper inventories goods held in custody by Kort Meyneken in Hamburg, taken by Lübeck privateers from a Spanish ship, witnessed by Hans Segestaken and Hennyng Kulemeyer, secretary of the London merchant community. The inventory includes cloth, flax, fine black broadcloth, and Russian or Flemish cloths. Notably, one pack of cloth was retrieved on the Elbe by Nicolaus Raschew, servant of Thomas Galen, and taken to England, and a piece of russet was sold to a court scrivener for 3 gold crowns.",
        "type": "inventory",
        "themes": ["trade", "piracy", "goods_seizure", "cargo", "maritime", "legal_proceedings", "textile_trade", "financial"],
        "people_mentioned": ["Johan Hoper", "Hans Segestaken", "Hennyng Kulemeyer", "Kort Meyneken", "Nicolaus Raschew", "Thomas Galen", "Johann van Horen", "Wyllem Aysche"],
        "goods_mentioned": ["cloth (packs)", "flax", "fine black broadcloth", "Russian or Flemish cloths", "russet cloth"],
        "notable": True,
        "notable_reason": "Records the diversion of a cloth pack to England by a servant of Thomas Galen and the sale of a piece of russet to a named scrivener, providing granular detail about how seized goods were dispersed before formal restitution.",
    },
    77: {
        "summary": "Kordt Meyneke itemises the costs he incurred in Hamburg for handling goods seized from two Spanish ships, including unloading, storage, drying, carting, crane fees, tolls, and warehouse rent, totalling 24 marks 14 shillings. He notes that no payment has yet been received. The document also records delivery of specific goods to named Lübeck and Hamburg councillors, including a piece of black English cloth delivered to councillor Hinrick Rademaker.",
        "type": "receipt",
        "themes": ["trade", "goods_seizure", "cargo", "maritime", "legal_proceedings", "financial", "restitution"],
        "people_mentioned": ["Kordt Meyneke", "Gotschalk Remelckraden", "Joachim Gerken", "Johan Hoper", "Hinrick Moller", "Gerdt Oldenborch", "Johan van Lennepen", "Johan van Horen", "Hinrick Rademaker"],
        "goods_mentioned": ["cloth (packs)", "flax", "chest", "basket", "tin vessels", "black English cloth"],
        "notable": False,
    },
    78: {
        "summary": "On 9 June 1534 in Hamburg, William Ayshe (English attorney) and Lübeck councillors Gerde Oldenbarch and Johan van Lennep appeared before Hamburg councillors Jochim Wullewevere and Hinrick Rademaker to arrange the return of seized goods. The document survives only as a title description, with no substantive text preserved.",
        "type": "legal_instrument",
        "themes": ["restitution", "goods_seizure", "legal_proceedings", "diplomacy", "maritime"],
        "people_mentioned": ["William Ayshe", "Gerde Oldenbarch", "Johan van Lennep", "Jochim Wullewevere", "Hinrick Rademaker"],
        "goods_mentioned": [],
        "notable": True,
        "notable_reason": "The document is fragmentary — only the title survives — making it an archival lacuna of significance for reconstructing the restitution proceedings.",
    },
    79: {
        "summary": "Before notary John Devereux in London, John Hampton of Faversham testifies under oath on behalf of himself and his partner John Bryngborne that their shallop, owned and mastered by John Williamson of Middelburg, was seized near Camber by armed Lübeck ships while carrying 32 weys of brown salt, 5,500 paving tiles, and a chest of goods belonging to their factor. The deposition values the seized cargo at £40 sterling and is made for the preservation of their legal rights.",
        "type": "deposition",
        "themes": ["piracy", "goods_seizure", "legal_proceedings", "testimony", "maritime", "trade", "cargo"],
        "people_mentioned": ["John Hampton", "John Bryngborne", "John Williamson", "John Devereux", "John God", "Richard Braunche"],
        "goods_mentioned": ["brown salt", "paving tiles", "chest with equipment and clothing"],
        "notable": True,
        "notable_reason": "Provides precise notarial testimony identifying the location of seizure (Camber, Surrey), the specific vessel and its Dutch master, and the exact cargo composition, making it a key evidentiary document in the broader legal proceedings.",
    },
    80: {
        "summary": "Before notary John Devereux in London, Humphrey Knyght (fishmonger) and Thomas Blancke (haberdasher) separately depose under oath regarding goods seized from a Flushing shallop captained by Adrian van Sterre by armed Lübeck ships. Knyght testifies that nine of fourteen barrels of salt fish belonging to him were taken, valued at £6 6s Flemish; Blancke testifies that a truss of 48 dozen diaper silk ribbons belonging to him was seized, valued at £14 16s Flemish plus 8s customs.",
        "type": "deposition",
        "themes": ["piracy", "goods_seizure", "legal_proceedings", "testimony", "maritime", "trade", "cargo", "food_trade", "textile_trade", "financial"],
        "people_mentioned": ["Humphrey Knyght", "Thomas Blancke", "Thomas Wakeham", "Adrian van Sterre", "Gilbert Pervisshe", "Walter Champion", "William Sawndirson", "John Devereux"],
        "goods_mentioned": ["salt fish (barrels)", "diaper silk ribbons"],
        "notable": True,
        "notable_reason": "Captures two independent depositions in a single instrument, with named apprentices loading goods on behalf of their masters, and provides specific valuations in Flemish currency for both fish and luxury silk goods seized.",
    },
    81: {
        "summary": "Before notary Michael Petri at Lübeck's lower town hall, Wilhelm Gilbancke of Colchester, servant of English Chancellor Thomas Audley, formally acknowledges receipt of 2½ hundredweight of salt restored by Lübeck, and accepts 125 Lübeck marks as full compensation for all remaining unreturned goods, including half-says cloth, salted cod, sturgeon, canvas, Holland linen, feather-beds, Icelandic fish, and mirrors. He swears a standing oath renouncing all further legal claims against Lübeck and its citizens on behalf of himself and his heirs.",
        "type": "legal_instrument",
        "themes": ["restitution", "goods_seizure", "legal_proceedings", "compensation", "maritime", "diplomacy", "financial", "food_trade", "textile_trade", "personal_property"],
        "people_mentioned": ["Wilhelm Gilbancke", "Thomas Audley (Thomas Artey)", "Thyle Thegetmeyger", "Ciriacus Wolmerstorp", "Jheronimus van Bromse", "Jurgen van Ehelenleys", "Michael Petri"],
        "goods_mentioned": ["salt", "half-says cloth", "salted cod", "sturgeon", "canvas", "Holland linen cloth", "feather-beds", "Icelandic fish", "hogsuckers", "ling (langen)", "mirrors"],
        "notable": True,
        "notable_reason": "The only document in this batch recording a formal, sworn quitclaim and settlement, naming the English Lord Chancellor Thomas Audley as the patron whose favour prompted Lübeck's generosity, and providing a detailed list of unreturned goods together with the precise cash settlement figure.",
    },
    82: {
        "summary": "Johann Hoper compiles a memorandum summarising goods lost from three seized ships — those of skippers Williamson, Adrian van Sterre, and Johann van Calessio (the Maria van Gatalope) — with valuations, held in Hamburg under his orders. The document acknowledges that the fate of goods from additional vessels, including one that was sunk, remains unknown. Hoper concludes with a warning that these matters must be carefully monitored to prevent further damage.",
        "type": "memorandum",
        "themes": ["piracy", "goods_seizure", "cargo", "maritime", "legal_proceedings", "financial", "trade", "food_trade", "textile_trade"],
        "people_mentioned": ["Johann Hoper", "Johann van Calessio"],
        "goods_mentioned": ["brown salt", "paving stones", "chest with equipment and clothing", "salted fish", "silk ribbons", "chest of money and household goods"],
        "notable": True,
        "notable_reason": "Synthesises losses across multiple seized vessels including one that was sunk, and explicitly flags uncertainty about the disposition of further goods, making it a key administrative overview document in the restitution proceedings.",
    },
}


# --- Load and update documents.json ---
with open("documents.json", "r", encoding="utf-8") as f:
    documents = json.load(f)

for doc in documents:
    did = doc["id"]
    if did in enrichments:
        e = enrichments[did]
        doc["summary"] = e["summary"]
        doc["document_type"] = e["type"]
        doc["themes"] = e["themes"]
        doc["people_mentioned"] = e["people_mentioned"]
        doc["goods_mentioned"] = e["goods_mentioned"]
        doc["notable"] = e["notable"]
        if e.get("notable_reason"):
            doc["notable_reason"] = e["notable_reason"]

with open("documents.json", "w", encoding="utf-8") as f:
    json.dump(documents, f, indent=2, ensure_ascii=False)

print(f"Updated documents.json with enrichment data for {len(enrichments)} documents")

# --- Update .md files ---
updated = 0
for did, e in enrichments.items():
    md_path = CATALOGUED / f"doc_{did}.md"
    if not md_path.exists():
        print(f"WARNING: {md_path} not found")
        continue

    content = md_path.read_text(encoding="utf-8")

    if "## Summary" in content:
        print(f"  {md_path} already has Summary section, skipping")
        continue

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

    # Insert before the first ## heading after the title
    file_lines = content.split("\n")
    insert_idx = None
    for i, line in enumerate(file_lines):
        if line.startswith("## ") and i > 0:
            insert_idx = i
            break

    if insert_idx is not None:
        file_lines.insert(insert_idx, enrichment_section + "\n")
        md_path.write_text("\n".join(file_lines), encoding="utf-8")
        updated += 1
    else:
        print(f"WARNING: Could not find insertion point in {md_path}")

print(f"Updated {updated} .md files with enrichment sections")
