"""Merge translations into letters.json and update .md files."""

import json
from pathlib import Path

CATALOGUED = Path("catalogued")

translations = {
    1: "marked with my mark, with a red stone.",
    2: """Written in Antwerp, the 21st of July 1533.

Cousin Ellen, with all my heart I commend myself to you, glad to hear of your good health, etc. You shall receive at the house of Peter Cole two little barrels of sturgeon, marked as below. The larger one (which is number 1) is for you and for good friends, and contains 10 pieces of sturgeon, of which 2 are half jowls. I would have Rowlond Schakerley receive one half jowl; my daughter Wilson must not be forgotten — she should have one round; Master Lock, one round. And if you think it best, Master Botry one round and Thomas Abraham the elder one round. As for the other little barrel (which is number 2), it is for my lord of Rutlond, and I would have it conveyed to him at Enffyld as soon as possible. Therefore I would ask that Thomas Wilson enquire after some of my said lord's servants at Holywelle — he shall not fail to find some of them — and that he see it safely conveyed to Enffyld in the best manner, for I suppose my lord is residing there. When God brings it to hand, I would have no time lost in the delivery of it, even if Thomas Wilson should take the greater trouble in my name to see it delivered.

Merten Albryght has arrived, by whom I have received one cask of ale and 4 venison pasties. I perceive that Roger Manyngton gave me the whole buck, for which I thank him heartily, finding myself much in his debt. I pray you remember him or Mistress Manyngton with a round of sturgeon until I may recompense him better.

And from Mistress Looke I have received 2 venison pasties. And so I remain in good health, at God's pleasure. How fare you?

Your William Gresham

Also, I marvel that Thomas Wilson did not send me the letter he delivered to Antony Vyvaldes's clerk to copy — which letter I have since received by way of my brother John Gresham, who came to this town the Monday after their departure from London, together with Master Locke and others, etc.

I trust you have received the sturgeon I sent you first, and that one barrel has been delivered to Master Cromwelle as I did write.

The 23rd day of this present month [23 July 1533].

And whereas it was written above that you should receive the 2 little barrels of sturgeon at Peter Cole's, this is only to advise you that you shall now receive them at Awdryan Johnson's, and order the matter as was said before. And so I commend myself to you, etc.""",
    3: """The 22nd day of July, 1533

Right worshipful sir, in the humblest manner that I can, I commend myself to your mastership, trusting in the Lord that your mastership is in good health, and likewise my mistress. This day I have received from your mastership two letters, dated the 8th day and the 17th day of July.

As for what your mastership writes concerning Charles Benche — it is the greatest pity I have heard since I came into this land, but against the ill chances of the world, happy is he who can withstand them. It is a great example to all men, but it is a great pity that it was proved upon him, for there was never a more faithful man living. Great pity it is, but I pray Jesus (who sends all things) to forgive him his misdeeds and have mercy on his soul and all Christian souls, amen.

This day I have bought from John van den Gyr: ginger, 2 bags at 20d; nutmegs, 2 bags Venice at 3s 6d; cloves, 1 bag at 5s 8d and 1 at 5s 7d; large mace, 1 bag at 9s 6d. The ginger has risen this day 2d in the pound, pepper a half-penny in the pound, and is like to rise more. Therefore, if your mastership has stock, make much of it, or else buy some, for it is likely to rise. Quicksilver 12d, vermilion at 16d. I am half agreed with a man to buy 10 or 20 bags of new rice. If I can have them for 10 shillings, payable at the Cold Mart [Note: a major seasonal trade fair], I will take 10 bags, for I think they will be no cheaper than they are now — they are selling for 9s 6d at this hour.

Your mastership writes to buy a bag of middle crocus [Note: likely saffron of a middling grade]. It is here at a great price, and they will not sell it now for less — they sell the large crocus alongside the other. Therefore it would be more profitable, if possible, to defer the purchase.

Your mastership shall receive, by the grace of God, through Awdryan Janson, according to what I have written in several letters: 5 butts of currants and two of pepper, and also 1 small truss resembling a truss of Wieringen [Note: possibly referring to a style of packing from Wieringen], bearing your mark, containing 36 lb. of cinnamon which cost 6s 6d. Therefore you had need to sell it for better than 4s 8d. As your mastership wishes, it is sold — make much of it. The large is at 7s 6d and will be dear. I have 200 kerseys [Note: a type of coarse woollen cloth], but if they were 200 at this hour, they would not be received, for there is great war where they should go, and therefore kerseys are at a great loss and are not likely to sell well for the next three marts. And the reason for this is causing spices to rise, as I shall inform your mastership more fully by the next letter that I will send. And then, God willing, I will come home with the first vessel or ship, or else by land.

I pressed Steven for the money that you have paid for him, along with various other matters on your mastership's behalf. He says that Harry Myles must pay for half of them, for he received the greater part of the goods without payment. I could get no more goods out of him. The truth is, as far as I can see, he has no goods and no great store of money. Therefore to recover anything by any means would be a great hindrance to him being here — but as I have reasoned with him, between him and me, it is not possible that he can ever prosper or go forward in deceiving you in this manner, as he has done so many times and will never stop. I told him that I could take it no other way but that he does this to shorten your life, or else he would ever do as he does so often. And with that he wept, along with various other things which would take too long to write at this time.

And thus the Lord be with your mastership and my mistress, your brother, and all the rest of your good friends.

I beg your mastership to be patient with my writing, though it is not so well as I would wish, and to be content with Steven and never trouble yourself over him, for I doubt not he will do well. There is no other likely outcome for all this. He is young and has learned as much as is possible. I think in my mind that he has grieved your mastership more at the heart than all the goods that your mastership has ever lost. But let all this pass — he will begin a new life, and by the grace of God he will do well in a short while.""",
    4: """Most heartily I commend myself to you and to all good neighbours, trusting that you are in good health, along with all my children and household and all others as I would have rehearsed them by name one by one. So you shall understand that I have received your letter that Robert Paris wrote to me by Master Kemp, and touching who shall have freight as soon as God sends it home here — as for a barrel for it, there is as scarce here as there is in London yet, but I trust we shall have better ships shortly.

Also the cause of my writing to you is that you shall receive from a hoy of Antwerp a vessel of fresh sturgeon marked with my mark. The master's name under God is Adriane Jonson. Pay him for the freight of it 6d, and send it to my lord. It is not so large as I have seen, but it is very good. And while I have seen 20 since I came here, there was never one to my mind before now. For either they proved red in the seething, or else they crumbled and mouldered away, so that I had no fancy to them.

Also I pray you have me recommended to Master Lark and Master Steward and Master Comptroller. Also I pray you look well to your folks and see that they stand not idly in any wise. And gather in your debts, for I must pay much money when I come home. I trust so, and the freight I look for. Also let your folks make me no debtors, but that they may gather up on Saturday at night in any wise. I pray you let the Goodman Stone see your bill, and the next. I trust we shall write — we shall have summer freight and the wind will come about. No more to you at this time, but Jesus keep you. Written at Antwerp the 17th day of July.

Also you shall receive 2 copper buckets of tin.""",
    5: """Right well beloved wife, I heartily commend me unto you, trusting in Jesus that you are in good health, along with all my household — thanks be to God. Also, you shall receive, by the grace of God, in the care of Richard Rede of Mylton Shore, a dry cask, a truss, a barrel of sheep bells, all under this mark.

Item: 6 painted cloths
Item: 27 dozen pounds of inkle at [Note: price written in merchant's code]
Item: furthermore, a sack of inkle under the same mark
Item: 3 dozen pounds of Ounce thread at [Note: price written in merchant's code]
Item: 1 dozen pounds of Ounce thread at [Note: price written in merchant's code]
Item: 4 pounds of Ounce thread at [Note: price written in merchant's code]
Item: 1½ dozen gold checks at [Note: price written in merchant's code]
Item: 3 bags of aglets weighing 202 pounds at [Note: price written in merchant's code]
Item: 3 gross hawk ends at [Note: price written in merchant's code]
Item: 9 pounds of inkle at [Note: price written in merchant's code]
Item: 4½ dozen, 1 broad says at [Note: price written in merchant's code]
Item: 5 dozen, 1 broad says at [Note: price written in merchant's code]
Item: 18 dozen new says at [Note: price written in merchant's code]
Item: ½ dozen says at [Note: price written in merchant's code]
Item: 3 gross razors at [Note: price written in merchant's code]
Item: 1 gross bosses at [Note: price written in merchant's code]
Item: 12,000 pack needles at [Note: price written in merchant's code]
Item: 7 dozen fine checks with gold at [Note: price written in merchant's code] per dozen
Item: 3½ dozen middle says at [Note: price written in merchant's code]
Item: 6 dozen bay silk at [Note: price written in merchant's code]
Item: 5 boxes of minikin pins at [Note: price written in merchant's code]
Item: 1 gross brass bells at [Note: price written in merchant's code]
Item: ½ gross brass bells at [Note: price written in merchant's code]
Item: 7 dozen leather at [Note: price written in merchant's code]
Furthermore, in the same ship, a sack of inkle weighing 500 pounds at [Note: price written in merchant's code]
Furthermore, in the same ship, a truss with 13 dozen leather at [Note: price written in merchant's code]
Item: 8½ dozen painted cloths at [Note: price written in merchant's code]
Item: furthermore, 100 reams of paper at [Note: price written in merchant's code]
Item: 50 reams of brown paper, double, at [Note: price written in merchant's code]
The freight of all is [Note: price written in merchant's code]
Item: a barrel of sheep bells, containing 4,200, at [Note: price written in merchant's code]

By the grace of Jesus, furthermore, in the care of Petter Colle of Andwarpe:
Item: 2 barrels of sturgeon containing 16 rounds and 6 gills at [Note: price written in merchant's code]
Under this mark, freight [Note: price written in merchant's code]""",
    6: """Right worshipful sir, in the most humble manner I heartily commend myself to you, trusting in God that you are in good health. Sir, you shall receive now, by the grace of God, by the bearer of this letter, whose name is Audryan Johnson of Andwarpe, under this mark: one barrel of large maces containing 42½ lb., and one hundredweight barrel of succade, two small barrels of orange flowers containing in all 186 lb., priced at 5d per lb.

Item: a truss containing my wearing gown.
And he is to receive for his freight 2s.
The inward goods are marked with this mark.

No more to you at this time, but may our Lord keep you in his care.""",
    7: """In Antwerp, the 21st day of July, 1533.

Right worshipful and well-beloved brother, my duty remembered. I heartily commend myself to you, trusting in God that you are in good health, which I pray God long may continue to His pleasure and according to your heart's most earnest desire.

I am writing to let you know that I have sent you a letter and a dozen lute strings, which I trust you have received by this time, and I am very eager to know whether they are good or bad. If they are of no use, I know where there is some making that is finer and likely better than those I sent you. Therefore, if you will have any more, send me money enough and you shall have strings enough.

Also, the letter which I sent you was written so hastily that I think you could scarcely read it. However, the time was so short I could write it no better.

I also ask you to give my regards to my father and my mother, and ask her for her blessing, and to all my brothers and sisters and all my other friends. I would have written to my mother at this time but to ask for her blessing — I trust it shall not be needed. Therefore, as soon as I can, I will write her a letter so that she shall know how I am spending my time. By the grace of Jesus, who ever preserve you and keep you and all other good friends, amen. Written in haste by the hand of your loving brother.""",
    8: """Friendly greetings as aforementioned. Liuken van Brussel, my dear landlady [Note: "werdinne" means a female host or landlady, possibly a business associate with whom lodging or goods were arranged]. I, Jan van Espen, have learned of the matter in which you instructed me, namely concerning the goods of Peter Nene that are said to be lying at Sint Joos ten Hoede [Note: a location, likely a storage or lodging house]. And you wished to come here to Brussel to deal with that same matter. You would be well able to get hold of those goods. And I hope to come and visit you shortly. And Wouter in de Nobele sends you his warmest greetings. And I commend myself warmly to Machielen and to all my good friends. Herewith remain commended to God. Written at Brussel in haste on the 26th day of May in the year 1533.

He who is your most obedient servant,

Jan van Espen""",
    9: """At Andwarpe, the 12th day of July, in the year 1533.

Sir, may it please you to know that, by God's grace, you shall receive through Audryan Johnson a dry crate containing the following:

24 dozen fygugurs H3H [Note: price in merchant's code] at 24s the dozen
25 dozen de doble larg + [Note: price in merchant's code] at 18s 6d
20 dozen de large Ø H3H [Note: price in merchant's code] at 9s
20 dozen de oultre fyn + [Note: price in merchant's code] at 11s
15 dozen de large bygare at 7s
10 dozen de fin bygare at 6s
10 dozen fyn 1d bredes fina at 9s 3d
8 dozen 1d bredes fin at 7s 10d
5 dozen de fygure Ø H3H [Note: price in merchant's code] at 18s
For the crate and nails: 2s
The which crate comes to £89 0s 8d

And as for the double large and the outer large: Colin did send his brother a letter about it, and his brother sent word back to him that he should not sell the double large under 19s, and the outer large under 11s 6d, because the yarn cost 6d more than it did before. And Colin says that for those 2 parcels he cannot reduce anything further — what he can reduce, he has already reduced for you. Furthermore, you should know that Colin is gravely ill and has been so for these 5 days, and he does not come out of his bed. And he and I have not yet settled our accounts. And as for Andryas Sallman, he says that he has a writ from the Emperor that no man shall receive money from him for these three years. Furthermore, you should know that there is shipping in Clas Frys of 175 bundles of paper, which cost £2 16s 8d per 100 sheets, and now one cannot buy any for £3. No more to you at this time, but may Jesus have you in His keeping.""",
    10: """Marten, I commend myself most warmly to you and wish to let you know that I have sent a messenger to Longuen. He went as far as Grevelingen, but reported that one could not pass through on account of the siege. And so I have had no choice but to be patient. Since then I have made further enquiries and have come to understand that one can in fact pass through there without having to declare anything to anyone.

Marten, I kindly ask you to speak with a skipper of your acquaintance, that he would be willing to give you the money that may be coming to you. Have him weigh the piece-goods that you have from me, and I shall satisfy that same skipper — one who would do it well and faithfully — but he must not give anything without bringing a letter with him, or else it is not properly secured, for I shall pay him his money immediately and also cover his labour. I would have come myself, but I have so much work that I cannot be free from the house.

Marten, I commend myself most warmly to your dear wife and send her a Jesus [Note: likely a devotional gift, perhaps a small image or token of Jesus; the word is partially illegible in the original] such as she had asked me for. Please receive it in good spirit. I thank you for your kind goodwill. Should I live to see the time, I hope to earn it back from you in return.

Written in haste on the 7th day of July, in the year 1533.""",
    11: """Right worshipful sir, my duty humbly considered, and so forth. Sir, you shall receive, by the grace of God, in Awdryan Johnson's keeping, a firkin containing 10 rounds of sturgeon, and so forth. So Jesus be with you, amen.""",
    12: """With friendly greetings as aforementioned to you, my dear and most beloved uncle. I commend myself as heartily as I am able to your good and amiable grace. My dear and most beloved uncle, it may please you to know that I am greatly distressed at having had no news of you, as I have not heard from you in so long, which causes me great sorrow, for I have written you so many letters and I receive no reply. But I must have patience until such time as it pleases you, my dear uncle. My dear and most beloved uncle, I commend and recommend myself to your good and amiable grace. And I beg you, my dear uncle, that you would be so good as to think upon all past matters [Note: likely referring to an outstanding debt or unresolved business between them], for it would cost you little and would help greatly one of your own poor blood. Thus I beg you, my dear uncle, please do remember me. Know, my dear uncle, that I have here in Antwerpen spoken with an Englishman who, as I understand, has married your daughter, and he told me that you are still hale and in good health, which was very glad news for me to hear. Thus I beg you, my dear uncle, that I may yet hold a place in your memory — no more for now, my dear uncle — but may God grant you and all your company long life and good health. My dear uncle, if I can render you any service here, I shall do so willingly and gladly. I beg you, my dear uncle, that it may please you to send me a reply of how you are faring. Written in haste at Antwerpen the 23rd of July in the year 1533.""",
    13: """At Antwerp, the 15th of July, in the year 1533; No. 1a

I trust by God that you are all in good health, etc. I am letting you know that I have sent Edward into Zeeland to come home with the first wind. Then, I would have you attend to your business and to take such money as shall happen to come in. And though you sell the better sheep for money, let there always be at least two in the flock. I would have you buy a flask of quicksilver, so long as you can have it for 9d at the most, as I think you shall better ship and sell away the almonds — and if you can make no store of any wares you have, except the 2 bales of madder, for which I would have 15s 6d per hundredweight in ready money at the least.

You may inform Edward Mewrelle that my hostess says she lent him a featherbed and a gown, and she marvels that he has not sent them back. If he has left them somewhere, bid him find such provision that they may be sent here with speed, for she says she shall otherwise pay for it.

And it was no wonder that Edward Martens's servant sold the bag of pepper to you, for there has not been so much in Antwerp in these past 7 years at one time.

Therefore, rid yourself of it as best you can, and if you have not yet sent me over any money by exchange, send it over now.

Pepper is dear at 27d and 3 mites less; cloves at 5s 6d — and therefore make no store of it, but sell if it be possible. Take heed of your beams and scales and weights, that you be not deceived in any way, and see that your comfits and [Note: "orradoes" — uncertain term, possibly a type of confection or preparation; identity unclear] be made as soon as Edward comes home. In any case, I fear that my cottons may go to a poor market. Then I shall not recover my costs. And see that you trust none [Note: "dbowttd" appears to be a scribal corruption, likely "doubt" or "doubtful credit" — meaning: trust no one of uncertain standing] unless you know them to be sure, or else that you have good surety. All other wares keep their prices as they did before. By other letters sent by Edward previously, and this — fare you well.""",
    14: """Friendly greetings written to you, my dearest husband Claes Raens. I let you know that I am well since Easter, and all my little household too, as I hope you are also.

I have received your letter and understood it well. You write to me about Machiel Dammasch's house. Know, Claes Raens, that Jana Braeckaet has married the Widow, so I think they will not sell but rather give it away.

Bernaet has also taken a husband, and he will not stay living there, because he does not want to do the buying and selling, so you may look into it. See whether they can be sold.

And Andries, the servant, has arrived and is well and healthy. And you do not write what the hops cost, since you have promised Pauelus Coernelys. And Diellyes van Goek has carted it away. And I have received that money — 30 shillings Flemish — so I still have enough in rolls for my household. And if you find good cheap goods, buy two good black ones and make sure the goods are good, for it is not always good to buy cheaply. And take good care that you do not make yourself sick, but go and tend to yourself. Nothing more at this time than may God preserve you and me in virtue.

Written in haste by me, Liesbet Raens, your housewife, on the feast day of Saint Jacob [Note: Saint James's Day, July 25].""",
    15: """Jesus

At Antwerp, the 24th day of July

Well-beloved wife, I heartily commend myself to you, trusting in Jesus that you are in good health and all your household.

I am writing to let you know that you shall receive from this bearer, Claes de Frise, 3 little firkins of sturgeon marked with my mark, which you shall deliver — the greatest of them to Master Blanke, and the second greatest, which is marked with the figure b4b. I would have you write a letter with all haste and send it to Coventry, for therein are 4 rounds for your mother, one, and each of your brothers, also one apiece. And the least of all has 2 rounds which I give to you to make merry with. And let Harry go to Master Hill to ask leave to take it up. And let him show him the letter, if he will not give you leave — for it is all to give away.

Thus Jesus preserve you in long life to His pleasure.

And whereas I have written that you shall receive the sturgeon from Claes de Frise, you shall receive it from Adrian Johnson, the bearer hereof.

By your husband,
Harry Austen""",
    16: """John Petey, I commend myself to you, trusting that my master, my lady, and all the household are in good health, of which I pray God for continuance. I desire you to give my commendations to all my friends and fellows, and not least to Master Nicholl, praying him to remember my gown — to have it taken to William Page's fuller to be dressed and dyed in a puce color. Once that is done, I pray you bid him fetch it home, and bid Hanyngton the tailor to make it ready for me against my coming home, and cause him to ruff the sleeves above, etc.

Item: at my departing at Billingsgate, I borrowed of John Bennett 20 shillings sterling for my costs, and Nycolas was there with my budget, and I brought him into Tower Street, where I was to receive from an armorer 24 shillings, which was ready, but he was out of the way. Wherefore I prayed you to receive the same 24 shillings from the said armorer — his name is Symond Cowper — and to give him a receipt in my name as need be. And of that, to give to John Bennett the 20 shillings I borrowed of him, so that I trust you have received it and given it to him; or else, if I were to learn the contrary, I would appoint him a place where he should receive the same 20 shillings.

Item: this is the substance of my letter. You shall receive out of Adryan Johnson's hoy of Antwerp half a sturgeon for my master, under his mark, which cost clear aboard with all manner of charges 39 shillings, paying for freight 8 pence.

Other news I have none to write, but that here is a difficult market and all manner of goods are here unreasonably dear and out of reach. White ware is very dear. [Note: The following appear to be commodity price quotations using abbreviated merchant notation and may be partially coded or in shorthand: "Holmes fustians g p £ lf, Osborns CC £ lpf, mather lRs and better, pepper gsg" — precise values are unclear.] All other goods are very dear, and especially all manner of mercery goods, so that men know not wherein to bestow their money. And yet they have bought it very dear. And thus our Lord keep you. In haste.

By your John Blundell""",
    17: """Jesus, Mary, Anna

Let this be written to you as a blessed greeting, to you my dearest son. Be pleased to know how greatly I long to hear how things may be with you and your wife, for I have heard nothing from you in a long while. And be pleased to know of me: I am in reasonably good health, after my old condition [Note: meaning she is managing as well as can be expected given her age or prior illness]. My beloved son, I would so very gladly see you once more before my death, if it were possible.

Your brother Peter sends you his warm greetings along with his wife. He now lives at Woeren at the mill. God grant him success there. And Marie, your sister, is not yet married. I wish that she had a good man. May God, who preserves and keeps you, my dearest son, bring you to a blessed end.

Written on Ascension Day [Note: the fortieth day after Easter, a moveable feast], in the year 1533, by me,

your devoted mother,
Katline Tsaseleren

Let me know whether you have received this letter.""",
    18: """Praise be to God.
Antwerp, 24 July, in the year 1533.

Via Adrian Janson, No. 32.

Know, Willem, that we are well and in good health, as I hope by the grace of God, and that the same is true for you.

Know that you shall receive from Adrian Janson, shipper from Antwerp, 2 small baskets containing 11 pieces of wood at 2 shillings 2 groats; also one hogshead containing 8 dozen and 4 pounds of fine yarn, and 4 dozen pounds of smooth round coloured yarn, purchased at 7 shillings 6 pence per dozen; also in this same sack, the same barrel, to be entered — 11 pieces of Tournai at 1 shilling per piece, that is 12 shillings per dozen; also 3 pieces called crossed says [Note: a type of lightweight twill-woven woollen cloth with a cross pattern] at 20 shillings Flemish per piece. They are approximately 14½ yards long or thereabouts; 1 carpet of silk thread at 22 shillings Flemish; 6 dozen figures at 25 shillings 6 pence; 4 gross of cord at 3 shillings 6 pence; 4 dozen large pieces at 19 shillings; also 1 further bale containing 22 dozen leather at 6 shillings; 12 dozen at 5 shillings 6 pence; 15 dozen at 4 shillings; also a pack of 6 tapestries in burlap wrapping; also 43 dozen tapestry pieces at 22 shillings 8 pence; 23 dozen Ypres doubles [Note: a double-width cloth from Ypres, a major Flemish textile city] at 16 shillings 6 pence per dozen.

Also 12 dozen Brussels ribbons at 15 shillings 2 pence; 6 dozen at 13 shillings 6 pence per dozen.

Also three pieces of kersey: 1 piece at 30 shillings, 1 piece at 28 shillings, 1 piece at 26 shillings. The merchant's mark is lacking.

Also one pack from Valenciennes, half ox-pieces: 37 pieces; 5 pieces at 21 shillings 8 pence; 3 pieces at 20 shillings 8 pence; 7 pieces at 19 shillings 8 pence; 6 pieces at 18 shillings 8 pence; 5 pieces at 17 shillings 8 pence; 3 pieces at 16 shillings 8 pence; 2 pieces at 15 shillings 8 pence; 1 piece at 15 shillings; 1 piece at 14 shillings; 2 pieces at 13 shillings 8 pence; 2 say-pieces at 12 shillings 8 pence.

Also you shall have in this same shipment 1 basket with three small crested jugs, 9 ewers, 15 hats, 8 items passed through, so that the crested pieces may be kept accordingly.""",
    19: """Jesus Maria, in the year 1533, on the 17th of July, in Cologne.

Greetings in the Lord, with all goodwill. Know this, Heinrich, good friend, that I wrote you a letter on the 14th of this month and am greatly vexed that you have not sent me your account. And since that date, two letters written by you have reached me, dated the 20th of June and the 1st of July. You write that you have received some crowns from Arnt Byrckman, and I shall repay him in crowns and render him the same in return. That shall be done, God willing. To Arnt and Johan van Gangell I shall duly pay the £30 sterling and shall see whether I might recover all their money from them — that which they have received in the country this year — so that they are secure in paying their exchange money, etc.

Furthermore, you write that I should still send you around 20 Mayssen [Note: a measure of gold, likely Maas weight] of gold, and that you still have enough silver. Here it is not possible to obtain even one measure for money. The goldsmiths will not make any more of them. I have commissioned them to make 25 by Remige [Note: the feast of St. Remigius, 1 October]. Before that time I shall not easily be able to bring anything to pass. The merzers are made and lying here at home, with nothing to pack alongside them. So I shall leave them lying until something comes along to pack with them.

Furthermore, you write that you would like to send me 3 blue caps with narrow borders, as soon as any arrive. I do not need the blue ones, unless they are fully saturated in colour and not streaky, and also not with white hairs showing, for they must be blue and remain blue, etc.

I have now obtained enough money by exchange to pay in Antwerp, praise God — as Otto will write to you — and I expect there will be no less than £400 sterling available to you before Bartholomew [Note: the feast of St. Bartholomew, 24 August]. So do take pains to buy good common woad with it, and one pack of good red and 2 fine russets of good colour, and this at the earliest opportunity possible. And as soon as you have laid out your money, come over. I would be glad if you were here for the fair, if that were possible. If not, then I must manage as best I can. God willing, as soon as you have laid out the money, come over per avviso [Note: by the next post or advice boat].

You write that you have not sent your account across because I did not write to you what the gold cost, and therefore you could not enter it in the book. Look back at your previous letters — when I sent you gold or silver you will easily find what it cost. And if not, you should have done as you have done hitherto and entered in the book whatever came of it. When we meet, it would soon be found what profit came of it. Wherever I told you the profit from it, I shall also hold to that, as is right. Not said because I should not know what is answered, but because you have left me entirely without your account. Therefore you are in the wrong, in my view, to let it rest as it is now.

I have received a letter dated the 6th of July. Within it I find your account summarised in brief. When the account comes to me itemised in detail, as it ought to be, and I find the items against mine to be correct, as they ought to be, then I will discharge you, as is right, and proceed to fulfil my promise. I wish however to be free of any bond with you per avviso — with that let the rest stand as it is.

Furthermore, this day I have loaded a large flat pack onto a ship bound for Antwerp. May the Lord God let it reach you in good condition, etc. With that, be commended to God the Lord, etc.

Derych Hoernner""",
    20: """You shall receive from the bearer of this letter, Audrien Janson of Antwerp, a barrel under this mark containing half a sturgeon, packed with 14 rounds and the half jowl, which is to be divided equally between my neighbour Laurens and myself — that is to say, 7 rounds apiece. And the jowl is to be sold to Mistress Jones, in case she will have it. She spoke to me about buying a jowl, as I recall. As long as she will have it at the price, we shall agree well. Furthermore, you shall understand that I sent by Humphrey Lewis's servant 5 firkins of ells and a half of seams, to be delivered to my wife for a sheet. The other, which was much better, is sold, as I understand from Master Wilson's servant, wherefore she must be content with it. Since the time cannot be extended, there was no other to be had — however, I have ordered another which I trust shall be ready by the time you receive this. Therefore I would not have my wife be too hasty in making use of it, for I have a period of consideration between now and the next fair as to whether I will have it or not. In case I do take it, I must pay 12 groats per ell, which is too much. Therefore let my wife keep it until she hears further.

Moreover, I pray you show Mistress Jarvis that I sent her 2 half-bundles of cloth for 2 shirts by William, Robert Stockfish's son-in-law, at the waterside at Billingsgate, who brought you a letter — trusting she has received it before now. It was all that I could get: they were never so scarce in Antwerp, as God knows.

Written in haste as above.

By me, James Bolney

Furthermore, you shall understand that I have sent you 2 letters before by overland post, which I trust have come into your hands long before now. And in accordance with the tenor of them, I will that you do the best you can and dispatch yourself and come over on the first ship that comes — it being too costly to come overland. I do not intend to delay long after your coming over, for various reasons, wherefore I will that you make haste, etc.

Copinger the fishmonger has the other half in the said ship.""",
    21: """At Antwerp, the 23rd day of July 1533

Brother Richard, I heartily commend myself to you, trusting in Jesus that my mistress with all the household are in good health, which I beseech Jesus long to continue to His pleasure, etc. Certifying you that my master has received your letter by master John Gresham, dated the 19th day of this month. And whereas you write to my master of master Bolinger's cloths, and if he comes to London again before my master comes home, you must buy them from him at some reasonable price for £25 10s, or as you see they are worth in quality. And give him £10 or £12 upon them until my master's coming home, and then he shall have the rest. And if there come any worsteds to the hall that are good and of any reasonable price, you must try if you can get them part for money and part on time. Also concerning the Saint Martin's worsteds, you must abate no money from the price that is set on them. And as for the fustians that you write of, my master can buy none to serve him at that price. Holms are worth £25 and Osborns of the grain £22 10s and fustians 21s 6d each. I can hear of none but the price named 16s — there is no kind of goods here to buy that can be sold at home to yield a profit of 26s in the pound.

Richard, and if master Lynch comes for any money, you must pay him none before my master comes home. As knows Jesus, who have you in His keeping.

By your fellow,
John Dene

Richard, my master has bought 5 bales of Bavernell of the grain, which cost £22. You must sell them for £17 13s 4d or better if you can, for here there are none to be had, and so you must show him that buys them. You must not let it be known but that 2 or 3 bales are packed in canvas, so that it should not be known what they are. You shall receive them by the grace of God in a hoy from Antwerp from Adrian Johnson's under this mark.

Richard, rather than fail, settle for £17 10s a bale. Also my master has bought 20 pieces of fustians. You must sell them for 17s, to be delivered at the coming home of the ships, or else before. And if any ship departs before then, Richard, you must sell them off, for they will be cheaper shortly. But you may tell the fustian shearers there are none to be had.

You shall receive in this ship but 4 of them, but you must make the bargain to deliver the 1 bale at that price as you sell the 4 bales — rather than fail, sell them for £17, for they will fall in price.""",
    22: """Worshipful sir, my duty considered, I humbly commend myself unto you, letting you know that you shall receive, by the grace of God, in good safety in Adrian Johnson's keeping: 9 sacks weighing 574, 750, 538, 464, 604, 500, 524, 516, 500, at 6 shillings 9 pence the hundredweight; gum [Note: "gum epoporeak" — likely gum opopanax or a similar medicinal resin, spelling uncertain] by the pound at 5 shillings; nigella romana 8 pounds at 6 pence; [Note: "sangloys" — unidentified commodity, possibly a spice or dyestuff] 14 pounds at 12 pence; lapis [Note: "lapis totte" — unidentified stone or mineral compound] by the pound at 18 pence; [Note: "armedactulus" — unidentified commodity, possibly a medicinal or aromatic substance] 6 pounds at 14 pence; senna 24¼ pounds at 18 pence in the senna; 1 pound of turbith at 8 shillings; and the armedactulus settoalle 3 pounds at 9 shillings 6 pence the pound. All these small parcels are loose in the ship. Bolt canvas 12 rolls, 1 half barrel of crossbow thread. These are marked with a cross, as God knows, who ever preserve you. Amen.

By your servant,
Robert Hobbes""",
    23: """Brother Christopher, I heartily commend myself to you, etc., letting you know that at the writing of this my master and I were in good health, God be thanked. Also you shall receive by Adrian Johnson of Antwerp 5 little casks — 2 with sturgeon, 2 with olives and capers, and another with succade — which were shipped at Antwerp on the day noted above and marked with this my master's mark.

Also I have received my pack and Richard Ponter's budgets from Martin Allbrook. Also I have sent by Master Prat, grocer, a letter and a dozen lute strings, which I trust you have received. Also I pray you send me word of how he likes them. Also at the writing of this my master cannot tell where I shall be, for he with whom I should have stayed has buried his wife and is living in his son's house. Therefore he will not have me with him, and so farewell. In haste, by your

Blase Saunders""",
    24: """Jesus, 1533, the 23rd day of July, in Antwerp.

Right worshipful and my singularly good master, in the most humble manner that I can, I commend myself unto you, trusting in Jesus that you are in good health, which I pray Jesus long to continue to his pleasure, with the same due to my mistress, etc. I certify you that as of yesterday I received letters from London, whereby I perceive that you have been in Derbyshire, where I trust you have prospered well, or else I would be sorry, as it shall become me to be.

And as for your money that I am indebted to you, it is no small sum. Notwithstanding, it is not yet within my power to pay, but I trust sometime to recover it. This shall be through your goodness.

And as touching the sales that have been, this show day just past was never worse, for your servant sold never a cloth, nor did a great many more than I.

Sir, this day there are letters come from Venice, whereby ginger is in good supply. Therefore if you have any stock at home, sell it well or keep it still, for that which you shall buy henceforth shall be dearer.

Sir, touching your two bills that I have of you, I shall see them delivered to you within these 14 days, God willing. And as for the 54 shillings sterling that you have paid to Mistress Hall, you must have of Harry Mylles for 475 pounds in lead weights of the same reckoning, and the rest I must give you or your servant.

Other news there is none but great murmuring of the death of the 2 strangers of the great misfortune, from which I pray Jesus keep every Christian man. Written in haste the day above as stated.

Sir, this day there shall be a court held here. And men think that there shall be a shipping again now at this Barbers Mart. If it be so, then farewell good sales of cloth for these seven years. I cannot as yet write the truth until afternoon. And may the Holy Ghost preserve you and all yours, amen.

Per your servant, Stephen Bodington.""",
    25: """Bernaert, I commend myself warmly to you and to your dear wife Maeyken. I write to let you know that Willem de Vlemmick has shed his fat belly. [Note: This likely refers to a significant change in Willem's physical appearance or health, possibly weight loss due to illness.] So changed, that you would not be able to recognize him. And give my warm regards to black Peter and to all the embroiderers and to little drunken cup [Note: an affectionate nickname for a mutual acquaintance] not forgotten, and to all the good friends. Herewith, remain commended to God. Written in haste on the 26th day of May in the year 1533.

Your devoted friend,

Jan van Espen""",
    26: """In the name of Jesus and Mary, the 23rd day of July 1533, in Antwerp.
To T. Brace and his company in London.

My last letter was held back by us due to a failure in conveyance, along with £100 sterling in gold. We shall send it by the next opportunity. Therefore, if you receive anything from Newbury now, then you can settle the account. You may wish to be paid within 8 or 10 hours, for against this £400 sterling trust — send such things as you have with diligence. Seal all things with our seal, and do not let everything go to the London stand, but place part of it at the waterside.

The purpose of this letter is only that you shall receive, by God's grace, on this ship with Adrian Johnson, one little truss under the mark shown in the margin, containing one coverlet of lilies. Deliver it to Mistress Smyng. Also, half a piece of lawn from Naef. Let Mistress Whale have it for the price. Also, another half piece of lawn at a certain cost. If she will have it, sell it for no less than the set price in sterling. It is half-price already. If she will not take it, show it to Mistress Shakeley. Also, one pair of writing tablets for Henry Brinklow.

Do your business secretly and with diligence.

Written by me, Henry Brinklow, in haste.

Spare not to send.

[Note: "d100,000 oy partes in o shep, videlicet Ely in o f ' d" — heavily abbreviated mercantile notation, likely referring to a consignment split across one ship; full meaning unclear due to coding.]""",
    27: """Friendly greetings as aforesaid to you, Marten Tehaselare, my dear friend.

You will be pleased to know that I, Katrijne, your mother, am in reasonable health at this time. As I hope, by the grace of God, that you also are, together with your wife and your household, of whom I have had no news, which weighs heavily on my heart.

Marten, my son, I wish to let you know that I have had a great illness, such that I believed I would never see you again. But God the Lord — may He be thanked — I have now recovered.

I wish to let you know that I have learned that you sent me a tabard of cloth, for which I thank you heartily.

Maerten, it has never truly come to my heart, as you had supposed, that it would have arrived at the right house. Marten, I wish you to know that I, Kathryna your mother, have a great desire to see you once more with my own living eyes, before I depart this earth. And know that I still have something particular to say and tell you, which I have always kept secretly in my heart.

Nothing more at this time, except that God be with you always. Written by me, Jan Speeckaert, in Brussels, the 27th day of May.

Also, Merten, my dear friend. I wish to let you know that the widow Bettulen, your wife's mother, sends you warm greetings, along with Lussken her daughter. And know that Babelken, her sister, has passed away; may God have mercy on her soul.""",
    28: """I greet you well with all honor, trusting in God that he is in good health throughout. And so I was at the writing of this. By the grace of God, he shall receive in Adrian Gonson's house in Antwerp — she is called the Games of Antwerp — two maunds of trenchers. In the one maund there are 3,000 and odd trenchers at 7 shillings per thousand, and in the other are 3,000 trenchers, costing 2 shillings per thousand. And he shall receive from them a flour bag, and in it there is a dozen sleys and 6 dozen 3-penny pieces for settles. They cost in all 4 shillings 6 pence Flemish. They are for my gossip John Nundeth. Let them pay for the sleys 4 shillings sterling, and for the penny pieces all together 3 shillings sterling.

I send you two letters, one of John Don's making. I trust he has received them. And I sent you a letter with Harold's ship and a small dry cask. I trust he has received these goods by this time, for there are diverse men who have come about. I have no letter as yet from any of them, whereof I marvel — how he has dealt with the wares that I sent you with Peter Classen, I hear nothing of it. I am here in a wretched case for money, for I have not gotten enough as yet. Nor can I get any grant from Master Davies's servant as yet — and I fear that he will deceive. And I have recalled one debt for the old money, and I have not sold half my nets as yet. I cannot make back the money they cost, and therefore buy no more of them unless they are very good and full of flour. Therefore in any wise do your best and raise money. Sell away what will go, for I fear lest I be troubled here. By the next letter he shall know more about it. Jesus speed you well. Written in Antwerp the 23rd day of July.

By your Richard Donne""",
    29: """Know, dear brother, that I have sent you with Peter Kalssen one hundred small fans, costing 15 and a half stuivers each. Likewise I have paid you 6 nobles and 10 stuivers more than your money's worth. I have also sent you a half dozen handkerchiefs, costing 21 stuivers, and another 5 handkerchiefs for 20 stuivers, and also three dozen fans and 7 more, which cost 14 stuivers — there was not a single one more to be had at that moment. And you have also received three cakes, costing 6 stuivers. And you have also received a heller's worth, costing three stuivers. And likewise one pound of yarn for three stuivers. And the basket for 6½ stuivers, and the toll on two hundred fans — 24 stuivers — together with the shipping, I have paid here. You therefore owe nothing for any of that. And he has sent me two stuivers once, and I have received two guilders on one occasion from Peter Tijs's mother, but I shall have no more from that, as those are my costs — for what I have, I do not know by what means you will arrange delivery of the letters, so that I might receive payment. And furthermore, I cannot get the costs for less than 10 stuivers. That is what they fetch, because it is market time. So I have reckoned that I shall receive 10 shillings and 5 stuivers once you have this hundred large fans at home. And now I have received one noble from Jan Peters, and I shall arrange all things for you, God willing.

Know, dear brother, it grieves me greatly that you have waited so long, but Our Lord knows that I could not bring the money together, yet I found a friend who lent me what was needed. The very cheapest small fans to be had in the city, in truth — and so I have paid 10 stuivers more on the small fans than your 6 nobles, as reckoned — whatever I have laid out in costs and expenses I shall reimburse, and God willing I will send you other goods. Written on the Feast of All Apostles by me, Jheronimus, your brother, always ready for your good. Greet our Katrin our sister sincerely, and Merten and Anne our niece, and Cornelis and Anne Banckers, and all other friends. Hubert also sells beer.

I am sending you with Knapkout 10 bundles of large fans.""",
    30: """Bedfellow, I heartily commend myself to you, letting you know that by the bearer of this letter, Adryan Johnson, master of a ship named the James of Antwerp, I am sending 2 firkins of sturgeon, also 3 small firkins more — one with olives, another with capers, and another with succade — which are in all 5 pieces, all marked in black with this mark in the margin. And you must pay for freight 12 pence, as the shipper's book does show. And as for one of the barrels of sturgeon and the succade, let it be opened to treat your gossips withal at your lying-in, praying God to send you well through it, which would be greatly to my comfort to hear of.

Furthermore, you shall understand that since my coming here, I did send you a letter by my cousin Pratt, with which I sent you a token, which shortly I trust you shall receive. And as soon as I can, I will bring you a token myself, by the grace of God, who keep you in His merciful governance.

Your bedfellow,
William Butler""",
    31: """Jesus, at Antwerp, the 23rd day of July, in the year 1533.

Right worshipful master, my duty considered, I heartily commend myself unto you, glad to hear of your good welfare, which I pray Jesus long to continue to his pleasure and to your heart's most desire, certifying you that at the making hereof my master was in good health, thanked be Jesus. And so he trusts that you are with all his household, etc. Certifying you that of late my master has sent you one letter bound with Master Laurence's letters, of all his whole mind. And at the making hereof he received one letter of Master Thomas's hand by the post. Also you shall receive out of Adrian Johnson of Antwerp 4 pokes of hops, costing 7 shillings 8 pence the hundredweight. The first penny you must pay for freight of 18 hundredweight — so I have written in his book — at 4 pence the hundredweight, and handling charges besides.

You shall understand that John Maye has bought at Arnemuiden 3 hundredweight of bay salt, costing £10 4 shillings the hundredweight, and every hundredweight is 10 ways. It is ready to depart hence with the next wind that blows from the east, and so is Adrian Johnson. My master trusts you shall have it for 8 pence a bushel and by the way for 25 shillings. He prays you to sell it beforehand if you can. Salt has risen at Arnemuiden within these 4 days to £11 5 shillings a hundredweight. Thus John Maye has written to my master.

And as touching the hops, iron, and nails, my master prays you to ride them to the most profit at their coming to you. Hones iron is here at 32 stivers the hundredweight, and Namur iron at 28 and a half stivers and 29 stivers Flemish. Madder is at 19 shillings a hundredweight and 19 shillings 6 pence, such as my master is accustomed to buy, and the 4th quality at 17 shillings and 17 shillings 8 pence the hundredweight if it be good. And hops 7 shillings the hundredweight and 6 shillings 8 pence the worst. Latten wire the hundredweight 32 shillings, black soap the barrel 23 shillings 8 pence and 24 shillings. Large maces the pound 10 shillings 6 pence, cloves the pound 6 shillings 8 pence, pepper the pound 2 shillings 3 pence. Here there is much shortage of alum and white soap coming in.

My master prays you to write him one letter of your mind as shortly as you can, and whether you will have any soap bought, and what wares you think it best to buy. He has much money lying here and does not know upon what ware he shall bestow his money so as to do any profit. In all things it is so dear here and cheap in England, which troubles him sorely. Also my master intends to dispatch and to come home shortly. He has sold all his cloths and dozens, saving 2 whites and 4 dozens. No more to you at this time, but Jesus have you in his keeping, amen.

By your servant,
Harry Maye""",
    32: """At Antwerp, the 24th day of July, in the year 1533.

My Kate, as heartily as I can, I commend myself to you, glad to hear of your good health along with all my boys. And so I send all my boys God's blessing and mine. And that Master Dick shall have more tomorrow before I die. And among all others, commend me to the little pig in the basket. And so commend me to Master FitzRamys and to good Mistress FitzRamys. And I have received a letter from him, which I well understand, and as this day and as shortly as I can, I shall send her a fine piece of cloth home.

And so, Kate, I have received a letter from you, which I well understand — you have written to me for seams, and it is too late to write now; however, if I do not bring them myself, Nicholas, when he comes, shall bring them. You should not have gone against me then when I was there myself, for then I would have brought them with me. Nevertheless, for fear of a sour look — I would have said a shrewish look — I dare do nothing other than to do my best as much as I can, etc.

And so, Kate, I have sent you a great barrel of sturgeon in a hoy from Antwerp called Adrian Johnson. In the said barrel there are 13 pieces with 130 jellies in the said barrel. Also you shall receive in the said ship a little barrel of sturgeon for Master Ressener, in which barrel there are 12 jellies and 16 rounds. And so, when it shall please God that you shall receive his letter, let it be delivered to Master Ressener and show him it is very good.

Also, you write to me that I should send you word to hear what the bill of payment was from Denssy. I delivered the said bill of Dinsey's to Master Daniell in my counter. And he knows full well how it stands. I know his mind: he is looking for his reward. I trust in God to be at home shortly and pay him myself.

And now, Kate, I wish I were at home, seeing that my side grieves me very sorely. I cannot tell what I shall say to it, for if your venison does not come shortly, I think I shall get none of it, as Christ knows — who ever keep you and yours, Amen.

Written in haste. Tomorrow I will write you more, for then is the holy day of Saint James's Day.

Yours ever, William Colsell, mercer""",
    33: """At Antwerp, the 2nd day of July, in the year 1533.

Right worshipful sir, my duty done, I commend myself to your mastership. Sir, you shall receive, by the grace of God, from Adrian Johnson of Antwerp, the bearer of this letter, a bundle containing 58 pieces of say, sorted as shall appear by this bill. Freight: 3 shillings sterling.

No. 1: 1 piece of say at 22s
No. 2: 1 piece of poor say at 23s
No. 3: 2 pieces at 24s
No. 4: 2 pieces at 25s
No. 5: 3 pieces at 26s
No. 6: 2 pieces at 27s
No. 7: 4 pieces at 28s
No. 9: 3 pieces at 29s
No. 10: 4 pieces at 30s
No. 11: 5 pieces at 31s
No. 12: 5 pieces at 32s
No. 13: 4 pieces at 33s
No. 14: 4 pieces at 34s
No. 15: 3 pieces at 35s
No. 16: 3 pieces at 36s
No. 17: 3 pieces at 37s
No. 18: 3 pieces at 38s
No. 19: 1 piece at 39s
No. 20: 1 piece at 40s
No. 21: 1 piece at 45s
No. 22: 2 pieces at 54s
No. 23: 1 piece at 60s

Total: 58 pieces amounting to £95 7s, besides the costs, which you shall know by my letter sent by land. In haste, yours,

John Westbury""",
    34: """On the 2nd of July, in the year 1533.

John Westbery, aboard the ship of Adrian Johnson of Antwerp, one bale under this mark. Freight: 3 shillings sterling.""",
    35: """Jesus

In Antwerp, the 22nd day of July, in the year 1533

Right worshipful Master Dawes, I commend myself to you as one not yet known to you, but I trust in God that within a short time we shall be better acquainted, etc.

Sir, the reason for my writing to you at this time is to certify you that Master Flege, my good master and friend, has at various times spoken to me of your goodness and your honest, true dealing, and of the wish that you would have him send certain wares that you have advised him of by your letters written to him, as I understand from your last letter, which you sent him by this bearer, Ariane Johnson, shipman of Antwerp. That letter is dated the first Monday in Lent [3 March 1533], etc. Sir, Master Flege has so much to do here with his merchandise of stall and of cloths, that he has no great inclination to trade into England. Sir, therefore, having seen his letters sent by you to him, and that you would be glad to show his servant the profits of your country, I have at this time heard of a hoy and have bought the following wares, and I purpose to be with you within this month after the writing of this letter.

These are the wares: 4,000 lb. of iron of Namur at 4s 3d per hundredweight; 2,000 pots at 3s 4d per hundredweight; 20,000 paving tiles at 3s 6d; 4,400 lb. of hops at 7s per hundredweight in small bags; and 2 hundredweight of Bay salt at £12 per hundredweight (the hundredweight being 10 and a half ways, London measure); 24 barrels of fustians at 12s per barrel; and 12 barrels of white salt; and I have also laded certain of 1,000 staple feather balls, of which there are as yet none come into Scotland. Also I shall bring with me a hundredweight of dressed flax, and hand baskets, and lanterns, and some bellows, and a thousand trenchers. Also I shall bring with me a small barrel of sturgeon to make acquaintance with.

Sir, I pray you to make known to your acquaintances that you have these wares coming, for I will do well by you. You should keep these wares as your own when they arrive, and, Sir, if you could make provision for a hundredweight or two hundredweight of cheeses and butter at a reasonable price, I would have it at my coming, if I might have licence for it. I pray you do your best against my coming, and then you shall know more of my mind. Sir, if you can buy mustard seed for 8s, 10s, or 12s a quarter, it would fetch a good price here; also tallow, and bacon, and malt, and barley, with various other goods.

Sir, I would have written to you at various times before now, but I could not find out how my letters might be conveyed to you, until this my friend Ariane Johnson showed me that he is very well acquainted with you. Sir, this bearer can tell you more of my mind, for he knows me well. Sir, thus I am bold to write to you at this time: I trust it shall be to your profit and mine. Also, by God's grace, we preserve in health. My good wishes to Maldon.

By your own to the best of his power, John Smyth, grocer, and one of the overseers to the Merchant Adventurers in Antwerp, and have been these ten years.""",
    36: """My friendly greetings beforehand, etc. Esteemed, great, gracious lords and good friends: I cannot conceal from your wisdoms how I have fared and continue to fare daily in the matter concerning the English. They have seized certain goods in our open ships, and what worry and trouble I, together with the common merchant community at the Steelyard [Note: the Hanseatic Kontor in London], have had on account of this is not to be put into writing. They bring us before the king every single day and present their complaints, and however they choose to frame things and whatever they put forward must be accepted as right without any contradiction whatsoever, so that I find myself in great distress together with the merchants. They wish to have the goods paid for by the merchants without delay. It is therefore my request that your Honourable Council endeavour to ensure that such goods as may be in the hold, which we have taken, remain together and are not dispersed, for they are not enemy goods. There are various kinds of goods among them, such as money and silken cloth, and I am greatly troubled that such goods should be disgracefully removed and diverted by the boat-men and skippers, who nevertheless do not allow themselves to be restrained and put out of the way what they can. Your Honourable Council should be well aware in advance of this, for whatever is diverted away, you will have to make good — so long as you do not wish to lose the Steelyard together with the Hanse and its privileges. Far better would it be to lose ten hundredweight of gold than such a privilege. Therefore I trust your Honourable Council will look into the matter in such a way that it will not prove necessary.

Also, gracious lords: a Spaniard has been seized, who has been permitted, as Gasck Remrade, to come to his legal remedy. As your Honourable Council will doubtless be well aware, the very ship which was taken from the Spaniard was seized in the Downs [Note: a well-known anchorage off the Kent coast in the English Channel]. The King of England now wishes to prohibit that same vessel on account of his waters. I would urgently request that that same ship be given back, and moreover that compensation be made for whatever he considers himself owed for the fact that we seized such a ship in his waters. It is therefore my friendly petition that those same goods may remain together, and if the boat-men or other persons have removed anything from them, that it be restored, or else that someone pay for it at the very highest price.

Furthermore, gracious lords: it is necessary that your Honourable Council, upon receipt of this letter, compose a letter as well as you are able, and it would be quite necessary that a suitable man come from our secretaries there, both in writing and in spoken petition, to the effect that we had not at all expected such treatment from his Royal Highness — that he should have dealt with our people in this manner, while throughout this entire year we have treated his subjects with all courtesy and have not in any way hindered them; and that the harm which has befallen us, by which we have been damaged, is such that we could well have done our enemies great injury, and nothing hindered this anywhere except the fact that I was detained here on land — as you will come to understand well enough from what I write.

Gracious lords: you may understand this better from what I have written to the Alderman together with the common merchant community; they too have written to you concerning all the circumstances in full. And the Alderman Hans Molenbeke, together with the merchant council, have applied every effort to have me released on free terms, but this could not be brought about for me. Nevertheless, I may go and stand wherever I wish within the city; I may only not leave the country. I therefore hope your Honourable Council will take this matter to heart and write accordingly, so that I may be freed and the merchants may remain undisturbed. Written in London, the 9th day of September 1533.

Marx Meyer,
Your servant.""",
}

# Load existing letters.json
with open("letters.json", "r", encoding="utf-8") as f:
    letters = json.load(f)

# Merge translations
for letter in letters:
    lid = letter["id"]
    if lid in translations:
        letter["modern_english_translation"] = translations[lid]

# Write updated letters.json
with open("letters.json", "w", encoding="utf-8") as f:
    json.dump(letters, f, indent=2, ensure_ascii=False)

print(f"Updated letters.json with {len(translations)} translations")

# Update .md files
for letter in letters:
    lid = letter["id"]
    if lid not in translations:
        continue
    md_path = CATALOGUED / f"letter_{lid:02d}.md"
    content = md_path.read_text(encoding="utf-8")

    # Add translation section before ## Editorial Notes
    if "## Modern English Translation" not in content:
        translation = translations[lid]
        content = content.replace(
            "## Editorial Notes",
            f"## Modern English Translation\n\n{translation}\n\n## Editorial Notes"
        )
        md_path.write_text(content, encoding="utf-8")

print(f"Updated {len(translations)} .md files with translations")
