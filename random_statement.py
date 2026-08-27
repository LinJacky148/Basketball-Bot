import numpy as np
nba = ["歡迎使用NBA顧問"]

MVP = [
    "2023-2024球員：Nikola Jokić\n隊伍：Denver Nuggets\n國籍：Serbia\n位置：Center\n"
    "2022-2023球員：Joel Embiid\n隊伍：Philadelphia 76ers\n國籍：Cameroon\n位置：Center\n"
    "2021-2022球員：Nikola Jokić\n隊伍：Denver Nuggets\n國籍：Serbia\n位置：Center\n"
    "2020-2021球員：Nikola Jokić\n隊伍：Denver Nuggets\n國籍：Serbia\n位置：Center\n"
    "2019-2020球員：Giannis Antetokounmpo\n隊伍：Milwaukee Bucks\n國籍：Greece\n位置：Power forward\n"
    "2018-2019球員：Giannis Antetokounmpo\n隊伍：Milwaukee Bucks\n國籍：Greece\n位置：Power forward\n"
]

新人王 = [
    "2023-2024球員：Victor Wembanyama\n隊伍：San Antonio Spurs\n國籍：France\n學校/先前經歷：Metropolitans 92\n選秀順位：1\n選秀年份：2023\n"
    "2022-2023球員：Paolo Banchero\n隊伍：Orlando Magic\n國籍：United States\n學校/先前經歷：Duke (Fr.)\n選秀順位：1\n選秀年份：2022\n"
    "2021-2022球員：Scottie Barnes\n隊伍：Toronto Raptors\n國籍：United States\n學校/先前經歷：Florida State (Fr.)\n選秀順位：4\n選秀年份：2021\n"
    "2020-2021球員：LaMelo Ball\n隊伍：Charlotte Hornets\n國籍：United States\n學校/先前經歷：Illawarra Hawks (Australia)\n選秀順位：3\n選秀年份：2020\n"
    "2019-2020球員：Ja Morant\n隊伍：Memphis Grizzlies\n國籍：United States\n學校/先前經歷：Murray State (So.)\n選秀順位：2\n選秀年份：2019\n"
    "2018-2019球員：Luka Dončić\n隊伍：Dallas Mavericks\n國籍：Slovenia\n先前經歷：Real Madrid (Spain)\n選秀順位：3\n選秀年份：2018\n"
]

最佳進步獎 = [
    "2023-2024球員：Tyrese Maxey\n隊伍：Philadelphia 76ers\n國籍：United States\n位置：Guard\n"
    "2022-2023球員：Lauri Markkanen\n隊伍：Utah Jazz\n國籍：Finland\n位置：Forward\n"
    "2021-2022球員：Ja Morant\n隊伍：Memphis Grizzlies\n國籍：United States\n位置：Guard\n"
    "2020-2021球員：Julius Randle\n隊伍：New York Knicks\n國籍：United States\n位置：Forward\n"
    "2019-2020球員：Brandon Ingram\n隊伍：New Orleans Pelicans\n國籍：United States\n位置：Forward\n"
    "2018-2019球員：Pascal Siakam\n隊伍：Toronto Raptors\n國籍：Cameroon\n位置：Forward\n"
]

最佳教練 = [
    "2023-2024賽季教練：Mark Daigneault\n隊伍：Oklahoma City Thunder\n勝-敗：57-25\n勝率：.695\n"
    "2022-2023賽季教練：Mike Brown\n隊伍：Sacramento Kings\n勝-敗：48-34\n勝率：.585\n"
    "2021-2022賽季教練：Monty Williams\n隊伍：Phoenix Suns\n勝-敗：64-18\n勝率：.780\n"
    "2020-2021賽季教練：Tom Thibodeau\n隊伍：New York Knicks\n勝-敗：41-31\n勝率：.569\n"
    "2019-2020賽季教練：Nick Nurse\n隊伍：Toronto Raptors\n勝-敗：46-18\n勝率：.719\n"
    "2018-2019賽季教練：Mike Budenholzer\n隊伍：Milwaukee Bucks\n勝-敗：60-22\n勝率：.732\n"
]

最佳第六人 = [
    "2023-2024球員：Naz Reid\n隊伍：Minnesota Timberwolves\n國籍：United States\n位置：Center\n"
    "2022-2023球員：Malcolm Brogdon\n隊伍：Milwaukee Bucks\n國籍：United States\n位置：Guard\n"
    "2021-2022球員：Tyler Herro\n隊伍：Miami Heat\n國籍：United States\n位置：Guard\n"
    "2020-2021球員：Jordan Clarkson\n隊伍：Utah Jazz\n國籍：Philippines\n位置：Guard\n"
    "2019-2020球員：Montrezl Harrell\n隊伍：Los Angeles Clippers\n國籍：United States\n位置：Power forward、Center\n"
    "2018-2019球員：Lou Williams\n隊伍：Los Angeles Clippers\n國籍：United States\n位置：Guard\n"
]

最佳第6人 = [
    "2023-2024球員：Naz Reid\n隊伍：Minnesota Timberwolves\n國籍：United States\n位置：Center\n"
    "2022-2023球員：Malcolm Brogdon\n隊伍：Milwaukee Bucks\n國籍：United States\n位置：Guard\n"
    "2021-2022球員：Tyler Herro\n隊伍：Miami Heat\n國籍：United States\n位置：Guard\n"
    "2020-2021球員：Jordan Clarkson\n隊伍：Utah Jazz\n國籍：Philippines\n位置：Guard\n"
    "2019-2020球員：Montrezl Harrell\n隊伍：Los Angeles Clippers\n國籍：United States\n位置：Power forward、Center\n"
    "2018-2019球員：Lou Williams\n隊伍：Los Angeles Clippers\n國籍：United States\n位置：Guard\n"
]

年度獎項 = [
    "最有價值球員 (MVP)2022-2023：Joel Embiid (Philadelphia 76ers)\n"
    "年度新秀 (Rookie of the Year)2022-2023：Paolo Banchero (Orlando Magic)\n"
    "最佳教練 (Coach of the Year)2022-2023：Mike Brown (Sacramento Kings)\n"
    "最佳防守球員 (Defensive Player of the Year)2022-2023：Jaren Jackson Jr. (Memphis Grizzlies)\n"
    "最佳第六人 (Sixth Man of the Year)2022-2023：Malcolm Brogdon (Boston Celtics)\n"
    "最佳進步球員 (Most Improved Player)2022-2023：Lauri Markkanen (Utah Jazz)\n"
    "最佳運動員精神獎 (Sportsmanship Award)2021-2022：Patty Mills (Brooklyn Nets)\n"
    "最佳隊友獎 (Teammate of the Year)2021-2022：Jrue Holiday (Milwaukee Bucks)\n"
    "社會正義冠軍獎 (Social Justice Champion Award)2022-2023：Stephen Curry (Golden State Warriors)\n"
    "關鍵時刻最佳球員獎 (Clutch Player of the Year)2022-2023：De'Aaron Fox (Sacramento Kings)\n"
]

最佳防守球員 = [
    "2023-2024球員：Rudy Gobert\n隊伍：Minnesota Timberwolves\n國籍：France\n位置：Center\n"
    "2022-2023球員：Jaren Jackson Jr.\n隊伍：Memphis Grizzlies\n國籍：United States\n位置：Power forward\n"
    "2021-2022球員：Marcus Smart\n隊伍：Boston Celtics\n國籍：United States\n位置：Point guard\n"
    "2020-2021球員：Rudy Gobert\n隊伍：Utah Jazz\n國籍：France\n位置：Center\n"
    "2019-2020球員：Giannis Antetokounmpo\n隊伍：Milwaukee Bucks\n國籍：Greece\n位置：Power forward\n"
    "2018-2019球員：Rudy Gobert\n隊伍：Utah Jazz\n國籍：France\n位置：Center\n"
]

年度第一隊 = [
    "2023-2024年度第一隊：Shai Gilgeous-Alexander\nNikola Jokić\nLuka Dončić\nGiannis Antetokounmpo\nJayson Tatum\n"
    "2022-2023年度第一隊：Giannis Antetokounmpo\nJayson Tatum\nJoel Embiid\nLuka Dončić\nShai Gilgeous-Alexander\n"
    "2021-2022年度第一隊：Luka Dončić\nDevin Booker\nJayson Tatum\nGiannis Antetokounmpo\nNikola Jokić\n"
    "2020-2021年度第一隊：Giannis Antetokounmpo\nNikola Jokić\nStephen Curry\nLuka Dončić\nKawhi Leonard\n"
    "2019-2020年度第一隊：LeBron James\nGiannis Antetokounmpo\nAnthony Davis\nJames Harden\nLuka Dončić\n"
    "2018-2019年度第一隊：James Harden\nStephen Curry\nGiannis Antetokounmpo\nPaul George\nNikola Jokić\n"
]

年度第1隊 = [
    "2023-2024年度第一隊：Shai Gilgeous-Alexander\nNikola Jokić\nLuka Dončić\nGiannis Antetokounmpo\nJayson Tatum\n"
    "2022-2023年度第一隊：Giannis Antetokounmpo\nJayson Tatum\nJoel Embiid\nLuka Dončić\nShai Gilgeous-Alexander\n"
    "2021-2022年度第一隊：Luka Dončić\nDevin Booker\nJayson Tatum\nGiannis Antetokounmpo\nNikola Jokić\n"
    "2020-2021年度第一隊：Giannis Antetokounmpo\nNikola Jokić\nStephen Curry\nLuka Dončić\nKawhi Leonard\n"
    "2019-2020年度第一隊：LeBron James\nGiannis Antetokounmpo\nAnthony Davis\nJames Harden\nLuka Dončić\n"
    "2018-2019年度第一隊：James Harden\nStephen Curry\nGiannis Antetokounmpo\nPaul George\nNikola Jokić\n"
]

年度第二隊 = [
    "2023-2024年度第二隊：Jalen Brunson\nAnthony Edwards\nKevin Durant\nKawhi Leonard\nAnthony Davis\n"
    "2022-2023年度第二隊：Jimmy Butler\nJaylen Brown\nNikola Jokić\nStephen Curry\nDonovan Mitchell\n"
    "2021-2022年度第二隊：Stephen Curry\nJa Morant\nDeMar DeRozan\nKevin Durant\nJoel Embiid\n"
    "2020-2021年度第二隊：Damian Lillard\nJoel Embiid\nChirs Paul\nJulius Randle\nLeBron James\n"
    "2019-2020年度第二隊：Kawhi Leonard\nPascal Siakam\nNikola Jokić\nDamian Lillard\nChirs Paul\n"
    "2018-2019年度第二隊：Damian Lillard\nKyrie Irving\nKevin Durant\nKawhi Leonard\nJoel Embiid\n"
]

年度第2隊 = [
    "2023-2024年度第二隊：Jalen Brunson\nAnthony Edwards\nKevin Durant\nKawhi Leonard\nAnthony Davis\n"
    "2022-2023年度第二隊：Jimmy Butler\nJaylen Brown\nNikola Jokić\nStephen Curry\nDonovan Mitchell\n"
    "2021-2022年度第二隊：Stephen Curry\nJa Morant\nDeMar DeRozan\nKevin Durant\nJoel Embiid\n"
    "2020-2021年度第二隊：Damian Lillard\nJoel Embiid\nChirs Paul\nJulius Randle\nLeBron James\n"
    "2019-2020年度第二隊：Kawhi Leonard\nPascal Siakam\nNikola Jokić\nDamian Lillard\nChirs Paul\n"
    "2018-2019年度第二隊：Damian Lillard\nKyrie Irving\nKevin Durant\nKawhi Leonard\nJoel Embiid\n"
]

年度第三隊 = [
    "2023-2024年度第三隊：LeBron James\nStephen Curry\nDomantas Sabonis\nTyrese Haliburton\nDevin Booker\n"
    "2022-2023年度第三隊：LeBron James\nJulius Randle\nDomantas Sabonis\nDe'Aaron Fox\nDamian Lillard\n"
    "2021-2022年度第三隊：Chirs Paul\nTrae Young\nLeBron James\nPascal Siakam\nKarl-Anthony Towns\n"
    "2020-2021年度第三隊：Rudy Gobert\nJimmy Butler\nPaul George\nBradley Beal\nKyrie Irving\n"
    "2019-2020年度第三隊：Jimmy Butler\nJayson Tatum\nRudy Gobert\nBen Simmons\nRussell Westbrook\n"
    "2018-2019年度第三隊：Russell Westbrook\nKemba Walker\nBlake Griffin\nLeBron James\nRudy Gobert\n"
]

年度第3隊 = [
    "2023-2024年度第三隊：LeBron James\nStephen Curry\nDomantas Sabonis\nTyrese Haliburton\nDevin Booker\n"
    "2022-2023年度第三隊：LeBron James\nJulius Randle\nDomantas Sabonis\nDe'Aaron Fox\nDamian Lillard\n"
    "2021-2022年度第三隊：Chirs Paul\nTrae Young\nLeBron James\nPascal Siakam\nKarl-Anthony Towns\n"
    "2020-2021年度第三隊：Rudy Gobert\nJimmy Butler\nPaul George\nBradley Beal\nKyrie Irving\n"
    "2019-2020年度第三隊：Jimmy Butler\nJayson Tatum\nRudy Gobert\nBen Simmons\nRussell Westbrook\n"
    "2018-2019年度第三隊：Russell Westbrook\nKemba Walker\nBlake Griffin\nLeBron James\nRudy Gobert\n"
]


巫師陣容 = [
    "Bilal Coulibaly - Guard\nChase Audige - Player\nJohnny Davis - Guard\nTyus Jones - Guard\nPatrick Baldwin - Forward\nDeni Avdija - Forward\n"
    "Ryan Rollins - Guard\nXavier Cooks - Forward\nJordan Poole - Guard\nJared Butler - Guard\nAnthony Gill - Forward\nLandry Shamet - Guard\n"
    "Daniel Gafford - Forward-Center\nCorey Kispert - Forward\nJules Bernard - Guard\nKyle Kuzma - Forward\nMike Muscala - Forward-Center\n"
    "Delon Wright - Guard\nTaj Gibson - Forward\nDanilo Gallinari - Forward\nEugene Omoruyi - Forward"
]

黃蜂陣容 = [
    "Nathan Mensah - Center\nBrandon Miller - Forward\nNick Smith Jr. - Guard\nAmari Bailey - Guard\nLeaky Black - Forward\nMiles Bridges - Forward\n"
    "LaMelo Ball - Guard\nJames Bouknight - Guard\nTerry Rozier - Guard\nNick Richards - Center\nEdmond Sumner - Guard\nMark Williams - Center\nBryce McGowens - Guard\n"
    "Theo Maledon - Guard\nCody Martin - Forward\nGordon Hayward - Forward\nFrank Ntilikina - Guard\nJT Thor - Forward\nKai Jones - Center-Forward\nP.J. Washington - Forward\nRJ Hunter - Guard"
]

老鷹陣容 = [
    "Miles Norris - Forward\nKobe Bufkin - Guard\nSeth Lundy - Guard\nMouhamed Gueye - Forward\nJarkell Joiner - Player\nKeaton Wallace - Guard\nBruno Fernando - Forward-Center\n"
    "Jalen Johnson - Forward\nTrent Forrest - Guard\nDejounte Murray - Guard\nPatty Mills - Guard\nTrae Young - Guard\nDe'Andre Hunter - Forward-Guard\n"
    "Bogdan Bogdanovic - Guard\nAJ Griffin - Forward\nClint Capela - Center\nOnyeka Okongwu - Forward-Center\nWesley Matthews - Guard\nGarrison Mathews - Guard\nSaddiq Bey - Forward"
]

熱火陣容 = [
    "Bam Adebayo - Center-Forward\nThomas Bryant - Center\nJimmy Butler - Forward\nTyler Herro - Guard\nKyle Lowry - Guard\nNikola Jović - Forward\n"
    "Kevin Love - Forward\nCaleb Martin - Forward\nDrew Peterson - Forward\nJosh Richardson - Guard\nDuncan Robinson - Forward\n"
    "Orlando Robinson - Center\nDru Smith - Guard\nCole Swider - Forward\nAlondes Williams - Guard"
]

魔術陣容 = [
    "Anthony Black - Guard\nJonathan Isaac - Forward\nCaleb Houstan - Guard\nChuma Okeke - Forward\nJalen Suggs - Guard\nPaolo Banchero - Forward\nJoe Ingles - Forward-Guard\n"
    "Brandon Williams - Guard\nKevon Harris - Guard\nD.J. Wilson - Forward\nMac McClung - Guard\nTrevelin Queen - Guard\nJett Howard - Guard\nGary Harris - Guard\n"
    "Markelle Fultz - Guard\nMoritz Wagner - Forward-Center\nFranz Wagner - Forward\nAdmiral Schofield - Forward\nWendell Carter Jr. - Center-Forward\nGoga Bitadze - Center-Forward\nCole Anthony - Guard"
]

尼克陣容 = [
    "Jaylen Martin - Guard\nJacob Toppin - Forward\nDonte DiVincenzo - Guard\nMiles McBride - Guard\nJosh Hart - Guard\nDuane Washington Jr. - Guard\nImmanuel Quickley - Guard\n"
    "Quentin Grimes - Guard\nDaQuan Jeffries - Guard-Forward\nRJ Barrett - Forward-Guard\nDylan Windler - Guard-Forward\nJalen Brunson - Guard\nEvan Fournier - Guard-Forward\nNathan Knight - Forward-Center\n"
    "Charlie Brown Jr. - Guard\nIsaiah Roby - Forward\nMitchell Robinson - Center-Forward\nJulius Randle - Forward-Center\nJericho Sims - Center\nRyan Arcidiacono - Guard\nIsaiah Hartenstein - Center-Forward"
]

七六人陣容 = [
    "Tyrese Maxey - Guard\nJames Harden - Guard\nMontrezl Harrell - Forward-Center\nMo Bamba - Center\nDe'Anthony Melton - Guard\nKelly Oubre Jr. - Forward-Guard\nJaden Springer - Guard\n"
    "Tobias Harris - Forward\nDanny Green - Guard\nRicky Council IV - Guard\nP.J. Tucker - Forward\nAzuolas Tubelis - Forward\nJoel Embiid - Center-Forward\nPatrick Beverley - Guard\n"
    "Terquavion Smith - Guard\nDanuel House Jr. - Forward-Guard\nDavid Duke Jr. - Guard\nFurkan Korkmaz - Guard-Forward\nFilip Petrusev - Center\nJavonte Smart - Guard\nPaul Reed - Forward"
]

籃網陣容 = [
    "Royce O'Neale - Forward\nDariq Whitehead - Forward\nMikal Bridges - Guard-Forward\nCameron Johnson - Forward\nDennis Smith Jr. - Guard\nDarius Bazley - Forward\nLonnie Walker IV - Guard-Forward\n"
    "Trendon Watford - Forward\nBen Simmons - Guard-Forward\nArmoni Brooks - Guard\nHarry Giles III - Forward-Center\nDay'Ron Sharpe - Center\nNoah Clowney - Forward\n"
    "Jalen Wilson - Forward\nCam Thomas - Guard\nSpencer Dinwiddie - Guard\nDorian Finney-Smith - Forward\nNic Claxton - Center"
]

塞爾提克陣容 = [
    "Dalano Banton - Forward\nOshae Brissett - Forward-Guard\nJaylen Brown - Guard-Forward\nJD Davison - Guard\nSam Hauser - Forward\nJrue Holiday - Guard\nAl Horford - Center-Forward\n"
    "Luke Kornet - Center-Forward\nSvi Mykhailiuk - Guard-Forward\nKristaps Porzingis - Forward-Center\nPayton Pritchard - Guard\nNeemias Queta - Center\n"
    "Jay Scrubb - Guard\nLamar Stevens - Forward\nDJ Steward - Guard\nJayson Tatum - Forward-Guard\nJordan Walsh - Guard\nDerrick White - Guard"
]

暴龍陣容 = [
    "Makur Maker - Center\nJavon Freeman-Liberty - Guard\nGradey Dick - Guard\nJalen McDaniels - Forward-Center\nO.G. Anunoby - Forward\nScottie Barnes - Forward\nPrecious Achiuwa - Forward\n"
    "Ron Harper Jr. - Forward\nGarrett Temple - Guard-Forward\nMouhamadou Gueye - Forward\nDennis Schroder - Guard\nJakob Poeltl - Center\nJeff Dowtin Jr. - Guard\nThaddeus Young - Forward\n"
    "Malachi Flynn - Guard\nMarkquis Nowell - Guard\nChris Boucher - Forward-Center\nOtto Porter Jr. - Forward\nGary Trent Jr. - Guard-Forward\nChristian Koloko - Center\nPascal Siakam - Forward"
]

公牛陣容 = [
    "Henri Drell - Forward\nAdama Sanogo - Forward\nMax Heidegger - Guard\nOnuralp Bitim - Forward\nJulian Phillips - Forward\nCoby White - Guard\nTorrey Craig - Forward\n"
    "Lonzo Ball - Guard\nAndre Drummond - Center\nJevon Carter - Guard\nAlex Caruso - Guard\nZach LaVine - Guard\nNikola Vucevic - Center\n"
    "DeMar DeRozan - Guard-Forward\nAyo Dosunmu - Guard\nCarlik Jones - Guard\nDalen Terry - Forward\nQuenton Jackson - Guard\nTerry Taylor - Forward\nJustin Lewis - Forward\nPatrick Williams - Forward"
]

騎士陣容 = [
    "Pete Nance - Forward\nJustin Powell - Guard\nMax Strus - Guard-Forward\nSharife Cooper - Guard\nTy Jerome - Guard-Forward\nCaris LeVert - Guard\nEvan Mobley - Center\n"
    "Zhaire Smith - Guard\nSam Merrill - Guard\nTristan Thompson - Center-Forward\nDarius Garland - Guard\nRicky Rubio - Guard\nIsaiah Mobley - Forward\n"
    "Georges Niang - Forward\nEmoni Bates - Forward\nDamian Jones - Center\nJarrett Allen - Center\nDean Wade - Forward-Center\nIsaac Okoro - Forward-Guard\nCraig Porter - Guard\nDonovan Mitchell - Guard"
]

溜馬陣容 = [
    "Tyrese Haliburton - Guard\nBennedict Mathurin - Guard-Forward\nObi Toppin - Forward\nAndrew Nembhard - Guard-Forward\nJarace Walker - Forward\nBuddy Hield - Guard\nT.J. McConnell - Guard\nKendall Brown - Guard\n"
    "Bruce Brown - Guard-Forward\nJordan Nwora - Forward\nIsaiah Wong - Guard\nIsaiah Jackson - Forward\nAaron Nesmith - Guard-Forward\nJalen Smith - Forward-Center\n"
    "Ben Sheppard - Guard\nDaniel Theis - Forward-Center\nMyles Turner - Center-Forward\nOscar Tshiebwe - Forward-Center"
]

活塞陣容 = [
    "Tosan Evbuomwan - Forward\nAusar Thompson - Guard-Forward\nMarcus Sasser - Guard\nMalcolm Cazalon - Guard\nJalen Duren - Center\nCade Cunningham - Guard\nJontay Porter - Center-Forward\n"
    "Monte Morris - Guard\nKillian Hayes - Guard\nJared Rhoden - Guard\nZavier Simpson - Guard\nIsaiah Livers - Forward\nJames Wiseman - Center\nAlec Burks - Guard\nStanley Umude - Guard\n"
    "Jaden Ivey - Guard\nBuddy Boeheim - Forward\nIsaiah Stewart - Forward-Center\nJoe Harris - Guard-Forward\nMarvin Bagley III - Forward\nBojan Bogdanovic - Forward"
]

公鹿陣容 = [
    "Omari Moore - Guard\nJazian Gortman - Guard\nDrew Timme - Forward\nTyTy Washington Jr. - Guard\nMarJon Beauchamp - Forward\nDamian Lillard - Guard\nMalik Beasley - Guard\nChris Livingston - Forward\nBobby Portis - Forward\n"
    "Brook Lopez - Center\nMarques Bolden - Center\nCameron Payne - Guard\nAJ Green - Guard\nKhris Middleton - Forward\nPat Connaughton - Guard\nLindell Wigginton - Guard\n"
    "Robin Lopez - Center\nGiannis Antetokounmpo - Forward\nThanasis Antetokounmpo - Forward\nAndre Jackson Jr. - Guard\nJae Crowder - Forward"
]

灰狼陣容 = [
    "Jaylen Clark - Guard\nLeonard Miller - Forward\nAnthony Edwards - Guard\nTrevor Keels - Guard\nJaden McDaniels - Forward\nKyle Anderson - Forward-Guard\nJordan McLaughlin - Guard\nWendell Moore Jr. - Guard\n"
    "Troy Brown Jr. - Guard-Forward\nJosh Minott - Forward\nNickeil Alexander-Walker - Guard\nMike Conley - Guard\nNaz Reid - Center-Forward\nDaishen Nix - Guard\n"
    "Shake Milton - Guard-Forward\nTyrese Martin - Guard\nVit Krejci - Guard\nRudy Gobert - Center\nKarl-Anthony Towns - Center-Forward\nMatt Ryan - Forward\nLuka Garza - Center"
]

爵士陣容 = [
    "Jordan Clarkson - Guard\nTaylor Hendricks - Forward\nCollin Sexton - Guard\nKeyonte George - Guard\nTalen Horton-Tucker - Guard\nBrice Sensabaugh - Forward\nJoey Hauser - Forward\nKris Dunn - Guard\n"
    "Romeo Langford - Guard-Forward\nSimone Fontecchio - Forward\nLuka Samanic - Forward\nJohn Collins - Forward-Center\nTaevion Kinsey - Guard\nLauri Markkanen - Forward-Center\n"
    "Walker Kessler - Center\nMicah Potter - Center\nOchai Agbaji - Guard\nJohnny Juzang - Guard\nNick Ongenda - Center\nKelly Olynyk - Forward-Center\nOmer Yurtseven - Center"
]

去年賽季戰績 = [ 
          "東區排名#1\n""公鹿:58勝-24負\n""勝率:.707\n""分區:35勝-17負\n""主場:32勝-9負\n""客場:26勝-15負\n""------------------\n"
          "東區排名#2\n""塞爾提克:57勝-25負\n""勝率:.695\n""分區:34勝-18負\n""主場:32勝-9負\n""客場:25勝-16負\n""------------------\n"
          "東區排名#3\n""76人:54勝-28負\n""勝率:.659\n""分區:34勝-18負\n""主場:29勝-12負\n""客場:25勝-16負\n""------------------\n"
          "東區排名#4\n""騎士:51勝-31負\n""勝率:.622\n""分區:34勝-18負\n""主場:31勝-10負\n""客場:20勝-21負\n""------------------\n"
          "東區排名#5\n""尼克:47勝-35負\n""勝率:.573\n""分區:32勝-20負\n""主場:23勝-18負\n""客場:24勝-17負\n""------------------\n"
          "東區排名#6\n""籃網:45勝-37負\n""勝率:.549\n""分區:30勝-22負\n""主場:23勝-18負\n""客場:22勝-19負\n""------------------\n"
          "東區排名#7\n""老鷹:41勝-41負\n""勝率:.500\n""分區:26勝-26負\n""主場:24勝-17負\n""客場:17勝-24負\n""------------------\n"
          "東區排名#8\n""熱火:44勝-38負\n""勝率:.537\n""分區:24勝-28負\n""主場:27勝-14負\n""客場:17勝-24負\n""------------------\n"
          "東區排名#9\n""暴龍:41勝-41負\n""勝率:.500\n""分區:26勝-26負\n""主場:27勝-14負\n""客場:14勝-27負\n""------------------\n"
          "東區排名#10\n""公牛:40勝-42負\n""勝率:.488\n""分區:27勝-25負\n""主場:22勝-19負\n""客場:18勝-23負\n""------------------\n"
          "東區排名#11\n""溜馬:35勝-47負\n""勝率:.427\n""分區:24勝-28負\n""主場:20勝-21負\n""客場:15勝-26負\n""------------------\n"
          "東區排名#12\n""巫師:35勝-47負\n""勝率:.427\n""分區:21勝-31負\n""主場:19勝-22負\n""客場:16勝-25負\n""------------------\n"
          "東區排名#13\n""魔術:34勝-48負\n""勝率:.415\n""分區:20勝-32負\n""主場:20勝-21負\n""客場:14勝-27負\n""------------------\n"
          "東區排名#14\n""黃蜂:27勝-55負\n""勝率:.329\n""分區:15勝-37負\n""主場:13勝-28負\n""客場:14勝-27負\n""------------------\n"
          "東區排名#15\n""活塞:17勝-65負\n""勝率:.207\n""分區:8勝-44負\n""主場:9勝-32負\n""客場:8勝-33負\n""------------------\n"
          "西區排名#1\n""金塊:53勝-29負\n""勝率:.646\n""分區:34勝-18負\n""主場:34勝-7負\n""客場:19勝-22負\n""------------------\n"
          "西區排名#2\n""灰熊:51勝-31負\n""勝率:.622\n""分區:30勝-22負\n""主場:35勝-6負\n""客場:16勝-25負\n""------------------\n"
          "西區排名#3\n""國王:48勝-34負\n""勝率:.585\n""分區:32勝-20負\n""主場:23勝-18負\n""客場:25勝-16負\n""------------------\n"
          "西區排名#4\n""太陽:45勝-37負\n""勝率:.549\n""分區:30勝-22負\n""主場:28勝-13負\n""客場:17勝-24負\n""------------------\n"
          "西區排名#5\n""快艇:44勝-38負\n""勝率:.537\n""分區:27勝-25負\n""主場:23勝-18負\n""客場:21勝-20負\n""------------------\n"
          "西區排名#6\n""勇士:44勝-38負\n""勝率:.537\n""分區:30勝-22負\n""主場:33勝-8負\n""客場:11勝-30負\n""------------------\n"
          "西區排名#7\n""湖人:43勝-39負\n""勝率:.524\n""分區:27勝-25負\n""主場:23勝-18負\n""客場:20勝-21負\n""------------------\n"
          "西區排名#8\n""灰狼:42勝-40負\n""勝率:.512\n""分區:29勝-23負\n""主場:22勝-19負\n""客場:20勝-21負\n""------------------\n"
          "西區排名#9\n""鵜鶘:42勝-40負\n""勝率:.512\n""分區:29勝-23負\n""主場:27勝-14負\n""客場:15勝-26負\n""------------------\n"
          "西區排名#10\n""雷霆:40勝-42負\n""勝率:.488\n""分區:25勝-27負\n""主場:24勝-17負\n""客場:16勝-25負\n""------------------\n"
          "西區排名#11\n""獨行俠:38勝-44負\n""勝率:.463\n""分區:28勝-24負\n""主場:23勝-18負\n""客場:15勝-26負\n""------------------\n"
          "西區排名#12\n""爵士:37勝-45負\n""勝率:.451\n""分區:24勝-28負\n""主場:23勝-18負\n""客場:14勝-27負\n""------------------\n"
          "西區排名#13\n""拓荒者:33勝-49負\n""勝率:.402\n""分區:23勝-29負\n""主場:17勝-24負\n""客場:16勝-25負\n""------------------\n"
          "西區排名#14\n""火箭:22勝-60負\n""勝率:.268\n""分區:12勝-40負\n""主場:14勝-27負\n""客場:8勝-33負\n""------------------\n"
          "西區排名#15\n""馬刺:22勝-60負\n""勝率:.268\n""分區:10勝-42負\n""主場:14勝-27負\n""客場:8勝-33負\n""------------------\n"
]         

公鹿去年排名=[
          "東區排名#1\n""公鹿:58勝-24負\n""勝率:.707\n""分區:35勝-17負\n""主場:32勝-9負\n""客場:26勝-15負\n""------------------\n"]
塞爾提克去年排名=[
          "東區排名#2\n""塞爾提克:57勝-25負\n""勝率:.695\n""分區:34勝-18負\n""主場:32勝-9負\n""客場:25勝-16負\n""------------------\n"]
七六人去年排名=[
    "東區排名#3\n""76人:54勝-28負\n""勝率:.659\n""分區:34勝-18負\n""主場:29勝-12負\n""客場:25勝-16負\n""------------------\n"]
騎士去年排名=[
          "東區排名#4\n""騎士:51勝-31負\n""勝率:.622\n""分區:34勝-18負\n""主場:31勝-10負\n""客場:20勝-21負\n""------------------\n"]
尼克去年排名=[
          "東區排名#5\n""尼克:47勝-35負\n""勝率:.573\n""分區:32勝-20負\n""主場:23勝-18負\n""客場:24勝-17負\n""------------------\n"]
籃網去年排名=[
          "東區排名#6\n""籃網:45勝-37負\n""勝率:.549\n""分區:30勝-22負\n""主場:23勝-18負\n""客場:22勝-19負\n""------------------\n"]
老鷹去年排名=[
          "東區排名#7\n""老鷹:41勝-41負\n""勝率:.500\n""分區:26勝-26負\n""主場:24勝-17負\n""客場:17勝-24負\n""------------------\n"]
熱火去年排名=[
          "東區排名#8\n""熱火:44勝-38負\n""勝率:.537\n""分區:24勝-28負\n""主場:27勝-14負\n""客場:17勝-24負\n""------------------\n"]
暴龍去年排名=[
          "東區排名#9\n""暴龍:41勝-41負\n""勝率:.500\n""分區:26勝-26負\n""主場:27勝-14負\n""客場:14勝-27負\n""------------------\n"]
公牛去年排名=[
          "東區排名#10\n""公牛:40勝-42負\n""勝率:.488\n""分區:27勝-25負\n""主場:22勝-19負\n""客場:18勝-23負\n""------------------\n"]
溜馬去年排名=[
          "東區排名#11\n""溜馬:35勝-47負\n""勝率:.427\n""分區:24勝-28負\n""主場:20勝-21負\n""客場:15勝-26負\n""------------------\n"]
巫師去年排名=[
          "東區排名#12\n""巫師:35勝-47負\n""勝率:.427\n""分區:21勝-31負\n""主場:19勝-22負\n""客場:16勝-25負\n""------------------\n"]
魔術去年排名=[
          "東區排名#13\n""魔術:34勝-48負\n""勝率:.415\n""分區:20勝-32負\n""主場:20勝-21負\n""客場:14勝-27負\n""------------------\n"]
黃蜂去年排名=[
          "東區排名#14\n""黃蜂:27勝-55負\n""勝率:.329\n""分區:15勝-37負\n""主場:13勝-28負\n""客場:14勝-27負\n""------------------\n"]
活塞去年排名=[
          "東區排名#15\n""活塞:17勝-65負\n""勝率:.207\n""分區:8勝-44負\n""主場:9勝-32負\n""客場:8勝-33負\n""------------------\n"]
金塊去年排名=[
          "西區排名#1\n""金塊:53勝-29負\n""勝率:.646\n""分區:34勝-18負\n""主場:34勝-7負\n""客場:19勝-22負\n""------------------\n"]
灰熊去年排名=[
          "西區排名#2\n""灰熊:51勝-31負\n""勝率:.622\n""分區:30勝-22負\n""主場:35勝-6負\n""客場:16勝-25負\n""------------------\n"]
國王去年排名=[
          "西區排名#3\n""國王:48勝-34負\n""勝率:.585\n""分區:32勝-20負\n""主場:23勝-18負\n""客場:25勝-16負\n""------------------\n"]
太陽去年排名=[
          "西區排名#4\n""太陽:45勝-37負\n""勝率:.549\n""分區:30勝-22負\n""主場:28勝-13負\n""客場:17勝-24負\n""------------------\n"]
快艇去年排名=[
          "西區排名#5\n""快艇:44勝-38負\n""勝率:.537\n""分區:27勝-25負\n""主場:23勝-18負\n""客場:21勝-20負\n""------------------\n"]
勇士去年排名=[
          "西區排名#6\n""勇士:44勝-38負\n""勝率:.537\n""分區:30勝-22負\n""主場:33勝-8負\n""客場:11勝-30負\n""------------------\n"]
湖人去年排名=[
          "西區排名#7\n""湖人:43勝-39負\n""勝率:.524\n""分區:27勝-25負\n""主場:23勝-18負\n""客場:20勝-21負\n""------------------\n"]
灰狼去年排名=[
          "西區排名#8\n""灰狼:42勝-40負\n""勝率:.512\n""分區:29勝-23負\n""主場:22勝-19負\n""客場:20勝-21負\n""------------------\n"]
鵜鶘去年排名=[
          "西區排名#9\n""鵜鶘:42勝-40負\n""勝率:.512\n""分區:29勝-23負\n""主場:27勝-14負\n""客場:15勝-26負\n""------------------\n"]
雷霆去年排名=[
          "西區排名#10\n""雷霆:40勝-42負\n""勝率:.488\n""分區:25勝-27負\n""主場:24勝-17負\n""客場:16勝-25負\n""------------------\n"]
獨行俠去年排名=[
          "西區排名#11\n""獨行俠:38勝-44負\n""勝率:.463\n""分區:28勝-24負\n""主場:23勝-18負\n""客場:15勝-26負\n""------------------\n"]
爵士去年排名=[
          "西區排名#12\n""爵士:37勝-45負\n""勝率:.451\n""分區:24勝-28負\n""主場:23勝-18負\n""客場:14勝-27負\n""------------------\n"]
拓荒者去年排名=[
          "西區排名#13\n""拓荒者:33勝-49負\n""勝率:.402\n""分區:23勝-29負\n""主場:17勝-24負\n""客場:16勝-25負\n""------------------\n"]
火箭去年排名=[
          "西區排名#14\n""火箭:22勝-60負\n""勝率:.268\n""分區:12勝-40負\n""主場:14勝-27負\n""客場:8勝-33負\n""------------------\n"]
馬刺去年排名=[
          "西區排名#15\n""馬刺:22勝-60負\n""勝率:.268\n""分區:10勝-42負\n""主場:14勝-27負\n""客場:8勝-33負\n""------------------\n"]
公鹿去年戰績=[
          "東區排名#1\n""公鹿:58勝-24負\n""勝率:.707\n""分區:35勝-17負\n""主場:32勝-9負\n""客場:26勝-15負\n""------------------\n"]
塞爾提克去年戰績=[
          "東區排名#2\n""塞爾提克:57勝-25負\n""勝率:.695\n""分區:34勝-18負\n""主場:32勝-9負\n""客場:25勝-16負\n""------------------\n"]
七六人去年戰績=[
    "東區排名#3\n""76人:54勝-28負\n""勝率:.659\n""分區:34勝-18負\n""主場:29勝-12負\n""客場:25勝-16負\n""------------------\n"]
騎士去年戰績=[
          "東區排名#4\n""騎士:51勝-31負\n""勝率:.622\n""分區:34勝-18負\n""主場:31勝-10負\n""客場:20勝-21負\n""------------------\n"]
尼克去年戰績=[
          "東區排名#5\n""尼克:47勝-35負\n""勝率:.573\n""分區:32勝-20負\n""主場:23勝-18負\n""客場:24勝-17負\n""------------------\n"]
籃網去年戰績=[
          "東區排名#6\n""籃網:45勝-37負\n""勝率:.549\n""分區:30勝-22負\n""主場:23勝-18負\n""客場:22勝-19負\n""------------------\n"]
老鷹去年戰績=[
          "東區排名#7\n""老鷹:41勝-41負\n""勝率:.500\n""分區:26勝-26負\n""主場:24勝-17負\n""客場:17勝-24負\n""------------------\n"]
熱火去年戰績=[
          "東區排名#8\n""熱火:44勝-38負\n""勝率:.537\n""分區:24勝-28負\n""主場:27勝-14負\n""客場:17勝-24負\n""------------------\n"]
暴龍去年戰績=[
          "東區排名#9\n""暴龍:41勝-41負\n""勝率:.500\n""分區:26勝-26負\n""主場:27勝-14負\n""客場:14勝-27負\n""------------------\n"]
公牛去年戰績=[
          "東區排名#10\n""公牛:40勝-42負\n""勝率:.488\n""分區:27勝-25負\n""主場:22勝-19負\n""客場:18勝-23負\n""------------------\n"]
溜馬去年戰績=[
          "東區排名#11\n""溜馬:35勝-47負\n""勝率:.427\n""分區:24勝-28負\n""主場:20勝-21負\n""客場:15勝-26負\n""------------------\n"]
巫師去年戰績=[
          "東區排名#12\n""巫師:35勝-47負\n""勝率:.427\n""分區:21勝-31負\n""主場:19勝-22負\n""客場:16勝-25負\n""------------------\n"]
魔術去年戰績=[
          "東區排名#13\n""魔術:34勝-48負\n""勝率:.415\n""分區:20勝-32負\n""主場:20勝-21負\n""客場:14勝-27負\n""------------------\n"]
黃蜂去年戰績=[
          "東區排名#14\n""黃蜂:27勝-55負\n""勝率:.329\n""分區:15勝-37負\n""主場:13勝-28負\n""客場:14勝-27負\n""------------------\n"]
活塞去年戰績=[
          "東區排名#15\n""活塞:17勝-65負\n""勝率:.207\n""分區:8勝-44負\n""主場:9勝-32負\n""客場:8勝-33負\n""------------------\n"]
金塊去年戰績=[
          "西區排名#1\n""金塊:53勝-29負\n""勝率:.646\n""分區:34勝-18負\n""主場:34勝-7負\n""客場:19勝-22負\n""------------------\n"]
灰熊去年戰績=[
          "西區排名#2\n""灰熊:51勝-31負\n""勝率:.622\n""分區:30勝-22負\n""主場:35勝-6負\n""客場:16勝-25負\n""------------------\n"]
國王去年戰績=[
          "西區排名#3\n""國王:48勝-34負\n""勝率:.585\n""分區:32勝-20負\n""主場:23勝-18負\n""客場:25勝-16負\n""------------------\n"]
太陽去年戰績=[
          "西區排名#4\n""太陽:45勝-37負\n""勝率:.549\n""分區:30勝-22負\n""主場:28勝-13負\n""客場:17勝-24負\n""------------------\n"]
快艇去年戰績=[
          "西區排名#5\n""快艇:44勝-38負\n""勝率:.537\n""分區:27勝-25負\n""主場:23勝-18負\n""客場:21勝-20負\n""------------------\n"]
勇士去年戰績=[
          "西區排名#6\n""勇士:44勝-38負\n""勝率:.537\n""分區:30勝-22負\n""主場:33勝-8負\n""客場:11勝-30負\n""------------------\n"]
湖人去年戰績=[
          "西區排名#7\n""湖人:43勝-39負\n""勝率:.524\n""分區:27勝-25負\n""主場:23勝-18負\n""客場:20勝-21負\n""------------------\n"]
灰狼去年戰績=[
          "西區排名#8\n""灰狼:42勝-40負\n""勝率:.512\n""分區:29勝-23負\n""主場:22勝-19負\n""客場:20勝-21負\n""------------------\n"]
鵜鶘去年戰績=[
          "西區排名#9\n""鵜鶘:42勝-40負\n""勝率:.512\n""分區:29勝-23負\n""主場:27勝-14負\n""客場:15勝-26負\n""------------------\n"]
雷霆去年戰績=[
          "西區排名#10\n""雷霆:40勝-42負\n""勝率:.488\n""分區:25勝-27負\n""主場:24勝-17負\n""客場:16勝-25負\n""------------------\n"]
獨行俠去年戰績=[
          "西區排名#11\n""獨行俠:38勝-44負\n""勝率:.463\n""分區:28勝-24負\n""主場:23勝-18負\n""客場:15勝-26負\n""------------------\n"]
爵士去年戰績=[
          "西區排名#12\n""爵士:37勝-45負\n""勝率:.451\n""分區:24勝-28負\n""主場:23勝-18負\n""客場:14勝-27負\n""------------------\n"]
拓荒者去年戰績=[
          "西區排名#13\n""拓荒者:33勝-49負\n""勝率:.402\n""分區:23勝-29負\n""主場:17勝-24負\n""客場:16勝-25負\n""------------------\n"]
火箭去年戰績=[
          "西區排名#14\n""火箭:22勝-60負\n""勝率:.268\n""分區:12勝-40負\n""主場:14勝-27負\n""客場:8勝-33負\n""------------------\n"]
馬刺去年戰績=[
          "西區排名#15\n""馬刺:22勝-60負\n""勝率:.268\n""分區:10勝-42負\n""主場:14勝-27負\n""客場:8勝-33負\n""------------------\n"]

巫師補強建議 = ["現有陣容的考量：\n巫師的表現在上季可能令不少球迷失望，四位主將已合作五季，但仍未能進入東區冠軍賽。下季將是中鋒Marcin Gortat的合約年，這意味著現有陣容最多只有一年的合作機會。若下季成績仍未有顯著提升，球團可能會考慮重組正選陣容。\n"
                "球員合約與續約：\n後備中鋒Jason Smith的表現不佳，而Jodie Meeks的上場時間也減少，他們的未來在球隊中仍是未知數。而輪換大前鋒Mike Scott的表現出色，但由於薪資空間限制，巫師可能只能提供稅後中產合約。\n"
                "交易與清人：\n後備中鋒Ian Mahinmi的表現不如預期，且其薪資相對較高，建議球團考慮將Kelly Oubre和Ian Mahinmi一同交易，以換取薪資空間和其他球員。\n"
                "新球員的考慮：\n太陽的中鋒Alex Len可能是一個不錯的選擇。他的表現不錯，但在太陽的地位不穩，巫師可以考慮用選秀權和Ian Mahinmi交易Alex Len。\n"
                "未來展望：\n若巫師在下季仍未能成功進入東區冠軍賽，球團可能會考慮打散現有陣容重新組建。\n"
                "希望主將John Wall能夠回復至上季的狀態，帶領球隊走得更遠。"]

黃蜂補強建議 = ["球員動態與合約：\n黄蜂隊已裁掉中鋒卡伊-琼斯。布克奈特成功接受了左膝手術，預計四周後重新評估。此外，卡伊-琼斯在社交媒體上宣布已向球隊申請交易。\n"
                "中鋒位置補強：\n考慮到卡伊-琼斯的交易申請和球隊已裁掉他的消息，黄蜂隊可能需要在中鋒位置上進行補強。\n"
                "外線進攻與防守加強：\n考慮球隊的戰績和現有陣容，黄蜂隊可能需要在外線進攻和防守上進行加強。\n"
                "未來展望：\n黄蜂隊應該考慮短期內找到一名能夠替代布克奈特的球員，並且考慮在中鋒和外線位置上的補強，以提高球隊的整體競爭力。"]

老鷹補強建議 = ["球員動態與合約：\n特雷-杨在近期比賽中表現出色，並在對鹈鹕的比賽中獲得15分5助攻的成績。此外，老鷹隊在2023年8月裁掉了捷克後衛維特-克雷伊奇。\n"
                "後場補強：\n考慮到老鷹隊近期裁掉了後衛維特-克雷伊奇，球隊可能需要在後場位置上進行補強，尤其是在後衛位置上。\n"
                "內線防守加強：\n老鷹隊在內線防守上有所不足，建議球隊在交易市場上尋找一名能夠提供內線防守支援的球員。\n"
                "年輕球員的培養：\n老鷹隊擁有一些有潛力的年輕球員，球隊應該加大對這些球員的培養力度，以確保球隊的未來發展。"]

熱火補強建議 = ["近期戰績考量：\n熱火隊在2022-23賽季表現出色，成功進入NBA總決賽，但在五場比賽中被丹佛金塊隊擊敗。儘管如此，他們在季後賽中展現了強大的實力和韌性。\n"
                "球員動態與合約：\n王牌球員Jimmy Butler在季後賽中的狀態明顯不如前幾輪，但熱火仍靠著角色球員的出色發揮，成功晉級東區冠軍賽。\n"
                "後場補強：\n考慮到Jimmy Butler的狀態波動，熱火隊可能需要在後場位置上進行補強，尤其是在得分後衛位置上。\n"
                "內線防守加強：\n雖然熱火隊在季後賽中展現了不錯的內線實力，但在總決賽中被金塊隊打壓，建議球隊在內線防守上進行加強。\n"
                "年輕球員的培養：\n熱火隊擁有一些有潛力的年輕球員，球隊應該加大對這些球員的培養力度，以確保球隊的未來發展。"]

魔術補強建議 = ["近期戰績考量：\n魔術隊從上季的谷底慢慢爬起，本季依然充滿了年輕潛力和不確定性。球隊的目標是「Level Up」，希望能夠在這季展現出更有競爭力的內容，並且戰績必須要有爆發性的成長。\n"
                "球員動態與合約：\n上季魔術隊的進攻可以說是一團混亂，全隊的進攻效率在聯盟墊底。新秀Jalen Suggs的投籃表現不佳，而Markelle Fultz的效率相當驚人。此外，Wendell Carter和新人前鋒Franz Wagner在前場的表現都相當出色。\n"
                "後場補強：\n魔術隊的後場擋拆和playmaking能力較弱，需要加強。Suggs和Fultz兩位後衛的搭配還需要時間磨合，但如果兩人能夠搭檔雙控球，可能能夠解決playmaking的問題。\n"
                "前場補強：\n魔術隊的前場有Wendell Carter和Franz Wagner兩位年輕球員，他們都已經展現出作為戰術核心的價值。但球隊還需要更多的前場球員來提供支援。\n"
                "年輕球員的培養：\n魔術隊有很多年輕球員，如Jalen Suggs、Markelle Fultz和Franz Wagner等。球隊應該加大對這些球員的培養力度，以確保球隊的未來發展。"]

尼克補強建議 = ["近期戰績考量：\n上賽季紐約尼克完成了更上一層樓的成就，自2012-13賽季之後再次重返東區聯盟季後賽第二輪的舞台，表現備受人們的認可。新賽季的戰術主軸肯定會比上賽季來得更加清晰，只是可以提升到怎麼樣的高度，這是尼克新賽季最大的考題。\n"
                "球員動態與合約：\n新指揮官Jalen Brunson打出了自己可擔當球隊王牌的身價，證明他離開達拉斯小牛是正確的選擇，也把尼克重新凝聚起來。總教練Tom Thibodeau總算將尼克整頓一番，找到了勝利的方程式。\n"
                "後場補強：\n尼克新賽季的主力陣容變化不大，重要的補強來說是補進了Brunson和Josh Hart的大學隊友Donte DiVincenzo以及控衛Ryan Arcidiacono。Arcidiacono可以填上Derrick Rose離開之後的替補控衛的位置，而DiVincenzo攻守兼具，有著紮實的基本功。\n"
                "前場補強：\nJulius Randle在新賽季注定成為尼克對手們會針對性防守的目標。他在上賽季繳出平均19.6分、5籃板、2.8助攻和0.4搶斷的表現，並且有著43.4%命中率、31%三分命中率和74%罰球命中率。\n"
                "內線補強：\nMitchell Robinson在進攻籃板率的統治力，首當其衝的受害者就是克里夫蘭騎士。他能夠繼續保持擎天柱的表現，新賽季依舊是敵隊高塔無法克服的問題。"]

七六人補強建議 = ["近期戰績考量：\n七六人隊在上賽季展現了不俗的實力，但在季後賽中未能達到預期的成果。新賽季的目標是進一步提升球隊的整體實力，並在季後賽中取得更好的成績。\n"
                "球員動態與合約：\n七六人的MVP恩比德（Joel Embiid）在社群媒體上表示，這個休賽季將會非常有趣。此外，七六人今年夏天捲入了哈登（James Harden）的「賣我」風波中，並傳出哈登指明要去洛杉磯快艇打球。\n"
                "後場補強：\n考慮到哈登的交易風波，七六人可能需要在後場位置上進行補強，尤其是在得分後衛位置上。\n"
                "前場補強：\n雖然恩比德的表現出色，但球隊仍需要在前場找到一名能夠與他搭檔的球員，以提高球隊的內線實力。\n"
                "簽下烏布瑞：\n七六人近期以1年底薪簽下了烏布瑞（Kelly Oubre Jr.）。烏布瑞上賽季在夏洛特黄蜂繳出了生涯新高的20.8分，他的加盟將為七六人帶來更多的進攻選項。"]

籃網補強建議 = ["近期戰績考量：\n籃網隊在上賽季擁有強大的三巨頭，但由於傷病和其他因素，球隊在季後賽中未能達到預期的成果。新賽季的目標是確保球隊的健康狀態，並在季後賽中取得更好的成績。\n"
                "球員動態與合約：\n籃網隊在休賽季與前鋒Darius Bazley簽下了一年的合約。這是籃網隊休賽季的開始，他們仍在尋找其他補強的機會。\n"
                "後場補強：\n考慮到球隊的後場已經非常強大，籃網隊應該專注於增強替補陣容，尤其是在後衛位置上。\n"
                "前場補強：\n籃網隊已經簽下了Darius Bazley，但他們仍然需要在前場找到更多的補強選項，以確保球隊的內線實力。\n"
                "防守加強：\n籃網隊在上賽季的防守上存在一些問題，他們應該尋找一些能夠提高球隊防守實力的球員。"]

塞爾提克補強建議 = ["近期戰績考量：\n塞爾提克隊在上賽季展現了不俗的實力，但在季後賽中面臨了一些挑戰。新賽季的目標是進一步提升球隊的整體實力，並在季後賽中取得更好的成績。\n"
                    "球員動態與合約：\n塞爾提克隊在休賽季進行了一些補強，但也面臨了一些球員的傷病問題。其中，Gallinari和Williams的傷病狀況對球隊的新賽季表現帶來了一定的不確定性。\n"
                    "後場補強：\n塞爾提克隊在後場有一定的實力，但仍需要進一步加強，尤其是在得分後衛位置上。\n"
                    "前場補強：\n考慮到Gallinari和Williams的傷病狀況，塞爾提克隊應該在前場進行補強，以確保球隊的內線實力。\n"
                    "考慮交易：\n塞爾提克隊應該考慮進行一些交易，以換取更多的補強選項和提高球隊的整體實力。"]

暴龍補強建議 = ["近期戰績考量：\n2022-23賽季對暴龍來說是一個失敗的賽季。他們在前一年直接晉級季後賽，並與七六人鏖戰了六場。但在主力骨幹全數留隊後，暴龍只打出了東區第九的成績，並在附加賽第一場就輸給了公牛。整季下來，他們經常在第四節被翻盤，還傳出有休息室紛爭的消息。最後，總教練Nick Nurse和主控Fred VanVleet都離開了球隊。\n"
                "陣容增減：\n暴龍在休賽季進行了一些球員的更迭。他們獲得了Dennis Schröder、Jalen McDaniels和Gradey Dick，而失去了Fred VanVleet、Dalano Banton和Will Barton。\n"
                "進攻策略：\n新任總教練Darko Rajakovic可能會帶來不同的進攻策略，更加強調「空間」和「球的流動」。球隊可能會更多地使用5-out的站位，並透過高位策應和掩護來製造進攻機會。\n"
                "三分球：\n暴龍在上賽季的三分球命中率僅為33.5%，這是他們需要改進的地方。他們應該尋找更多的外圍射手來提高三分球的命中率。\n"
                "球員調整：\nSiakam和Anunoby都出現在交易傳言中，球隊可能會考慮進行一些交易來獲得更好的補強選項。"]

公牛補強建議 = ["近期戰績考量：\n上一季的公牛在開季表現出色，但隨著賽季進行，他們的表現開始下滑。在一個相對失望的情境下，他們結束了2021-22賽季。儘管公牛在Jimmy Butler被交易後的四年內重返季後賽，但他們為了達到這一目標，消耗了大量的資產，這使得他們在未來幾年的薪資空間和選秀等交易籌碼上都受到限制。\n"
                "球員異動：\n公牛在休賽季進行了一些球員的更迭。他們獲得了Dennis Schröder、Jalen McDaniels和Gradey Dick，而失去了Fred VanVleet、Dalano Banton和Will Barton。此外，公牛還簽下了前明星中鋒Andre Drummond和前明星控衛Goran Dragic。\n"
                "進攻策略：\n新賽季的公牛可能會有不同的進攻策略，更加強調「空間」和「球的流動」。他們可能會更多地使用5-out的站位，並透過高位策應和掩護來製造進攻機會。\n"
                "三分球：\n公牛需要提高他們的三分球命中率，這是他們需要改進的地方。他們應該尋找更多的外圍射手來提高三分球的命中率。\n"
                "球員調整：\n公牛應該考慮進行一些交易，以換取更多的補強選項和提高球隊的整體實力。"]

騎士補強建議 = ["近期戰績考量：\n騎士隊在去年夏天策動了「6換1」的大型交易，獲得了明星後衛Donovan Mitchell，並成功重返季後賽。然而，新賽季他們並未有大動作補強，這使得Mitchell面對更大的挑戰。\n"
                "球員異動：\nMitchell從爵士被交易至騎士後，打出了生涯年，場均繳出28.3分。此外，騎士隊今夏最受矚目的補強是32歲的Tristan Thompson回歸，他曾在2016年協助騎士奪冠。\n"
                "進攻策略：\n新賽季的騎士可能會有不同的進攻策略，更加強調「空間」和「球的流動」。他們可能會更多地使用5-out的站位，並透過高位策應和掩護來製造進攻機會。\n"
                "三分球：\n騎士隊需要提高他們的三分球命中率，這是他們需要改進的地方。他們應該尋找更多的外圍射手來提高三分球的命中率。\n"
                "球員調整：\n騎士應該考慮進行一些交易，以換取更多的補強選項和提高球隊的整體實力。"]

溜馬補強建議 = ["核心確立：\n印第安納溜馬隊已確立以Tyrese Haliburton為核心的未來發展方向。他們的策略是為Haliburton找尋合適的幫手，同時也在累積未來的資產。\n"
                "選秀與自由市場操作：\n從選秀會到自由市場的操作，溜馬隊的目的都是為了不浪費Haliburton的黃金時期。他們希望能夠在短時間內，為Haliburton找到合適的搭檔，並且建立一支能夠在季後賽中有所作為的球隊。\n"
                "外線射手：\n考慮到Haliburton的傳球能力，溜馬隊應該尋找一些能夠打開戰局的外線射手，這樣可以給Haliburton更多的傳球選項。\n"
                "內線防守：\n除了外線射手，溜馬隊還需要一名能夠在內線提供防守支援的球員，這樣可以幫助球隊在防守端有更好的表現。\n"
                "年輕球員的發展：\n考慮到Haliburton的年齡，溜馬隊應該將重點放在年輕球員的發展上，這樣可以確保球隊在未來幾年都能保持競爭力。"]

活塞補強建議 = ["上賽季回顧：\n活塞隊在上賽季的戰績並不理想，只贏得了17場比賽，輸掉了65場，成為了NBA最差的球隊。儘管如此，他們在2023選秀中只獲得第五順位的選秀權。\n"
                "新秀與交易：\n去年的五號秀杰登-艾维打出了令人驚喜的新秀賽季，而球隊也在賽季中期交易得到了前榜眼秀詹姆斯-怀斯曼。休賽期引援方面，活塞隊引進了蒙蒂-威廉姆斯（主帥）、乔-哈里斯（交易）、蒙特-莫里斯（交易）等球員。\n"
                "外線射手：\n考慮到球隊的進攻策略，活塞隊應該尋找一些能夠提供外線火力的射手，這樣可以為球隊的進攻帶來更多的選擇。\n"
                "內線支援：\n詹姆斯-怀斯曼在加盟球隊後的表現相當不錯，但球隊仍需要在內線找到更多的支援，特別是在防守端。\n"
                "年輕球員的發展：\n活塞隊有許多有潛力的年輕球員，如奥萨尔·汤普森、杰登·艾维和基利安·海耶斯。球隊應該重視他們的發展，並給予他們更多的上場機會。\n"
                "活塞隊在新賽季的展望中，應該重視年輕球員的發展，並且在休賽期進行適當的補強，以提高球隊的整體實力。"]

公鹿補強建議 = ["上賽季回顧：\n公鹿隊在2023年進行了重大的交易，成功引進了明星後衛Damian Lillard。這一策略使得公鹿隊的實力得到了顯著的提升，並為他們在新賽季中帶來了更高的期望。\n"
                "球員異動：\n除了Lillard，公鹿隊還進行了其他補強。他們簽下了佩恩，以一年底薪合約提升後場戰力深度。這些補強使得公鹿隊在新賽季中具有更強的競爭力。\n"
                "外線射手：\n公鹿隊擁有Giannis Antetokounmpo和Damian Lillard這兩位超級明星，但他們仍需要更多的外線射手來提供火力支援。\n"
                "內線防守：\n公鹿隊在內線的防守上仍有提升的空間，他們應該尋找一名能夠提供內線防守支援的球員。\n"
                "年輕球員的發展：\n公鹿隊擁有一些有潛力的年輕球員，他們應該給予這些球員更多的機會，以確保球隊在未來仍具有競爭力。\n"
                "公鹿隊在新賽季的展望中，應該重視球隊的整體平衡，並在休賽期進行適當的補強，以確保他們在季後賽中有所作為。"]

灰狼補強建議 = ["上賽季回顧：\n灰狼隊在上賽季表現出色，成為西區的一支黑馬。他們的後衛愛德華在2023籃球世界盃中表現出色，成為美國男籃的第一得分手。此外，愛德華的三分命中率達到3成69，場均得分24.6分，成為球隊的進攻核心。\n"
                "球員異動與表現：\n灰狼隊在今年夏天並沒有進行太多的補強動作。他們的防守型中鋒戈貝爾的場上效率一直受到質疑，而先發中前鋒唐斯的球風也受到了一些批評。\n"
                "內線問題：\n灰狼隊應該考慮如何更好地利用「雙塔」唐斯和戈貝爾的組合。如果他們無法在新賽季中打出默契，那麼球隊應該考慮進行交易，以提高球隊的整體實力。\n"
                "外線射手：\n雖然愛德華的三分射手能力出色，但球隊仍然需要更多的外線火力來支援他。\n"
                "年輕球員的發展：\n灰狼隊有一些有潛力的年輕球員，如Jaden McDaniels。球隊應該給予這些球員更多的機會，以確保他們能夠在未來繼續為球隊做出貢獻。\n"
                "總的來說，灰狼隊在新賽季中的表現仍然值得期待。他們擁有一些出色的球員，如愛德華和唐斯，但球隊仍然需要在一些位置上進行補強，以確保他們在季後賽中有所作為。"] 

爵士補強建議 = ["上賽季回顧：\n爵士隊在上賽季進行了一些重大的交易，其中最受矚目的是將Donovan Mitchell交易至克里夫蘭騎士。儘管失去了Mitchell，但爵士隊仍然擁有一支具有競爭力的陣容。\n"
                "球員異動與表現：\nMitchell在新球隊的表現相當出色，他在一場比賽中狂轟71分，成為聯盟史上單場得分最高的球員之一。此外，騎士隊在休賽季進行了一些補強，其中最受矚目的是簽下了Tristan Thompson。\n"
                "側翼深度：\n爵士隊在側翼位置的深度上存在一些問題，他們應該尋找一些能夠提供火力和防守的球員。\n"
                "內線支援：\n儘管爵士隊擁有一些出色的內線球員，但他們仍然需要在這一位置上進行補強，特別是在防守端。\n"
                "年輕球員的發展：\n爵士隊擁有一些有潛力的年輕球員，他們應該給予這些球員更多的機會，以確保他們能夠在未來繼續為球隊做出貢獻。\n"
                "總的來說，爵士隊在新賽季中的展望仍然值得期待。他們擁有一支具有競爭力的陣容，但仍然需要在一些位置上進行補強，以確保他們在季後賽中有所作為。"]

雷霆補強建議 = ["現有陣容的考量：\n"
                "2022-23的雷霆相較於重建的前兩季有所進步，例如團隊投籃命中率提升到聯盟20名前後，且在創造對手失誤次數上全聯盟最多。但雷霆的最大缺陷是護框能力，對手在進攻籃板與二波得分都有明顯優勢。\n"
                "球員合約與續約：\n"
                "雷霆在休賽季失去了Jared Butler和Dario Saric，但獲得了Vasilije Micic、Cason Wallace、Keyontae Johnson、Victor Oladipo、Davis Bertans和Jack White。\n"
                "新球員的考慮：\n"
                "雷霆的先發陣容包括Shai Gilgeous-Alexander、Josh Giddey、Luguentz Dort、Jalen Williams和Chet Holmgren。板凳球員包括Vasilije Micic、Tre Mann、Cason Wallace等。\n"
                "未來展望：\n"
                "雷霆的護框仍然是一大問題，即使有了Chet Holmgren，這個問題也不容易解決。此外，雷霆的先發陣容缺少優秀的射手，這在關鍵時刻可能會成為問題。雷霆的總教練Mark Daigneault和GM Sam Presti都面臨著如何提升球隊競爭力的挑戰。\n"
                "建議：\n"
                "考慮透過交易或自由市場補強護框能力。\n"
                "在外線射手方面，可以考慮引進更多有經驗的球員來提供火力支援。\n"
                "繼續培養年輕球員，特別是在防守端。\n"
                "雷霆在新球季的目標應該是挑戰西區前8名，並嘗試在季後賽中取得更好的成績。"]

拓荒者補強建議 = ["上賽季回顧：\n"
                "拓荒者隊在季前賽的表現中，有一些起伏。他們在對陣太陽和爵士的比賽中都遭遇了敗北，但在對陣魔術和BREAKERS的比賽中取得了勝利。\n"
                "球員異動與表現：\n"
                "新球員Scoot Henderson在季前賽中的表現相當出色，他的高光時刻和表現都受到了球迷和媒體的關注。此外，Mike Schmitz對於他的新秀評估也相當正面。\n"
                "補強建議：\n"
                "外線射手：\n拓荒者隊在外線射手方面可能需要進一步的補強，以提供更多的火力支援。\n"
                "內線防守：\n雖然球隊在內線有一些不錯的選擇，但他們仍然需要一名能夠提供內線防守支援的球員。\n"
                "年輕球員的發展：\nScoot Henderson的發展將是球隊未來的一大亮點，球隊應該給予他更多的機會和資源，以確保他能夠繼續進步。\n"
                "總的來說，拓荒者隊在新賽季中的展望仍然值得期待。他們擁有一些出色的球員，但仍然需要在一些位置上進行補強，以確保他們在季後賽中有所作為。"]

金塊補強建議 = ["球員異動與表現：\n"
                "金塊隊在今年休賽季與雷霆完成了一筆交易，他們將2029年的首輪選秀權交換為2023年的次輪第37順位選秀權、2024年的次輪選秀權，以及2024年雷霆手中順位最差的首輪選秀權。\n"
                "補強建議：\n"
                "年輕球員的發展：\n金塊隊擁有多名優質的年輕球員，球隊應該給予他們更多的機會和資源，以確保他們能夠繼續進步。\n"
                "薪資管理：\n考慮到球隊的核心球員如約基奇、莫瑞、小波特和戈登的高薪資，金塊隊需要有效地管理薪資空間，以確保球隊的競爭力。\n"
                "外線射手：\n金塊隊應該考慮在外線射手方面進行補強，以提供更多的火力支援。\n"
                "總的來說，金塊隊在新賽季中的展望仍然值得期待。他們擁有一支具有競爭力的陣容，但仍然需要在一些位置上進行補強，以確保他們在季後賽中有所作為。"]

灰熊補強建議 = ["現有陣容的考量：\n"
                "孟菲斯灰熊隊在2023年與當家球星貝恩（Desmond Bane）簽訂了一份5年最高可達到2.07億美元的提前續約合同。貝恩在上賽季的表現相當出色，場均貢獻21.5分、5.0籃板、4.4助攻和1.0搶斷。他的三分球命中率達到了40.8%，且在季後賽中的表現更是讓人驚艷。儘管灰熊隊在季後賽中被勇士淘汰，但貝恩的表現無疑是球隊的亮點。\n"
                "球員合約與續約：\n"
                "貝恩的新合同將於2024-2025賽季生效。預計到那時，灰熊將成為一支超級納稅球隊，因為小賈倫‧傑克遜、莫蘭特、貝恩三位球隊核心每人都手握一份億元合同。\n"
                "新球員的考慮：\n"
                "目前的資料中沒有提到灰熊隊在自由市場上的補強動作，但考慮到球隊的薪資結構和未來的發展方向，球隊可能需要在自由市場上尋找合適的補強選手，特別是在後場和內線。\n"
                "未來展望：\n"
                "灰熊隊在上賽季的表現已經相當不錯，但要在西部打進更深的位置，仍需加強陣容的深度和多樣性。球隊應該在自由市場上尋找有經驗的老將和有潛力的年輕球員，以增強球隊的競爭力。"]

火箭補強建議 = ["綜合分析：\n火箭隊近期有一些重要的人事變動。Victor Oladipo 因為他的左膝髕骨腱撕裂傷勢，可能在2023/24賽季大部分時間都無法上場。但火箭隊計劃在2月的交易截止日期之前保留他，除非在此之前能夠交易他。此外，火箭隊還考慮了一些可能的交易目標，包括 Alec Burks 和 Talen Horton-Tucker。\n"
                "建議：\n"
                "交易策略：\n考慮到Oladipo可能的長時間缺席，火箭隊應該考慮在交易市場上尋找替代選手。Alec Burks 和 Talen Horton-Tucker 是已經與火箭隊有所聯繫的潛在交易目標。火箭隊可以利用Oladipo的到期合同和其他資產作為交易籌碼。\n"
                "球員發展：\n火箭隊應該繼續發展年輕球員，如Jabari Smith Jr. 和 Tari Eason，他們在夏季聯賽中的表現相當出色。此外，新加入的Dillon Brooks也應該得到更多的出場時間，但他需要控制自己的情緒，避免不必要的驅逐。\n"
                "防守策略：\n新加入的Dillon Brooks被認為是一名出色的防守球員，但他需要提高自己的投籃選擇和效率。火箭隊應該加強整體的防守策略，特別是在一對一的防守上。\n"
                "問題與思考：\n"
                "Oladipo的未來：\n考慮到他的傷勢和合同狀況，火箭隊應該如何處理Oladipo的未來？\n"
                "年輕球員的發展：\n火箭隊應該如何平衡年輕球員的發展和賽季的競爭力？\n"
                "交易策略：\n火箭隊是否還需要在交易市場上尋找更多的補強選手，以增強球隊的深度和競爭力？\n"]

鵜鶘補強建議 = ["球隊近況回顧：\n"
                "鵜鶘隊在2023年的季前賽中有一些值得注意的表現。他們在對陣魔術的比賽中以104比92獲勝，其中有五名球員得分上雙，包括首發前鋒CJ McCollum、Jonas Valanciunas以及替補新秀Trey Jemison。此外，球隊的當家球星Brandon Ingram在對陣魔術的比賽中獲得18分，而Zion Williamson在上半場就拿下16分並有5次搶斷。\n"
                    "補強建議：\n"
                    "外線射手：\n鵜鶘隊在外線射手方面可能需要進一步的補強，以提供更多的火力支援。\n"
                    "內線防守：\n考慮到Jonas Valanciunas和Zion Williamson的特點，鵜鶘隊可能需要尋找一名能夠提供內線防守支援的球員。\n"
                    "年輕球員的發展：\n鵜鶘隊擁有一些有潛力的年輕球員，如Trey Jemison和EJ Liddell，球隊應該給予他們更多的機會，以確保他們能夠繼續進步。\n"
                    "未來展望：\n"
                    "鵜鶘隊在新賽季中的展望仍然值得期待。他們擁有一支年輕且充滿潛力的陣容，但仍然需要在一些位置上進行補強，以確保他們在季後賽中有所作為。"]

馬刺補強建議 = ["球隊近況回顧：\n"
                "馬刺隊在2023年的季前賽中有一些起伏。他們在對陣活塞和雷霆的比賽中均遭遇敗北，但在對陣熱火的比賽中取得了勝利。當家球星Devin Vassell在對陣火箭的比賽中獲得了25分，而Zach Collins不僅在籃板上拿下9個，還有5次助攻。\n"

                "補強建議：\n"

                "外線射手：\n馬刺隊在外線射手方面可能需要進一步的補強，以提供更多的火力支援。"
                "內線補強：\n雖然Zach Collins的表現不錯，但馬刺隊可能還需要在內線上尋找更多的補強選手，以確保籃板和內線得分的穩定。\n"
                "年輕球員的發展：\n馬刺隊有一些有潛力的年輕球員，如Victor Wembanyama和Jeremy Sochan，球隊應該給予他們更多的機會，以確保他們能夠繼續進步。\n"
                "未來展望：\n"
               "馬刺隊在新賽季中的展望仍然值得期待。他們擁有一支年輕且充滿潛力的陣容，但仍然需要在一些位置上進行補強，以確保他們在季後賽中有所作為。\n"]

獨行俠補強建議 = ["球隊近況回顧：\n"
                "獨行俠隊在2023年的季前賽中展現了一定的競爭力。從最近的新聞中，我們可以看到球隊在對陣火箭的比賽中，當家球星Devin Vassell拿下了25分的出色表現。此外，Zach Collins在籃板端也有出色的貢獻，並且在助攻方面也有所斬獲。球隊在對陣狼隊的比賽中雖然輸球，但Hardy的22分表現仍然亮眼。此外，球隊還簽下了Taze Moore，並在季前賽中與狼隊進行了兩次對決。\n"

                "補強建議：\n"

                "外線射手：\n獨行俠隊在外線射手方面可能需要進一步的補強，以提供更多的火力支援。\n"
                "內線補強：\n雖然Zach Collins的表現不錯，但獨行俠隊可能還需要在內線上尋找更多的補強選手，以確保籃板和內線得分的穩定。\n"
                "年輕球員的發展：\n獨行俠隊應該給予年輕球員，如Taze Moore和其他新秀更多的機會，以確保他們能夠繼續進步。\n"
                "未來展望：\n"
                "獨行俠隊在新賽季中的展望仍然值得期待。他們擁有一支年輕且充滿潛力的陣容，但仍然需要在一些位置上進行補強，以確保他們在季後賽中有所作為。"]

勇士補強建議 = ["球隊近況回顧：\n"
                "勇士隊在2023年的季前賽中展現了強大的競爭力，目前保持著4-0的不敗紀錄。其中，Stephen Curry在對陣Sacramento Kings的比賽中獲得了30分，並在比賽的最後時刻投進了致勝球，幫助勇士隊以116-115戰勝Kings。此外，Jonathan Kuminga在對陣Los Angeles Lakers的季前賽開幕戰中獲得了24分的出色表現。\n"
                "補強建議：\n"
                "增強板凳深度：\n雖然勇士隊的主力球員表現出色，但他們可能需要在板凳球員方面進行補強，以確保在主力球員休息時仍能保持競爭力。\n"
                "尋找內線防守專家：\n考慮到聯盟中的其他強隊，勇士隊可能需要尋找一名內線防守專家，以增強內線的防守能力。\n"
                "年輕球員的培養：\n勇士隊應該繼續給予像Jonathan Kuminga這樣的年輕球員更多的機會，以確保他們能夠繼續進步。\n"
                "未來展望：\n"
                "勇士隊在新賽季中的展望非常光明。他們擁有一支經驗豐富且充滿天賦的陣容，但仍然需要在一些位置上進行補強，以確保他們在季後賽中能夠走得更遠。"]

湖人補強建議 = ["球隊近況回顧：\n"
                "湖人隊在2023年的季前賽中表現不俗，但也有一些起伏。他們在對陣金州勇士和密爾瓦基公鹿的比賽中都遭遇了敗北。特別是在對陣公鹿的比賽中，湖人隊以97-108的比分輸球。儘管如此，球隊的一些主要球員，如Anthony Davis，仍然在季前賽中展現了出色的表現。\n"
                "補強建議：\n"
                "增強板凳深度：\n湖人隊的主力球員都具有很高的競技水平，但在板凳球員方面可能需要進一步的補強，以確保在主力球員休息時仍能保持競爭力。\n"
                "尋找內線補強：\n考慮到聯盟中的其他強隊，湖人隊可能需要在內線上進行補強，以確保籃板和內線得分的穩定。\n"
                "年輕球員的培養：\n湖人隊應該繼續給予年輕球員更多的機會，以確保他們能夠繼續進步\n。"
                "未來展望：\n"
                "湖人隊在新賽季中的展望仍然充滿挑戰。他們擁有一支經驗豐富且充滿天賦的陣容，但仍然需要在一些位置上進行補強，以確保他們在季後賽中能夠走得更遠。"]

快艇補強建議 = ["球隊近況回顧：\n"
                "快艇隊在2023年的賽季中有著起伏的表現。他們在對陣金州勇士、密爾瓦基公鹿和猶他爵士的比賽中都遭遇了敗北。然而，他們也在對陣丹佛金塊的比賽中取得了勝利。球隊的主要球員，如Kawhi Leonard和Paul George，仍然在賽季中展現了出色的表現。\n"
                "補強建議：\n"
                "增強板凳深度：\n快艇隊的主力球員都具有很高的競技水平，但在板凳球員方面可能需要進一步的補強，以確保在主力球員休息時仍能保持競爭力。\n"
                "尋找外線射手：\n考慮到聯盟中的其他強隊，快艇隊可能需要在外線上進行補強，以確保三分球的得分能力。\n"
                "年輕球員的培養：\n快艇隊應該繼續給予年輕球員更多的機會，以確保他們能夠繼續進步。\n"
                "未來展望：\n"
                "快艇隊在新賽季中的展望仍然充滿挑戰。他們擁有一支經驗豐富且充滿天賦的陣容，但仍然需要在一些位置上進行補強，以確保他們在季後賽中能夠走得更遠。"]

太陽補強建議 = ["球隊近況回顧：\n"
                "太陽隊在2023年的賽季中展現了不俗的實力，但仍有一些比賽中的失誤和不足之處。從官方網站的資訊中，我們可以看到太陽隊在近期的比賽中有著不同的表現，例如對陣活塞、金塊和拓荒者的比賽結果。\n"
                "補強建議：\n"
                "增強內線防守：\n太陽隊在內線上可能需要更多的支援，尤其是在對抗其他強隊的大前鋒和中鋒時。\n"
                "尋找更多的外線射手：\n太陽隊在外線上的得分能力仍有提升的空間，可以考慮在交易市場上尋找合適的射手。\n"
                "培養年輕球員：\n太陽隊擁有一些有潛力的年輕球員，球隊應該給予他們更多的機會和時間，讓他們在實戰中獲得成長。\n"
                "未來展望：\n"
                "太陽隊在新賽季中的展望仍然充滿挑戰。他們需要在一些關鍵位置上進行補強，以確保在季後賽中能夠走得更遠。希望這些建議能夠對太陽隊的未來發展提供一些參考。"]

國王補強建議 = ["球隊近況回顧：\n"
                "從官方網站的資訊中，我們可以看到國王隊在2023年的賽季中有著不同的表現。他們在對陣金州勇士、密爾瓦基公鹿、多倫多暴龍和洛杉磯湖人的比賽中都遭遇了敗北。特別是在對陣勇士的比賽中，國王隊僅以一分之差輸掉了比賽。\n"
                "補強建議：\n"
                "增強外線射手\n：國王隊在外線得分上可能需要更多的支援，尤其是在對抗其他強隊時。\n"
                "尋找內線補強：\n國王隊的內線可能需要進一步的補強，以確保籃板和內線得分的穩定。\n"
                "培養年輕球員：\n國王隊擁有一些有潛力的年輕球員，球隊應該給予他們更多的機會和時間，讓他們在實戰中獲得成長。\n"
                "未來展望：\n"
                "國王隊在新賽季中的展望仍然充滿挑戰。他們需要在一些關鍵位置上進行補強，以確保在季後賽中能夠走得更遠。希望這些建議能夠對國王隊的未來發展提供一些參考。"]

補強建議 = ["請輸入你要尋找的隊伍，例如湖人補強建議"]

巫師補強名單 = ["簽約／交易獲得：\n"
                "Jordan Poole：與金州勇士交易中獲得\n"
                "Patrick Baldwin Jr.：與金州勇士交易中獲得\n"
                "Ryan Rollins：與金州勇士交易中獲得\n"
                "Mike Muscala：與波士頓塞爾蒂克交易中獲得\n"
                "Danilo Gallinari：與波士頓塞爾蒂克交易中獲得\n"
                "Tyus Jones：與曼非斯灰熊交易中獲得\n"
                "Landry Shamet：與鳳凰城太陽交易中獲得\n"
                "Chris Paul：與鳳凰城太陽交易中獲得\n"
                "Kyle Kuzma：4年1億200萬美金合約\n"
                "Eugene Omoruyi：雙向合約\n"
                "Jared Butler：雙向合約\n"
                "Taj Gibson：1年320萬美金合約\n"
                "Deni Avdija：未知合約\n"
                "John Butler Jr.：雙向合約\n"
                "離隊：\n"
                "Kristaps Porzingis：交易至波士頓塞爾蒂克\n"
                "Jordan Goodwin：交易至鳳凰城太陽\n"
                "Isaiah Todd：交易至鳳凰城太陽\n"
                "Bradley Beal：交易至鳳凰城太陽\n"
                "Chris Paul：交易至金州勇士\n"
                "Monte Morris：交易至底特律活塞\n"
                "Cameron Payne：交易至聖安東尼奧馬刺\n"
                "Quenton Jackson：釋出\n"
                "Dejan Vasiljevic：釋出\n"
                "Chase Audige：釋出\n"
                "Jules Bernard：釋出\n"
                "Gabe Kalscheur：釋出\n"
                "Michael Foster Jr.：釋出\n"
                "Malik Fitts：釋出\n"
                "Devon Dotson：釋出\n"
                "Hamidou Diallo：釋出\n"
                "Taj Gibson：釋出\n"
                "Xavier Cooks：釋出"]


老鷹補強名單 = ["簽約／交易獲得：\n"
                "LaMelo Ball：5年2億6000萬美金合約\n"
                "Miles Bridges：1年790萬美金合約\n"
                "Amari Bailey：雙向合約\n"
                "Leaky Black：雙向合約\n"
                "P.J. Washington：3年4800萬美金合約\n"
                "Theo Maledon：雙向合約\n"
                "Ish Smith：1年合約\n"
                "離隊：\n"
                "Dennis Smith Jr.\n"
                "Xavier Sneed：釋出\n"
                "Kobi Simmons：釋出\n"
                "Jaylen Sims：釋出\n"
                "Trevon Scott：釋出\n"
                "Angelo Allegri：釋出\n"
                "Kai Jones：釋出\n"
                "Nathan Mensah：釋出\n"
                "RJ Hunter：釋出\n"
                "Terrell Brown Jr.：釋出\n"
                "Edmond Sumner：釋出"]

熱火補強名單 = ["簽約／交易獲得：\n"
                "Josh Richardson：2年合約，首年290萬、第2年球員選項\n"
                "Kevin Love：2年合約，首年370萬、第2年球員選項\n"
                "Orlando Robinson：1年合約\n"
                "Jamaree Bouyea：雙向合約\n"
                "Dru Smith：雙向合約\n"
                "Thomas Bryant：2年540萬美金合約、第2年球員選項\n"
                "R.J. Hampton：雙向合約\n"
                "Cole Swider：雙向合約\n"
                "離隊：\n"
                "Victor Oladipo：交易至奧克拉荷馬雷霆\n"
                "Gabe Vincent\n"
                "Max Strus\n"
                "Brandon McCoy：釋出\n"
                "Jon Elmore：釋出\n"
                "Caleb Daniels：釋出\n"
                "Jamaree Bouyea：釋出\n"
                "Alondes Williams：釋出\n"
                "Drew Peterson：釋出\n"
                "Cheick Diallo：釋出\n"
                "Justin Champagnie：釋出"]

魔術補強名單 = ["簽約／交易獲得：\n"
                "Joe Ingles：2年2200萬美金合約\n"
                "Mo Wagner：2年1600萬美金合約\n"
                "Moritz Wagner：2年1600萬美金合約\n"
                "Admiral Schofield：雙向合約\n"
                "Cole Anthony：未知合約\n"
                "離隊：\n"
                "Jay Scrubb：釋出\n"
                "Bol Bol：釋出\n"
                "Alex Morales：釋出\n"
                "D.J. Wilson：釋出\n"
                "Miye Oni：釋出\n"
                "Brandon Williams：釋出\n"
                "Daeqwon Plowden：釋出\n"
                "Mac McClung：釋出"]

尼克補強名單 = ["簽約／交易獲得：\n"
                "Donte DiVincenzo：4年5000萬美金合約\n"
                "Jaylen Martin：雙向合約\n"
                "Nathan Knight：雙向合約\n"
                "Duane Washington Jr.：雙向合約\n"
                "Dylan Windler：雙向合約\n"
                "Josh Hart：4年8100萬美金合約\n"
                "Charlie Brown Jr.：雙向合約\n"
                "Jacob Toppin：雙向合約\n"
                "離隊：\n"
                "Derrick Rose\n"
                "Obi Toppin\n"
                "Obadiah Noel：釋出\n"
                "Dmytro Skapintsev：釋出\n"
                "Isaiah Roby：釋出\n"
                "Jaylen Martin：釋出\n"
                "Nathan Knight：釋出\n"
                "Duane Washington Jr.：釋出\n"
                "Isaiah Roby：釋出\n"
                "Brandon Goodwin：釋出\n"
                "Mamadi Diakite：釋出"]

七六人補強名單 = ["簽約／交易獲得：\n"
                    "Ricky Council IV：雙向合約\n"
                    "Terquavion Smith：雙向合約\n"
                    "Patrick Beverley：1年320萬美金合約\n"
                    "Mo Bamba：1年234萬美金合約\n"
                    "Montrezl Harrell：1年合約\n"
                    "Danny Green：1年319萬美金合約\n"
                    "Kelly Oubre Jr.：1年合約\n"
                    "Javonte Smart：雙向合約\n"
                    "Ricky Council IV：雙向合約\n"
                    "離隊：\n"
                    "George Niang\n"
                    "Shake Milton\n"
                    "Jalen McDaniels\n"
                    "Marcus Bagley：釋出\n"
                    "David Duke Jr.：釋出\n"
                    "Ricky Council IV：釋出\n"
                    "Jared Brownridge：釋出\n"
                    "Montrezl Harrell：釋出\n"
                    "Azuolas Tubelis：釋出"]

籃網補強名單 = [ "簽約／交易獲得：\n"
                 "Cam Johnson：4年1億800萬美金合約\n"
                 "Dennis Smith Jr.：1年合約252萬美金合約\n"
                 "Lonnie Walker IV：1年合約\n"
                 "Jalen Wilson：雙向合約\n"
                 "Dariq Whitehead：4年1470萬美金合約\n"
                 "Noah Clowney：4年合約\n"
                 "Darius Bazley：4年合約1146萬美金合約\n"
                 "Armoni Brooks：雙向合約\n"
                 "Trendon Watford：1年合約201萬美金合約\n"
                 "離隊：\n"
                 "渡邊雄太\n"
                 "Seth Curry\n"
                 "Patty Mills：交易至休士頓火箭\n"
                 "Joe Harris：交易至底特律活塞\n"
                 "RaiQuan Gray：釋出\n"
                 "Edmond Sumner：釋出\n"
                 "Nerlens Noe\n"
                 "Keifer Sykes：釋出\n"
                 "Jordan Hall：釋出\n"
                 "Scottie Lindsey：釋出\n"
                 "Kyler Edwards：釋出\n"
                 "Kameron Hankerson：釋出\n"
                 "Trey McGowens：釋出\n"
                 "Darius Bazley：釋出\n"
                 "Patrick Gardner：釋出\n"
                 "Kennedy Chandler：釋出"] 

塞爾提克補強名單 = ["簽約／交易獲得：\n"
                    "Kristaps Porzingis：與華盛頓巫師交易中獲得、2年6000萬美金合約續約\n"
                    "Oshae Brissett：2年未知合約\n"
                    "Dalano Banton：2年421萬美金合約\n"
                    "Jordan Walsh：4年760萬美金合約\n"
                    "JD Davison：雙向合約\n"
                    "Jay Scrubb：雙向合約\n"
                    "Jaylen Brown：5年總值3.04億萬美金合約\n"
                    "Svi Mykhailiuk：1年未知合約\n"
                    "Neemias Queta：雙向合約\n"
                    "Jrue Holiday：與波特蘭拓荒者交易中獲得\n"
                    "Payton Pritchard：延長合約、4年3000萬美金合約\n"
                    "Nathan Knight：雙向合約\n"
                    "離隊：\n"
                    "Marcus Smart：交易至曼非斯灰熊\n"
                    "Mike Muscala：交易至華盛頓巫師\n"
                    "Danilo Gallinari：交易至華盛頓巫師\n"
                    "Grant Williams：三方交易中交易至達拉斯獨行俠\n"
                    "Justin Champagnie：釋出\n"
                    "Brandon Slater：釋出\n"
                    "Jordan Schakel：釋出\n"
                    "Taylor Funk：釋出\n"
                    "Malcolm Brogdon：交易至波特蘭拓荒者\n"
                    "Robert Williams III：交易至波特蘭拓荒者\n"
                    "Kylor Kelley：釋出\n"
                    "DJ Steward：釋出\n"
                    "Reginald Kissoonlal：釋出\n"
                    "Wenyen Gabriel：釋出\n"
                    "James Banks III：釋出\n"
                    "Jay Scrubb：釋出"]

暴龍補強名單 = ["簽約／交易獲得：\n"
                "Jakob Poeltl：4年8000萬美金合約\n"
                "Dennis Schroder：2年2600萬美金合約\n"
                "Jalen McDaniels：2年930萬美金合約\n"
                "Markquis Nowell：雙向合約\n"
                "Jeff Dowtin Jr.：未知合約\n"
                "Garrett Temple：1年319萬美金合約\n"
                "離隊：\n"
                "Fred VanVleet\n"
                "Dalano Banton\n"
                "Joe Wieskamp：釋出\n"
                "Kevin Obanor：釋出\n"
                "Darryl Morsell：釋出\n"
                "Makur Maker：釋出\n"
                "Justise Winslow：釋出\n"
                "Mouhamadou Gueye：釋出\n"
                "Jeff Dowtin Jr.：釋出\n"
                "Omari Moore：釋出"]

公牛補強名單 = ["簽約／交易獲得：\n"
                "Nikola Vucevic：3年6000萬美金合約\n"
                "Coby White：3年3300萬美金合約\n"
                "Jevon Carter：3年2000萬美金合約\n"
                "Torrey Craig：2年537萬美金合約\n"
                "Julian Phillips：4年810萬美金合約\n"
                "Ayo Dosunmu：3年2100萬美金合約\n"
                "Javon Freeman-Liberty：雙向合約\n"
                "Onuralp Bitim：雙向合約\n"
                "Terry Taylor：2年421萬美金合約\n"
                "離隊：\n"
                "Patrick Beverley\n"
                "Marko Simonovic：釋出\n"
                "Max Heidegger：釋出\n"
                "Henri Drell：釋出\n"
                "Quenton Jackson：釋出\n"
                "Kahlil Whitney：釋出\n"
                "Derrick Favors：釋出\n"
                "Carlik Jones：釋出"]

騎士補強名單 = ["簽約／交易獲得：\n"
                "Caris LeVert：2年3200萬美金合約\n"
                "Georges Niang：3年2600萬美金合約\n"
                "Max Strus：4年6300萬美金合約、先簽後換\n"
                "Damian Jones：與猶他爵士交易中獲得\n"
                "Ty Jerome：2年500萬美金合約\n"
                "Isaiah Mobley：雙向合約\n"
                "Craig Porter：雙向合約\n"
                "Emoni Bates：雙向合約\n"
                "Tristan Thompson：1年未知合約\n"
                "離隊：\n"
                "Cedi Osman：釋出\n"
                "Lamar Stevens：釋出\n"
                "Robin Lopez：釋出\n"
                "Zhaire Smith：釋出\n"
                "Devontae Shuler：釋出\n"
                "Justin Powell：釋出\n"
                "Pete Nance：釋出\n"
                "Aleem Ford：釋出\n"
                "Rob Edwards：釋出\n"
                "Sharife Cooper：釋出"] 

溜馬補強名單 = ["簽約／交易獲得：\n"
                "Bruce Brown：2年4500萬美金合約\n"
                "Tyrese Haliburton：5年2億6000萬美金合約\n"
                "Obi Toppin：與紐約尼克交易中獲得\n"
                "Isaiah Wong：雙向合約\n"
                "Oscar Tshiebwe：雙向合約\n"
                "Kendall Brown：雙向合約\n"
                "Aaron Nesmith：未知合約\n"
                "離隊：\n"
                "Oshae Brissett\n"
                "Chris Duarte：交易至沙加緬度國王\n"
                "Elfrid Payton：釋出\n"
                "Jordan Bell：釋出\n"
                "Reid Travis：釋出\n"
                "Darius McGhee：釋出\n"
                "Kyle Mangas：釋出"]

活塞補強名單 = ["簽約／交易獲得：\n"
                "Monte Morris：與華盛頓巫師交易中獲得\n"
                "Malcolm Cazalon：雙向合約\n"
                "Jared Rhoden：雙向合約\n"
                "Joe Harris：與布魯克林籃網交易中獲得\n"
                "Isaiah Stewart：4年6400萬美金合約\n"
                "Stanley Umude：雙向合約\n"
                "離隊：\n"
                "R.J. Hampton：釋出\n"
                "Eugene Omoruyi：釋出\n"
                "Ryan Turell：釋出\n"
                "Zavier Simpson：釋出\n"
                "Nate Roberts：釋出\n"
                "Jontay Porter：釋出\n"
                "David Nwaba：釋出\n"
                "Treveon Graham：釋出\n"
                "Tosan Evbuomwan：釋出\n"
                "Buddy Boeheim：釋出"]

公鹿補強名單 = ["簽約／交易獲得：\n"
                "Khris Middleton：3年1億200萬美金合約\n"
                "Brook Lopez：2年4800萬美金合約\n"
                "Jae Crowder：1年合約\n"
                "Robin Lopez：未知合約\n"
                "Malik Beasley：1年合約\n"
                "AJ Green：複數年未知合約\n"
                "Andre Jackson Jr：未知合約\n"
                "Thanasis Antetokounmpo：2年360萬美金合約\n"
                "TyTy Washington Jr.：雙向合約\n"
                "Damian Lillard：三方交易中獲得\n"
                "Cameron Payne：1年合約\n"
                "Marques Bolden：雙向合約\n"
                "Giannis Antetokounmpo：3年1.86億美金提前續約\n"
                "離隊：\n"
                "Jevon Carter\n"
                "Joe Ingles\n"
                "Alex Antetokounmpo：釋出\n"
                "Iverson Molinar：釋出\n"
                "Grayson Allen：三方交易中離隊\n"
                "Jrue Holiday：三方交易中離隊\n"
                "Drew Timme：釋出\n"
                "Omari Moore：釋出\n"
                "Jazian Gortman：釋出"]

灰狼補強名單 = ["簽約／交易獲得：\n"
                "Naz Reid：3年4200萬美金合約\n"
                "Troy Brown Jr.：2年800萬美金合約\n"
                "Nickeil Alexander-Walker：2年900萬美金合約\n"
                "Shake Milton：2年1000萬美金合約\n"
                "Luka Garza：雙向合約\n"
                "Anthony Edwards：5年2億6000萬美金合約\n"
                "Jaylen Clark：雙向合約\n"
                "Leonard Miller：未知合約\n"
                "Matt Ryan：雙向合約\n"
                "Daishen Nix：雙向合約\n"
                "Jaden McDaniels：未知合約\n"
                "離隊：\n"
                "Taurean Prince：釋出\n"
                "Nathan Knight：釋出\n"
                "Vit Krejci：釋出\n"
                "Matt Ryan：釋出\n"
                "Tyrese Martin：釋出\n"
                "Trevor Keels：釋出\n"
                "D.J. Carton：釋出\n"
                "Javonte Cooke：釋出\n"
                "Brian Bowen II：釋出"]

爵士補強名單 = ["簽約／交易獲得：\n"
                "Jordan Clarkson：延長合約、3年5500萬美金合約\n"
                "Joey Hauser：雙向合約\n"
                "John Collins：與亞特蘭大老鷹交易中獲得\n"
                "Omer Yurtseven：2年324萬美金合約\n"
                "Johnny Juzang：雙向合約\n"
                "Josh Christopher：雙向合約\n"
                "離隊：\n"
                "Damian Jones：交易至克利夫蘭騎士\n"
                "Rudy Gay：交易至亞特蘭大老鷹\n"
                "Vernon Carey Jr.：釋出\n"
                "Nick Ongenda：釋出\n"
                "Taevion Kinsey：釋出\n"
                "Joey Hauser：釋出\n"
                "Romeo Langford：釋出\n"
                "Keshawn Justice：釋出\n"
                "Michael Devoe：釋出\n"
                "Isaiah Miller：釋出"]

雷霆補強名單 = ["簽約／交易獲得：\n"
                "Victor Oladipo：與邁阿密熱火交易中獲得\n"
                "Vasilije Micic：3年2350萬美金合約\n"
                "Jack White：2年合約\n"
                "Keyontae Johnson：雙向合約\n"
                "Cason Wallace：雙向合約\n"
                "Patty Mills：未知合約，再交易至亞特蘭大老鷹\n"
                "Rudy Gay：與亞特蘭大老鷹交易中獲得\n"
                "Usman Garuba：與亞特蘭大老鷹交易中獲得\n"
                "TyTy Washington Jr.：與亞特蘭大老鷹交易中獲得\n"
                "Lindy Waters III：雙向合約\n"
                "Olivier Sarr：雙向合約\n"
                "離隊：\n"
                "Patty Mills：交易至亞特蘭大老鷹\n"
                "TyTy Washington Jr.：釋出\n"
                "Usman Garuba：釋出\n"
                "Victor Oladipo：交易至休士頓火箭\n"
                "Jeremiah Robinson-Earl：交易至休士頓火箭\n"
                "KJ Williams：釋出\n"
                "Hunter Maldonado：釋出\n"
                "Jahmi'us Ramsey：釋出\n"
                "Jaden Shackelford：釋出\n"
                "Caleb McConnell：釋出\n"
                "Adam Flagler：釋出\n"
                "Jack White：釋出"]

拓荒者補強名單 = ["簽約／交易獲得：\n"
                    "Jerami Grant：5年1億6000萬美金合約\n"
                    "Ibou Badji：雙向合約\n"
                    "Rayan Rupert：未知合約\n"
                    "John Butler Jr.：雙向合約\n"
                    "Matisse Thybulle：3年3300萬美金合約續留\n"
                    "Moses Brown：1年未知合約\n"
                    "Kevin Knox：1年未知合約\n"
                    "Jrue Holiday：三方交易中獲得\n"
                    "Toumani Camara：三方交易中獲得\n"
                    "Deandre Ayton：三方交易中獲得\n"
                    "Malcolm Brogdon：與波士頓塞爾蒂克交易中獲得\n"
                    "Robert Williams III：與波士頓塞爾蒂克交易中獲得\n"
                    "Skylar Mays：雙向合約\n"
                    "Justin Minaya：雙向合約\n"
                    "Ish Wainright：未知合約\n"
                    "Duop Reath：雙向合約\n"
                    "離隊：\n"
                    "Trendon Watford：釋出\n"
                    "Drew Eubanks\n"
                    "Cam Reddish\n"
                    "Jeenathan Williams：釋出\n"
                    "Damian Lillard：三方交易中離隊\n"
                    "Ashton Hagans：釋出\n"
                    "Jrue Holiday：交易至波士頓塞爾蒂克\n"
                    "Malachi Smith：釋出\n"
                    "Antoine Davis：釋出\n"
                    "George Conditt IV：釋出\n"
                    "John Butler Jr.：釋出\n"
                    "Duop Reath：釋出\n"
                    "Kevin Knox II：釋出\n"
                    "Ibou Badji：釋出"]

金塊補強名單 = ["簽約／交易獲得：\n"
                "DeAndre Jordan：1年未知合約\n"
                "Reggie Jackson：2年1025萬美金合約\n"
                "Justin Holiday：1年未知合約\n"
                "Hunter Tyson：4年770萬美金合約\n"
                "Julian Strawther：未知合約\n"
                "Jalen Pickett：4年未知合約\n"
                "Collin Gillespie：雙向合約\n"
                "Braxton Key：雙向合約\n"
                "Jay Huff：雙向合約\n"
                "Zeke Nnaji：4年3200萬美金合約\n"
                "離隊：\n"
                "Bruce Brown\n"
                "Jack White：釋出\n"
                "Jeff Green\n"
                "Andrew Funk：釋出\n"
                "Armaan Franklin：釋出\n"
                "Souley Boum：釋出\n"
                "Au'Diese Toney：釋出\n"
                "Jamorko Pickett：釋出\n"
                "Amida Brimah：釋出\n"
                "Bryce Wills：釋出"]

灰熊補強名單 = ["簽約／交易獲得：\n"
                "Marcus Smart：與波士頓塞爾蒂克交易中獲得\n"
                "Desmond Bane：5年2億700萬美金合約\n"
                "Derrick Rose：2年650美金合約\n"
                "Isaiah Todd：與鳳凰城太陽交易中獲得\n"
                "Josh Christopher ：與休士頓火箭交易中獲得\n"
                "GG Jackson：雙向合約\n"
                "離隊：\n"
                "Tyus Jones：交易至華盛頓巫師\n"
                "Dillon Brooks：交易至休士頓火箭\n"
                "Mychal Mulder：釋出\n"
                "Matt Hurt：釋出\n"
                "Jason Preston：釋出\n"
                "Timmy Allen：釋出\n"
                "David Johnson：釋出\n"
                "Shaquille Harrison：釋出\n"
                "Adonis Arms：釋出"]

火箭補強名單 = ["簽約／交易獲得：\n"
                "Darius Days：雙向合約\n"
                "Fred VanVleet：3年1億3000萬美金合約、第3年球隊選項\n"
                "Trevor Hudgins：雙向合約\n"
                "Dillon Brooks：4年8000萬美金合約、先簽後換\n"
                "Jock Landale：4年3200萬美金合約\n"
                "Jeff Green：1年600萬美金合約\n"
                "Patty Mills：與布魯克林籃網交易中獲得\n"
                "Aaron Holiday：1年234萬美金合約\n"
                "Jermaine Samuels Jr.：雙向合約\n"
                "Boban Marjanovic：1年289萬美金合約\n"
                "Reggie Bullock：1年底薪合約\n"
                "Victor Oladipo：未知合約\n"
                "Jeremiah Robinson-Earl：未知合約\n"
                "Nate Hinton：雙向合約\n"
                "Nate Williams：雙向合約\n"
                "離隊：\n"
                "Daishen Nix：釋出\n"
                "TyTy Washington Jr.：交易至亞特蘭大老鷹\n"
                "Usman Garuba：交易至亞特蘭大老鷹\n"
                "Kenyon Martin Jr.：交易至洛杉磯快艇\n"
                "Josh Christopher：交易至曼菲斯灰熊\n"
                "Patty Mills：交易至奧克拉荷馬雷霆\n"
                "Joshua Obiesie：釋出\n"
                "Kevin Porter Jr.：交易至奧克拉荷馬雷霆\n"
                "Nate Hinton：釋出\n"
                "Jeremiah Robinson-Earl：釋出\n"
                "Darius Days：釋出\n"
                "Trevor Hudgins：釋出"]

鵜鶘補強名單 = ["簽約／交易獲得：\n"
                "Herb Jones：4年5400萬美金合約\n"
                "Cody Zeller：1年310萬美金合約\n"
                "E.J. Lidell：3年620萬美金合約\n"
                "Kaiser Gates：雙向合約\n"
                "Matt Ryan：釋出名單揀選\n"
                "離隊：\n"
                "Josh Richardson\n"
                "Jaxson Hayes\n"
                "Garrett Temple：釋出\n"
                "Devin Cannady：釋出\n"
                "Liam Robbins：釋出\n"
                "Landers Nolley II：釋出\n"
                "Tevian Jones：釋出\n"
                "Trey Jemison：釋出\n"
                "Malcolm Hill：釋出\n"
                "Jalen Crutcher：釋出\n"
                "Izaiah Brockington：釋出"]

馬刺補強名單 = ["簽約／交易獲得：\n"
                "Tre Jones：2年2000萬美金合約\n"
                "Julian Champagnie：4年1200萬美金合約\n"
                "Cedi Osman：三方交易獲得\n"
                "Lamar Stevens：三方交易獲得\n"
                "Sandro Mamukelashvili：1年200萬美金合約\n"
                "Sir'Jabari Rice：雙向合約\n"
                "Reggie Bullock：三方交易中獲得\n"
                "Cameron Payne：與鳳凰城太陽交易中獲得\n"
                "Sidy Cissoko：3年未知合約\n"
                "Devin Vassell：5年1.46億美元提前續約（相關報導）\n"
                "Zach Collins：延長合約、3年2205萬美金提前續約\n"
                "Charles Bediako：雙向合約\n"
                "離隊：\n"
                "Keita Bates-Diop\n"
                "Lamar Stevens：釋出\n"
                "Cameron Payne：釋出\n"
                "Javante McCoy：釋出\n"
                "Setric Millner Jr.：釋出\n"
                "RaiQuan Gray：釋出\n"
                "Reggie Bullock：釋出\n"
                "Paul Watson：釋出\n"
                "Erik Stevenson：釋出\n"
                "Khem Birch：釋出"]

獨行俠補強名單 = ["簽約／交易獲得：\n"
                    "Kyrie Irving：3年1億2600萬美金合約\n"
                    "Seth Curry：2年800萬美金合約\n"
                    "Dwight Powell：3年1200萬美金合約\n"
                    "Dante Exum：1年270萬美金合約\n"
                    "Grant Williams：三方交易中獲得\n"
                    "Richaun Holmes：與沙加緬度國王交易中獲得\n"
                    "Mike Miles Jr.：雙向合約\n"
                    "Derrick Jones Jr.：未知合約\n"
                    "Markieff Morris：1年320萬美金合約\n"
                    "Dexter Dennis：雙向合約\n"
                    "Greg Brown III：雙向合約\n"
                    "Josh Green：未知合約\n"
                    "離隊：\n"
                    "Reggie Bullock：三方交易中交易至聖安東尼奧馬刺\n"
                    "JaVale McGee：釋出\n"
                    "Jordan Walker：釋出\n"
                    "Mike Miles Jr.：釋出\n"
                    "Joe Wieskamp：釋出\n"
                    "Tony Bradley：釋出"]

勇士補強名單 = ["簽約／交易獲得：\n"
                "Chris Paul：與華盛頓巫師交易中獲得\n"
                "Draymond Green：4年1億美金合約\n"
                "Cory Joseph：1年合約\n"
                "Trayce Jackson-Davis：4年合約\n"
                "Dario Saric：1年合約270萬美金合約\n"
                "Lester Quinones：雙向合約\n"
                "Usman Garuba：雙向合約\n"
                "Jerome Robinson：雙向合約\n"
                "離隊：\n"
                "Jordan Poole：交易至華盛頓巫師\n"
                "Patrick Baldwin Jr.：交易至華盛頓巫師\n"
                "Ryan Rollins：交易至華盛頓巫師\n"
                "Ty Jerome\n"
                "Donte DiVincenzo\n"
                "Jayce Johnson：釋出\n"
                "Donovan Williams：釋出\n"
                "Javan Johnson：釋出\n"
                "Kendric Davis：釋出\n"
                "Yuri Collins：釋出\n"
                "Javonte Green：釋出\n"
                "Rodney McGruder：釋出\n"
                "Rudy Gay：釋出"]

湖人補強名單 = ["簽約／交易獲得：\n"
                "Taurean Prince：1年450萬美金合約\n"
                "Gabe Vincent：3年3300萬美金合約\n"
                "八村壘：3年5100萬美金合約\n"
                "Cam Reddish：2年未知合約\n"
                "Jaxson Hayes：2年未知合約、第2年球員選項\n"
                "D'Angelo Russell：2年3700萬美金合約\n"
                "Austin Reaves：4年5600萬美金合約\n"
                "D'Moi Hodge：雙向合約\n"
                "Colin Castleton：雙向合約\n"
                "Anthony Davis：3年1.86億美元提前續約，年均薪約為6200萬美元\n"
                "Christian Wood：2年570萬美金合約\n"
                "Jarred Vanderbilt：4年4800萬美金合約\n"
                "離隊：\n"
                "Shaquille Harrison：釋出\n"
                "Mo Bamba：釋出\n"
                "Troy Brown Jr.\n"
                "Dennis Schroder\n"
                "Malik Beasley\n"
                "Cole Swider：釋出\n"
                "Bryce Hamilton：釋出\n"
                "Vincent Valerio-Bodon：釋出\n"
                "Scotty Pippen Jr.：釋出\n"
                "Damion Baugh：釋出\n"
                "Louis King：釋出\n"
                "Quinndary Weatherspoon：釋出"]

快艇補強名單 = ["簽約／交易獲得：\n"
                "Russell Westbrook：2年780萬美金合約、第2年球員選項\n"
                "Kenyon Martin Jr.：與休士頓火箭交易中獲得\n"
                "Mason Plumlee：1年500萬美金合約\n"
                "Jordan Miller：雙向合約\n"
                "Joshua Primo：雙向合約\n"
                "離隊：\n"
                "Eric Gordon：釋出\n"
                "Jason Preston：釋出\n"
                "Bryson Williams：釋出\n"
                "Nate Darling：釋出\n"
                "Xavier Moon：釋出\n"
                "Joey Hauser：釋出"]

太陽補強名單 = ["簽約／交易獲得：\n"
                "Jordan Goodwin：與華盛頓巫師交易中獲得\n"
                "Isaiah Todd：與華盛頓巫師交易中獲得\n"
                "Bradley Beal：與華盛頓巫師交易中獲得\n"
                "Drew Eubanks：2年未知合約\n"
                "Josh Okogie：1年234萬美金合約\n"
                "Keita Bates-Diop：2年500萬美金合約\n"
                "Damion Lee：1+1合約\n"
                "Chimezie Metu：1年未知合約\n"
                "渡邊雄太：2年500萬美金合約、第2年球員選項\n"
                "Eric Gordon：2年未知合約\n"
                "Toumani Camara：4年未知合約\n"
                "Saben Lee：雙向合約\n"
                "Bol Bol：1年216萬美金合約\n"
                "Udoka Azubuike：雙向合約\n"
                "Grayson Allen：三方交易中獲得\n"
                "Keon Johnson：三方交易中獲得\n"
                "Nassir Little：三方交易中獲得\n"
                "Jusuf Nurkic：三方交易中獲得\n"
                "離隊：\n"
                "Landry Shamet：交易至華盛頓巫師\n"
                "Chris Paul：交易至華盛頓巫師\n"
                "Jock Landale\n"
                "Torrey Craig\n"
                "Isaiah Todd：交易至曼非斯灰熊\n"
                "Cameron Payne：交易至聖安東尼奧馬刺\n"
                "Toumani Camara：三方交易中離隊\n"
                "Deandre Ayton：三方交易中離隊\n"
                "Ish Wainright：釋出\n"
                "Keon Johnson：釋出"]

國王補強名單 = ["簽約／交易獲得：\n"
                "Harrison Barnes：3年5400萬美金合約\n"
                "Trey Lyles：2年1600萬美金合約+獎金\n"
                "Sasha Vezenkov：3年2000萬美金合約\n"
                "Alex Len：1年320萬美金合約\n"
                "Domantas Sabonis：5年2億1700萬美金合約\n"
                "Jalen Slawson：雙向合約\n"
                "Colby Jones：4年876萬美金合約\n"
                "Keon Ellis：雙向合約\n"
                "Chris Duarte：與印第安納溜馬交易中獲得\n"
                "Aleksandar Vezenkov：3年2000萬美金合約\n"
                "Nerlens Noel：1年290萬美金合約\n"
                "Neemias Queta：未知合約\n"
                "JaVale McGee：未知合約\n"
                "離隊：\n"
                "Chimezie Metu\n"
                "Richaun Holmes：交易至達拉斯獨行俠\n"
                "PJ Dozier：釋出\n"
                "Skal Labissiere：釋出\n"
                "Neemias Queta：釋出\n"
                "Nerlens Noel：釋出\n"
                "James Akinjo：釋出\n"
                "Jeremy Lamb：釋出\n"
                "Chance Comanche：釋出\n"
                "Deonte Burton：釋出\n"
                "Jake Stephens：釋出\n"
                "Jaylen Nowell：釋出\n"
                "Dane Goodwin：釋出"]

補強名單 = ["請輸入你要尋找的隊伍，例如湖人補強名單"]

第一順位選秀=["順位:1\n球員:Victor Wemban-yama\n球隊:馬刺\n位置:C/F"]

第二順位選秀=["順位:2\n球員:Brandon Miller\n球隊:黃蜂\n位置:SF"]

第三順位選秀=["順位:3\n球員:Scoot Henderson\n球隊:拓荒者\n位置:PG"]

第四順位選秀=["順位:4\n球員:Amen Thompson\n球隊:火箭\n位置:PG"]

第五順位選秀=["順位:5\n球員:Ausar Thompson\n球隊:活塞\n位置:SG"]

第六順位選秀=["順位:6\n球員:Anthony Black\n球隊:魔術\n位置:PG"]

第七順位選秀=["順位:7\n球員:Bilal Coulibaly\n球隊:巫師\n位置:SF"]

第八順位選秀=["順位:8\n球員:Jarace Walker\n球隊:溜馬\n位置:PF"]

第九順位選秀=["順位:9\n球員:Taylor Hendricks\n球隊:爵士\n位置:PF"]

第十順位選秀=["順位:10\n球員:Cason Wallace"]

第十一順位選秀=["順位:11\n球員:Jett Howard\n球隊:魔術\n位置:SF"]

第十二順位選秀=["順位:12\n球員:Dereck Lively\n球隊:獨行俠\n位置:C"]

第十三順位選秀=["順位:13\n球員:Gradey Dick\n球隊:暴龍\n位置:SF"]

第十四順位選秀=["順位:14\n球員:Jordan Hawkins\n球隊:鵜鶘\n位置:SG"]

第十五順位選秀=["順位:15\n球員:Kobe Bufkin\n球隊:老鷹\n位置:SG"]

第十六順位選秀=["順位:16\n球員:Keyonte George\n球隊:爵士\n位置:SG"]

第十七順位選秀=["順位:17\n球員:Jalen Hood-Schifino\n球隊:湖人\n位置:PG"]

第十八順位選秀=["順位:18\n球員:Jaime Jaquez Jr.\n球隊:熱火\n位置:SF"]

第十九順位選秀=["順位:19\n球員:Brandin Podziemski\n球隊:勇士\n位置:SG"]

第二十順位選秀=["順位:20\n球員:Cam Whitmore\n球隊:火箭\n位置:SF"]

第二十一順位選秀=["順位:21\n球員:Noah Clowney\n球隊:籃網\n位置:PF"]

第二十二順位選秀=["順位:22\n球員:Dariq Whitehead\n球隊:籃網\n位置:SF"]

第二十三順位選秀=["順位:23\n球員:Kris Murray\n球隊:拓荒者\n位置:PF"]

第二十四順位選秀=["順位:24\n球員:Olivier-Maxence Prosper\n球隊:獨行俠\n位置:PF"]

第二十五順位選秀=["順位:25\n球員:Marcus Sasser\n球隊:活塞\n位置:SG"]

第二十六順位選秀=["順位:26\n球員:Ben Sheppard\n球隊:溜馬\n位置:SG"]

第二十七順位選秀=["順位:27\n球員:Nick Smith Jr.\n球隊:黃蜂\n位置:SG"]

第二十八順位選秀=["順位:28\n球員:Brice Sensabaugh\n球隊:爵士\n位置:SF"]

第二十九順位選秀=["順位:29\n球員:Julian Strawther\n球隊:金塊\n位置:SF"]

第三十順位選秀=["順位:30\n球員:Kobe Brown\n球隊:快艇\n位置:SF"]

第三十一順位選秀=["順位:31\n球員:James Nnaji\n球隊:黃蜂\n位置:C"]

第三十二順位選秀=["順位:32\n球員:Jalen Pickett\n球隊:金塊\n位置:PG"]

第三十三順位選秀=["順位:33\n球員:Leonard Miller\n球隊:灰狼\n位置:PF"]

第三十四順位選秀=["順位:34\n球員:Colby Jones\n球隊:國王\n位置:SF"]

第三十五順位選秀=["順位:35\n球員:Julian Phillips\n球隊:公牛\n位置:SF"]

第三十六順位選秀=["順位:36\n球員:Andre Jackson\n球隊:公鹿\n位置:SF"]

第三十七順位選秀=["順位:37\n球員:Hunter Tyson\n球隊:金塊\n位置:PF"]

第三十八順位選秀=["順位:38\n球員:Jordan Walsh\n球隊:塞爾提克\n位置:SF"]

第三十九順位選秀=["順位:39\n球員:Mouhamed Gueye\n球隊:老鷹\n位置:PF"]

第四十順位選秀=["順位:40\n球員:Maxwell Lewis\n球隊:湖人\n位置:SF"]

第四十一順位選秀=["順位:41\n球員:Amari Baileyn球隊:黃蜂\n位置:SG"]

第四十二順位選秀=["順位:42\n球員:Tristan Vukcevic\n球隊:巫師\n位置:C"]

第四十三順位選秀=["順位:43\n球員:Rayan Rupert\n球隊:拓荒者\n位置:SG"]

第四十四順位選秀=["順位:44\n球員:Sidy Cissoko\n球隊:馬刺\n位置:SF"]

第四十五順位選秀=["順位:45\n球員:Gregory Jackson\n球隊:灰熊\n位置:PF"]

第四十六順位選秀=["順位:46\n球員:Seth Lundy\n球隊:老鷹\n位置:SF"]

第四十七順位選秀=["順位:47\n球員:Mojave King\n球隊:溜馬\n位置:SG"]

第四十八順位選秀=["順位:48\n球員:Jordan Miller\n球隊:快艇\n位置:SF"]

第四十九順位選秀=["順位:49\n球員:Emoni Bates\n球隊:騎士\n位置:SF"]

第五十順位選秀=["順位:50\n球員:Keyontae Johnson\n球隊:雷霆\n位置:SF"]

第五十一順位選秀=["順位:51\n球員:Jalen Wilson\n球隊:籃網\n位置:SF"]

第五十二順位選秀=["順位:52\n球員:Toumani Camara\n球隊:太陽\n位置:SF"]

第五十三順位選秀=["順位:53\n球員:Jaylen Clark\n球隊:灰狼\n位置:SG"]

第五十四順位選秀=["順位:54\n球員:Jalen Slawson\n球隊:國王\n位置:SF"]

第五十五順位選秀=["順位:55\n球員:Isaiah Wong\n球隊:溜馬\n位置:SG"]

第五十六順位選秀=["順位:56\n球員:Tarik Biberovic\n球隊:灰熊\n位置:SG"]

第五十七順位選秀=["順位:57\n球員:Trayce Jackson-Davis\n球隊:勇士\n位置:PF"]

第五十八順位選秀=["順位:58\n球員:Chris Livingston\n球隊:公鹿\n位置:SF"]





# 主函數 改參數
def random_statement(p1):
    return np.random.choice(p1)
