"""Merge translations into documents.json and update doc .md files."""

import json
from pathlib import Path

CATALOGUED = Path("catalogued")

translations = {
    37: """Copy of the examination and deposition of Adrian Johnson, sailor, etc., before the honourable council of Lübeck.

[1.] In the year etc. 1533, in the 6th indiction, on the 25th day of the month of September, at the instigation of the honourable council, a skipper from Antwerp by the name of Adrian Johnson and Hinrik Kron were summoned in the morning at 7 o'clock to the chancellery by the lords Hinrik Kerchrinck and Herman Schute, appointed by the honourable council for this purpose, in order to examine and hear them — each one separately, however.

[2.] Likewise, first of all, lord Hinrik Kerchrinck put it to the skipper from Antwerp where he was from, what his home was, and where he intended to go with the ship. To this the skipper answered that he was based in Antwerp, was a citizen there, and intended to sail with the ship to England at the instigation of the merchants. Further, the skipper was asked when and at what time Hinrik Kron, the captain, had come to him at sea. To this the skipper said that he had come to him off England, on around the 19th day of the month of August, in the forenoon at around 10 or 11 o'clock, about 3 sea-miles from shore. And if Hinrik Kron had not come to him, he would have run the ship aground and thereby saved all the merchants' goods. Further the skipper was asked in what manner Kron came to him and what he did to him. The skipper answered: he did nothing particular to me, except that he fired a shot fairly high into the sail. Then he [the skipper] had immediately struck [his colours]. Further the skipper was asked when and why he had to transfer the goods from his ship into Kron's bogarde [Note: a type of flat-bottomed river or coastal vessel]. The skipper said the ship took on so much water that it was impossible to save it, since the previous year he had run the ship aground at Ostend in Flanders, from which the ship had received a crack so large that he had had to fill the sides back up again with wainscoting boards; from this he had feared that the ship had sustained another split and that the ship was then beyond saving. So the goods were hoisted with some difficulty from the ship into Kron's bogarde from toward evening until nearly midnight. Finally, the skipper was questioned earnestly and most sharply about money that he was also supposed to have had in his ship, and to whom it belonged. To this the skipper answered and said there was money in two small pouches, of which one pouch had been thrown down into the ship beside the pump while it was still midday, as he still hoped to save both ship and goods. But the other pouch he carried on his person inside his sleeve, until he had to give it to Hinrik Kron. And he counted it out, and it amounted to approximately 34 or 25 pieces of gold. And that same money, as he understood, belonged to a man from Cologne. The letters [i.e. the documents accompanying the cargo] would confirm that, but otherwise he knew of no other money.

[3.] Secondly, Hinrik Kron was asked how he had come to the skipper. To this Hinrik Kron answered that he had been left behind from the fleet by order of the fleet, with his bogarde, overnight near Dawerin [Note: possibly Davryn / the Downs area, off the Kent coast]. There in the morning he set sail, expecting after the departure of the fleet to find the Danes, but since they were not there, he searched further along the coast, where some 26 vessels lay at anchor, but not his own — which is why he sailed away from there; he first obliged the man from Middelburg to strike [his colours] and then fired a shot fairly high into the sail of the man from Antwerp, Adrian Johnson, from a certain ship, who likewise immediately struck and came to him in the small boat he sent to him, coming alongside at around 10 or 11 o'clock in the day. And whatever the skipper might say, if he [Kron] had not come to him, he would not have been able to save a single piece of cargo, the ship took on so much water from midday toward evening. Further Hinrik Kron also said that he had pressed the skipper to hand over some money that was supposed to be in the ship; the skipper took out of his sleeve a small pouch about a finger's length and immediately, in the presence of the skipper, there were counted from it 31 English gold coins called engellotten [Note: English gold angels] and 4 double ducats.

Written within Lübeck at the chancellery there, in the year, day, month and indiction as stated above.

Witnesses: Johan Wilmessen and Johann Hußer, both citizens of Middelburg.

Nicolaus Clone, notary, duly called to the foregoing, wrote this with his own hand.

The present copy has been audited and collated by me, Michael Petri, cleric of the diocese of Schwerin, public notary by apostolic and imperial authority, and it agrees with its original, as attested by my own hand.

---""",
    38: """The copy of such an examination and deposition was translated as follows.

[1.] In the year of the Lord 1533, in the sixth indiction, on the 25th day of the month of September, at the instigation of the honourable council of Lübeck, a certain master of a ship, or sailor, from Antwerp named Adrian Johnson, and Hinrik Kron, captain, were examined and questioned in the morning at the seventh hour in the chancellery of Lübeck — each of those examined being summoned separately — by the honourable lords Hinrik Kerrinck and Hermann Schute, councillors of Lübeck, appointed for this purpose by the honourable council of Lübeck.

[2.] First, the aforesaid lord Hinrik Kerckrinck asked the aforesaid Adrian, master of the ship, where he was from or from what homeland, and where he had intended to sail. To this the same Adrian answered and said that he was from Antwerp and was a citizen there, and that it had been his intention to sail to England at the instigation of merchants. The same Adrian was further asked when and at what time Hinrik Croen, captain of Lübeck, had come to his ship at sea and had approached him. To this the same Adrian, master of the ship, answered and said that he had come to his ship within the bounds or limits of England on the nineteenth day of the month of August, at around the tenth or eleventh hour before noon, three sea-miles from shore. And if the same captain Hinrik Kron had not approached him, he would then have sailed his ship to shore and thus saved all the merchants' goods. The said Adrian was further asked by the said lord Hinrik, councillor, by what means captain Hinrik Kron had approached him and what he had done to him. To this the said Adrian Johnson, sailor, answered that he had done nothing particular to him, except that he had fired at least one shot of a cannon ball fairly high into the sail of the ship, and thus he had at once surrendered. The same Adrian the sailor was still further examined and questioned by the said lord Hinrik the councillor, when and why he had unloaded his goods entrusted to him from his said hoy [Note: a type of small coastal sailing vessel] and re-loaded them onto the ship of captain Hinrik Kron. Then Adrian Johnson answered and said that he had done this for the preservation of the goods existing in his said ship, because his ship had been made so leaky and filled with water that it would be impossible for him to save those goods. For in the previous year he had run his said vessel, named "to the East," aground in Flanders, and on account of this the ship had been damaged and suffered injury, so much so that he was compelled to repair its upper parts with certain planks. From this he concluded that the aforesaid ship had again and afresh received an injury, and since there was no hope of saving it, the aforesaid goods were from evening time until after midnight conveyed from his ship and placed in the ship of the said captain Hinrik. Finally, the same Adrian was solemnly and sharply examined and questioned about certain monies said to be in the said hoy, and to whom those monies belonged. To which question the oft-mentioned Adrian answered and said that it was true that some monies had been in two small pouches, one of which had been thrown down to the bilge-pump of the said ship; and since it had been midday, he had hoped still to keep both ship and goods. But the remaining pouch he had kept with him in his sleeve, until he was compelled to hand it to captain Hinrik Croen. And immediately that money was counted from the said pouch and he stated the number to be thirty-four or twenty-five gold coins (as he himself more truly believed), belonging to a certain man from Cologne; and that the documents would show this clearly, and that he knew of no other monies.

[3.] Likewise, the aforesaid Hinrik Kron was then examined and questioned as to how he had come to the aforesaid Adrian, master of the ship, or had approached him. To which the same captain Hinrik Kron answered and said that he, with his ship commonly called a bogarde, had by order of the Lübeck fleet fallen behind overnight and had stayed near Daveren [Note: the Downs off the Kent coast]. And there in the morning he had prepared to sail, thinking to make for the port of Dunse [Note: possibly Dungeness or the Downs] after the fleet's departure; and when he did not find his fleet there, he searched further along the coast close to shore. And he found another fleet of 26 ships, but not his own. And when he had sailed away from there, he first found a man from Middelburg and compelled him to lower his sail, and consequently one shot of a cannon was then fired fairly high into the sail of the ship of Adrian Johnson, the man from Antwerp, by certain persons, who had likewise immediately surrendered, and the small boat which had been sent toward him came alongside at the tenth or eleventh hour of the day; and let the said Adrian say what he would — if he had not approached him, he would not have saved the least part of his goods, since his said ship had been from midday to evening so leaky and filled with water. Likewise, the same Hinrik Kron further said and stated that he had compelled the aforesaid Adrian, master of the ship, to give over certain monies existing in the said ship, and had received from him from his sleeve a pouch about one finger's length, and had counted those monies from the said pouch in the presence of the said master of the ship, the number therein being thirty-one English gold florins called engellotten and four double ducats, also called dupiones.

[4.] Done at Lübeck, in the chancellery of Lübeck, in the same year, indiction, day, and month as aforesaid, with Johann Wilemessen and Johann Huster, citizens of Middelburg, present there as witnesses, called and requested.

Nicolaus Clone, notary, duly called to the foregoing, wrote this with his own hand.

The present copy has been audited, collated, and diligently translated by me, Michael Petri, cleric of the diocese of Schwerin, public notary by holy apostolic and imperial authority, and it agrees in substance with its original, which I attest with my own hand.

---""",
    39: """[1.] In the year of the Lord 1534 [Note: misdated; should be 1533], in the seventh indiction, on the 25th day of the month of September, at the instigation of the honourable council of Lübeck, a certain master of a ship, or sailor, from Antwerp named Adrian Johnson, and Henrik Croen, captain, were examined and questioned in the morning at the seventh hour in the chancellery of Lübeck — each of them being summoned separately — by the honourable lords Henrik Karckrinck and Hermann Schute, councillors of Lübeck, appointed for this purpose by the honourable council of Lübeck.

[2.] First, the aforesaid lord Henrik Karckrinck asked the aforesaid Adrian, master of the ship, where he was from or from what homeland, and where he had intended to sail. To this he answered and said that he was from Antwerp and was a citizen there, and that it had been his intention to sail to England at the instigation of merchants. The same Adrian, master of the ship, was further asked when and at what time Henrik Croen, captain of Lübeck, had come to his ship and had approached him. To this the same Adrian the sailor answered and said that he had come to his ship within the bounds or limits of England on the nineteenth day of the month of August, at around the tenth or eleventh hour of that day before noon, three sea-miles from shore; and if the same captain Henrik Croen had not approached him, he would then have sailed his ship to shore and thereby would have saved the merchants' goods. He was further asked by the said lord Henrik the councillor, by what means captain Henrik Croen had approached him and what he had done to him. To this the same Adrian Johnson, master of the ship, answered that he had done nothing particular to him, except that he had fired at least one shot of a cannon ball fairly high into the sail of the ship, and thus he had at once surrendered. The same Adrian, master of the ship, was still further examined and questioned by the said lord Henrik, councillor of Lübeck, when and why he had unloaded his goods entrusted to him from his said ship and re-loaded them onto the ship of captain Henrik Croens. Then Adrian answered and said that he had done this for the preservation of the goods existing in his said ship, because his ship had been made so leaky and filled with water that it would be impossible for him to save those goods. For in the previous year he had run his said vessel, named "to the East," aground in Flanders, and on account of this his ship had been damaged and suffered injury, so much so that he was compelled to repair its upper parts with certain planks. From this he concluded that his said ship had again and afresh received an injury, and since there was no hope of saving it, the aforesaid goods were from evening time until after midnight conveyed from his ship and placed in the said captain Henrik's ship. Finally the same Adrian was sharply questioned about certain monies said to be in his said ship, and to whom such monies belonged. To which question the oft-mentioned Adrian answered and said that it was true that some monies had been in two small pouches, one of which he had thrown down to the bilge-pump of the said ship; and since it had been midday, he had hoped still to keep both ship and goods. But the remaining pouch he had kept with him in his sleeve, until he was compelled to hand it to captain Henrik Croon. And immediately that money was counted and he stated the number to be thirty-four or twenty-five gold coins, as he himself more truly believed, belonging to a certain man from Cologne, and that the documents would show this clearly, and that he knew of no other monies.

[3.] Likewise, the aforesaid captain Henrik Croen was then examined and questioned as to how he had come to the aforesaid Adrian, master of the ship, or had approached him. To which the same captain Henrik Croen answered and said that he, with his ship commonly called a bogarde, had by order of the Lübeck fleet fallen behind overnight and had stayed at Daveron [Note: near the Downs], and there in the morning had prepared to sail, expecting after the fleet's departure to make for the port of Dunse [Note: possibly Dungeness or the Downs]; and when he did not find the Lübeck fleet there, he searched further along the coast close to shore, and saw another fleet of twenty-six ships, and did not find his own fleet; and when he had sailed away from there, he first found a man from Middelburg and compelled him to lower his sail, and consequently one shot of a cannon was then fired fairly high into the sail of the ship of Adrian Johnson, the man from Antwerp, who had likewise immediately surrendered, and the small boat had come alongside at the tenth or eleventh hour of the day; and also saying that the said Adrian might say what he wished — if he had not approached him, he would not have saved the least part of his goods, since his said ship had been from midday until evening so leaky and filled with water. Likewise, the same Henrik Croen further said and stated that he had pressed the aforesaid Adrian Johnson, master of the ship, to give over certain monies existing in the said ship, and had received from him from his sleeve a small pouch about one finger's length, and had counted those monies from the said pouch in the presence of the said master of the ship, the number therein being thirty-one English gold florins called angelottes and four double ducats, also called dupiones.

[4.] These matters were transacted at Lübeck, in the chancellery of Lübeck, in the same year, indiction, day, and month as aforesaid, with Johann Wilmessen and Johann Husser, citizens of Middelburg, present there as witnesses, called and requested.

Nicholaus Clove, notary, called to the foregoing, attests and signifies this with his own hand.

The present copy has been audited, collated, and diligently translated by me, Michael Petri, cleric of the diocese of Schwerin, public notary by holy apostolic and imperial authority, and it agrees in substance with its original, which he attests with his own hand.

---""",
    40: """[1.]
William Lok, mercer

Item: shipped in [the vessel of] Adrian Johnson 1 bale containing 65 pieces of camlets [Note: a luxury fabric, often of wool or silk], of which 50 pieces tawny and 15 pieces black. The bale is marked with this mark [merchant's mark no. 1 in the left margin].

My servant told the shipman to enter it in his book in the name of Peter Welsser for fear of meeting any Scottish ships.

[2.]
Robert Meredyth, mercer

Item: shipped in [the vessel of] Adrian Johnson of Antwerp 1 bale of says [Note: a fine woollen or serge cloth] containing 70 pieces, under this mark written in the margin [merchant's mark no. 2 in the left margin], in his book.

[3.]
In [the vessel of] Adrian Johnson

William Mery, grocer

Currants, 3 butts: No. 1, No. 5, No. 7
A pipe containing pepper, 2 bags
A small truss containing cinnamon, 36 lb.
Under this mark in the margin [merchant's mark no. 3 in the left margin].

Anno 1533

[4.] Laden by me, John Proctor of London, merchant tailor, in [the vessel of] Adrian Johnson of Antwerp, a bale of says, assortment 3, containing 38 pieces, under this mark in the margin [merchant's mark no. 4 in the left margin], of the numbers and prices as follows:

No. 1: a piece at 17s 2d
No. 2: a piece at 18s 2d
No. 3: a piece at 19s 2d
No. 4: a piece at 20s 2d
No. 5: a piece at 21s 2d
No. 6: a piece at 22s 2d
No. 7: a piece at 23s 2d
No. 8: a piece at 24s 2d
No. 9: a piece at 25s 2d
No. 10: a piece at 26s 2d
No. 11: a piece at 27s 2d
No. 12: a piece at 28s 2d
No. 13: a piece at 29s 2d
No. 14: a piece at 30s 2d
No. 15: a piece at 31s 2d
No. 16: 2 pieces at £3 4s 4d
No. 17: a piece at 33s 2d
No. 18: 2 pieces at £3 8s 4d
No. 19: 2 pieces at £3 10s 4d
No. 20: 2 pieces at £3 12s 4d

Sum: £10 16s 8d Flemish

Sum: £22 14s 4d

Paid for packing, canvas sheets, porterage, carriage, customs: 6s 2d
So the total that this bale of says costs me on board the said [vessel of] Adrian Johnson, with the costs: £62 19s 4d Flemish. I sent no letter with the shipper nor wrote in his book because of the Scots.

No. 21: a piece at 37s 2d
No. 22: 2 pieces at £3 16s 4d
No. 23: 2 pieces at £2 18s 4d
No. 24: 2 pieces at £4 4d
No. 25: 2 pieces at £4 2s 4d
No. 26: a piece at £2 2s 2d
No. 27: a piece at 44s 2d
No. 28: a piece at £2 5s 2d
No. 29: a piece at 46s 2d
No. 30: a piece at £2 10s 2d
Sum: £29 2s 2d

[5.]
At London, the 8th day of September, anno 1533

Shipped by me, John Westbery, mercer, in [the vessel of] Adrian Johnson of Antwerp, a truss under this mark no. 2 [merchant's mark no. 5 in the left margin], containing 58 pieces of says, which 58 pieces of says cost me in the town of Antwerp £95 7s Flemish, besides 2 carpets and 8 ells of canvas to pack them with and other costs; and the freight of them is 3s sterling.

per me John Westbery

[6.] Shipped by me, Harry Bechar, in [the vessel of] Adrian Johnson of Antwerp, one sack containing 530 lb. weight of inkle thread [Note: a linen tape or braid] under this mark [merchant's mark no. 6 in the left margin]; cost of the sack: £19 17s 6d. Sum.

[7.] Shipped by John Popam in [the vessel of] Adrian Johnson of Antwerp: Item 8 sacks of hops under this mark [merchant's mark no. 7 follows]. More laden by the same John Popam: a dry cask containing 20 dozen quartering says, 25 dozen hats, 3 dozen checks [Note: checked cloth], 12 dozen girdling says of the new making; 4 gross of knives, 6,000 awl blades [Note: or arrowheads; the reading is uncertain], 12 dozen worth of inkle [Note: linen braid]. The sum of the goods in the dry cask, besides the hops, in value: £68, and this is the mark of the cask.

[8.] Shipped by me, John Ambrose, at Antwerp, a truss containing 4 bags under this mark [merchant's mark no. 8 in the left margin].

[9.] Shipped by Thomas Dichffyld of London in [the vessel of] Adrian Johnson of Antwerp, a dry cask containing 127 dozen haberdashery [Note: the word "cramare" refers to small wares, pedlar's goods] of divers sorts, under this mark in the margin [merchant's mark no. 9 in the left margin], which goods cost me at first purchase £89 8d Flemish.

[10.] [Damaged or incomplete entry] content in worth £17,176 Flemish.

[11.] Shipped by me, William Chamberlayne, in [the vessel of] Adrian Johnson of Antwerp, 4 sacks of hops weighing 2,140 lb., cost with the costs £7 5s 4d; and a ream of writing paper, cost 4s; and 2 pairs of carved bellows, one of them painted, cost 3s 4d: [total] £7 12s 8d [merchant's mark no. 10 in the left margin].

Item: shipped in [the vessel of] Adrian Johnson by me, Richard Travea, 561 [units — nature of goods uncertain] [Note: the original words "dudes" and "amez jame" are unidentified; they appear to be either an unrecorded commodity or a corrupted entry].

[12.] Shipped in [the vessel of] Adrian Johnson by me, Harry Austen, a fardel [Note: a bundle or small pack] under this mark [merchant's mark no. 11 in the left margin], containing 68 pieces of Hollands [Note: fine linen cloth from Holland].

Item: more in the said ship under this mark [merchant's mark no. 12 in the left margin]: 3 little firkins of sturgeon.

[13.] Shipped in [the vessel of] Adrian Johnson for me, John Edwards, a dry cask containing the following parcels: 15 dozen lb. Outnorth [Note: possibly a type of thread or cloth from northern Germany], 8 dozen hats, a gross of candlesticks, 20 lb. red wire, 4½ dozen say ribbons, 1½ dozen needles, 2 gross 2 dozen knives, 6 lb. fringe, 4 dozen daggers, 4 dozen check pieces, 3 dozen inkle ribbons, 3 dozen glasses. The sum of these goods as it cost: £39.

[14.] Shipped in [the vessel of] Adrian Johnson of Antwerp by Robert Reynolds, containing as follows [merchants' marks no. 13 and no. 14 in the left margin]:

Item: 23 pockets of hops
Item: 25 bundles of kettle bonds [Note: metal hoops or bindings for kettles or barrels]
Item: 4 sacks of hemp

[15.] Shipped in [the vessel of] Adrian Johnson at Antwerp, the 5th day of July, for me, Robert Dene:
Hops, 9 sacks weighing 4,970 lb., under this mark [merchant's mark no. 15 in the left margin], £17, for:

Gum: £6 20s
Gum arabic [Note: "Nygola Romana" may refer to a specific variety of gum]: £8 4s
Dragon's blood [Note: a red resin]: £14 14s
Lapis [stone] toto [Note: possibly lapis lazuli or another mineral pigment]: £6 9s [Note: "Lapis toto" is unidentified; possibly a garbled entry]
Armatlus [Note: unidentified commodity]: £6 7s
Comus [Note: unidentified commodity]: £47 57s
In this bag: fine turbit [Note: turpeth, a medicinal root]: £1 8s

[16.] Shipped in [the vessel of] Adrian Johnson by me, Richard Doune, 2 maunds [Note: wicker baskets] of trenchers [Note: wooden or bread platters] under this mark [merchant's mark no. 16 in the left margin].

[17.] Shipped in [the vessel of] Adrian Johnson by Thomas Marston, factor for Matthew Dale of London, haberdasher, a truss of this mark [merchant's mark no. 17 in the left margin], containing 22 pieces of Saint Thomas worsted [Note: a type of worsted cloth, possibly from Saint Thomas's parish or a named quality].

per me Matthew Dale

[18.] Shipped for Richard Wilson, mercer, by Cornelis Williamson, in [the vessel of] Adrian Johnson, 3 bales of Osnabrück fustians [Note: "Osburnys fustyans" — a coarse linen cloth from Osnabrück] of the bundle, in 2 trusses, under this mark [merchant's mark no. 18 in the left margin].

per me Richard Wilson

[19.] Shipped for William Mery, grocer, in [the vessel of] Adrian Johnson: 2 butts of currants and 1 pipe containing 2 bags of pepper, and a small truss containing 36 lb. of cinnamon, and therewith 2 Frisian [Note: "froyes"] frocks [Note: garments], under this mark [merchant's mark no. 19 in the left margin].

[20.] Laden by me, William Gresham, in [the vessel of] Adrian Johnson, 4 barrels of sturgeon, of which 2 barrels are marked with this mark [merchant's mark no. 20 follows] and 2 barrels with this mark [merchant's mark no. 21 follows], as it appears in the ship's book; which sturgeon cost £9 10s Flemish.

per me William Gresham

[21.] Shipped in [the vessel of] Adrian Johnson of Antwerp for me, Nicholas Tycheborn, grocer of London: one truss containing three bags of dry pepper and two chests of sugar under this [merchant's mark no. 22 follows, repeated in the left margin]: 1 say, 3 bags of pepper and 2 chests of sugar.

Item: shipped in [the vessel of] Adrian Johnson: 2 chests with apparel and a little coffer and

[22.] a bundle with a featherbed.

by me Nicholas Tychebourne

by me Thomas Brown

Item: shipped in [the vessel of] Adrian Johnson: 3 tonne of Seville oil marked with this mark

[23.] [merchant's mark no. 23 follows].

by me William Ristlayn, mercer

[24.] Robert Laurens, draper: shipped in [the vessel of] Adrian Johnson 2 bound chests, and in those same 2 chests: 12 breastplates and 12 backplates of harness [Note: armour], and 19 pairs of harness-skins [Note: leather padding worn under armour] harness, and 5 dozen made shirts and 7 fine made shirts and a dozen fine napkins of fine diaper [Note: a linen cloth woven in a small diamond pattern] and a sliced carpet [Note: possibly a cut-pile carpet]. All these parcels are in these 2 bound chests, with this mark [merchant's mark no. 24 follows, repeated in the left margin, but mirror image], and more: 2 half-barrels of sturgeon.

[25.] Shipped in [the vessel of] Adrian Johnson of Antwerp for Edward Morton, grocer of London: one barrel of large mace [Note: the spice] containing 42½ lb., marked with this mark [merchant's mark no. 25 in the left margin].

Item: more 3 barrels of succade [Note: candied peel or preserved fruit] containing in all 200 lb., marked with this mark [merchant's mark no. 26 follows].

Item: more 30 dozen empty barrels.

[26.] Shipped in [the vessel of] Adrian Johnson of Antwerp for William Cowsett, mercer of London, these parcels: 1 barrel containing one whole sturgeon and another barrel containing half a sturgeon, and a little barrel of salad oil, and a little barrel of capers, and a little barrel of olives [merchant's mark no. 27 in the left margin].

---""",
    41: """In the year etc. 1533, in the 6th indiction, on the 13th day of the month of September, at the instigation of the honourable lords Nicolaus Bardewick and Herman Schute, appointed by the honourable council for this purpose, the goods were inventoried and recorded in my presence as public notary and in the presence of the witnesses named below — those goods which had been unloaded from the ship of Adrian Johnson and subsequently hoisted and loaded into the bogarde of Hinrik Kron.

Item: first, hoisted from the bogarde into the lighter [Note: a flat-bottomed barge used to transfer goods to shore]:

[1.] Item: 1 bale of Louvain cloth [Note: "louwendes" — cloth from Leuven/Louvain], marked thus [merchants' marks no. 1, 2 and 3 in the right margin].
[2.] Item: also 5 bales [merchant's mark no. 4 in the right margin].
[3.] Item: also 2 sacks [merchant's mark no. 5 in the right margin].
[4.] Item: also 1 cask [merchant's mark no. 6 in the right margin].
[5.] Item: also 1 cask [merchant's mark no. 7 in the right margin].
[6.] Item: also 1 dry small cask, unmarked.
[7.] Item: 2 bales [merchant's mark no. 8 in the right margin].
[8.] Item: also 1 bale of says [merchant's mark no. 9 in the right margin].
[9.] Item: 1 Prussian chest with sugar, without mark.
[10.] Item: 1 cask with bread [merchant's mark no. 10 in the right margin].
[11.] Item: also 1 bale with white silk [merchant's mark no. 11 in the right margin].
[12.] Item: also 1 cask, is wet [merchant's mark no. 12 in the right margin].
[13.] Item: also 1 cask [merchant's mark no. 13 in the right margin].
[14.] Item: also 2 bound chests with leather bindings.
[15.] Item: also 1 cloth with broad braid-work [Note: "bonegelt" — decorative trim or braid] [merchant's mark no. 14 in the right margin].

Total: 22

Witnesses: Hans Vaget and Peter vom Hagen

That it is as stated above, I, Nicolaus Clone, attest with my own handwriting.

Item: in the same year and in the same indiction, on the 15th day of the month of September [15 Sept. 1533], the following goods were hoisted from the aforesaid bogarde of Hinrik Kron into the lighter.

[16.] Item: 1 bale [merchant's mark no. 15 in the right margin].
[17.] Item: 1 bale [merchant's mark no. 16 in the right margin].
[18.] Item: also 1 cask [merchant's mark no. 17 in the right margin].
[19.] Item: also 1 cask [merchant's mark no. 18 in the right margin].
[20.] Item: also 1 bale [merchant's mark no. 19 in the right margin].
[21.] Item: 1 basket with stoneware jugs [merchant's mark no. 20 in the right margin].
[22.] Item: 1 small cask [merchant's mark no. 21 in the right margin].
[23.] Item: also 2 bales [merchant's mark no. 22 in the right margin].
[24.] Item: also 1 bale [merchant's mark no. 23 in the right margin].
[25.] Item: also 3 small bales [merchant's mark no. 24 in the right margin].
[26.] Item: also 2 sacks [merchant's mark no. 25 in the right margin].
[27.] Item: also 1 small cask [merchant's mark no. 26 in the right margin].
[28.] Item: also 1 bale [merchant's mark no. 27 in the right margin].
[29.] Item: also 1 bale [merchant's mark no. 28 in the right margin].
[30.] Item: 10 small bales with haberdashery [Note: "maldelen" — small wares, pedlar's goods] [merchant's mark no. 29 in the right margin].
[31.] Item: also 2 bound chests [merchant's mark no. 30 in the right margin].
[32.] Item: also 4 small bales [merchants' marks no. 31 and 32 in the right margin].
[33.] Item: also 1 small bale [merchant's mark no. 33 in the right margin].
[34.] Item: 1 narrow cask with haberdashery [Note: "krmgude" — small traded goods].
[35.] Item: also 1 small package [merchant's mark no. 34 in the right margin].
[36.] Item: also 3 small casks [merchant's mark no. 35 in the right margin].
[37.] Item: also 1 small cask [merchant's mark no. 36 in the right margin].
[38.] Item: also 1 small package [merchant's mark no. 37 in the right margin].
[39.] Item: also 2 small casks [merchant's mark no. 38 in the right margin].
[40.] Item: also 1 small cask [merchant's mark no. 39 in the right margin].
[41.] Item: also 1 small cask [merchant's mark no. 40 in the right margin].
[42.] Item: also 1 small chest [merchant's mark no. 41 in the right margin].
[43.] Item: also 1 small cask [merchant's mark no. 42 in the right margin].
[44.] Item: also 1 small cask [merchant's mark no. 43 in the right margin].
[45.] Item: 2 brass buckets.
[46.] Item: 2 small chests without mark.
[47.] Item: 26 pieces of brass wire.
[48.] Item: 8 pieces of canvas.
[49.] Item: 1 small pouch [merchant's mark no. 44 in the right margin].
[50.] Item: 1 small pouch that is red, like bole [Note: "bolus" — a red clay pigment used in medicine and gilding].
[51.] Item: 3 sacks full of pepper [merchant's mark no. 45 in the right margin].
[52.] Item: also 1 bale [merchant's mark no. 46 in the right margin].
[53.] Item: also 1 small cask [merchant's mark no. 47 in the right margin].
[54.] Item: also 6 bales [merchant's mark no. 48 in the right margin].
[55.] Item: also 1 bale [merchant's mark no. 49 in the right margin].
[56.] Item: also 1 small bale [merchant's mark no. 50 in the right margin].
[57.] Item: also 1 small cask [merchant's mark no. 51 in the right margin].
[58.] Item: also 1 small bale [merchant's mark no. 52 in the right margin].
[59.] Item: also 1 bale of linen [merchant's mark no. 53 in the right margin].
[60.] Item: 1 small cask [merchant's mark no. 54 in the right margin].
[61.] Item: 1 small cask with haberdashery.
[62.] Item: 1 dry cask.
[63.] Item: 1 small cask [merchant's mark no. 55 in the right margin].
[64.] Item: 1 small bale [merchant's mark no. 56 in the right margin].
[65.] Item: ½ small cask without mark.
[66.] Item: 2 sacks of little worth.
[67.] Item: 1 bundle containing 2 pieces of linen cloth, 2 gowns, 1 lining of the same kind, 2 white pieces of twine, and 4 blankets.
[68.] Item: 1 small bundle with cords.
[69.] Item: 1 dry small cask with cinnamon.
[70.] Item: 1 leather bag.
[71.] Item: 1 bed and 1 feather coverlet.
[72.] Item: 5 pieces of iron band [Note: iron strapping].
[73.] Item: 220 pieces of iron wire, some of them beaten into barrels.
[74.] Item: 1 small painted little box.
[75.] Item: 1 cooking iron [Note: possibly a trivet or iron cooking implement].

Total: 97

Witnesses as above.

That it is as stated, I, Nicolaus Clone, clerk of the diocese of Ratzeburg, notary by imperial authority, attest with this my own hand.

Grand total of all goods received: 119 pieces.

---""",
    42: """In the year 1533, in the 6th indiction, on the 13th day of the month of September, at the instigation of the honourable lords Nicolaus Bardewick and Herman Schute, town councillors here in Lübeck, appointed by the honourable council for this purpose, all the following goods were inventoried and recorded in my presence as public notary and in the presence of the witnesses named below — those goods which had been unloaded from the ship of Adrian Johnson, skipper of Antwerp, and subsequently hoisted and loaded into the bogarde of Hinrik Kron of Lübeck.

Those acting as above.

[1.] Item: 1 bale of Louvain cloth, marked [merchant's mark no. 1 in the right margin].
[2.] Item: also 5 bales [merchant's mark no. 2 in the right margin].
[3.] Item: also 2 sacks [merchant's mark no. 3 in the right margin].
[4.] Item: also 1 small cask [merchant's mark no. 4 in the right margin].
[5.] Item: also 1 cask [merchant's mark no. 5 in the right margin].
[6.] Item: also 1 dry small cask [merchant's mark no. 6 in the right margin].
[7.] Item: also 2 bales [merchant's mark no. 7 in the right margin].
[8.] Item: also 1 bale with says or [arsch — unclear] [merchant's mark no. 8 in the right margin].
[9.] Item: also 1 Prussian chest with sugar, without mark.
[10.] Item: also 1 cask with bread [merchant's mark no. 9 in the right margin].
[11.] Item: also 1 bale [merchant's mark no. 10 in the right margin].
[12.] Item: also 1 cask, is wet [merchant's mark no. 11 in the right margin].
[13.] Item: also 1 cask, is wet [merchant's mark no. 12 in the right margin].
[14.] Item: also 2 bound ship-chests with rough leather bindings.
[15.] Item: also 1 small black cloth with broad braid-work [merchant's mark no. 13 in the right margin].

Witnesses: Hans Vaget and Peter Hagenouw.

That it is as stated, I, Nicolaus Klon, attest with my own handwriting.

Item: in the same year and in the same indiction, on the [15th] day of the month of September:

[16.] Item: also 1 bale, marked thus [merchant's mark no. 14 in the right margin].
[17.] Item: also 1 bale [merchant's mark no. 15 in the right margin].
[18.] Item: also 1 cask [merchant's mark no. 16 in the right margin].
[19.] Item: also 1 cask [merchant's mark no. 17 in the right margin].
[20.] Item: also 1 bale [merchant's mark no. 18 in the right margin].
[21.] Item: also 1 basket with stoneware jugs [merchant's mark no. 19 in the right margin].
[22.] Item: also 1 small cask [merchant's mark no. 20 in the right margin].
[23.] Item: also 1 bale [merchant's mark no. 21 in the right margin].
[24.] Item: also 1 bale [merchant's mark no. 22 in the right margin].
[25.] Item: also 3 small bales [merchant's mark no. 23 in the right margin].
[26.] Item: also 2 sacks [merchant's mark no. 24 in the right margin].
[27.] Item: also 1 small cask [merchant's mark no. 25 in the right margin].
[28.] Item: also 1 bale [merchant's mark no. 26 in the right margin].
[29.] Item: also 1 bale [merchant's mark no. 27 in the right margin].
[30.] Item: also 2 small bales [merchant's mark no. 28 in the right margin].
[31.] Item: also 2 bound ship-chests [merchant's mark no. 29 in the right margin].
[32.] Item: also 4 small bales [merchant's mark no. 30 in the right margin].
[33.] Item: also 1 small bale [merchant's mark no. 31 in the right margin].
[34.] Item: also 1 narrow small cask with some haberdashery.
[35.] Item: also 1 small package [merchant's mark no. 32 in the right margin].
[36.] Item: also 3 small casks [merchant's mark no. 33 in the right margin].
[37.] Item: also 1 small cask [merchant's mark no. 34 in the right margin].
[38.] Item: also 1 small package [merchant's mark no. 35 in the right margin].
[39.] Item: also 2 small casks [merchant's mark no. 36 in the right margin].
[40.] Item: also 1 small cask [merchant's mark no. 37 in the right margin].
[41.] Item: also 1 small cask [merchant's mark no. 38 in the right margin].
[42.] Item: also 1 small chest [merchant's mark no. 39 in the right margin].
[43.] Item: also 1 small cask [merchant's mark no. 40 in the right margin].
[44.] Item: also 1 small cask [merchant's mark no. 41 in the right margin].
[45.] Item: also 2 brass buckets.
[46.] Item: 2 small chests without mark.
[47.] Item: twenty-six pieces of brass wire.
[48.] Item: eight pieces of canvas.
[49.] Item: also 1 small pouch [merchant's mark no. 42 in the right margin].
[50.] Item: also 1 small pouch that is like bole [Note: a red clay pigment].
[51.] Item: also 3 sacks full of pepper [merchant's mark no. 43 in the right margin].
[52.] Item: also 1 bale [merchant's mark no. 44 in the right margin].
[53.] Item: also 1 small cask [merchant's mark no. 45 in the right margin].
[54.] Item: also [6] bales [merchant's mark no. 46 in the right margin].
[55.] Item: also 1 bale [merchant's mark no. 47 in the right margin].
[56.] Item: also 1 small bale [merchant's mark no. 48 in the right margin].
[57.] Item: also 1 small cask [merchant's mark no. 49 in the right margin].
[58.] Item: also 1 small bale [merchant's mark no. 50 in the right margin].
[59.] Item: also 1 bale of linen [merchant's mark no. 51 in the right margin].
[60.] Item: also 1 small cask [merchant's mark no. 52 in the right margin].
[61.] Item: also 1 small cask with haberdashery.
[62.] Item: also 1 small dry cask.
[63.] Item: also 1 small cask with Louvain bindings [merchant's mark no. 53 in the right margin].
[64.] Item: also 1 small bale [merchant's mark no. 54 in the right margin].
[65.] Item: also 1 small half-cask without mark.
[66.] Item: 2 sacks of little worth.
[67.] Item: in a bundle: 2 gowns, 2 pieces of linen cloth, 1 lining of the same kind, 2 pieces of white twine, and 4 blankets.
[68.] Item: 1 small bundle with cords.
[69.] Item: 1 dry small cask with cinnamon.
[70.] Item: 1 leather bag.
[71.] Item: 1 bed and 1 feather coverlet.
[72.] Item: also 5 pieces of iron banding.
[73.] Item: also 220 pieces of iron wire, some of them beaten into barrels.
[74.] Item: 1 small painted box.
[75.] Item: 1 cooking iron.

Witnesses: Hans Vaget and Peter Hagenow.

That it is as stated above, I, Nicolaus Klon, attest with my own handwriting.""",
    43: """Shipped by me, William Mery, grocer, under this mark [merchant's mark no. 1 in the left margin], in the vessel of Adrian Johnson of Antwerp:

One dry pipe [Note: a large cask] containing pepper, 2 bags weighing 519 lb. at 27d per lb. Flemish money. Sum: £58 7s 9d

Currants: 3 butts [Note: large barrels] weighing 4,514 lb. at 29s per hundredweight, Flemish money. Sum: £54 3s

Cinnamon: Note — 1 small bag weighing 36 lb., of which I have received only 18 lb. It cost 6s 4d per lb. Flemish. Sum of the half: £5 14s

Total sum: £118 4s 9d

---""",
    44: """Item: in the same year, indiction, day and month, the following marks were likewise inspected in the manner described above. This was done at the instigation of William Ashe, deputed thereto by his associates from England, etc.

[1.] Item: one small package marked thus [merchant's mark no. 1 in the right margin].

[2.] Item: one cask marked thus [merchant's mark no. 2 in the right margin].

[3.] Item: one cask marked thus [merchant's mark no. 3 in the right margin].

[4.] Item: one small piece of cloth with broad bone-gilt [Note: cloth with decorative gilt trim], marked thus [merchant's mark no. 4 in the right margin].

[5.] Item: furthermore, six pieces of canvas found.

Witnesses: as above [Herr Heinrich Kordes and Tyle Lutguwe]
Nicolaus Klone wrote this with his own hand.

---""",
    45: """Item: Robert Dene has shipped in the vessel of Adrian Johnson of Antwerp, firstly: 9

[1.] Item: John Edward has shipped in the vessel of Adrian Johnson of Antwerp 1 cask marked thus [merchant's mark no. 1 in the right margin].

[2.] Item: Jürgen Conink and Heinrich Brinklave have shipped in the vessel of Adrian Johnson of Antwerp one small package under one of these 3 marks — they do not know which one it is [merchants' marks no. 2, 3 and 4 in the right margin].

[3.] sacks of hops marked thus [merchant's mark no. 5 in the right margin].

[4.] [merchant's mark no. 6 in the right margin].

[5.] [in the right margin].

[6.] cloth. The bale is marked thus [merchant's mark no. 8 in the right margin].

Item: furthermore, 12 bolts of canvas and one pack marked thus [merchant's mark no. 7 in the right margin].

Item: in many small porcelain vessels [Note: or small apothecary wares] belonging to the apothecary's trade, under this mark [merchant's mark in the right margin].

Item: Randall Atkinson has shipped in the vessel of Adrian Johnson 1 bale containing 38 pieces of cloth.

---""",
    46: """A copy of the letter of appointment of Richard Plunthon.

To all those to whom these our present letters of certification shall be shown, and in particular to the honourable and wise lords, the burgomasters and council of Lübeck, our dear friends — the burgomasters, aldermen and council of the city of Bergen op Zoom send greetings. Be it known, testified and certified truly, that on the day hereunder written, there came before us and personally appeared, in notable number, certain established merchants of the nation of the kingdom of England, residing and trading here, and gave us to understand that in the past summer last gone, 37 persons together with their associates had loaded and shipped in the city of Antwerp, in a ship belonging to Adrian Johansen, certain diverse merchandise of great estimation and value, in order to have it conveyed by the said ship into the aforesaid kingdom of England. And coming around Zeeland near the borders of that same land, there arrived and came aboard the warships of the aforesaid city of Lübeck, which took the aforesaid ship with all the aforesaid merchandise by force and violence, as if they had been enemies of the aforesaid kingdom — some goods and merchandise they transferred into their ships — and therewith sailed to the aforesaid Lübeck. And therefore the said aggrieved merchants came before the royal Majesty of England aforesaid, to lay before him the matter clearly, so that his royal grace granted his sealed letters and furthermore appointed to accompany the said aggrieved merchants a merchant of that same nation named Thomas Gigges, to show and present the said letters and further to be able to demand and receive the said seized goods, all in accordance with the content and tenor of the said letters. And since they report that the said Thomas Gigges lies very ill in this city here and is not fit to travel, they have therefore lawfully before us appointed and constituted, and do appoint and constitute by these presents, in the place of the said Thomas, another person named Richard Plompton, to present the said royal letters to the said council of Lübeck, and further to be able to exact and receive freely and unconditionally the aforesaid seized goods, all in accordance with the said letters. And they have furthermore pledged before us in good faith before God to uphold and abide by whatever shall be done herein by the said Richard Plompton, binding themselves and all their goods, movable and immovable, present and future, without deceit or ill intent. In testimony whereof we have caused the seal of the aforesaid city of Bergen to be appended below on the 24th day of February, in the year thirty-three according to the Brabant calendar [Note: i.e. 24 February 1534, old style — in Brabant the new year began on 25 March, so February still fell within the year 1533 by that reckoning].

C. de Mera

The present copy has been examined and collated by me, Michael Petri, clerk of the diocese of Schwerin, public notary by sacred apostolic and imperial authority, and it agrees with its true original, as I attest with my own hand.

---""",
    47: """In the year 1534, in the seventh indiction, on Wednesday the first day of the month of April [1 April 1534], the honourable, prudent and wise lords Hermann Schute and Gottke Engelstede, councillors of Lübeck, acting on behalf of the honourable council there in Lübeck, and in the presence of me, the undersigned public notary, and the witnesses specially summoned and requested hereunto — did in the presence of the worthy man Richard Plunthon of England, who stated he was secretary of the fellowship of merchants there and as fully authorised agent empowered to receive the goods and articles described below, hand over, render account of, and return the said goods. The said Richard Plunthon likewise, as fully authorised agent and representative of the merchants in England, received and accepted the same back into his custody. The said goods and articles had been taken in the previous year on the open sea by persons appointed by the Lübeckers during the Holland war, albeit without the authority of the honourable council of Lübeck, and had been loaded in the hoy [Note: a type of coastal vessel] of the skipper Adrian Johansen.

So it is, as stated above. Michael Petri, notary, requested in connection with the foregoing, wrote this with his own hand.

The aforesaid appointed lords of the council here were ready and willing to open all the following packages for Richard Plunthon, if he wished to have them opened, etc.; which Richard received to his full satisfaction and was well content without opening them.

So it is. I, the same notary as above, Michael Petri, requested, attest this with my own hand.

[1.] First, they delivered to Richard and he received one large pack: therein were 58 pieces of say [Note: a fine-textured cloth] marked thus [merchant's mark no. 1 in the left margin], worth £96 1s Flemish, belonging to John Westborre.

[2.] Item: delivered to Richard Plunthon and received by him, 1 large bale of cloth containing 70 pieces; cost in all £136 Flemish; belonging to Robert Meredy, marked thus [merchant's mark no. 2 in the left margin].

[3.] Item: further delivered to Richard and received by him, one dry cask; therein were many small porcelain wares [Note: or apothecary goods]; belonging to John Edward; marked thus [merchant's mark no. 3 in the left margin], and valued together at £39 Flemish.

[4.] Item: further they delivered to Richard and he received one small chest; therein were 16 bundles of cypress-wood chests [Note: or goods packed in cypress]; belonging to John Gerholt; marked thus [merchant's mark no. 4 in the left margin] and valued at £54 sterling.

[5.] Further, Richard received 2 packs; therein 4 bales of sardonyx [Note: possibly "sardokes," a type of cloth or textile]; belonging to Richard Wilson; marked thus [merchant's mark no. 5 in the left margin] and valued at £86 Flemish.

Item: further delivered to him, 2 small tuns of rumbi [Note: a type of spirits] marked thus [merchant's mark no. 9 in the left margin].

[6.] Item: further Richard received, which the lords delivered to him, one bale; therein were 38 pieces of say, belonging to John Practor, marked thus [merchant's mark no. 6 in the left margin]. Cost with all charges: £62 19s 4d Flemish.

[7.] Item: further the lords delivered to Richard Plunthon and he received one pack; belonging to Henry Augustin; therein 68 pieces of Holland linen, marked thus [merchant's mark no. 7 in the left margin]. Cost: £89 15s 2d Flemish.

[8.] Item: further Richard received from the aforesaid lords one bale; belonging to William Lock; therein were 65 pieces of camlet [Note: a costly fabric of eastern origin, later imitated in Europe], of which 50 were tawny and 15 black, marked thus [merchant's mark no. 8 in the left margin], and costing £84 10s.

[9.] [Merchant's mark no. 9 in the left margin]; belonging to William Colsell. Cost: £6 Flemish.

[10.] Item: further the lords returned to Richard Plunthon 3 small tuns of rumbi, belonging to William Grossen, of two different marks, marked thus [merchant's marks no. 10 and 10a in the left margin].

[11.] Item: further Richard received 2 rough leather-bound chests, therein certain garments and letters; valued together at £30 sterling, without a mark. Belonging to Anthony Serene.

[12.] Item: further the lords returned to Richard and he acknowledged receipt — 2 black ironbound chests; they were opened and found to be as they should be, so that Richard received them to his full satisfaction; and they belonged to Robert Laurence of London. And delivered therewith: 2 brass buckets. The whole valued approximately at £17 7s 8d Flemish. Marked thus [merchant's marks no. 11 and 12 in the left margin].

[13.] Item: further Richard Plunthon received from the lords and was delivered — 4 sacks of pepper marked thus [merchant's mark no. 13 in the left margin], which belonged to and was shipped by Richard Osborne, and which weighed 892 lb. The pound costs 2s 3d Flemish: that is £100 2s 3d Flemish.

[14.] Item: further the lords returned and accounted to Richard one sack of yarn, which belonged to and was shipped by Henry Beger. This sack weighed 530 lb. The pound costs 9d Flemish and is marked thus [merchant's mark no. 14 in the left margin]. Sum in total: £19 17s 5d Flemish.

[15.] Item: further Richard received from the aforesaid lords and was delivered — one bale of pepper; therein 3 sacks of pepper; weighing in all 751 lb. 12 oz., belonging to Nicholas Tysborne, and marked thus [merchant's mark no. 15 in the left margin].

[16.] Item: further the lords returned to Richard Plunthon and delivered — one half-tun of canvas-wrapped linen, belonging to and shipped by Edward Morton, marked thus [merchant's mark no. 16 in the left margin]; and therein were 42½ lb. of mace [Note: the spice].

[17.] Item: further the lords delivered to Richard one small package with servants' clothing, marked thus [merchant's mark no. 17 in the left margin], and which he received.

[18.] Item: further the lords delivered to Richard and returned — 3 sacks of hemp, marked thus [merchant's mark no. 18 in the left margin], belonging to and shipped by Robert Reinholt. Item: also delivered to him therewith, 5 bundles of kettle-hooks or kettle-hoops [Note: iron fittings for cauldrons].

[19.] Item: further they delivered to Richard and he acknowledged receipt — 4 half-bales of Ulm sardonyx [Note: textiles associated with Ulm]; belonging to William Bateman; marked thus [merchant's mark no. 19 in the left margin] and each bale containing 25 half-pieces. Sum: £51 5s.

Item: further Richard received from the lords one leather travelling sack with...

[20.] Item: further Richard received from the lords, who delivered it to him, and which belonged to and was shipped by William Mery — one sack of cinnamon weighing 36 lb.; cost per lb. 6s 4d; packed in 2 black frieze coats. Cost: 12s groot, and it was in a tun without a mark.

[21.] Item: further Richard Plunthon received back from the lords and which they delivered to him — 7 pieces of canvas and 1 small tun of yarn, item a small bundle of red stones and a small sack of leaves [Note: possibly dyestuffs], belonging to Robert Den; marked thus [merchant's mark no. 20 in the left margin].

[22.] Item: the lords further delivered to Richard, which he received — one large dry cramp-cask [Note: a dry goods vat]; therein was haberdashery, belonging to and shipped by Thomas Distfelt, marked thus [merchant's mark no. 21 in the left margin]; and cost in all £89 8d Flemish.

[23.] clothing without a mark; belonging to Ralph Warinthun.

[24.] Item: further the lords delivered to Richard Plunthon and he acknowledged receipt — one small package; therein 3 bundles of buckram [Note: a stiff cloth]; item one large Flemish blanket; item one piece of fur; item one red woman's gown. All of this belonged to the wife of Thomas Bruns.

[25.] Augustin Hindt.

[26.] and one small coverlet; also belonging to the said wife of Thomas Bruns.

[27.] Item: further the lords returned to Richard and he acknowledged receipt — 2 pieces of linen cloth, 2 pieces of yarn, marked thus [merchant's mark no. 22 in the left margin]; and belonging to the wife of John Martyn.

[28.] Item: further Richard received from the lords, and which was delivered to him — one large dry cramp-cask, marked thus [merchant's mark no. 23 in the left margin]; and therein was haberdashery, belonging to John Pappham.

[29.] Item: further Richard has been returned and delivered — 3 small bundles of silk, marked thus [merchant's mark no. 24 in the left margin]; costing £13 sterling; belonging to Maryn Capella.

[30.] Item: further the lords rendered to Richard Plunthon and returned — 36 sugarloaves; belonging to Nicholas Tysborne; marked thus [merchant's mark no. 25 in the left margin].

[31.] Present at this and throughout were the honourable and prudent men Heinrich Warnboke and Jasper van Dalen, resident citizens of Lübeck, witnesses specially summoned and requested for this purpose.

Item: further Richard Plunthon received from the lords — one bed, two chests...

Item: further Richard received from the lords one man's coat; belonging to Augustin Hindt.

So it is as stated above, which I Michael Petri, public notary by sacred apostolic and imperial authority, attest with my own hand.

[Postscript, dating from 9 April 1534 or shortly thereafter]

The aforesaid goods and articles the said Richard has itemised and sworn to, and has — as was right and proper — fully and entirely released and acquitted the honourable council of Lübeck and all those having any interest therein from any further claim thereto, as is more fully set out, published and recorded in a notarial instrument drawn up for that purpose [No. 48], all without deception or ill intent.

So it is as stated above. I, the same notary as mentioned above, Michael Petri, wrote this with my own hand.

---""",
    48: """[1.]
In the name of God, amen. By this present public instrument let it be clearly apparent and known to all that in the year from the birth of the Same one thousand five hundred and thirty-four, in the seventh indiction, on Thursday the ninth day of the month of April [9 April 1534], during the reign of the most glorious, most unconquered and Catholic prince and lord, the lord Charles the Fifth, by the grace of God Emperor of the Romans, ever augustus, and king of Germany, Spain, both Sicilies, Jerusalem, Hungary, Dalmatia, Croatia, etc., archduke of Austria, duke of Burgundy, etc., in the fifteenth year of his reign — whereas it had previously been and was the case that in the recent year of Our Lord one thousand five hundred and thirty-three, in the month of August, in the time of the wars and hostilities between the Lübeckers on the one part and the Hollanders on the other part, the notable lords of the council of the city of Lübeck had, among other things, caused certain goods — which had been in a certain ship, commonly called a hoy, of the city of Antwerp, of which the master or captain was Adrian Johansen, and which had been seized by the aforesaid Lübeckers' appointed hired soldiers [Note: milites stipendiarii — mercenary troops or privateers] on the open sea, yet without the consent or mandate of the said lords of the Lübeck council — to be received into their custody and caused to be faithfully preserved, not otherwise than for the benefit and advantage of the fellowship of merchants: therefore before the same prudent and notable men, the lords proconsuls and councillors of the aforesaid city of Lübeck, assembled in council in their council chamber and seat, and in the presence of me, the undersigned public notary, and of the witnesses hereunder written specially summoned and requested for this purpose, there appeared personally and in person the commendable man Richard Plunthon, inhabitant of the city of London in the kingdom of England and, as he stated, secretary of the fellowship of merchants there, legitimate procurator of diverse merchants of the aforesaid kingdom of England, as he gave lawful proof of his mandate of procuration, who designated diverse goods belonging to his principals and intended for the said hoy, acting not under duress, deceit, fear, fraud or sinister contrivance, but of his own free, unconstrained and personal will, and did confess and in truth openly and publicly acknowledge and confess, both in his own name and in the names of all his principals and constituents, that on the first day of the aforesaid month of April [1 April 1534] he had already received back and did truly and effectively receive from the notable men, the lords Hermann Schuten and Godehard Engelsteden, councillors of Lübeck, specially deputed hereto by the notable council of Lübeck, those very goods and merchandise which the said hired soldiers, dispatched on warships or hostile vessels of the said city of Lübeck, had in the previous year within the limits and ports of the kingdom of England plundered, taken and carried off from his principals.

[2.] And first: one large bale or pack belonging to a certain John Westborri, worth ninety-six pounds and one shilling Flemish.

[3.] Item: furthermore one other large bale or pack of one hundred and thirty-six pounds Flemish, belonging to a certain Robert Meredy. Within these bales or packs were contained various and many precious goods and merchandise.

[4.] Item: a certain large dry vat belonging to a certain John Eduart, in which were various portions and merchandise, valued together, as estimated, at thirty-nine pounds Flemish.

[5.] Item: furthermore the same Richard Plunthon received and acknowledged receipt of one chest worth fifty-four pounds sterling, belonging and pertaining to a certain John Gerholt.

[6.] Item: furthermore the same Richard confessed to having received back two bales or packs belonging and pertaining to a certain Richard Wilsun, valued at eighty-six pounds Flemish.

[7.] Item: furthermore one bale or pack belonging and pertaining to a certain John Practor, worth with all expenses sixty-two pounds, nineteen shillings and four pence Flemish.

[8.] Item: furthermore another bale or pack belonging to a certain Henry Augustin, valued at eighty-nine pounds, fifteen shillings and two pence Flemish.

[9.] Item: furthermore another bale or pack belonging to a certain William Lock, worth eighty-four pounds and ten shillings.

[10.] Item: furthermore the same Richard Plunthon attested to having received and recovered two small tuns of rumbi [Note: a type of spirits or cordial] belonging to a certain William Kolsel, worth together six pounds Flemish.

[11.] Item: furthermore three other small tuns of rumbi belonging to a certain William Grossen.

[12.] Item: furthermore the same Richard stated that he had received back and recovered from the said lords councillors two iron-bound chests, which the aforesaid lords councillors had caused to be opened for him and which were found to be proper and as they should be, and which the said Richard acknowledged as sufficiently received, belonging to a certain Robert Laurentii of the city of London, together with two brass urns [Note: venis de auricalco — vessels of brass or latten], valued together at seventeen pounds, seven shillings and eight pence Flemish.

[13.] Item: furthermore two other iron-bound leather chests, in which were certain garments and various letters, valued together at thirty pounds sterling, belonging and pertaining to a certain Anthony Sehrene.

[14.] Item: four sacks of pepper weighing together one hundred pounds, two shillings and three pence Flemish, belonging and pertaining to a certain Richard Ausborne.

[15.] Item: furthermore one sack of thread belonging and pertaining to a certain Henry Betzer, weighed and valued at nineteen pounds, seventeen shillings and five pence Flemish.

[16.] Item: furthermore the aforesaid Richard Plunthon publicly confessed to having received back and recovered one bale or pack of pepper, in which three sacks of pepper were contained, belonging and pertaining to a certain Nicholas Tisborne, weighed and measured at seven hundred and fifty-one pounds and twelve ounces.

[17.] Item: furthermore one half-tun of linen cloth bound on the outside, in which were certain spices, namely forty and a half pounds of mace [Note: floris muscatorum — literally "flowers of musk," i.e. mace], belonging and pertaining to a certain Edward Morthon.

[18.] Item: one small pack in which were certain garments belonging to a certain servant.

[19.] Item: three sacks of hemp [Note: canabis] belonging and pertaining to a certain Robert Reygenholt, and five iron bundles pertaining to cauldrons [Note: fasciculos ferreos spectantes ad caldarios — iron fittings or handles for kettles].

[20.] Item: furthermore four medium bales or packs worth fifty-one pounds and five shillings, belonging and pertaining to a certain William Bateman.

[21.] Item: furthermore one sack in which were certain spices, namely cinnamon, weighing thirty-six pounds, worth six shillings and four pence per pound. This sack was contained within one tun without a merchant's mark, belonging and pertaining to a certain Robert Meri.

[22.] Item: furthermore the aforesaid Richard Plunthon confessed to having received seven bundles of a certain coarse linen cloth commonly called canvas [Note: kannefast], and one small tun with linen thread, and a small sack with red stones.

[23.] Item: furthermore a small sack containing certain leaves useful for dyeing [Note: certa folia valentia ad colorem], belonging to a certain Robert Dene.

[24.] Item: furthermore a large dry vat in which were various goods and portions of merchandise, valued at eighty-nine pounds and eight pence, belonging and pertaining to a certain Thomas Distfelt.

[25.] Item: a leather sack containing certain garments, belonging to a certain Ralph Warinthun.

[26.] Item: furthermore a small bale or pack containing certain goods, furs and garments, belonging to the wife of a certain Thomas Bruns.

[27.] Item: one tunic belonging to Augustin Hindt.

[28.] Item: furthermore one bed, two chests and one coverlet [Note: consolier — a cover or quilt], belonging to the said wife of Thomas Bruns.

[29.] Item: two round bundles of linen cloth and two bundles of thread, belonging to the wife of a certain John Martini.

[30.] Item: furthermore a large dry vat containing various goods and merchandise, belonging and pertaining to a certain John Pappham.

[31.] Item: three bundles of raw silk [Note: bissi crudi] worth thirteen pounds sterling, belonging to a certain Maryn Capella.

[32.] Item: furthermore thirty-six sugarloaves, belonging to a certain Nicholas Tisborn.

[33.] Item: furthermore the aforesaid Richard Plunthon publicly confessed to having received back and recovered from the notable lord Tilemann Tegetmeyger, councillor of Lübeck, specially deputed hereto by the notable council of Lübeck, one large vat of oil and three tuns or vats of oil — commonly called pipes [Note: pypen — large barrel-casks] — belonging to a certain William Cassellin.

[34.] Item: furthermore fifteen other small tuns of rape oil and three sacks of hops [Note: humili], belonging and pertaining to a certain Hamnoth Hammekottes, citizen of London.

[35.] The aforesaid Richard Plunthon, for the purpose and occasion of seeking restitution of these goods and merchandise, had come to the city of Lübeck in the names of his principals, and before the magnificent and notable council of Lübeck he openly and publicly — in the presence of the same lords of the Lübeck council — confessed that all and singular the goods listed above, both large and small bales or packs, each noted and specified under its mark, in accordance with the tenor of a certain certification produced in relation thereto, together with the small as well as the large items contained within, nothing of these being taken away or removed, had been restored, returned and consigned to him liberally and favourably, as aforesaid. And he swore, with arm extended and the first fingers raised, a bodily oath upon the holy Gospels of God, that the aforesaid goods belonged and pertained to his abovenamed principals, subjects of the aforesaid kingdom of England, and to no others, and not to any enemies of the said Lübeckers; and for such lawful restitution and real discharge of the abovescribed goods he gave and rendered thanks to the said lords of the Lübeck council. And concerning all and singular the aforementioned goods, things and merchandise, both small and great, so restored, received and consigned, the aforesaid Richard Plunthon, in the names of all his principals and their heirs, did fully release, liberate and acquit the aforesaid proconsuls, councillors and the whole council of the city of Lübeck and all citizens and inhabitants of the said city and all others whosoever whose interest it is or may be in any way in future, from the said received goods, and made with them a final settlement, acquittance and perpetual pact of not seeking again a thing already received, renouncing also the exception that the said goods had not been thus received or had not been received, and the hope of future receipt and payment, by which he could defend himself in any way against the foregoing or any part thereof, or for gain; so that neither the said council nor their citizens or inhabitants should henceforth in perpetuity be summoned, vexed, disturbed or molested in court or out of court on account of the said seizures of goods and merchandise, as aforesaid, but should be held, maintained and preserved immune, harmless, inoffensive, absolved and released therefrom, with solemn stipulation intervening and under the mortgage and obligation of all and singular his goods, movable and immovable, present and future, and with every other renunciation of law and fact necessary hereto and every safeguard. And he swore, touching the holy scriptures, a bodily oath upon the holy Gospels of God, that he and his principals would firmly and inviolably observe all the foregoing, under penalty of the guilt of perjury.

Concerning all and singular the aforesaid matters, the notable and prudent man, the lord Joachim Gerkens senior, proconsul of Lübeck, in the name of the whole council of Lübeck, requested me, the undersigned public notary, to draw up one or more public instrument or instruments recording the above.

These acts were done in the aforesaid city of Lübeck, in the council house there, before the lords of the council, in the year, indiction, day, month and other particulars as stated above. Present there were the prudent and honourable men Hermann Iserhell and Conrad Kock, citizens of Lübeck, witnesses specially summoned and requested for the foregoing.

I approve, I Michael the notary, having placed what was omitted through error.
Likewise I, the same undersigned notary, approve the erasure committed in the words "seven hundred and fifty-one pounds" in the thirty-fourth line counted from the beginning of this instrument, as I attest with my own hand.

And I, Michael Petri, clerk of the diocese of Schwerin, public notary by sacred apostolic and imperial authority — because I was present together with the aforesaid witnesses at this confession, acquittance, promise, renunciation and swearing of oath, and at all and singular the foregoing, while they were being performed and transacted as aforesaid, and saw and heard them so done and took note thereof — have therefore drawn up, subscribed, published and reduced into this public form the present public instrument, faithfully written by another's hand while I was in the meantime occupied with other business, and extracted from my notes, and have signed, confirmed and authenticated it with my customary and accustomed sign, name and surname, in faith, strength and evident testimony of all and singular the foregoing, having been asked and requested.

[Notary's mark of Michael Petri]""",
    49: """Another copy of the instrument of quitclaim and acknowledgement of the receipt of various notable goods by Richard Plunthon on behalf of the honourable council of Lübeck.

[1.] In the name of the Lord, amen. Let it be clearly apparent and known to all through this present public instrument that in the year from the nativity of the same [Lord] one thousand five hundred and thirty-four, the seventh indiction, on Thursday the ninth day of the month of April [9 Apr. 1534], during the reign of the most glorious, unconquered and Catholic prince and lord, lord Charles the Fifth, by the favour of divine clemency ever-august Emperor of the Romans and King of Germany, the Spains, both Sicilies, Jerusalem, Hungary, Dalmatia etc., Archduke of Austria and Duke of Burgundy etc., in the fifteenth year of his empire — whereas it had been and is the case that recently, in the year of the Lord one thousand five hundred and thirty-three, in the month of August, at the time of the wars and hostilities between the Lübeckers on the one part and the Hollanders on the other part, the honourable lords of the council of the city of Lübeck had, among certain other goods, [seized goods] in a certain ship — commonly called a hoy [Note: a type of coastal sailing vessel] — of the town of Antwerp, whose master or captain was Adrian Johnson at that time, and [those goods had been] seized on the open sea by the mercenary soldiers deputed by the said Lübeckers, yet without the consent and mandate of the said lords of the council of Lübeck; and whereas those goods, once they had come and been brought to the city of Lübeck, the aforesaid Lübeck council had received into its custody for no other purpose than for the benefit and advantage of the common merchants and had caused them to be faithfully preserved — therefore, before those same prudent and honourable men, the lords burgomasters and councillors of the aforesaid city of Lübeck, assembled in council in the council chamber and council seat, and in the presence of me, the undersigned public notary, and of the witnesses named below, specially summoned and requested for this purpose, there appeared personally and in person the commendable man Richard Plunthon, a resident of the city of London in the kingdom of England and, as he asserted, secretary of the common merchants there, a lawful attorney of certain various merchants of the aforesaid kingdom of England, as the letter of his mandate of procuration attests; he designated various goods belonging to his principals and pertaining to them as having been in the said hoy, not compelled or induced by force, deceit, fear, fraud or malicious contrivance, but of his own free and willing accord; and he had confessed and openly and publicly in truth acknowledged and did confess, both in his own name and in the name of all his principals, that he had previously, on the first day of the aforesaid month of April [1 Apr. 1534], already received those goods and merchandise from the honourable men lords Hermann Schuten and Godhard Engelsteden, councillors of Lübeck deputed for this purpose by the honourable council of Lübeck — namely those goods and merchandise which, in the immediately preceding year and month, under the coasts and in the harbours of the kingdom of England, the said mercenary soldiers dispatched with the warships and hostile fleets of the said city of Lübeck had seized, taken and carried away from his principals — and that he had truly and effectively received them.

[2.] And first, one large bale or bundle belonging to a certain John Westborri, of the value of ninety-six pounds and one shilling Flemish.

Item, yet another large bale or bundle of the value of one hundred and thirty-six pounds Flemish, belonging to a certain Robert Meredi. In these bales or bundles there were various and many precious items and merchandise.

[3.] Item, a certain large dry cask belonging to a certain John Edward, in which there were various items and merchandise, of the value together, as estimated, of thirty-nine pounds Flemish.

[4.] Item, likewise the said Richard Plunthon received and acknowledged having received a chest of the value of fifty-four pounds sterling, belonging and pertaining to a certain John Gherholt.

[5.] Item, likewise the said Richard acknowledged having recovered two bales or bundles belonging and pertaining to a certain Richard Wilsun, worth eighty-six pounds Flemish.

[6.] Item, likewise one bale or bundle belonging and pertaining to a certain John Practor, of the value with all charges of sixty-two pounds, nineteen shillings and four pence Flemish.

[7.] Item, likewise another bale or bundle belonging to a certain Henry Augustyn, worth eighty-nine pounds, fifteen shillings and two pence Flemish.

[8.] Item, likewise one bale or bundle belonging and pertaining to a certain William Lock, of the value of eighty-four pounds and ten shillings.

[9.] Item, likewise one other bale or bundle belonging and pertaining to a certain William Lock [Note: the Latin reads "Wilhelm Lock" but the section number and context suggest this entry properly belongs to a different merchant; the Low German parallel text at Doc 51 item [8] shows this as Wilhelm Lock with camlots, and [9] as Wilhelm Colsen with tuns of sturgeon — the Latin text appears to have suffered some disruption here], of the value of eighty-four pounds and ten shillings.

Item, likewise three other small tuns of sturgeon [Note: Latin "rumbum"; Low German "stors" — sturgeon] belonging to a certain William —

[10.] Item, likewise the said Richard Plunthon attested to having received and recovered two small tuns of sturgeon belonging to a certain William Kolsel, of the total value of six pounds Flemish.

[11.] [Note: this item number appears without a complete corresponding entry in the Latin; the Low German parallel text shows it relates to Wilhelm Grosshen.] Item, likewise the said Richard reported to the aforesaid lords councillors that he had recovered and received two iron-bound chests, which the aforesaid lords of the council had caused to be opened and were found to be in proper order as they ought to be, and which Richard himself had accepted as sufficiently received, belonging to a certain Robert Laurentii of the city of London, together with two bronze urns, valued together at seventeen pounds, seven shillings and eight pence Flemish.

[12.] Item, likewise two other iron-bound leather chests, in which were certain garments and various letters, valued together at thirty pounds sterling, belonging and pertaining to a certain Anthony Serene.

[13.] Item, four sacks of pepper weighing together one hundred pounds [at] two shillings and three pence Flemish [per pound], belonging and pertaining to a certain Richard Ousborne.

[14.] Item, likewise one sack of thread or containing thread, belonging and pertaining to a certain Henry Betzer, weighed and valued at nineteen pounds and seventeen shillings and five pence Flemish.

[15.] Item, the aforesaid Richard Plunthon further publicly acknowledged having recovered and received one bale or bundle of pepper — in which four sacks of pepper were contained — belonging and pertaining to a certain Nicholas Tysborne, weighed and measured at seven hundred and fifty-one pounds and twelve ounces.

[16.] Item, likewise one half-tun wrapped on the outside in linen cloth, in which were certain spices, namely forty-two and a half pounds of mace [Note: "flores muscatorum," literally "nutmeg flowers" = mace], belonging and pertaining to a certain Edward Morton.

[17.] Item, [a small packet with certain garments] belonging to a certain servant.

[18.] Item, [three sacks of hemp] belonging to a certain Reynenholt and five iron bundles belonging to cauldrons [Note: "fasciculos ferreos spectantes ad caldarios" — iron fittings or hoops for kettles/cauldrons].

[19.] Item, likewise four half-bales or bundles of the value of fifty-one pounds and five shillings, belonging and pertaining to a certain William Bateman.

[20.] Item, likewise one sack in which were certain spices, namely cinnamon weighing thirty-six pounds, each pound worth six shillings four pence. This sack was in a tun without a mark, belonging and pertaining to a certain Robert Meri.

[21.] Item, likewise the aforesaid Richard Plunton acknowledged having received seven pieces of a certain coarse linen cloth commonly called kannefust [Note: Low German "kannefast" — a type of coarse linen canvas] and one small tun with linen thread and a small sack with red stones.

[22.] [A small parcel belonging to a certain] Robert Dene.

[23.] Item, likewise a large dry cask in which there were various items and quantities of merchandise, valued at eighty-nine pounds and eight pence, belonging and pertaining to a certain Thomas Dystfelt.

Item, likewise a small bundle in which were certain garments belonging to [a certain person].

Item, likewise a small sack in which were certain leaves useful for dye. This [item —]

Item, three sacks of hemp belonging and pertaining to a certain Robert [Reynenholt —]

Item, a leather sack with certain garments belonging to a certain [person —]

Item, two round bundles of linen cloth and two bundles of thread belonging [to —]

Item, likewise a large dry cask in which there were various quantities of merchandise, belonging and [pertaining to —]

Item, three bundles of raw silk [Note: "bissi crudi"] of the value of thirteen pounds sterling, belonging [to —]

Item, likewise one small bale or bundle with certain short furs and [—]

Item, likewise one tun belonging to a certain Augustine Hindt.

Item, likewise the aforesaid Richard Plunthon attested to having received one bed —

[24.] [belonging to] Rodolph Warynthun.

[25.] [—] garments belonging to the wife of a certain Thomas Bruns.

[26.] [—]

[27.] two chests and one coffer [Note: "confor" — a small chest or coffer] belonging to the same wife of Thomas Bruns.

[28.] [—] to the wife of a certain John Martini.

[29.] [—] belonging to a certain John Pappham.

[30.] [—] to a certain Maryn Capella.

Item, likewise thirty-six loaves of sugar belonging to a certain Nicholas Tisborne.

[31.] Item, likewise the aforesaid Richard Plunthon publicly —

[32.] [33.] acknowledged having received from the honourable lord Tylemannus Thegetmeyger, councillor of Lübeck, deputed for this purpose by the honourable council of Lübeck, one large vat of oil and three tuns or vats of oil — commonly called pipes [Note: Low German "pypen" — large barrels, equivalent to pipes] — belonging to a certain William Cassellyn.

[34.] Item, likewise fifteen small tuns of rape oil and three sacks of hops, belonging and pertaining to a certain Hammot Hammetrottes, citizen of London, for the restoration of which merchandise and goods —

[35.] The said Richard Plunthon had betaken himself to the city of Lübeck in the name of his principals and from the magnificent and honourable council of Lübeck he had received back truly and effectively all and singular the goods written above, the tuns, the large as well as the small bales or bundles, each noted and specified under their mark, according to the tenor of a certain certification exhibited in relation to them, together with the small as well as the large items contained therein, nothing of these plundered or abstracted; and he acknowledged openly and publicly before the said lords of the council of Lübeck that the said goods had been restored, returned and delivered to him in a liberal and favourable manner, as stated above; and he swore with arm outstretched and the first fingers raised, bodily oath upon the holy Gospels of God, that the said goods aforesaid belong and pertain to his above-named principals, inhabitants of the aforesaid kingdom of England, and to no others, enemies of the said Lübeckers; and for such lawful restitution and real delivery of the said goods written above he gave and rendered thanks to the said lords of the council of Lübeck. And of and concerning all and singular the aforesaid goods, merchandise — both small and large — thus restored, received and delivered, the said aforesaid Richard Plunthon, in the name of all his principals and their heirs, fully and completely released, freed and absolved the aforesaid burgomasters, councillors and the entire council, and all citizens and inhabitants of the said city of Lübeck and all others and each of them who have or may have any interest therein at any point in the future, in respect of the said goods received; and made a final quitclaim and perpetual agreement never henceforth to seek again what had once been obtained; renouncing also the exception that the said goods thus received by him had not been had or received, and [renouncing] the hope of future having and claiming thereof, by which he might defend himself against the foregoing or any part thereof in any way, or [claim] profit — so that neither the said council nor their citizens or inhabitants can or should thereafter in perpetuity be summoned, vexed, disturbed or troubled in court or out of court on account of the seizure of these goods and merchandise as aforesaid, but [the said council and citizens] shall keep and observe them immune, unharmed, blameless, absolved and free of any claim, with solemn stipulation intervening and under mortgage and obligation of all and singular his goods, movable and immovable, present and future, and every other renunciation of law and sacred matter necessary to this matter and every precaution. And that he and his principals will firmly and inviolably observe all the foregoing he swore under pain of the guilt of perjury, oath taken touching the holy scriptures upon the holy Gospels of God; and of and concerning all and singular the aforesaid matters the honourable and prudent man lord Joachim Gherkens, senior burgomaster of Lübeck, in the name of the entire council of Lübeck, requested of me, the undersigned public notary, that one or more public instrument or instruments be made.

These acts were done in the aforesaid city of Lübeck, in the council house there and before the lords of the council, in the year, indiction, day, month and other circumstances as above. Present there were the prudent and honourable men Hermann Iserahel and Conrad Kock, citizens of Lübeck, witnesses specially summoned and requested for the foregoing.

And I, Michael Petri, clerk of the diocese of Schwerin, public notary by sacred apostolic and imperial authority, was personally present at all this confession, quitclaim, promise, renunciation and oath-taking and all other and singular matters aforesaid while they were, as stated above, being done and transacted, together with the aforementioned witnesses; I saw and heard these things done in this manner and took notes thereof. Therefore I have drawn up this present public instrument, written in my own hand and extracted from my notes, and have subscribed, published and reduced it to this public form, and have signed, confirmed and fortified it with my customary and accustomed sign, name and surname, in witness, strength and evident testimony of all and singular the foregoing, as requested and required.

This present copy has been checked and collated by me, the same Michael Petri, clerk and notary as above-named. And it agrees with its original, as I attest in my own hand.

---""",
    50: """[No content — document title only: Richard Plunthon acknowledges receiving from the Lübeck councillor Tyle Thegetmeyger, by order of the Lübeck council, the following goods: one great vat of oil and eight pipes of oil belonging to William Cassellyn; fifteen small tuns of rape oil and three sacks of hops belonging to Homont Hametrettes of London.]

---""",
    51: """Copy for the honourable council of Lübeck of the restitution of certain restored goods.

[I] Anthonius Oberomiza

In the year 1534, the seventh indiction, on Thursday the twelfth of the month of March, the honourable and highly wise lords, lord Clawes Bardewick and lord Hermen Schute, councillors of Lübeck, by order of the honourable council there at Lübeck and before a public notary and the undersigned witnesses specially summoned and requested for this purpose, in the presence of the honourable man Anthonius Oberomiza, a Venetian dwelling in London in England, as the principal owner to himself of the following goods and items — not out of obligation but out of goodwill and out of reverence and favour of the royal grace of England — have graciously returned, accounted for and delivered [the said goods]; and the aforesaid Anthonius, from such delivery, has received them back with gratitude; he also specified and designated them, and thereupon swore a solemn oath to God and His saints that the following items belong to himself alone and to no Hollander, Brabanter or Zealander, and that no one else has any share or part in them, etc. According to the tenor of a public instrument made thereupon etc. And these items had been laden in skipper Adrian Johnson's hoy and were taken in the last preceding summer by the Lübeck privateers [Note: "uthligger" — an armed vessel sent out to sea; a privateer or freebooter] against the Hollanders on the open sea, yet without the order and consent of the honourable council of Lübeck.

Done at Lübeck, where Anthonius took the oath in the chancellery [Note: "cancellaria" — the council's administrative office], and for the acknowledgement and recovery of the items in the house of Hinrick Cordes, citizen of Lübeck, in the presence of the honourable men Laurens Wellmes, Hermen Mollers and lord Ghert Falcken, resident citizens of Lübeck, specially and individually summoned and requested for this purpose.

So it is as above, which I, Michael Petri, public notary by apostolic and imperial authority, attest in my own hand as required for the foregoing.

Item, the following items the named lords have delivered to Anthonius Oberomiza and which he has received:

Nine dozen stone pots
6 dozen tin pots and 9 pots
Item, 5 dozen bells and 5 bells
Item, 10 mirrors
Item, one image or holy figure
Item, 8 platters
Item, 10 candlesticks
Item, 6 basins with pig-bristle [Note: "naschen myt swyne bosten" — washing basins with pig-bristle brushes, or possibly bristle-lined receptacles]
Item, 4 compasses [Note: "marck cyrkel" — marking compasses or dividers] and 4 compasses [Note: possibly two types, marking and drawing compasses]
Item, 26 hammers
Item, 8 tongs
Item, these aforesaid items were in one large basket.

Now since the same Dutch hoy in which the aforesaid Anthonius Oberomiza's goods had been laden had sunk and otherwise been wrecked, so that the same Anthonius complained that he was still missing some goods and items that had either sunk or been taken from him by the Lübeck fighting men, etc., therefore afterwards the honourable council of Lübeck, through their appointed deputies, out of particular benevolence, came to a full, complete and entire settlement with the aforesaid Anthonius in respect of all goods and items that had sunk or been taken from him and which he was still missing, [agreeing upon] a good sum of money, which he has, to his full satisfaction, truly and well received in counted cash from Gottken Engelsteden and lord Albert Clever, councillors of Lübeck appointed for this purpose, on a set day and time before me, public notary, and witnesses specially summoned for this purpose; and he has thereupon released and given a full quitclaim to the aforesaid honourable council and all the common citizens and inhabitants of the city of Lübeck, for himself and his heirs, of all the goods and items written above — received, sunk and taken — and also of everything else he was still missing, and also of costs, damages, expenses, profits and interest, fully and entirely quit, released, free and clear of all claims; and renounced all legal rights etc. He also swore a solemn oath for himself and his heirs never to speak or make demand in respect thereof etc., so that the honourable council and the city of Lübeck shall be quit, free, released and clear with a single payment.

According to the tenor of a public instrument made thereupon in which this matter is more fully contained, without deceit or ill intent.

So it is as above, which I, Michael Petri, public notary by apostolic and imperial authority, attest in my own hand as required for the foregoing.

[II] Martinus de Federigo

In the same year 1534, the seventh indiction, on Thursday the twelfth of the month of March, the honourable and highly wise lords, lord Clawes Bardewick and lord Hermen Schute, councillors of Lübeck appointed for this purpose, before the aforesaid Anthonius Oberomiza, before me as public notary and the undersigned witnesses summoned and requested for this purpose, as a true and undoubted attorney and agent of the honourable man Martinus de Federigo, Venetian merchant, his principal, have accounted for, delivered and handed over one bale of silk marked thus [merchant's mark no. 1 in the left margin]; which bale belongs to the named Martinus de Federigo and which the aforesaid Anthonius Oberomiza has received back on his behalf with gratitude; and he has fully released and given a quitclaim to the aforesaid honourable council and all the common citizens and inhabitants and the entire imperial city of Lübeck in respect thereof. He also swore on his principal's soul never again to make any claim therefor, so that the honourable council and city of Lübeck should be quit, free, released and clear by virtue of this one delivery; and renounced all legal rights on behalf of his principal and all his heirs, according to the tenor of a public instrument made thereupon in which this matter is more fully set out and contained — all without deceit or ill intent. This bale of silk was also laden in skipper Adrian Johnson's hoy.

Done at Lübeck, after the swearing of the oath in the chancellery and the receipt of the bale, in the house of Hinrick Cordes, in the presence and company of the honourable men Laurens Willmes, Herman Moller and Gert Falcken, resident citizens of Lübeck, as witnesses specially and individually summoned and requested for this purpose.

So it is as above, which I, Michael Petri, public notary by sacred apostolic and imperial authority, attest in my own hand as required for the foregoing.

[III] Richard Plunthon

In the year 1534, the seventh indiction, on Wednesday the first day of the month of April [1 Apr. 1534], the honourable, prudent and wise lords, lord Hermen Schute and Gotke Engelstede, councillors of Lübeck, by order of the honourable council there at Lübeck and before me as public notary and the undersigned witnesses specially summoned and requested for this purpose, in the presence of the honourable man Richard Plunthon from England and, as he said, secretary of the common merchants there, and appointed as a fully authorised [agent] for the receipt of the following goods and items — out of reverence, grace and favour of the most illustrious, most mighty, high-born prince and lord, lord Henry, King of England etc. — have delivered, accounted for and returned them; and thereupon the aforesaid Richard Plunthon, as a fully authorised agent and representative of the merchants in England, has accepted and received them back into his keeping. These following goods and items were taken in the past year by the Lübeck appointees in the war against the Hollanders on the open sea, yet without the order of the honourable council of Lübeck, and were laden in skipper Adrian Johnson's hoy.

So it is as above; I, Michael Petri, notary, wrote this in my own hand as required for the foregoing.

The aforesaid appointed lords of the council here were ready and willing to open these following bales for Richard Plunthon if he wished to have them opened, etc.; but Richard received them to his full satisfaction and was well satisfied without opening them.

So it is; I, the same Michael Petri, notary as above, attest this in my own hand as required for the foregoing.

[1.] Firstly, one large bale they have delivered to Richard Plunthon and which he has received from the aforesaid lords. In it were 58 pieces of says [Note: Low German "sagen" — says, a type of woollen cloth], marked thus [merchant's mark no. 2 in the left margin], costing £96 1s Flemish, and belonging to Johan Westborre.

[2.] Item, likewise the lords have delivered to Richard Plunthon and which he has received: 1 large bale of arras [Note: Low German "arsch" — arras cloth], therein 70 pieces, costing in all £136 5s Flemish, marked thus [merchant's mark no. 3 in the left margin], and belonging to Rubbert Meredi.

[3.] Item, likewise delivered to Richard and which he has received: one large dry cram-cask [Note: Low German "cramfaet" — a dry cask used for storing miscellaneous small wares or haberdashery]. In it were many small items, marked thus [merchant's mark no. 4 in the left margin], belonging to Johan Eduwarth, and standing together at £39 Flemish.

[4.] Item, likewise they have delivered to Richard and which he has received: one small chest. In it were 16 bundles of cypress [Note: Low German "sipperkost" — possibly "Cypres-kost," Cyprus goods, a luxury textile or merchandise from Cyprus]. Belongs to Johan Gerholt, marked thus [merchant's mark no. 5 in the left margin], and stands at £54 sterling.

[5.] Likewise Richard has received 2 bales, therein 4 bales of sardoks [Note: Low German "sardokes" — a type of coarse woollen cloth; also rendered "sardas"]. Belong to Richard Wilsun, marked thus [merchant's mark no. 6 in the left margin], and standing at £86 Flemish.

[6.] Item, likewise Richard has received, which the lords have delivered to him, one bale. In it were 38 pieces of says and belonging to Johan Practor, marked thus [merchant's mark no. 7 in the left margin]. Costs with all charges £62 19s 4d Flemish.

[7.] Item, likewise the lords have delivered to Richard Plunthon and which he has received: one bale belonging to Hinrick Augustyn, therein 68 pieces of Holland louwent [Note: Low German "Hollandesch louwent" — Holland cloth or Holland linen, a fine linen cloth from Holland], marked thus [merchant's mark no. 8 in the left margin]. Costs £89 15s 2d Flemish.

[8.] Item, likewise Richard has received from the aforesaid lords one bale belonging to Wilhelm Lock. In it were 65 pieces of camlots [Note: Low German "kammelottes" — camlet, a luxury fabric, possibly originally of camel hair; here 50 tawny and 15 black], of which 50 tawny and 15 black, marked thus [merchant's mark no. 9 in the left margin], and costing £84 10s.

[9.] Item, likewise delivered to him: 2 small tuns of sturgeon, marked thus [merchant's mark no. 10 in the left margin]. Belonging to Wilhelm Colsen. Costing £6 Flemish.

[10.] Item, likewise the lords have returned to Richard Plunthon 3 small tuns of sturgeon belonging to Wilhelm Grosshen, marked with two different marks thus [merchant's marks no. 11 and 11a in the left margin].

[11.] Item, likewise Richard has received from the lords 2 rough iron-bound chests of leather. In them were some garments and letters. Valued together at £30 sterling. Unmarked. Belonging to Anthonio Serene.

[12.] Item, likewise the lords have delivered back to Richard Plunthon 2 black iron-bound chests. They were opened and found to be in order as they should be, so that Richard received them to full satisfaction. And they belonged to Rubbert Laurens of London. And therewith delivered 2 brass buckets. This together estimated at approximately £17 groats and 7s 8d Flemish, marked thus [merchant's marks no. 12 and 13 in the left margin].

[13.] Item, likewise Richard Plunthon has received back from the lords, and which has been delivered to him, 4 sacks of pepper, marked thus [merchant's mark no. 14 in the left margin], which belong to and were shipped by Richard Außborne, and they weighed 891 pounds. The pound costs 2s 3d Flemish. That is £100 2s 3d Flemish.

[14.] Item, likewise the lords have delivered back to Richard and handed over one sack of yarn, which belongs to and was shipped by Hinrick Beger. This sack weighed 530 pounds. The pound costs 9d Flemish and is marked thus [merchant's mark no. 15 in the left margin]. The sum total is £19 17s 5d Flemish.

[15.] Item, likewise Richard has received from the lords, and which has been delivered to him, one bale of pepper, therein 3 sacks of pepper. They weighed in all 751 pounds and 12 ounces and belong to Nicolaus Tisborne and were marked thus [merchant's mark no. 16 in the left margin].

[16.] Item, likewise the lords have delivered back to Richard Plunthon, and which he has received, one half-tun wrapped in kannefast [Note: a coarse linen canvas cloth], which belongs to and was shipped by Eduwartus Mortson, marked thus [merchant's mark no. 17 in the left margin], and in it were 42½ pounds of mace.

[17.] Item, likewise the lords have delivered to Richard Plunthon one small packet with servant's garments, marked thus [merchant's mark no. 18 in the left margin], and which he has received.

[18.] Item, likewise the lords have delivered and handed over to Richard 3 sacks of hemp, marked thus [merchant's mark no. 19 in the left margin], which belong to and were shipped by Rubbert Reyneholt. Item, also delivered to him therewith 5 bundles of kettle-hooks or kettle-bands [Note: Low German "ketelhenge offte ketelbande" — hanging fittings or iron hoops/bands for kettles or cauldrons].

[19.] Item, likewise they have delivered and handed over to Richard 4 half-bales of Ulm sardock [Note: Low German "Olmer sardock" — sardock cloth from Ulm], belonging to Wilhelm Bateman, marked thus [merchant's mark no. 20 in the left margin], each bale containing 25 half-pieces. Sum £51 Flemish.

[20.] Item, likewise Richard has received from the lords, which they have delivered to him, and which belongs to and was shipped by Wilhelm Meri: one sack of cinnamon weighing 36 pounds. Each pound costs 6s 4d. Packed in 2 black coats made of frieze cloth. Costing 12s groat and was in a tun, unmarked.

[21.] Item, likewise Richard Plunthon has received back from the lords, and which they have delivered to him: 7 pieces of kannefast and 1 small tun of yarn. Item, a small bundle with red stones and a small sack with leaves [Note: possibly dyestuff leaves], which belongs to Rubbert Den, marked thus [merchant's mark no. 21 in the left margin].

[22.] Item, the lords have delivered to Richard, which he has received: one large dry cram-cask. In it was haberdashery [Note: Low German "cramwerck" — miscellaneous small wares, haberdashery], which belongs to and was shipped by Thomas Dystfelt, marked thus [merchant's mark no. 22 in the left margin]. And costs in all £89 8d Flemish.

[23.] [—] garments unmarked and belonging to Raff Warynthun.

[24.] Item, likewise the lords have delivered and handed over to Richard Plunthon one packet [Note: "pascheens" — possibly a satchel or bundle], therein three bundles of sickle-thong [Note: Low German "sickelthun" — possibly strap or cord used for binding; or a type of small sickle], one large Flemish blanket, one piece of each [type of] fodder-cloth [Note: "elck foder" — unclear; possibly one piece of fur lining], one red woman's gown. All this belongs to the wife of Thomas Bruns.

[25.] [—] belonging to Augustin Hindt.

[26.] [—] and one small coffer. Belonging likewise to the said wife of Thomas Bruns.

[27.] Item, likewise the lords have delivered, handed over to Richard Plunthon and which he has received: 2 pieces of louwent [Note: a type of linen cloth], 2 pieces of yarn, marked thus [merchant's mark no. 23 in the left margin]. And belonging to the wife of Johan Martins.

[28.] Item, likewise Richard has received from the lords, and what has been delivered to him, one large dry cram-cask, marked thus [merchant's mark no. 24 in the left margin], and in it was haberdashery, belonging to Johan Pappham.

[29.] Item, likewise there has been handed over to Richard and delivered back: 3 small bundles of silk, marked thus [merchant's mark no. 25 in the left margin], costing £13 sterling. Belonging to Maryn Capella.

[30.] Item, likewise the lords have accounted for and delivered back to Richard Plunthon 36 loaves of sugar belonging to Nicolaus Tysborne, marked thus [merchant's mark no. 26 in the left margin].

Present at and over [these proceedings] were the honourable and prudent men Hinrick Warmbake and Jasper van Dalen, resident citizens of Lübeck, witnesses specially summoned and requested for this purpose.

So it is as above, which I, Michael Petri, public notary by apostolic and imperial authority, attest in my own hand.

The aforesaid goods and items the aforesaid Richard Plunton has inventoried and sworn to, and — as is proper — has given a full and entire quitclaim to the honourable council of Lübeck and all those concerned in the matter, as is more fully set out and contained in a public instrument made thereupon — all without deceit or ill intent.

So it is as above; the same Michael, notary as above, wrote this in his own hand.

IV

Item, likewise the aforesaid Richard Plunton has further received back from lord Thyle Thegetmeyger, councillor of Lübeck, by order of the honourable council of Lübeck, and what has been delivered to him:

[1.] First of all, one great cask with [boem olie — tree oil, i.e.] olive oil and yet 3 pipes of oil, belonging to Wilhelm Cassellen, marked thus [merchant's mark no. 27 in the left margin].

[2.] Item, likewise Richard has received from the aforesaid lord Thyle: 15 small tuns of rape oil and 3 sacks of hops, marked thus [merchant's mark no. 28 in the left margin], and belonging to Hamont Hammetrottes of London.

Item, in respect of this too Richard Plunthon has given a full and entire quitclaim to the honourable council of Lübeck before me as public notary, etc.

Item, these goods were laden in skipper Johan Wilmessen's ship.

So it is as above; Michael Petri, notary, wrote this in his own hand.

---""",
    52: """Copy of the [instrument of] appointment of Martin de Federigo.

In the name of God, amen. Let it be clearly apparent to all through this present public instrument that in the year of the Lord from the Incarnation according to the usage and reckoning of the English church one thousand five hundred and thirty-three [Note: the English church used the Annunciation Style, meaning the new year began on 25 March; thus "1533" in this document corresponds to what we would call early 1534], the seventh indiction, in the eleventh year of the pontificate of our most holy father in Christ and lord, lord Clement, by divine providence the Seventh Pope, on the third day of the month of February, in the dwelling-house of me, the undersigned public notary, situated in the public street of Lombard Street in the parish of Blessed Mary Woolnoth [Note: a church in the City of London] in the city of London, in the presence of me the same notary and the witnesses named below, the distinguished man Martinus de Frederigo, merchant of Venice, appeared personally and of his own free will and certain knowledge, by all ways, modes, right, cause and form by which he most fully and effectively could and can, made, constituted, created, named and solemnly ordained, and by the tenor of this present public instrument makes, constitutes, creates, names and ordains the discreet man Anthonium Obromiza, merchant also of Venice, though absent, yet as if present, to be his true, lawful and undoubted attorney, agent, representative and manager of his affairs and special envoy — namely specifically and expressly on behalf of the said constituting lord and in his stead and name — to demand, exact, levy, recover and receive, and to acknowledge having received and had, in court and out of court, from all and singular persons whosoever whose interest it is, will be or can in any way in the future concern, a certain bale of raw silk called Talanna [Note: possibly a place-name indicating origin, or a trade designation] weighing one hundred and sixty-four pounds by English weight at the rate of sixteen ounces to the pound or mark, marked with the sign shown in the margin of this present public instrument together with a number, and also a small fardel [Note: a bundle or package] with two dozen handkerchiefs [Note: "manutergiorum" — hand-cloths or towels] of a total value of seventy pounds sterling or thereabouts, which were recently taken by violence at sea by the Lübeck sea-pirates [Note: "maris piratos" — the document uses the strong language "sea-pirates" rather than "privateers"] off the coast of England from a certain vessel [Note: "schuta" — a flat-bottomed barge or lighter; distinct from a "hoya"] of the town of Antwerp, whose master was Adrian Johnson; and to compel those persons, if taken or detained, to make consignment and delivery of the said bale of raw silk and handkerchiefs, or to give adequate satisfaction for the same, together with all and singular damages, expenses, losses and interest whatsoever incurred, done and sustained and to be incurred, done and sustained on that occasion, by arrest of their persons and imprisonment, by arrest, sale and distraint of their goods, and also by ecclesiastical censures and by every other appropriate and due mode of compulsion; and if it seems fit to the same attorney, to treat, compound, agree, transact and reach compromise with the aforesaid persons and each or any of them in reason of the foregoing with respect to what has been received, had and recovered, and concerning any final settlement and agreement in that regard — to quit, free, put an end to and absolve, and to give, make and tender letters of quitclaim, final discharge and release, with a covenant never henceforth to seek anything further therefrom in perpetuity; to cause and procure seizures, sequestrations, proclamations, precepts, prohibitions, detentions and arrests, both of persons and goods, if necessary; and when the time comes, to command that they be relaxed, lifted and remitted; and for the foregoing and the matters written below, if need be, to appear before whatsoever lords, admirals, mayors, bailiffs, sheriffs, officials, auditors, jurors, judges, legislators, lieutenants and other judges and ministers of justice, both ecclesiastical and secular, whatever authority or jurisdiction they exercise and by whatever name they are known, in court and out of court; to respond, act and defend; to give, make and offer a libel or libels [Note: a formal written statement of claim] and any petitions orally or in writing; to respond to what has been offered and produced by the opposing party; to sue, counter-sue, raise exceptions and reply; to contest the suit or suits; to swear to calumny [Note: oath that a suit is brought in good faith, not maliciously] and to tell the truth, both on his own soul and on the soul of the said constituting party; to posit and set out articles; to respond to positions and articles on the part of the opposing party; to watch witnesses swear; to produce witnesses, letters and any other documents in testimony and to rebut others produced against them; to allege crimes and defects; to protest against summonses, notifications and denunciations, and to make requests in the cause or causes; to conclude; to implore the office of the judge; to hear his interlocutory and definitive sentences and to appeal and protest against it or them and against any grievance; to pursue and notify spiritual appeals and protests and, if he wishes, to renounce a legal claim; to seek and obtain an apostle [Note: a letter of request from a lower to a higher court] and costs of the suit and to require their assessment and to swear thereupon; and to substitute in his place once or several times one or more attorney or attorneys having a similar or lesser authority and power, and to revoke, annul and dismiss him or them so substituted, and, with him or them so revoked, to resume the business of this present procuration in himself, the present mandate remaining in force; and also for all other and singular matters to urge, do, procure and execute, which in all and singular the foregoing and in matters depending from, arising from, contingent upon, accessory, annexed and connected to them shall be necessary and entirely expedient, and which the order of law and the merits of the said matters demand and require, and which the said constituting party could do, execute and fulfil if he were present in person, even if they were of such a kind as to require by law, usage, style or local custom a more special mandate — the said constituting party giving and granting to his aforesaid attorney and the substitute or to be substituted by him in all and singular the foregoing and matters depending thereon as stated above full, ample, broad, free and general mandate with full, ample, broad, free and general administration, power and authority; the said constituting party promising me, the undersigned public notary, as a public person in public office, stipulating and receiving in the name and on behalf of all and singular persons whose interest it is, will be or can in any way in the future concern, that he will perpetually and at all times hold ratified, approved, valid and firm all and everything whatsoever and howsoever shall be done, transacted or in any way procured in all and singular the foregoing and matters depending thereon as above by his said attorney and by whomever and whosoever shall be substituted by him, under mortgage and obligation of all and singular his goods, present and future. And wishing to relieve his said attorney and whomever and whosoever shall be substituted by him from all burden of security, he promised and solemnly covenanted to me the said and undersigned notary, in the aforesaid capacity of written instrument, to stand to judgment and to abide by the judgment with all its clauses, unless he shall be noted [Note: "pronotus" — formally indicted or condemned], upon all which foregoing matters thus transacted the said constituting party requested and earnestly required that one or more public instruments be made and delivered to him by me, the undersigned notary.

These acts were done at London, as written and recited above, those then present there being the prudent men John Anthonio Negro and Hieronimo de Mezi, merchant of Venice, witnesses specially summoned and requested for the foregoing.

And because I, Edward Barbour, clerk, citizen of the city of London, public notary by sacred apostolic authority, was personally present at the aforesaid appointment of attorney, constitution, ordination, grant of power, and all other and singular matters aforesaid while they were, as stated above, being transacted and done, together with the aforementioned witnesses, and saw and heard these things done in this manner, I therefore, being otherwise occupied, had this instrument written by another, and signed it with my customary and accustomed sign and names, as requested and required. And it is known to me, the said notary, that there is a correction [erasure] of the words "and handkerchief(s)" [Note: "ac manutergione ad hujusmodi"] in the seventeenth line, which is manifestly a scribal error.

---""",
    53: """The letter of legality [Note: "littera legalitatis" — an authentication or certificate of the official standing of a notary] of this instrument.

To all and singular sons of holy mother Church who shall see, read or hear these present letters: Christopher Ascue, knight, mayor and alderman of the city of London in the renowned kingdom of England, everlasting greeting in the Lord. Because we ought to confirm, and as we are bound to bear witness in truth about, those whom uprightness adorns with good character and whose conduct in other meritorious aspects of life has been laudably commended — so that in the reliable carrying out of their affairs trust and credence may be given to them, and errors of any kind may be wholly eradicated — therefore it is that by the tenor of these presents we make known to all of you how our beloved fellow citizen Edward Barboure, clerk of the diocese of London and citizen of the city of London, public notary by sacred apostolic authority, who has written, published and reduced to public form the instrument attached hereto [No. 52] in his own hand, and signed it with his customary and accustomed sign and name, is a public notary by apostolic authority who has long faithfully exercised among us the art, office and faculty of the notarial profession and currently exercises it, and to whom as a public and authentic person for the drawing up and making of instruments of any kind for men's affairs resort is made daily by all persons, and whose writing and instruments both in court and out of court have been and are accustomed to be given full faith by all. Wherefore we earnestly request and ask of all of you that to the said instrument attached hereto as aforesaid, wherever it may be shown or is to be shown, you may be willing to give full credence.

Written at the aforesaid London under the seal of the office of our mayoralty of the aforesaid city, on the fourth day of the month of February in the year of the Lord according to the usage and reckoning of the English church one thousand five hundred and thirty-three [Note: Annunciation Style; = 1534 modern reckoning], and in the twenty-fifth year of the reign of Henry the Eighth, by the grace of God King of England and France, defender of the faith and lord of Ireland.

These two present copies have been checked and collated by me, Michael Petri, clerk of the diocese of Schwerin, public notary by sacred apostolic and imperial authority, and agree with their true originals, as I attest in my own hand.

---""",
    54: """Anthonius Oberomiza

In the year 1534, the seventh indiction, on Thursday the twelfth of the month of March, the honourable and highly wise lords, lord Clawes Bardewick and lord Hermen Schute, councillors of Lübeck, by order of the honourable council there at Lübeck and before me as public notary and the undersigned witnesses specially summoned and requested for this purpose, in the presence of the honourable man Anthonius Oberomiza, a Venetian dwelling in London in England, as the principal owner to himself of the following goods and items — not out of obligation but out of goodwill and out of reverence and favour of the royal grace of England — have graciously returned, accounted for and delivered [the said goods]; and the aforesaid Anthonius, from such delivery, has received them back with gratitude; he also specified and designated them and thereupon swore a solemn oath to God and His saints that the following items belong to himself alone and to no Hollander, Brabanter or Zealander, and that no one else has any share or part in them — according to the tenor of a public instrument made thereupon etc. And these items had been laden in skipper Adrian Johnson's hoy and were taken in the last preceding summer by the Lübeck privateers against the Hollanders on the open sea, yet without the order and consent of the honourable council of Lübeck.

Done at Lübeck, where Anthonius took the oath in the chancellery and for the delivery and recovery of the items in the house of Hinrick Cordes, citizen of Lübeck, in the presence of the honourable men Laurens Wilmers, Hermen Mollers and Gerth Falcken, resident citizens of Lübeck, as witnesses specially and individually summoned and requested for this purpose.

So it is as above, which I, Michael Petri, public notary by apostolic and imperial authority, attest in my own hand as required for the foregoing.

Item, the following items the named lords have handed over to Anthonius Oberomiza and which he has received:

Nine dozen stone pots
6 dozen tin pots and 9 pots
Item, 5 dozen bells and 5 bells
Item, 10 mirrors
Item, one image or holy figure
Item, 8 platters
Item, 10 candlesticks
Item, 6 basins with pig-bristle
Item, 4 marking compasses and 4 compasses
Item, 26 hammers
Item, 8 tongs
Item, these aforesaid items were in one large basket.

Now since the same Dutch hoy in which the aforesaid Anthonius's goods had been laden had sunk and otherwise been wrecked, so that the same Anthonius complained that he was still missing some goods and items that had either sunk or been taken from him by the Lübeck fighting men, etc., therefore afterwards the honourable council of Lübeck, out of particular benevolence, came to a full, complete and entire settlement with the aforesaid Anthonius in respect of all goods and items that had sunk or been taken from him and which he was still missing, [agreeing upon] a good agreed sum of money, which he has, to his full satisfaction, truly and well received in counted cash from lord Gotken Engelsteden and lord Albert Clever, councillors of Lübeck appointed for this purpose, on a set day, and [he swore] an oath before me as public notary and witnesses specially summoned for this purpose; and he has thereupon released and given a full quitclaim to the aforesaid honourable council and all the common citizens and inhabitants of the city of Lübeck, for himself and his heirs, of all the goods and items written above — received, sunk and taken — and also of everything else he was still missing, and also of costs, damages, expenses, profits and interest, fully and entirely quit, released, free and clear and of all claims; and renounced all legal rights etc. He also swore a solemn oath for himself and his heirs never again to make any claim or demand therefor etc., so that the honourable council and the city of Lübeck shall be quit, free, released and clear with a single payment, according to the tenor of a public instrument made thereupon in which this matter is fully set out and contained — without deceit or ill intent.

So it is as above, which I, Michael Petri, public notary by apostolic and imperial authority, attest in my own hand as required for the foregoing.""",
    55: """In the same year 1534, in the seventh indiction, on Thursday the twelfth day of the month of March, the honorable and highly wise lords Claus Bardewick and Hermann Schute, councillors of Lübeck specially deputed for this purpose, delivered, surrendered, and handed over to the oft-mentioned Anthonius Oberomiza, before me the undersigned public notary and the witnesses called and requested for this purpose, as to a true and undoubted procurator and authorized agent of the honorable man Martin de Federigo, Venetian merchant, his principal, one bale of silk marked thus [merchant's mark no. 1 in the left margin], which bale belongs to the said Martin de Federigo, and which the above-named Anthonius Oberomiza received back on his behalf with gratitude, and [thereby] fully released and acquitted the aforesaid honorable council, all and every citizen and inhabitant of the entire imperial city of Lübeck. He also swore on his principal's soul never again to raise any claim in the matter, so that the honorable council and city of Lübeck shall by means of this delivery be quit, free, clear, and released, and he renounced and waived all legal rights in the name of his principal and all his heirs, as set out in a public instrument drawn up to that effect, in which the foregoing is further set forth and elaborated — all without fraud or malice. This bale of silk had also been loaded aboard the hoy of skipper Adrian Johansen.

Done at Lübeck, after the taking of the oath in the chancellery and the receipt of the bale, in the house of Hinrick Cordes, in the presence and attendance of the honorable men Laurens Wilmes, Herman Moller, and Ghert Falcken, resident citizens of Lübeck, as witnesses specially called and requested for this purpose, jointly and severally.

This is as stated above, which I, Michael Petri, public notary by sacred apostolic and imperial authority, requested for the foregoing, attest with my own hand.

---""",
    56: """Copy of the instrument of quitclaim and acknowledgment of goods received by Anthonius Oberomiza on behalf of the honorable council of Lübeck.

In the name of the Lord, amen. Let it be clearly apparent and known to all through this present public instrument that in the year from the Nativity of the same Lord one thousand five hundred and thirty-four, the seventh indiction, on Tuesday the thirty-first and last day of the month of March, under the reign of the most glorious, most unconquered, and Catholic prince and lord, lord Charles the Fifth, by the grace of divine clemency ever-august Emperor of the Romans, and king of Germany, Spain, both Sicilies, Jerusalem, Hungary, Dalmatia, Croatia, etc., Archduke of Austria, and Duke of Burgundy, etc., in the fifteenth year of his reign — whereas it had previously occurred that in the year of the Lord one thousand five hundred and thirty-three, in the month of August, during the time of wars and hostilities between the people of Lübeck on the one part and the Hollanders on the other part, the honorable lords of the council of Lübeck, among other goods, seized certain goods that were in a certain ship commonly called a hoy [Note: a type of single-masted coastal vessel] belonging to the city of Antwerp, of which the master or captain was Adrian Johansen (as he then was), and which had been seized on the open sea by the hired soldiers [Note: Latin milites stipendiarii, meaning mercenary or contracted soldiers] deputed by the said people of Lübeck, yet without the consent and mandate of the said lords of the council of Lübeck; and when those goods had arrived at or been brought to the city of Lübeck, the aforesaid council had received them into their custody for no other purpose than for the benefit and advantage of common merchants, and had caused them to be faithfully preserved — therefore, before the distinguished and prudent men, lords Godehard Engelstede and Albert Clever, councillors of Lübeck, deputed for this purpose by the distinguished council of Lübeck and assembled together for the conduct of this business in the upper chamber of the town hall of Lübeck, in my presence as public notary and that of the witnesses named below, specially called and requested for these matters — there appeared in person the prudent man Anthonius Oberomiza, a Venetian, residing as he declared in the kingdom of England in the city of London, who in person and on his own behalf designated certain goods as belonging to himself as the primary party, and one bale of raw silk called Talanna [Note: a type of raw silk, possibly from Talamone in Tuscany], weighing one hundred and sixty-four pounds in English measure at the rate of sixteen ounces to the pound, as belonging respectively to the prudent man Martin de Federigo, likewise a Venetian merchant, his principal, as having been in the said hoy — not compelled or induced by force, deceit, fear, fraud, or malicious contrivance, but by his own pure, free, spontaneous, and personal will, he had declared and openly and publicly acknowledged in truth, and did acknowledge and confess, both in his own name and in that of the said Martin his principal, sustained by his legitimate mandate for this purpose, that previously on the twelfth day of the said month of March, out of favor and reverence for the most serene prince and lord, lord Henry, King of England, from the distinguished and prudent men, lords Nicholas Bardewick and Hermann Schute, councillors of Lübeck, deputed for this purpose by the distinguished council of Lübeck, he had first, as the duly appointed and constituted procurator of the said Martin de Federigo his principal — as he demonstrated by proof of his mandate of procuration — truly and effectively received back the said bale of raw silk designated above and belonging to the said Martin his principal, and those goods and merchandise which the said hired soldiers the previous year and month, off the shores and ports of the kingdom of England, dispatched with the warships or vessels of war or hostility of the said city of Lübeck, had seized, taken, and carried away from him Anthonius Oberomiza, namely: nine dozen stoneware jugs or cups; item six dozen tin cups and nine tin cups; item seven dozen small bells and campanellas [Note: small bells], and seven campanellas; item ten mirrors and a certain image; item eight tin dishes or tarschas [Note: a type of flat dish]; item ten candlesticks; item six chests of silk made from pig bristles [Note: brushes made from pig-hair packed in chests]; item four iron rings for signs and further three iron rings; item twenty-six iron hammers; item eight iron tongs. He reported that the aforesaid goods had all been together in one large basket [Note: Latin magno canistro]. And for the purpose of seeking the restitution of those goods the said Anthonius Oberomiza had come to the city of Lübeck, and he had openly and publicly declared and acknowledged that those goods had been generously returned, restored, and delivered to him by the said lords councillors; and the said Anthonius swore, with arm outstretched and the foremost fingers raised, a bodily oath on the holy Gospels of God, that the aforesaid goods belonged to himself and the bale of raw silk to the said Martin, and to no others among the enemies of the said people of Lübeck. And since the same Anthonius had further complained that certain goods or merchandise belonging to him had been abstracted or alienated from the said hoy, or had gone missing when the said ship suffered shipwreck, and for the compensation of the same and for all other damages and all and every costs incurred on that account and for all loss of interest and profit, the said lords Godehard Engelstede and Albert Clever, the aforesaid councillors, in the name of the entire council of Lübeck, generously and favorably, in the presence of me the notary and the witnesses named below, assigned and paid to the same Anthonius Oberomiza twenty-five Rhenish florins [Note: a gold coin of the Holy Roman Empire] in ready and counted money, and those twenty-five florins he accepted gratefully in settlement of his claim, and he declared himself well paid, discharged, and acquitted for such lawful satisfaction and real settlement, and gave thanks. And concerning all and each of the aforesaid goods and the bale of raw silk and the said twenty-five florins and all other alienated, abstracted, plundered, or sunken goods — having been restored, received, and discharged — the oft-said Anthonius Oberomiza, fully on behalf of himself and the said Martin de Federigo on account of the aforesaid bale of raw silk, and in the names of their heirs, released, freed, wholly acquitted and absolved the aforesaid council, magistracy, councillors, and all citizens and inhabitants of Lübeck, and granted them a final settlement, quitclaim, and perpetual covenant not to seek anything further — renouncing also the exception [Note: a formal legal defence] of the said goods having been restored and paid and of such a sum of money not having been held or received, and of any future hope of holding, receiving, and being paid, by which he might be able in any way to defend or protect himself against the foregoing or any part thereof — to such a degree that neither the said council nor their citizens or inhabitants may henceforth ever in perpetuity be sued, harassed, disturbed, or troubled in court or outside it on account of these and all the received, discharged, plundered, or sunken goods and concerning the said sum of money, but willing to keep and observe them as immune, harmless, indemnified, absolved, and freed from these obligations by solemn stipulation [Note: a formal verbal contract], with the imposition of a mortgage and obligation over all his movable and immovable goods, present and future, and by any other renunciation of law and fact necessary for this purpose, and every precaution; and he swore by oath, touching the sacred things on the holy Gospels of God, that he and the said Martin, on account of the aforesaid bale of raw silk, would firmly and inviolably observe all the foregoing, under penalty of the guilt of perjury. Concerning all and each of the aforesaid matters, the said lord Godehard Engelstede in the name of the entire council of Lübeck requested through me the undersigned public notary that one or more public instrument or instruments be drawn up.

These things were done in the aforesaid city of Lübeck, in the upper chamber of the town hall there, in the year, indiction, day and other circumstances stated above, with the honorable men, lords Johannes Proth and Joachim Sevelt, priests of Lübeck, and the prudent and honorable men Johannes Vorhorde, layman of Cologne, and Thomas Dusterhusen and Simon Schulren, citizens of Lübeck, being present as witnesses specially called and requested for the foregoing.

And I, Michael Petri, cleric of the diocese of Schwerin, public notary by sacred apostolic and imperial authority — since I was present together with the named witnesses at this confession, quitclaim, promise, renunciation, and oath-taking, and all and each of the foregoing, while they were being thus conducted and transacted as stated above, and I saw and heard them so done and took note of them — I therefore drew up, subscribed, published, and reduced to this public form this present public instrument, faithfully written by another hand while I was in the meantime occupied with other business, and extracted from my notes, and I signed, confirmed, and strengthened it with my customary and accustomed sign, name, and surname in faith, confirmation, and manifest testimony of all and each of the foregoing, having been called upon and required.

[Notarial sign of Michael Petri]

---""",
    57: """Copy of the instrument of quitclaim and acknowledgment of goods received by Anthonius Oberomiza on behalf of the distinguished council of Lübeck.

In the name of the Lord, amen. Let it be clearly apparent and known to all through this present public instrument that in the year from the Nativity of the same Lord one thousand five hundred and thirty-four, the seventh indiction, on Tuesday the thirty-first and last day of the month of March, under the reign of the most glorious, most unconquered, and Catholic prince and lord, lord Charles the Fifth, by the grace of divine clemency ever-august Emperor of the Romans, and king of Germany, Spain, both Sicilies, Jerusalem, Hungary, Dalmatia, Croatia, etc., Archduke of Austria, and Duke of Burgundy, etc., in the fifteenth year of his reign — whereas it had previously occurred that in the year of the Lord one thousand five hundred and thirty-three, in the month of August, during the time of wars and hostilities between the people of Lübeck on the one part and the Hollanders on the other part, the honorable lords of the council of Lübeck, among other goods, seized certain goods that were in a certain ship commonly called a hoy belonging to the city of Antwerp, of which the master or captain was Adrian Johansen (as he then was), and which had been seized on the open sea by the hired soldiers deputed by the said people of Lübeck, yet without the consent and mandate of the said lords of the council of Lübeck; and when those goods had arrived at or been brought to the city of Lübeck, the aforesaid council had received them into their custody for no other purpose than for the benefit and advantage of common merchants, and had caused them to be faithfully preserved — therefore, before the distinguished and prudent men, lords Godehard Engelstede and Albert Clever, councillors of Lübeck, deputed for this purpose by the distinguished council of Lübeck and assembled together for the conduct of this business in the upper chamber of the town hall of Lübeck, in my presence as public notary and that of the witnesses named below, specially called and requested for these matters — there appeared in person the prudent man Anthonius Oberomeza, a Venetian, residing as he declared in the kingdom of England in the city of London, who in person on his own behalf designated certain goods as belonging to himself as the primary party, and one bale of raw silk called Talanna, weighing one hundred and sixty-four pounds in English measure at the rate of sixteen ounces to the pound, as belonging respectively to the prudent man Martin de Federigo, likewise a Venetian merchant, his principal — as having been in the said hoy — not compelled or induced by force, deceit, fear, fraud, or malicious contrivance, but by his own pure, free, spontaneous, and personal will, he had declared and openly and publicly acknowledged in truth, and did acknowledge and confess, both in his own name and in that of the said Martin his principal, sustained by his legitimate mandate for this purpose, that previously on the twelfth day of the said month of March, out of favor and reverence for the most serene prince and lord, lord Henry, King of England, from the distinguished and prudent men, lords Nicholas Bardewick and Hermann Schute, councillors of Lübeck, deputed for this purpose by the distinguished council of Lübeck, he had first, as the duly appointed and constituted procurator of the said Martin de Federigo his principal — as he demonstrated by proof of his mandate of procuration — truly and effectively received back the said bale of raw silk designated above and belonging to the said Martin his principal, and those goods and merchandise which the said hired soldiers the previous year and month, off the shores and ports of the kingdom of England, dispatched with the warships or vessels of war or hostility of the said city of Lübeck, had seized, taken, and carried away from him Anthonius Oberomiza, namely: nine dozen stoneware jugs or cups; item six dozen tin cups and nine tin cups; item seven dozen small bells and campanellas, and seven campanellas; item ten mirrors and a certain image; item eight tin dishes or tarschas; item ten candlesticks; item six chests of silk made from pig bristles; item four iron rings for signs and further three iron rings; item twenty-six iron hammers; item eight iron tongs. He reported that the aforesaid goods had all been together in one large basket. And for the purpose of seeking the restitution of those goods the said Anthonius Oberomiza had come to the city of Lübeck, and he had openly and publicly declared and acknowledged that those goods had been generously returned, restored, and delivered to him by the said lords councillors; and the said Anthonius swore, with arm outstretched and the foremost fingers raised, a bodily oath on the holy Gospels of God, that the aforesaid goods belonged to himself and the bale of raw silk to the said Martin, and to no others among the enemies of the said people of Lübeck. And since the same Anthonius had further complained that certain goods or merchandise belonging to him had been abstracted or alienated from the said hoy, or had gone missing when the said ship suffered shipwreck, and for the compensation of the same and for all other damages and all and every costs incurred on that account and for all loss of interest and profit, the said lords Godehard Engelstede and Albert Clever, the aforesaid councillors, in the name of the entire council of Lübeck, generously and favorably, in the presence of me the notary and the witnesses named below, assigned and paid to the same Anthonius Oberomiza twenty-five Rhenish florins in ready and counted money, and those twenty-five florins he accepted gratefully in settlement of his claim, and he declared himself well paid, discharged, and acquitted for such lawful satisfaction and real settlement, and gave thanks. And concerning all and each of the aforesaid goods and the bale of raw silk and the said twenty-five florins and all other alienated, abstracted, plundered, or sunken goods — having been restored, received, and discharged — the oft-said Anthonius Oberomeza, fully on behalf of himself and the said Martin de Federigo on account of the aforesaid bale of raw silk, and in the names of their heirs, released, freed, wholly acquitted and absolved the aforesaid council, magistracy, councillors, and all citizens and inhabitants of Lübeck, and granted them a final settlement, quitclaim, and perpetual covenant not to seek anything further — renouncing also the exception of the said goods having been restored and paid and of such a sum of money not having been held or received, and of any future hope of holding, receiving, and being paid, by which he might be able in any way to defend or protect himself against the foregoing or any part thereof — to such a degree that neither the said council nor their citizens or inhabitants may henceforth ever in perpetuity be sued, harassed, disturbed, or troubled in court or outside it on account of these and all the received, discharged, plundered, or sunken goods and concerning the said sum of money, but willing to keep and observe them as immune, harmless, indemnified, absolved, and freed from these obligations by solemn stipulation, with the imposition of a mortgage and obligation over all his movable and immovable goods, present and future, and by any other renunciation of law and fact necessary for this purpose, and every precaution; and he swore by oath, touching the sacred things on the holy Gospels of God, that he and the said Martin, on account of the aforesaid bale of raw silk, would firmly and inviolably observe all the foregoing, under penalty of the guilt of perjury. Concerning all and each of the aforesaid matters, the said lord Godehard Engelstede in the name of the entire council of Lübeck requested through me the undersigned public notary that one or more public instrument or instruments be drawn up.

These things were done in the aforesaid city of Lübeck, in the upper chamber of the town hall there, in the year, indiction, day and other circumstances stated above, with the honorable men, lords Johannes Proth and Joachim Sevelt, priests of Lübeck, and the prudent and honorable men Johannes Vorhorde, layman of Cologne, and Thomas Dusterhusen and Simon Schulren, citizens of Lübeck, being present as witnesses specially called and requested for the foregoing.

And I, Michael Petri, cleric of the diocese of Schwerin, public notary by sacred apostolic and imperial authority — since I was present together with the named witnesses at this confession, quitclaim, promise, renunciation, and oath-taking, and all and each of the foregoing, while they were being thus conducted and transacted as stated above, and I saw and heard them so done and took note of them — I therefore drew up, subscribed, published, and reduced to this public form this present public instrument, written with my own hand and extracted from my notes, and I signed, confirmed, and strengthened it with my customary and accustomed sign, name, and surname in faith, confirmation, and manifest testimony of all and each of the foregoing, having been called upon and required.

This present copy was compared and collated by me, the same Michael Petri, cleric and notary as above-named, and it agrees with its original, which I attest with my own hand.

---""",
    58: """Our friendly greetings and whatever good we are able to offer! Honorable and wise, especially favorable, good friends! Our fellow council-members and citizens, namely Johann Campman, Peter Heynebach, Hermann Suyderman, Dirk Horner, Peter Slootkenn, and Johann Borner, have approached us and made known to us how, some time past, they had freighted goods on a ship with a shipper named Adrian Janssoon, to be conveyed and brought to England; which goods, as they understand and make known, having been carried by storm or similar circumstances at sea, have arrived at your honorable city of Lübeck and been received into safekeeping — as your honor is informed by the present bearer, Jacob van Mulheim, whom they have dispatched with the present letter sealed under our city seal, with full authority and instruction to defend said goods on their behalf, whether by oath or otherwise, as your honorable body shall determine from him. And they have further requested of us that we likewise act by virtue of the Hanse [Note: the Hanseatic League] and be favorable to him in this matter, as is then reasonable and proper, as your honorable body knows well how to conduct and carry itself. Also, since we look to and trust in your honorable body for all favorable assistance and friendship, we request and desire in friendly earnest that your honorable body, as a friendly favor to us and for the benefit of our aforesaid citizens, be willing to grant full credence to the said Jacob, their authorized agent, in his business regarding the aforesaid goods, and to be so favorable, supportive, and helpful that our aforesaid people may be assisted in coming to their goods without any penalty or loss, as your honorable body would willingly have done likewise in our case, and as we fully trust in you and all goodness together with favor and friendship in particular — to which same your honorable body may our Lord God preserve in all fortunate welfare and governance for a long time. Written on the 6th day of October in the year etc. [15]33.

Burgomaster and council of the city of Cologne.

---""",
    59: """Item in the year of the Lord 1533, in the 6th indiction, on the 19th day of the month of October, the following marks were recorded on the aforesaid bales and goods — which goods were in the ship of the above-named Adrian Johansen — and were inspected and listed in the presence of lords Nicholas Bardewick and Hermann Schute, as follows, however brought about through the efforts of the honorable lord Master Henning Kulemeiger, cleric, secretary of the honorable merchant community at London in England, resident at the Steelyard [Note: the Kontor, or Hanseatic trading post, in London], this being done out of goodwill and with the leave of an honorable councillor here in Lübeck, for the benefit of the merchants of the Cologne Third [Note: one of the three administrative divisions of the Hanseatic League, grouping the western Hanseatic towns including Cologne].

[1.] Item two bales of Osnabrück fustian [Note: a type of heavy cotton cloth from Osnabrück] marked thus [merchant's mark no. 1 in the right margin] and twenty-six pieces of brass wire marked thus [merchant's mark no. 2 in the right margin].

[2.] Item one cask with silk marked thus [merchant's mark no. 5 in the right margin].

[3.] Item one pack marked thus [merchant's mark no. 6 in the right margin].

[4.] Item one small chest marked thus [merchant's mark no. 7 in the right margin].

[5.] Item one small barrel marked thus [merchant's mark no. 8 in the right margin].

[6.] Item another cask marked thus [merchant's mark no. 9 in the right margin].

[7.] Item one cask with haberdashery goods marked thus [merchant's mark no. 4 in the right margin].

[8.] Item one bale with saws or the like marked thus [merchant's mark no. 3 in the right margin].

Witnesses: lord Hinrick Kordes and Tyle Lutguwe.
Nicholas Klone wrote this with his own hand.

---""",
    60: """Item in the year etc. 33, on the 20th day of October, through the efforts of the honorable lord Master Henning Kulemeier aforesaid, and also in the presence of lords Nicholas Bardewick and Hermann [Schute], one cask marked thus [merchant's mark no. 1 follows] was opened and inspected, in which were found several bundles wrapped in paper, and among them a small linen purse with money. The same was sealed, confirmed, and authenticated with this mark [merchant's mark no. 2 follows].

Witnesses: Marcus Luthmar, Sivert Kock, Claus Haselouwe.

All these established citizens were specially called and summoned here for this purpose.

This is as stated above, which I, Nicholas Klone, attest with my own hand. Done at Lübeck in the year of the Lord as above, the notary having been called upon and required for this purpose.""",
    61: """Item, forty-five bundles of silk belonging to Johann Borne, marked thus [merchant's mark no. 1 in the right margin].

Item, also two bales of sardoc [Note: a type of woolen cloth] belonging to Johann Kamman, marked thus [merchant's mark no. 2 in the right margin].

Item, one small chest with glassware and a slaughter-cloth [Note: a type of protective cloth] belonging to Dirick Horner.

Item, in the year 1533, in the 6th indiction, on the 6th day of the month of November, Jacob von der Mulln, with the permission of an honorable council member, and also in the presence of the honorable lords Nicolaus Bardewick and Hermann Schuten, received the following goods, which had been unloaded from Adrian Johanssen's ship and subsequently hoisted into Hinrick Krons's warehouse under the Englishmen's [district].

[1.]
Marked thus [merchant's mark no. 1 in the right margin].

[2.]
[merchant's mark no. 2 in the right margin].

[3.]
[merchant's mark no. 3 in the right margin].

[4.]
Item, also one small cask belonging to a poor young man, marked thus [merchant's mark no. 4 in the right margin]; and for this mark the aforementioned Jacob shall procure a certificate for the honorable council here in Lübeck and have it delivered into their hands.

[5.]
Item, also twenty-six pieces of copper wire belonging to Johann Kamman, marked thus [merchant's mark no. 5 in the right margin]; and for this mark the aforementioned Jacob shall likewise procure a certificate, etc.

Item, also one vat with sixty bundles and one slaughter-cord, marked thus [merchant's mark no. 6 follows], belonging to Peter Sclotzke; among the aforementioned bundles, a linen parcel marked thus [merchant's mark no. 7 follows], containing four hundred sun-crowns [Note: a gold coin, the écu au soleil] belonging to Peter Heinebach. In the same parcel yet another small purse was found, marked thus [merchant's mark no. 8 follows], in which were found forty-two and a half angel-nobles [Note: English gold coins] belonging to Hermen Suderman.

[6.]

Witnesses: Lord Albert Kleve and Adrian Johanssen.

So it is as stated above, which I, Nicolaus Klne, attest with my own signature. Done in Lübeck in the year of the Lord as stated above, I, the notary, having been requested and called upon.

---""",
    62: """Praise be to God.

Know, dear Johann, good friend, that when you arrive in Lübeck, please also make enquiry about your tun. There were clothes in it, and the tun is marked with this mark [merchant's mark no. 1 in the right margin]. It belongs to a fellow who has recently moved to England and is a servant of Johan Borne. He also has certain goods there with it. So Johann Born had himself included with him in the letter which our lords will be sending there; and as for what goods he has with it, we had no knowledge that our lords had written about the goods, so do your best and press for it, that one might get it back. If it does come back to hand, you shall be given a good drink-money [Note: a gratuity].

Item, namely these are the clothes that are therein, as written hereafter:

one taffeta English underskirt
one black worsted doublet
one black sardonet doublet
two pairs of black hose

one cotton camlet collar [Note: camlet was a fine fabric, often of mixed wool and silk]
one black leather collar
Item, also two black pelts and five shirts
also two pairs of shoes
also two wooden kitchen pots and other sundry things, such as books and fine cloths

and other things more, which are worth money.

Dear Johann, do your best then. You will be well rewarded for it. You shall deliver this letter to my lord's servant in Lübeck. He is well known there. He shall also be of help to you. You shall ask for him at the wine-cellar. They will give you directions there.

---""",
    63: """Item, in the year etc. 33, on the 27th day of the month of September, Hinrick Houwide,

[1.]
citizen of Bremen, received from the aforesaid goods [namely those in Adrian Johnson's ship: no. 42] eleven pieces of bales, all marked thus [merchant's mark no. 1 follows], with the permission of an honorable council.

Item, the aforementioned Hinrick Houwide also received from the same aforesaid

[2.]
goods, in the name and stead of Albert Kreien, two bales with almonds, marked thus [merchant's mark no. 2 follows]. This too was done with the permission of an honorable council and in the presence of the honorable lords Nicolaus Bardewick and Hermen Schuten.

Witnesses: Lord Hinrick Kordes and Tyle Lutzouwe.

Nicolaus Klone wrote this with his own hand.

---""",
    64: """Honorable and prudent Lord Harmen Schute! Your honor should know that by our privateers [Note: Lübeck's authorized raiders] operating under England, a ship named after Adrian Johansen was seized, in which a fellow, born into the Hanse [Note: the Hanseatic League] in Deventer, named Roleff Vos, had one dry small cask with this mark [merchant's mark no. 1 in the left margin]. Therein should be 37 pieces of Bruges satin [Note: "Bruggesch settin," a high-quality silk fabric from Bruges], as the color and quality will sufficiently indicate, along with a power of attorney which I hold from the honorable merchant residing in England, likewise Roleff Vos's own handwriting.

Also therein should have been a chest and a small cask [merchant's mark no. 2 in the left margin] belonging to a man born in Wesel, in the land of Cleves, but now residing in England, for whom Lord Marcus Meyger also has authority. However, as people now hear, the goods are being returned to their owners, and accordingly a representative of Cologne by the name of Hynrick im Wynckel has been here in Lübeck and has received part of the goods. They do not know, however, whether their goods were also released and received by the representative. The aforementioned Roleff Vos has therefore granted me full power of attorney before the merchant community in London to receive his goods; the other man, however, has asked Lord Marcus Meyger and me alongside him to bring his goods. Since goods with the above-mentioned marks are still present, and an honorable council together with your honor are disposed toward this matter, I would wish to make a friendly request of your honor that you be so good as to look out for goods bearing such marks and give me a favorable answer thereon. Wherever I can be of service and goodwill to your honor, I will at all times be found ready and willing. God willing, to whom I commend your honor.

[signed] Jheronimus Molhusen

---""",
    65: """On 1 June 1534, Hermann Schute, councillor of Lübeck, at the behest of the Lübeck council, delivered and handed over to the worthy and distinguished man, Master Johan Vorhorde — given that he was accompanying the honorable, prudent, and most wise lords Gerth Odingborg and Hans van Elphram, also councillors of Lübeck, as appointed ambassadors to the royal majesty of England together with the appointed secretary — one dry merchandise cask in which goods were contained, and one square large chest or bale, marked thus [merchant's mark no. 1 in the left margin], belonging to Richard Engelbarth, a Hanseatic merchant residing in the kingdom of England. The aforementioned Master Johan Vorhorde received the said dry merchandise cask and square chest or bale from Lord Hermen Schuten as stated, and gave his promise to deliver and hand them over to the said Richard Engelbarth. Done at Lübeck in the year and on the day as stated above. — 1 June 1534. Lübeck.

---""",
    66: """In the name of God, amen. By this present public instrument let it be evident to all, that in the year of the Lord from the Incarnation one thousand five hundred and thirty-three, in the sixth indiction, in the pontificate of the most holy father in Christ and our lord, Lord Clement, by divine providence Pope of this name the seventh, in his tenth year, on the twentieth day of September [20 Sept. 1533], before me, the undersigned public notary, and the witnesses named below, there appeared in person the prudent men Robert Pagiet, citizen and alderman of the city of London, Thomas Gale, citizen and haberdasher [Note: a dealer in men's clothing and accessories] of the same city, aged, as he declared, about fifty-seven years, Robert Wilford, aged about thirty-six years, and Ralph Foxley, aged about thirty-seven years, both citizens and merchants of the aforesaid city, and William Wilford, citizen and grocer of the same city, aged about twenty-six years — all men of good repute and unblemished conduct, not induced, seduced, compelled, deceived or circumvented by force, fraud, fear, deceit or any sinister contrivance, as is evident, but of their own free, pure and spontaneous will, for future record and for the declaration of the truth of the matters written below, and for the preservation and defense of their rights, both those of them collectively and of each one of them individually — declared, deposed and certified to me, the undersigned public notary, by their separate oaths made upon and over the holy Gospels of God, in the manner and form following, namely:

[1.]
First, the aforesaid Robert Pagiet, alderman, having deliberated, declared, deposed and certified to me, the undersigned public notary, by his oath made upon and over the holy Gospels of God, touching the written text with his right hand, that it was and is true that the same Robert Pagiet, the deponent, in the month of August last past [Aug. 1533], before the date of this present public instrument, caused to be loaded and taken on board, in the port of the city of London, in a certain ship called the Christopher of Moros, in the parts of Galicia [Note: northwestern Spain], of which Johannes Shewards was then master under God, two packs of linen, each of which was marked with the first mark of the said Robert Pagiet made in the margin of this present public instrument [merchant's mark no. 1 in the left margin].

[2.]
Item, the aforesaid Thomas Gale declared by word of mouth, deposed and certified to me, the undersigned public notary, by his oath made upon and over the holy Gospels of God, touching the written text with his right hand, that it was and is true that the same Thomas Gale, the deponent, of his own goods in the said month of August [Aug. 1533], in the aforesaid port and in the aforesaid ship called the Christopher, of which the aforesaid Johannes Shewars was then master, caused to be loaded and taken on board one pack, numbered 4, containing sixteen short woolen cloths and twelve pieces of statutory [Note: cloth cut to the legally prescribed standard length] of blue color for wrapping the same, upon canvas, marked with the second mark in the margin [merchant's mark no. 2 in the left margin] of this present instrument, of the colors and lengths as follows: a violet 24¾ yards, a vesset [Note: a shade of tawny-brown] 24¼ yards, a red 25½, a muster [Note: a grey-brown mixed cloth] 24¾, a green medley 24¼, a muster 24¾, a violet 24¼, a blue 24, a blue 24½, a blue 24. And furthermore the same Thomas Gale, the deponent, declared, deposed and certified to me, the said notary, by his oath made as above, that it was and is true that each piece of the said sixteen woolen cloths and the said 12 pieces of statutory of the deponent were marked with the third mark in the margin [merchant's mark no. 3 in the left margin] of this present public instrument, impressed in lead and affixed to each of the said cloths and statutories.

[3.]
Item, the aforesaid Robert Wilford, having deliberated, declared, deposed and certified to me, the undersigned public notary, by his oath made upon and over the holy Gospels of God, touching the written text with his right hand, that it was and is true that the same Robert Wilford, the deponent, in the aforesaid month of August [Aug. 1533], caused to be loaded and taken on board in the said ship in the aforesaid port of the city of London three fardles [Note: bundles or bales] of short woolen cloths with their wrappings, belonging to and pertaining to the aforesaid Robert Wilford and his brothers, each fardle of the same being marked on the outside upon the canvas with the fourth mark in the margin [merchant's mark no. 4 in the left margin] of this present instrument; the first of these, numbered 1, containing sixteen cloths, was of the following numbers, colors and lengths, namely: 297 blue 24¾ yards, 298 blue 24½, 283 blue 23¾, 284 blue 24½, 245 blue 24½, 259 vesset 25¼, 272 vesset 25, 165 medley 24½, 173 medley 25, 299 red 24¾, 224 russet 25, 175 russet 25¼, 54 muster 25, 172 muster 25, 171 muster 25½, 277 plunket [Note: a dull grey-blue color] 26. The total length of the said sixteen cloths is 400 yards and one quarter, together with three pieces of cottons for wrapping the same fardle numbered 1, as follows: a green 21¼ yards good, green 21¾ yards good, green 20¾ yards good; each piece of the said sixteen woolen cloths being marked with the fifth mark in the margin [merchant's mark no. 5 in the left margin] of this present instrument, impressed in lead and affixed to each of the said cloths. The 2nd fardle of the said three contains nine cloths of the following color, of which 4 are of blue color and one russet, each of the said five cloths bearing the sixth mark in the margin [merchant's mark no. 6 in the left margin] of this present public instrument impressed in wax; and the remaining four cloths in the same 2nd fardle, of the following numbers, colors and lengths: 1 a violet 28¼ yards, 3 a tawny 26, 5 a medley 25 yards, a plunket 22¾ with two pieces of Northern dozens [Note: a cheaper woolen cloth from northern England], a russet 12 yards, 1 russet for wrapping the same; and each of those cloths was marked with the seventh mark in the margin [merchant's mark no. 7 in the left margin] of this present instrument, impressed in lead. And the 3rd fardle of the same contains 35 pieces of Northern dozens and four pieces for wrapping the said 3rd fardle.

[4.]
Item, the aforesaid Ralph Foxley declared by word of mouth, deposed and certified to me, the undersigned public notary, by his oath made upon and over the holy Gospels of God, touching the written text with his body, that he, Ralph, the deponent, in the aforesaid month of August [Aug. 1533], caused to be loaded and taken on board of his own goods in the aforesaid ship called the Christopher two packs of woolen cloths called Northern dozens of various colors, one of the said two packs being marked on the outside on the canvas with the number 5 and with the eighth mark in the margin [merchant's mark no. 8 in the left margin] of this present instrument, containing 36 pieces together with eight pieces of the said dozens for wrapping the same pack; and the other pack thereof, marked on the outside on the canvas with the number 5 and likewise with the aforesaid mark immediately preceding, containing 26 further pieces together with 8 pieces of the said dozens for wrapping the same pack; and each piece of the said dozens was impressed in lead with the pelican [Note: a lead seal bearing a pelican device].

[5.]
Item, the aforesaid William Wilford declared, deposed and certified to me, the said notary, by his oath made upon and over the holy Gospels of God, touching the written text with his right hand, that the same William Wilford in the aforesaid month of August [Aug. 1533] caused to be loaded in the said ship one cloth of puke [Note: a fine woolen cloth of dark color] containing 22 yards, and one remnant of russet containing 7½ yards, by English measure, enclosed in a wrapper of buckram [Note: a stiff coarse linen cloth], and one bargelot [Note: a small barrel or container] made in Spain with certain things enclosed therein, to the value of £4 sterling.

[6.]
Item, the aforesaid Ralph Foxley, swearing as above, declared, deposed and certified to me, the said notary, that it was and is true that Geoffrey Vaughan, his apprentice, had in the said ship at the time of her capture, in cash and other goods and equipment belonging to him, to the value of £4 13s 4d sterling.

[7.]
And furthermore, the aforesaid Thomas Gale, Robert Wilford, Ralph Foxley and William Wilford, swearing as above, declared, deposed and certified to me, the said notary, that it was and is true that they and each of them had caused separate cockets [Note: official customs certificates] to be made in the name of the said Johannes Sewars solely for fear of the Scots and their armed ships.

These acts were done as written and recited above, in the presence then and there of the discreet men John Joyce and Richard Gryg, citizens and merchants of the aforesaid city of London, within the house of me, the notary hereto subscribed, situated in the public street of Lombard Street of the same city, witnesses specially called and requested for the aforesaid matters.

And because I, John Devereux, clerk, citizen of the city of London, public notary by sacred apostolic and imperial authority, was personally present at the aforesaid declarations, depositions and certifications of the aforesaid deponents made by their separate oaths in the form as above, and at all and singular the other matters aforesaid, while, as is stated above, they were transacted and carried out, together with the aforementioned witnesses, and saw and heard all and singular these things so done; therefore this instrument — being otherwise occupied — I caused to be written by another, and signed it with my customary and accustomed sign and name, in faith and testimony of all and singular the aforesaid matters.

[Notary's mark of John Devereux of London]

---""",
    67: """The following goods are in the custody of Kort Meyneken.

Item, 1 small package of saws therein, 9 saws.
Item, 10 heavy tin vessels.
Item, 14 bundles of flax.
Item, 1 basket and some chests; what is therein I do not know.
The Spanish ship with its artillery lies before Hamburg within the boom [Note: a chain or barrier across the harbor] on the Elbe, in good custody.

These goods and packs, as listed above, have been inspected by the honorable Lord Hans Sengesakenn [councillor of Lübeck] and the learned Master Hennyngus [Kulemeyer], secretary of the merchant community [Note: the Hanseatic Kontor] in London, together with other credible persons, who will give testimony thereto where it should be necessary. And for greater authentication, two copies of this document have been made of identical wording and content, subscribed in the hand of the honorable Lord Hans Segestaken himself, one to remain with the honorable council of Lübeck, the other to be sent with the merchant's secretary to London. Given and written at Hamburg, the 2nd of November in the year 1533.

[signed] Hans Senghstake

---""",
    68: """The following goods were found in the Spaniards' chests, which are presently in the custody of Korth Meyken in Hamburg.

From the chests of this ship.

A
7 lengths of English woolen cloth
13 pairs of knotted sleeves
1 blue English cloak
2 shirts

B
1 length of grey English cloth
1 coat with kneeling [Note: possibly knee-length] stitching
1 small package of saws
1 shirt
6 tin saltcellars
2 compasses

C
1 length of pelt cloth
3 lengths of ruddock [Note: a reddish-brown cloth]
2 grey coats
1 old pair of hose
1 beret
1 black old Spanish cap
1 Castilian leather pouch [Note: "kastilipper," likely a type of Spanish leather bag or wallet]
1 tin jug
1 chart [Note: a sea chart]
1 compass
3 carnation-colored items in gold [Note: possibly gold-decorated items]

From Reymar Otten

D
3 grey cloaks
2 palt [Note: worn or patched] coats
1 pair of white woolen breeches

E
2 small lengths of cloth
3 doublets
1 black coat
2 cooks [Note: cooking pots]
1 length of grey Scottish cloth
6 shirts
3 pairs of old hose
1 grey cloak
1 parney [Note: possibly a type of headgear or garment]

2 English chests
½ half cask with its fittings

F
1 black old Spanish cap
3 small lengths of blue cloth
2 small tin jugs
1 Castilian leather pouch
1 pair of old hose
3 old bonnets

G
3 large tin wash-basins
27 tin bowls [Note: "segalen," possibly small dishes or plates]
25 small tin vessels
2 tin jugs
2 brass candlesticks
1 brass mortar
1 red banner
4 pairs of knotted hose
1 length of English cloth
1 new saw doublet [Note: possibly a jacket or doublet made of serge or similar fabric]
4 pairs of new hose
1 white hose-cloth
2 black new caps
2 new palt coats
1 all-wool black English cloth
2 pairs of new shoes

H
2 tin jugs
1 small basket with trinkets [Note: "pluserye," small ornamental items]

J
3 tin spice vessels
26 tin bowls
2 children's berets
3 woolen cloth-wrappers [Note: "wattwellelinde," possibly pieces of cloth used for wrapping]
1 Spanish cap
1 mirror
1 pair of old hose
1 old doublet
1 pair of small children's shoes

K
2 tin jugs
8 tin vessels
8 tin bowls
1 tin salt-vessel
4 shirts

L
3 fine tin spice vessels in o [Note: possibly stored in a specific container, "o" unexplained]

M
1 black Spanish garment
2 pairs of croslets [Note: "krussen," possibly ruffled collar pieces]
1 pair of breeches
2 old shirts

N
1 new black surcoat — is in o [Note: see above]

O
1 black Spanish cap
1 black palt coat
2 grey surcoats
1 length of white cloth
1 length of pelt cloth
1 pair of red hose
1 beret

P
1 small Castilian leather pouch
and other trinkets with more cloth

Q
1 new palt coat
4 packages of cut clothing or tailor's cuttings [Note: "schrotarwick," fabric offcuts or pre-cut garment pieces]

R
1 Spanish cap with 1 white cross
1 black coat-cloth
1 blue coat-cloth
4 pairs of white hose
2 surcoats
1 pale coat
1 compass
2 lengths of plush cloth [Note: "stunda pluse," lengths of plush or velvet fabric]
1 chart
4 bonnets

S
2 lengths of blue cloth
1 brown hose-cloth
1 length of wool-cloth [Note: "woldeck," possibly a woolen covering]
1 Spanish cap
3 pairs of hose
1 grey cloak
3 shirts
3 Castilian leather pouches
6 pairs of shoes
3 coats' backs [Note: "rokens beke," possibly coat-back fabric pieces]

T
1 grey coat-cloth
1 length of black cloth
2 palt coats
3 pieces of toweling [Note: "dwolkes," possibly coarse cloth for drying]
1 blue parney
1 pair of hose

U
[no items listed]

V
4 pairs of lower hose [Note: under-hose or stockings]
1 Castilian leather pouch
2 pairs of ruffs [Note: "krassen," collar ruffs or frilled pieces]
2 mirrors

W
1 length of Damasked [Note: damask-patterned] cloth
1 length of red English cloth
1½ all-wool white English cloth
1 Spanish cap
1 old doublet
40 small tin vessels
1 tin wine-jug
4 Spanish bows

From the dark hose-covered baskets [Note: "duster hosen bereven korffen," baskets wrapped in dark hose-cloth or leather]""",
    69: """On 7 April 1534, in the presence of the undersigned notary (Johannes Kloth alias Platen), Johannes Hulpp, proconsul of Hamburg in the diocese of Bremen, specially deputized by the Hamburg council, there appeared Alphonsus de Sancto Johan, a Spanish merchant residing in London in England, and Joan de Lusis, of the Galician town of Muros, in their capacity as plenipotentiary deputies of Albert de Astudillo, Ferdinand de Verdese, Johannes de Arabiano and Joannes de Bewariis. Also present was magister Johannes Hoper, specially deputized by the Lübeck council, to settle claims in their own names as well as those of their principals and fully recover goods which, in the summer of 1533 off the coast of England, were taken by paid soldiers [Note: milites stipendarii — mercenary soldiers or privateers in Lübeck's pay] of Lübeck who with their warships seized the Spaniards' ship, seized these goods and carried them away to Hamburg, for the restitution of which the Spaniards have come to Hamburg. There, in the presence of Joachim Gherkens, proconsul, and Johannes de Lennepen, the Spaniards were — by the explicit command and assent of the Lübeck council — given satisfaction for the value of: (1) 83 large and small bales of cloth, as itemized (with their merchants' marks) in a certified schedule which was publicly displayed; (2) 48 dickers [Note: a dicker = a unit of ten hides] of hides; (3) 1 small bundle of flax; (4) 10 tin vessels with 20 chests belonging to the shipmaster and the mariners containing goods and clothing; (5) 20 casks or barrels of Lisbon oil; (6) 1 hundredweight of Brouage salt, estimated to be worth 96 marks Lübeck currency. The ship (called in the common German tongue a carvel) Christopher, captained by the said Joan de Lusis, together with certain goods and merchandise belonging to him, was sold by the said procurators Alphonsus de Sancto Joan and Joan de Lusis for 1,230 marks Lübeck currency in Hamburg. The said Joan de Lusis complained that certain articles of clothing, chests and goods belonging to him and his mariners had been taken, for which the Lübeck council compensated him with 100 marks Lübeck currency in cash. The plenipotentiaries Alphonsus de Sancto Joan and Joan de Lusis acknowledge, by oath, receipt of adequate compensation, wherewith all their claims and those of their principals (and their heirs) against Lübeck are deemed to have been satisfied. Witnesses: Jodocus Burhorne, Sebastianus de Winthen, citizens of Hamburg. Notary: Johannes Kloth alias Platen, cleric of the diocese of Bremen. This true copy of the notarial instrument is attested by Michael Petri, cleric of the diocese of Schwerin. — 7 April 1534. Hamburg.""",
    70: """The shipmaster [Note: rector navis] Johannes de Lusis, dwelling in the town of Muros in Galicia, and Alphonsus de Sancto Joan, dwelling in the city of London in England, both Spaniards, acting as the procurators and commissioners of Joan Bewariis, dwelling in the said town of Muros, acknowledge receipt (for themselves and their principals and their heirs) in the Hamburg proceedings [Note: dieta Hamburgensi] from the Lübeck proconsul Joachim Gherkens""",
    71: """and the Lübeck council member Johannes de Lennepen (acting at the behest of the entire council) of compensation for all the goods taken by those of Lübeck in a ship called Christophorus, skippered by the said Joan de Lusis, off the coast of England the previous summer, namely one bale of cloth and 11 chests containing in all 7

Alphonsus de Sancto Joan, a Spaniard residing in London in England, acting as procurator of Albert de Astudilla, Ferdinand de Verdese and Johannes de Arabiano, acknowledges (also in the name of his principals) receipt of the goods taken in the previous year by paid soldiers of Lübeck off the coast of England, having come to Hamburg to receive them from Joachim Gherkens, proconsul, and Johannes de Lennepen, councillor of Lübeck, namely 79 large and small bales of cloth, one bale of flax, 40 dickers of hides, 10 vessels of tin, 9 chests with clothing and other things, and all other goods taken off England. As for the goods taken from ships called hoyes [Note: hoyges — flat-bottomed coastal trading vessels], namely 20 casks of Lisbon oil and 1 hundredweight of Brouage salt, he acknowledges receipt of 96 marks Lübeck currency representing the full value of these goods. He declares all claims to have been satisfied. In testimony whereof he has sealed this quitclaim with his own signet and signed it with his full name. Done in Hamburg, 7 April 1534. Translated from the German and attested by Michael Petri, cleric of the diocese of Schwerin, notary. — 7 April 1534. Hamburg.""",
    72: """In the name of God, amen. Let it be evident to all by this present public instrument that in the year of the Lord's incarnation one thousand five hundred and thirty-three, the sixth indiction, in the tenth year of the pontificate of the most holy father in Christ and our lord Clement, by divine providence Pope of this name the seventh, on the 20th day of the month of September [20 Sept. 1533], within the dwelling house of me, the undersigned public notary, situated in the public street of Lombard Street in the parish of Blessed Mary Wolnoth in the city of London, there appeared in person before me, the said notary, and the witnesses underwritten, the prudent men Thomas Cole, citizen and merchant tailor of the said city, aged, as he stated, 64 years or thereabouts, and Simon Briganden, likewise citizen and merchant tailor of the aforesaid city, aged, as he recalls, about 28 years, men of good repute and unblemished conduct, induced, led, compelled, deceived or circumvented by no force, deceit, fear, fraud or any sinister contrivance, but of their own pure, free, clear and spontaneous wills, for future record and for declaration of the truth of the matters underwritten, as was evident and as they openly and publicly stated and confessed, and as each of them separately stated and confessed, for the defence and preservation of their rights and those of either of them, spoke, deposed and certified to me, the undersigned public notary, by their separate oaths taken in the manner and form following, namely:

[1.]
First, the said Thomas Cole, with deliberate intent, spoke, deposed and certified to me, the undersigned public notary, by his oath sworn upon and over the holy Gospels of God, physically touching the scriptures with his right hand, that it was and is true that he, Thomas Cole, the deponent, in the month of July last past before this present public instrument, in a certain ship then called the Maria de Gatolope, of which Johannes de Calegio was master under God's authority, caused three bales of woollen cloths, containing 30 cloths and 6 pieces of cotton for wrapping them, to be loaded and laded in the port of the city of London from his own proper goods, each cloth and each piece of cotton in the same being marked in lead with his own mark, the first placed in the margin of this instrument [merchant's mark no. 1 in the left margin], at the end of each of them, and on the outside upon the canvas of each of them the second mark placed in the margin of this instrument [merchant's mark no. 2 in the left margin]; and that the length of each of the same appears by a certain schedule written in Thomas's own hand, sewn on top and of the following colours, namely: the first bale contains as follows: a green 26¼ yards, a visset [Note: a type of cloth, possibly "visset" or woad-dyed] 24¾ yards, a visset 24½, a green medley 25, a red 26, 1 red 26, a red 26, a red 26, a red 26, a red 26 with two wrappings, a horseflesh [Note: a grey-brown cloth colour] 22½ good [yards], a russet 26½. The second bale contains: a tawny 24½, a blue 24¼, a blue 24, a musterdevillers [Note: a type of grey cloth] 25, a musterdevillers 25, a russet 25¾, a violet 24¼, 1 violet 24¾, a green medley 24, a visset 25 with two wrappings, a russet 22¼ good, a yellow 22½ good. And the third bale contains: a russet 24½, a plunket [Note: a pale blue cloth] 25¾, a violet 24¾, a blue 24½, a blue 24¾, a green medley 25, a visset 24½, a tawny 24½, a musterdevillers 25¼, a musterdevillers 25¼ with two wrappings, a kennet [Note: a type of coarse cloth] 23 good and a green 22 good. Likewise the said Thomas the deponent by the said oath, as above, spoke, deposed and certified to me, the undersigned public notary, that it was and is true that he, the deponent, caused separate bills of lading [Note: schedulas cognosciamenti — bills of lading or recognition notes] to be written and subscribed concerning the loading of these 3 bales of cloth in the name of Francis Maswelle, a foreigner, solely out of fear of the Scots and their armed ships.

[2.]
Likewise the aforesaid Simon Briganden by the oral testimony of his living voice spoke, deposed and certified to me, the said undersigned public notary, by his oath sworn upon and over the holy Gospels of God, physically touching the scriptures with his right hand, that it was and is true that he, Simon the deponent, in the aforesaid month of July, from his own proper goods, in the aforesaid ship and in the said port of London, caused one pack of woollen cloths to be loaded and laded, marked on the outside with his own mark of Simon, placed in the margin of this instrument [merchant's mark no. 3 in the left margin], numbered 3, also placed upon the same pack, of the following colours and lengths, namely: a visset 25½ yards, 1 medley 26, a blue 24¼, a russet 24, a light green 26¾, a musterdevillers 25½, a medley 25½, a visset 25¼, a blue 24¼, a light green 26, a plunket so called 24¾, a plunket 25½, 3 gings [Note: a type of cloth], 5 russets of the North, 10 yards of fine brown green — caused to be loaded and laded. Likewise the said Simon, swearing as above, spoke, deposed and certified to me, the said undersigned public notary, that it was and is true that he, Simon the deponent, caused separate bills of lading to be written and subscribed concerning the loading of this pack numbered 3 belonging to the deponent in the name of Peter de Berevey, a foreigner, solely out of fear of the Scots and their armed ships.

These acts were performed as written and recited above, in the presence then and there of the discreet men John Banckes and Ralph Foxley, citizens and merchants of the aforesaid city of London, witnesses specially called and requested for the foregoing.

And I, John Devereux, clerk, citizen of the city of London, public notary by apostolic and imperial authority, was personally present at the aforesaid statements, depositions and certifications of the aforesaid deponents and each of them made by their separate oaths in the form as above, as well as at all and singular the other foregoing matters while, as is stated above, they were being conducted and done, together with the witnesses named above, and saw and heard all and singular the same being so done; therefore this instrument — being hindered elsewhere — I caused to be written by another, and signed it with my accustomed and customary sign and name, in faith and testimony of all and singular the foregoing, having been asked and requested.

[Notary's mark of John Devereux]""",
    73: """Johannes Hampton has confirmed and attested by his sworn oath that:

[1.]
He, both for himself and in the name of Johannes Bryngborne, whose factor [Note: commercial agent] the said Johannes is, had a barge upon which Johannes Williamson of Middelburg in Holland was shipmaster, and had freighted it with the following goods bound for Zeeland, namely 32 weys [Note: a unit of weight] of brown salt in English measure and 5,500 castle stones [Note: castrickstened — possibly cobblestones or building stone] and one chest with the equipment and clothing of the said factor, and the goods were worth 40 pounds sterling.

[2.] Humphrey Knight has confirmed by his oath that his factor Thomas Wakeham had shipped in a barge belonging to Flushing, upon which Adrian van Sterree was master, 14 barrels of salt fish, some of which barrels are marked thus [merchant's mark no. 1 follows], and that the Lübeck warships encountered the said barge and took from it 9 barrels of fish, on account of which he, the said Humphrey, suffered a loss of as good as 6 pounds and 6 shillings Flemish groats, together with expenses.

[3.] Thomas Blanke has confirmed by his oath that his factor Gilbert Pervissche had shipped in the aforesaid barge a small bundle in which 48 dozen silk girdles were enclosed, and that the said small pack was worth 14 pounds and 16 shillings Flemish groats, over and above the toll, which amounted to 8 shillings Flemish.

[4.] Thomas Cole has confirmed and attested by his oath that he had shipped in a ship called Maria de Gatalope, upon which Johannes de Calegio was master, 3 packs of woollen cloth. In the same were 30 cloths and 6 pieces of cotton for wrappings, each cloth and piece of cotton marked with the said Thomas's mark pressed in lead at the margin, at the end of each of them, and marked on the outside on the wrapping with the other mark [merchant's marks nos. 2 and 3 in the left margin]; and the length of the said cloths appears by a schedule written in his own hand and sewn over it, of the following colours: thus the first pack contains: a green 26 yards 1 quarter, 1 visset 24 yards 3 quarters, 1 visset 24 yards 2 quarters, 1 dark green 25 yards, 1 red 26 yards, 1 red 26 yards, 1 red 26 yards, 1 red 26 yards, 1 red 26 yards, 1 red 26 yards with 2 wrappings of the so-called horseflesh colour 22 good yards 2 quarters, 1 russet 26 yards 2 quarters. The second pack contains: 1 tawny 24 yards 2 quarters, 1 blue 24 yards 1 quarter, 1 blue 24 yards, 1 musterdevillers 25 yards, 1 musterdevillers 25 yards, 1 russet 25 yards 3 quarters, 1 violet 24 yards 1 quarter, 1 violet 24 yards 3 quarters, 1 dark green 24 yards, 1 visset 25 yards with 2 wrappings, 1 russet 22 good yards 1 quarter, 1 yellow 22 good yards 2 quarters. And the third pack contains: 1 russet 24 yards 2 quarters, 1 light blue 25 yards 3 quarters, 1 violet 24 yards 3 quarters, 1 blue 24 yards 2 quarters, 1 blue 24 yards 3 quarters, 1 dark green 25 yards, 1 visset 24 yards 2 quarters, 1 tawny 24 yards 2 quarters, 1 musterdevillers 25 yards 1 quarter, 1 musterdevillers 25 yards 1 quarter with 2 wrappings, 1 ekemut [Note: a cloth type, possibly "acorn-coloured"] 23 good yards and 1 green 22 good yards. Likewise the said Thomas has attested by the same oath that he caused separate bills of lading to be written in the name of Francis Maswelle, a foreigner, solely out of fear of the Scots and their warships, as a token and acknowledgement of the freighting of the 3 packs.

[5.] Simon Briganden has confirmed and attested by his oath that he had shipped in the said ship Maria de Gatalope from his own proper goods 1 pack of woollen cloth, marked on the outside with his own mark at the margin [merchant's mark no. 4 in the left margin], being numbered third, likewise marked upon the said pack with the following colours and lengths: 1 visset 25 yards 2 quarters, 2 medleys 26 yards, 1 blue 24 yards 1 quarter, 1 russet 24 yards, 1 light green 26 yards 3 quarters, 1 musterdevillers 25 yards 2 quarters, 1 medley 25 yards 2 quarters, 1 visset 25 yards 1 quarter, 1 blue 24 yards 1 quarter, 1 light green 26 yards, 1 plunket so called 24 yards 3 quarters, 1 plunket 25 yards 2 quarters, 3 gings so named, 5 russets made on the north side 10 yards, or fine brown coarse cloth.

[6.] Robert Pagiet, alderman, has confirmed by his sworn oath that he had shipped in a ship called the Christopher de le Moria [Note: Christopher of La Moria, i.e. Muros] in the territory of Galicia, upon which Johannes Shewars was master, 2 packs of flax, both of which said packs are marked with Robert's mark at the margin [merchant's mark no. 5 in the left margin].

[7.] Thomas Gale has confirmed by his oath that he had shipped in the aforesaid ship 1 pack — the fourth in number — containing 16 short cloths and 12 pieces of the so-called statute bloody [Note: statutes blodie — a regulated type of red cloth] colour for wrappings, with another mark [merchant's mark no. 6 in the left margin] marked upon the linen wrapping, of the following colours and lengths: 1 violet 24 yards 3 quarters, 1 visset 24 yards 1 quarter, 1 red 25 yards and 1 quarter, 1 musterdevillers 24 yards 3 quarters, 1 dark green 24 yards 1 quarter, 1 musterdevillers 24 yards 3 quarters, 1 violet 24 yards 1 quarter, 1 visset 24 yards 3 quarters, 1 dark green 24 yards 3 quarters, 1 russet 24½ yards, 1 russet 24 yards 1 quarter, 1 blue 24 yards 3 quarters, 1 blue 25½ yards, 1 blue 24 yards, 1 blue 24½ yards, 1 blue 24 yards. And furthermore the same Thomas Gale has attested by the previous oath that all these 16 pieces of such woollen cloth are as much his own property as the aforesaid 12 pieces of statute cloth of the said colour, with the third mark at the margin [merchant's mark no. 7 in the left margin] pressed in lead and attached to each individual cloth.

[8.] Robert Wilfordt has confirmed by his oath that he had shipped in the much-mentioned ship 3 packs of short woollen cloths with the wrappings of the same cloths, belonging properly and outright to the said Robert and his brothers, each individual pack of the same being marked on the outside upon the wrapping linen with the fourth mark as it stands at the margin [merchant's mark no. 8 in the left margin]; and the first of these pieces contains 16 cloths in number, colour and length as follows: no. 297 blue 24 yards 3 quarters, no. 298 blue 24 yards 2 quarters, no. 293 blue 23 yards 3 quarters, no. 284 blue 24 yards 2 quarters, no. 245 blue 24 yards 2 quarters, no. 259 visset 25 yards 1 quarter, no. 272 visset 25 yards, no. 165 medium 25 yards 2 quarters, no. 173 medium 25 yards, no. 299 red 25 yards 3 quarters, no. 224 russet 25 yards, no. 175 russet 25 yards 1 quarter, no. 34 musterdevillers 25 yards, no. 172 musterdevillers 25 yards, no. 171 musterdevillers 25 yards 2 quarters, no. 277 plunket so called 26 yards. After these 16 cloths, a total length of 400 yards and 1 quarter, with 3 pieces of cotton for the wrappings of the same pack — the first in number contains as follows: 1 green 21 good yards 1 quarter, 1 green 21 good yards 3 quarters, 1 green 20 good yards 3 quarters — each individual piece of such short cloth being marked with the fifth mark at the margin [merchant's mark no. 9 in the left margin] pressed in lead and attached to each individual cloth. The second pack of the said three contains 9 cloths of the following colour, of which 4 are of the so-called bloody colour and 1 russet, each individual cloth of the 5 being marked with the sixth mark at the margin [merchant's mark no. 10 in the left margin] pressed in wax; and the remaining 4 cloths in the same second pack of the following number, colour and length: 1 violet 28 yards 1 quarter, 3 tawnies 26 yards, 5 mediums 25 yards, 5 plunkets 22 yards 3 quarters with 2 pieces made on the north side called dozens [Note: dosseyns — a grade of cloth], 1 russet 12 yards, 1 russet for the wrapping of the same, and each individual cloth of the 4 being marked with the chief mark at the margin [merchant's mark no. 11 in the left margin] pressed in lead. And the 3rd pack contains 35 pieces made on the north side called dozens and 4 pieces for the wrappings of the said 3 packs.

[9.] Ralph Voxley has confirmed by his sworn oath that he had shipped in the aforesaid ship from his own proper goods 2 packs of woollen cloths called Northern dozens [Note: a grade of cloth from northern England], of various colours [Note: man niperley vorwe — of no particular or mixed colours], of which 1 of the said 2 packs is marked on the outside upon the folded linen, being the fifth in number, with the eighth mark at the margin [merchant's mark no. 12 in the left margin], and contains 30 pieces and 6, with 8 pieces of such dozens for the wrappings of the same packs; and from these the packs marked on the outside upon the folded linen are the sixth in number and likewise marked with the aforementioned mark, and contain 36 pieces with 8 pieces of such 12 dozens for the wrappings of the same packs, and to each individual piece of the 12 dozens is attached a pelican pressed in lead.

[10.] William Wilfordt has confirmed by his sworn oath that he had shipped in the much-mentioned ship 1 fine cloth of the colour called puke [Note: a high-quality dark cloth], containing 22 yards, and 1 piece of russet containing 7½ yards in English measure, wrapped in buckram [Note: a stiff coarse linen fabric] so called, and a baize [Note: bargelot — a type of coarse woollen cloth] made in Spain with particular equipment placed within the same baize in the chest so called, which was worth 4 pounds sterling.

[11.] Also the much-mentioned Ralph Foxley has confirmed by his oath that his servant Geoffrey Vaughan had in the same ship at the time it was taken, in counted money together with other things and equipment belonging properly to him, as good as £4 13s 4d sterling.

[12.] Likewise the aforementioned Thomas Gale, Robert Wilfordt, Ralph Foxley and William Wilfordt have attested by their previous oath that they had separate customs certificates [Note: tollen breve — customs or toll documents] written under the name of the said Johannes Sewars solely out of fear of the Scots and their warships, so that their said goods might pass more safely.""",
    74: """I, Johann Hoper, publicly acknowledge by this my own handwriting that the honourable Mr Johann Segestaken and Gosslick Remmynctotes have come to an agreement with the respectable Mathias van Ryne to take the Spanish goods into his house for safekeeping. For this, the honourable council of the city of Lübeck shall and will pay, per quarter year, for each of the large packs of cloth, of which there are 13 in number, 4 shillings Lübeck currency, and for each of the small packs, of which there are 67 in number, likewise for each dicker of hides, of which there are 48 in number, and 1 small pack of flax, 2 shillings Lübeck currency. If furthermore these goods should remain with the aforementioned Mathias van Ryne for more than one quarter year, then the said storage fee shall continue and, after the quarter year, payment shall be made in equal proportion to the foregoing, and the aforementioned Mathias shall keep faithful custody of these 3 goods [Note: i.e. the three categories of goods] on behalf of the honourable council of the city of Lübeck and deliver them to no one else without the special order of the honourable city of Lübeck, without any deception. In witness and testimony thereof, 2 identical copies of this document of the same tenor and content have been prepared and cut apart [Note: indenture — the document was physically cut in a jagged line to create matching halves as proof of authenticity], one to be kept by Johann Hoper and the other by Mathias van Ryne. Given and written at Hamburg, 2 November 1533.""",
    75: """I, Johann Hoper, hereby publicly acknowledge by this my own handwriting that, acting under orders from the honourable council of the imperial city of Lübeck, my lords, I have inspected and found in the keeping of the honourable Mathias van Ryne, citizen of Hamburg, through the honourable Hans Sengestaken and Goslick Rennerelickrath [Note: also rendered Reminckrode] and the privateers of the Lübeck warships, certain Spanish goods, which are to be held in the custody of the aforesaid Mathias van Ryne for the benefit of the patron until a convenient time for sailing.

Large packs:
[merchant's mark no. 1]  1 pack of cloth, No. 2
[merchant's mark no. 2]  1 pack of cloth, No. 1
[merchant's mark no. 3]  3 packs, Nos. 5, 6, 7
[merchant's mark no. 4]  2 packs, Nos. 12, 13
[merchant's mark no. 5]  No. 13: 1 pack
[merchant's mark no. 6]  [No.] 13: 1 pack
[merchant's mark no. 7]  1 pack, No. 1
[merchant's mark no. 8]  2 packs of cloth, Nos. 3, 4
Item, also 1 pack of cloth whose mark cannot be identified.

Small packs:
[merchant's mark no. 9]   19 small packs of cloth, Nos. 88, 74, 73, 91, 90, 81, 151, 100, 76, 78, 86, 87, 89, 84, 83, 79, 82, 92, 77
[merchant's mark no. 10]  10 small packs, Nos. 96, 95, 99, 98, 104, 97, 94, 103, 101, 102
[merchant's mark no. 11]  4 small packs, Nos. 21, 23, 24, 22
[merchant's mark no. 12]  4 small packs, Nos. 1, 2, 3, 4
[merchant's mark no. 13]  18 small packs, Nos. 1, 2, 3, 5, 4, 6, 7, 8, 9, 10, 11, 47, 51, 52, 49, 46, 48, 50
[merchant's mark no. 14]  12 small packs, Nos. 22, 27, 26, 25, 24, 29, 33, 28, 30, 32, 33, 31

[merchant's mark no. 15 follows]  Under this mark: 48 deckers [Note: a decker = 10 hides] of salted ox hides.

Total packs, small and large: 80.

---""",
    76: """I, Johan Hoper, hereby acknowledge before all persons that, acting under orders from the honourable council of the imperial city of Lübeck, my lords, I have inspected and found in the keeping of the honourable Kort Meyneken, citizen of Hamburg, placed in faithful custody through the honourable Hans Segestaken, councillor, and the privateers of the Lübeck warships, certain similar goods, which are to be held in the custody of the aforesaid Kort Meyneken for the benefit of the parties until a convenient time for sailing.

[1.] Under this mark:
[merchant's mark no. 1]
1 pack of cloth, No. 1
1 pack of cloth, No. 2
1 pack of cloth, No. 3
1 pack of cloth, No. 5
1 pack of cloth, No. 6

[2.] Under this mark:
[merchant's mark no. 2]
1 pack of cloth, No. 1
1 pack of cloth, No. 2
1 pack of cloth, No. 3

[3.] Under this mark:
[merchant's mark no. 3]
1 pack of cloth, No. 3

[4.] Under this mark:
[merchant's mark no. 4]
2 packs of flax
1 piece of fine black broadcloth [Note: "puck laken" — a type of fine woollen cloth]
2 large Russian or Flemish cloths, sealed [Note: "rusken edder wesker vor pitzert" — the precise distinction is uncertain]

One pack of cloth No. 4 bearing the mark of the first entry was received back on the Elbe before Hamburg by Nicolaus Raschew, servant of Thomas Galen, and taken by him to England. And 1 piece of russet [Note: a coarse reddish-brown cloth] of 7½ yards English measure he sold to Johann van Horen, a [court] scrivener [Note: "menserscriver"], for 3 gold crowns.

The aforesaid goods and packs, as written above, have been jointly inspected by the honourable Hans Segestaken and the learned Master Hennyng [Kulemeyer], secretary of the merchant community in London, who will furnish witness thereof wherever it shall be needful. In further testimony hereof, two copies of this document have been made, of identical wording and content, written out one from the other and subscribed with both our names and our own handwriting; one sent to the honourable council in Lübeck, the other to the secretary of the merchant community in London. Given and written at Hamburg, 2 November 1533.

[Signed] Wyllem Aysche, Englishman [merchant's mark no. 5 follows below]
[Signed] Johan Hoper, wrote this

---""",
    77: """[Unsealed.]

[1.]
Item: received from Gotschalk Remelckraden, from what was in the Spanish ship, 5 packs of cloth as follows [merchant's mark no. 1 in the left margin], also 2 packs of flax as follows [merchant's mark no. 2 in the left margin].

Paid: for unloading this cargo from the hold of the ship and bringing it to the crane: 5 marks.

[2.] Also received: 3 packs of cloth as follows [merchant's mark no. 3 in the left margin]; also 1 pack of cloth as follows [merchant's mark no. 4 in the left margin]; also 1 chest, 1 basket, 10 large tin vessels, 1 piece of black English cloth.

Paid: crane fee — 11½ shillings
Carting in and out of the warehouse — 2 marks 4 shillings
Warehouse rent — 2 marks 8 shillings
Paid: for opening and closing the cloth [bales] — 1 mark 7½ shillings
Paid: for 1 rope — 5 shillings
Paid: for bringing the flax into the yard — 8 shillings
Yard rent — 8 shillings
For bringing [it] from the yard — 4 shillings
Paid: for opening, closing and drying the flax — 11 shillings
For carting the cloth and the flax to the ship — 13 shillings
[Dorse:] Toll at the town hall — 6 marks 2 shillings
The heart [harbour?] toll [Note: "des haerttÿgen thollen" — possibly a specific Hamburg toll] — 12 shillings
My [own] money — 3 marks
Total in all: 24 marks 14 shillings

Throughout, all reckoning kept to good account; all that is reckoned, no payment [yet] received [Note: "keyne betalynge gade befalen" — goods commended to God, i.e., not yet paid]. Written at Hamburg, 2 June 1534.

[Signed] Kordt Meÿneke

[Recto side, 2nd column:]

[3.] Delivered to Herr Joachim Gerken and Master Johan Hoper here in my house: 1 chest, 1 basket, 10 vessels — shipped in [the vessel of] Hinrick Moller by order of Herr Gerdt Oldenborch and Herr Johan van Lennepen and Johan van Horen — these same 9 packs of cloth.

[4.] Delivered to Herr Hinrick Rademaker [councillor of Hamburg] in my house: 1 piece of black English cloth [see no. 78].

---""",
    78: """[Paper. Unsealed.]

[Note: The content of this document as preserved consists only of the title description. On 9 June 1534, in Hamburg, the procurator or attorney William Ayshe, an Englishman, and Gerde Oldenbarch and Johan van Lennep, councillors and authorised representatives of the Lübeck council, appeared before representatives of the Hamburg council, namely Jochim Wullewevere and Hinrick Rademaker, to arrange the return of the seized goods.]

---""",
    79: """In the name of God, amen. By this present public instrument let it be clearly apparent to all that in the year of the Lord from the Incarnation one thousand five hundred and thirty-three, in the sixth indiction [Note: "indictio" — a fifteen-year cycle used to date documents], in the pontificate of the most holy father in Christ and our lord, the lord Clement, by divine providence Pope of that name the seventh, in the tenth year of his pontificate, namely on the 18th day of the month of September [18 Sept. 1533], within the house of residence of me, the undersigned public notary, situated on the public street of Lombard Street in the parish of the Blessed Mary Wolnoth in the city of London, there appeared in person before me, the said notary, and the witnesses underwritten, the discreet man John Hampton of Faversham in the county of Kent in the parts of the kingdom of England, merchant, aged sixty years or thereabouts, both in his own name and in the name and on behalf of the prudent man John Bryngborne, also of the same town, merchant, who is, as he asserted, his partner in mercantile affairs; not induced, led astray, compelled, deceived or circumvented by force, fraud, fear, deceit or any sinister contrivance, as was clearly apparent, but of his own free, pure and spontaneous will, for the preservation and defence of the rights of the said John Hampton and John Bryngborne, he stated, deposed and certified to me, the undersigned public notary, by his oath made upon and over the holy Gospels of God, touched by him bodily with his right hand, that it was and is true that a certain shallop [Note: "scuta" — a flat-bottomed vessel] of which John Williamson of Middelburg in Zeeland was owner and master under God's authority, while sailing towards the said town of Faversham and laden by their factor in the aforesaid Zeeland with the following goods — namely thirty-two weys [Note: a unit of dry measure] of brown salt of English measure, five and a half thousand paving tiles, and one chest with the equipment and clothing of their said factor — belonging and pertaining in full right to the said John Hampton and John Bryngborne, was recently seized while near the shores of Camber [Note: Camber, co. Surrey] in the said kingdom of England by certain armed ships of Lübeck; and that all the aforesaid goods at the time of the seizure of the said shallop, up to the full loading of the said shallop, were the proper goods of the said John Hampton and John Bryngborne, and that they were then of the value of forty pounds sterling.

These acts were performed as written above and as recited, in the presence then and there of the discreet men John God and Richard Braunche, citizens and merchants of the said city, witnesses specially called and requested for the aforesaid matters.

And because I, John Devereux, clerk, citizen of the city of London, public notary by apostolic and imperial authority, was personally present together with the aforesaid witnesses at the aforesaid statements, depositions and certifications of the aforesaid deponent made by his oath in the form described above, as well as at all and each of the other aforesaid matters, while, as stated above, they were being transacted and done, and I saw and heard them done in such a manner, I therefore caused this instrument — being detained elsewhere — to be written by another, and signed it with my accustomed and usual sign and name, as requested, in attestation of all the aforesaid matters.

[Notary's mark of John Devereux of London]

---""",
    80: """In the name of God, amen. By this present public instrument let it be clearly apparent to all that in the year of the Lord from the Incarnation one thousand five hundred and thirty-three, in the sixth indiction, in the pontificate of the most holy father in Christ and our lord, the lord Clement, by divine providence Pope the seventh, in the tenth year of his pontificate, namely on the twentieth day of the month of September [20 Sept. 1533], within the house of residence of me, the undersigned public notary, situated on the public street of Lombard Street in the parish of the Blessed Mary Wolnoth in the city of London, there appeared in person before me, the said notary, and the witnesses underwritten, the prudent men Humphrey Knyght, citizen and fishmonger of the said city, aged, as he stated, fifty-seven years or thereabouts, and Thomas Blancke, citizen and haberdasher of the aforesaid city, aged, as he recalled, forty-seven years or thereabouts, men of good repute and unblemished conduct, not induced, led astray, compelled, deceived or circumvented by force, fraud, fear, deceit or any sinister contrivance, as was clearly apparent, but of their own free, pure and spontaneous wills, for future record and for the declaration of the truth of the matters underwritten, and for the preservation and defence of the rights of the said Humphrey Knyght and Thomas Blancke and either of them, they stated, deposed and certified to me, the undersigned public notary, by their separate oaths made upon and over the holy Gospels of God, in the manner and form following, that is to say:

[1.]
First, the aforesaid Humphrey Knyght by his living voice stated, deposed and certified to me, the undersigned public notary, by his oath made upon and over the holy Gospels of God, touched by him bodily with his right hand, that it was and is true that a certain Thomas Wakeham, apprentice of the said Humphrey, as he asserted, caused to be loaded and laded in a certain shallop of Flushing, of which Adrian van Sterre was sailor or skipper, in foreign parts, the number of fourteen barrels of salt fish, of which every such barrel was marked with such a mark [merchant's mark no. 1 follows] belonging to the said Humphrey, as the proper goods of the said Humphrey; and that the said shallop, while pursuing its voyage towards the port of the said city, was met by certain armed ships of Lübeck, and they took out of the said shallop nine barrels from those fourteen barrels of salt fish belonging to the aforesaid Humphrey and carried them away, to the damage of the said Humphrey amounting to the sum of six pounds and six shillings in Flemish groat currency [Note: moneta grossorum Flandrie — Flemish groats, a unit of account], together with the expenses of those nine barrels so seized as above.

[2.]
Item, the aforesaid Thomas Blancke, with deliberate intent, stated, deposed and certified to me, the undersigned public notary, by his oath made upon and over the holy Gospels of God, touched by him bodily with his right hand, that it was and is true that a certain Gilbert Pervisshe, apprentice of the said Thomas, as is said, loaded and laded a small truss [Note: "trusse" — a bale or bundle] in the aforesaid shallop of the said Adrian van Sterre of Flushing, in which was enclosed forty-eight dozen diaper silk ribbons [Note: "diaper silk ryband" — woven silk ribbons with a diaper pattern]; and that the said truss of diaper ribbons was seized from the said shallop by the aforesaid certain armed ships of Lübeck and carried away, to the damage of the said deponent.

[3.] And further the same Thomas, deposing under oath as above, stated, deposed and certified to me the said notary that the said truss was worth at the time of its loading in the said shallop fourteen pounds and sixteen shillings in Flemish groat currency, besides [Note: "aultra" — above and beyond] the customs of the said deponent amounting to the sum of eight shillings of the same Flemish groats.

These acts were performed as written above and as recited, in the presence then and there of the venerable man Walter Champion, citizen and alderman of the aforesaid city, and the discreet man William Sawndirson, citizen and fishmonger of the same city, witnesses specially called and requested for the aforesaid matters.

And because I, John Devereux, clerk, citizen of the city of London, public notary by apostolic and imperial authority, was personally present together with the aforesaid witnesses at the aforesaid statements, depositions and certifications made by their separate oaths in the form described, as well as at all and each of the other aforesaid matters, while, as stated above, they were being transacted and done, and I saw and heard them done in such a manner, I therefore composed this instrument written by my own hand, and signed it with my accustomed and usual sign and name in attestation and testimony of all and each of the aforesaid matters, as requested and required.

[Notary's mark of John Devereux of London]

---""",
    81: """In the year 1534, in the seventh indiction, on the 23rd day of the month of June [23 June 1534], in the presence of me, the public notary undersigned, and the witnesses specially summoned and requested thereunto, there appeared in person the honourable man Wilhelm Gilbancke, of the city of Colchester in England, and at that time, as he stated, servant of the honourable and learned lord Thomas Artey [Note: Thomas Audley], Chancellor to the royal majesty of England; and he declared, acknowledged and stated in the best manner, way, form and fashion that he by law best should, could and might, of his own free will and considered mind, that the 2½ hundredweight [Note: "C" = centner] of salt that had been taken from him by the Lübeck privateers [Note: "Lupeschen uthligger"] against the Hollanders in the previous year, from a ship of Zierikzee [Note: "Sircksee"], had been graciously and generously restored to him by the honourable council of the city of Lübeck, and that he had received it back with all gratitude and full satisfaction.

Whereas the aforesaid Wilhelm Gilbancke still lacked and was missing the following items — namely: 12 pieces of half-says [Note: "halve sagen" — a lighter variety of woollen cloth known as "says"], 12 tuns of salted cod [Note: "soltes kabbelauwen" — salted codfish], 2 quarter-barrels of sturgeon [Note: "verondell stors"], 60 ells of canvas [Note: "kannefust" — a coarse canvas fabric], 12 ells of Holland linen cloth [Note: "Hollandesch louwent"], 2 feather-beds in a basket, half a hundred Icelandic fish [Note: "Ylandesche vische" — dried Icelandic fish, probably stockfish], 3 hogsuckers [Note: "hodesuckers" — the meaning is uncertain; possibly a type of dried fish], 3 further long fish called "langen" [Note: "lange" — long fish, likely ling], and 6 mirrors — all of which had likewise been taken and seized by the aforesaid Lübeck privateers; nevertheless, the honourable council of the city of Lübeck, out of special reverence, grace and favour toward his royal majesty of England and to the pleasure of the aforementioned lord Thomas Artey, had to the same Wilhelm Gilbancke, in recompense for the goods written above, and also for all damage, cost, expenditure and loss that he had thereby incurred, well and contentedly paid and settled once and for all the sum of one hundred and twenty-five Lübeck marks, which he had also received with all gratitude in full and in counted coin from lord Thyle Thegetmeyger, councillor at Lübeck, appointed thereto by the whole honourable council of Lübeck, and retained in his full possession. Wherefore the aforesaid Wilhelm Gilbancke, in the presence of me the public notary and the witnesses specially summoned and requested thereunto, did for himself and all his heirs born and unborn, with regard to the aforesaid 2½ hundredweight of salt and the other goods named above, as well as costs, damage, expenditure, interest, profit and loss, fully and completely once and for all release, discharge, acquit and quit the aforementioned honourable council and the whole city of Lübeck, and also all their citizens and inhabitants, and all those who have or in time to come may have any dealings therein, from any and all claim and demand; and he renounced all spiritual and secular legal remedies and all recourse, in whatsoever form the same might be availed of, so that the honourable council and each and every citizen and inhabitant of Lübeck, and those whom this may concern, shall by virtue of such payment made remain once and for all and for ever quit, free, discharged and released from him and his heirs. Furthermore the same Wilhelm Gilbancke, before me the notary and touching with his hand the Holy Scripture, did knowingly swear a standing oath [Note: "stavedes edes" — an oath taken standing with raised arm and outstretched fingers] to God the Almighty, to His saints and to the Holy Gospel, with raised arm and outstretched fingers, that neither he nor his heirs shall at any time speak against or seek to contest this, under the penalty of the offence of perjury incurred by the very act of swearing, etc., as a further public instrument to be drawn up concerning the same shall more fully set forth — all without deceit or bad faith. Whereon, etc.

Done at Lübeck, in the lower town hall there, in the presence and company of the learned and distinguished Ciriacus Wolmerstorp, cleric of the diocese of Lübeck and public notary, and also the noble and honourable Junkers Jheronimus van Bromse and Jurgen van Ehelenleys of the diocese of Münster, as witnesses specially summoned and requested thereto jointly and severally.

[Latin attestation clause:] This is as stated above. Michael Petri, cleric of the diocese of Schwerin, public notary by apostolic and imperial authority, having been requested for the aforesaid matters, wrote this with his own hand.

---""",
    82: """[Headed:] In declaration of the certificates and instruments [pertaining to] the chests [and] the English goods.

[1.]
In the ship of skipper Williamson of Middelburg:
32 weys of brown salt of English measure
5½ thousand paving stones [Note: "astrickes steynen" — paving or cobble stones]
1 chest with his equipment and clothing, to the value of £40 sterling

[2.]
In the ship of skipper Adrian van Sterre: salted fish to the value of £8 and 6 shillings Flemish groats

1 small package, containing 48 silk ribbons [Note: "syden girdelen" — silk girdles or ribbons] to the value of £14 and 16 shillings Flemish groats

and the customs thereon: 8 shillings Flemish payment [Note: "peymentes" — a Flemish unit of account]

[3.]
In the Maria van Gatalope [Note: the source title notes this is an error for Christopher de Moria], of which Johann van Calessio was skipper: a chest of money, household goods and other things to the value of £4 13 shillings and 4 pence sterling.

[4.]
In whatever other Cologne [Note: "collesken" — possibly meaning goods of Cologne origin or another Low Countries provenance; interpretation uncertain] end of goods from the similar foreign goods taken up in ships and the one that was sunk — it is not yet known what will become of their share in those goods.

These matters, together with others, are to be kept carefully in mind in order to avoid further damage — it is strongly advised, which I give to understand in good faith.

[Signed] Johann Hoper""",
}


def main():
    # Update documents.json
    with open("documents.json", "r") as f:
        documents = json.load(f)

    for doc in documents:
        did = doc["id"]
        if did in translations:
            doc["modern_english_translation"] = translations[did]

    with open("documents.json", "w") as f:
        json.dump(documents, f, indent=2, ensure_ascii=False)
    print(f"Updated documents.json with {len(translations)} translations")

    # Update .md files
    updated = 0
    for doc in documents:
        did = doc["id"]
        if did not in translations:
            continue

        md_path = CATALOGUED / f"doc_{did}.md"
        if not md_path.exists():
            print(f"  WARNING: {md_path} not found")
            continue

        content = md_path.read_text()

        if "## Modern English Translation" in content:
            print(f"  {md_path} already has translation section, skipping")
            continue

        # Insert before ## Editorial Notes
        if "## Editorial Notes" in content:
            content = content.replace(
                "## Editorial Notes",
                f"## Modern English Translation\n\n{translations[did]}\n\n## Editorial Notes"
            )
        else:
            # Append at end
            content = content.rstrip() + f"\n\n## Modern English Translation\n\n{translations[did]}\n"

        md_path.write_text(content)
        updated += 1

    print(f"Updated {updated} .md files")


if __name__ == "__main__":
    main()
