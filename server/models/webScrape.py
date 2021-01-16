import praw
import pandas as pd
import datetime as dt
from praw.models import MoreComments
from praw.reddit import Subreddit
import re
import json

reddit = praw.Reddit(client_id='Yx811ChQuzwdCg', \
                     client_secret='KPTiWELMRKl89hW85LY_l89qpchG7A', \
                     user_agent='webScrapeReddit', \
                     username='bill_cui57', \
                     password='Happytime1')


# url = "https://www.reddit.com/r/wallstreetbets/comments/ky3qg6/weekend_discussion_thread_for_the_weekend_of/"

# submission = reddit.submission(url=url)


# submission.comments.replace_more(limit=None)
# for top_level_comment in submission.comments:
#     print(top_level_comment.body)


tickerSet= {
"A",
"AA",
"AAIC",
"AAIC.PRB",
"AAIC.PRC",
"AAN",
"AAP",
"AAT",
"AB",
"ABB",
"ABBV",
"ABC",
"ABEV",
"ABG",
"ABM",
"ABR",
"ABR.PRA",
"ABR.PRB",
"ABR.PRC",
"ABT",
"AC",
"ACA",
"ACB",
"ACC",
"ACCO",
"ACEL",
"ACH",
"ACI",
"ACIC",
"ACIC.U",
"ACIC.WS",
"ACM",
"ACN",
"ACND",
"ACND.U",
"ACND.WS",
"ACP",
"ACRE",
"ACV",
"ADC",
"ADCT",
"ADEX.U",
"ADM",
"ADNT",
"ADS",
"ADT",
"ADX",
"AEB",
"AEE",
"AEFC",
"AEG",
"AEL",
"AEL.PRA",
"AEL.PRB",
"AEM",
"AENZ",
"AEO",
"AER",
"AES",
"AFB",
"AFC",
"AFG",
"AFGB",
"AFGC",
"AFGD",
"AFGE",
"AFI",
"AFL",
"AFT",
"AG",
"AGCB",
"AGCO",
"AGD",
"AGI",
"AGM",
"AGM.A",
"AGM.PRC",
"AGM.PRD",
"AGM.PRE",
"AGM.PRF",
"AGO",
"AGO.PRB",
"AGO.PRE",
"AGO.PRF",
"AGR",
"AGRO",
"AGS",
"AGX",
"AHC",
"AHH",
"AHH.PRA",
"AHL.PRC",
"AHL.PRD",
"AHL.PRE",
"AHT",
"AHT.PRD",
"AHT.PRF",
"AHT.PRG",
"AHT.PRH",
"AHT.PRI",
"AI",
"AIC",
"AIF",
"AIG",
"AIG.PRA",
"AIN",
"AIO",
"AIR",
"AIRC",
"AIT",
"AIV",
"AIW",
"AIZ",
"AIZN",
"AIZP",
"AJAX",
"AJAX.U",
"AJAX.WS",
"AJG",
"AJRD",
"AJX",
"AJXA",
"AKO/A",
"AKO/B",
"AKR",
"AL",
"AL.PRA",
"ALB",
"ALC",
"ALE",
"ALEX",
"ALG",
"ALIN.PRA",
"ALIN.PRB",
"ALIN.PRE",
"ALK",
"ALL",
"ALL.PRB",
"ALL.PRG",
"ALL.PRH",
"ALL.PRI",
"ALLE",
"ALLY",
"ALLY.PRA",
"ALP.PRQ",
"ALSN",
"ALTG",
"ALTG.PRA",
"ALTG.WS",
"ALUS",
"ALUS.U",
"ALUS.WS",
"ALV",
"ALX",
"AM",
"AMBC",
"AMBC.WS",
"AMC",
"AMCR",
"AME",
"AMG",
"AMH",
"AMH.PRD",
"AMH.PRE",
"AMH.PRF",
"AMH.PRG",
"AMH.PRH",
"AMK",
"AMN",
"AMOV",
"AMP",
"AMPY",
"AMRC",
"AMRX",
"AMT",
"AMWL",
"AMX",
"AN",
"ANET",
"ANF",
"ANH",
"ANH.PRA",
"ANH.PRB",
"ANH.PRC",
"ANTM",
"AOD",
"AON",
"AONE",
"AONE.U",
"AONE.WS",
"AOS",
"AP",
"APAM",
"APD",
"APG",
"APH",
"APLE",
"APO",
"APO.PRA",
"APO.PRB",
"APRN",
"APSG",
"APSG.U",
"APSG.WS",
"APTS",
"APTV",
"APTV.PRA",
"AQN",
"AQNA",
"AQNB",
"AQUA",
"AR",
"ARA",
"ARC",
"ARCH",
"ARCO",
"ARD",
"ARDC",
"ARE",
"ARES",
"ARES.PRA",
"ARGD",
"ARGO",
"ARGO.PRA",
"ARI",
"ARL",
"ARLO",
"ARMK",
"ARNC",
"AROC",
"ARR",
"ARR.PRC",
"ARW",
"ASA",
"ASAN",
"ASAQ",
"ASAQ.U",
"ASAQ.WS",
"ASB",
"ASB.PRC",
"ASB.PRD",
"ASB.PRE",
"ASB.PRF",
"ASC",
"ASG",
"ASGI",
"ASGN",
"ASH",
"ASIX",
"ASPL",
"ASPL.U",
"ASPL.WS",
"ASPN",
"ASR",
"ASX",
"AT",
"ATA.U",
"ATAC",
"ATAC.U",
"ATAC.WS",
"ATCO",
"ATCO.PRD",
"ATCO.PRE",
"ATCO.PRG",
"ATCO.PRH",
"ATCO.PRI",
"ATEN",
"ATGE",
"ATH",
"ATH.PRA",
"ATH.PRB",
"ATH.PRC",
"ATH.PRD",
"ATHM",
"ATI",
"ATKR",
"ATO",
"ATR",
"ATTO",
"ATUS",
"ATV",
"AU",
"AUY",
"AVA",
"AVAL",
"AVAN",
"AVAN.U",
"AVAN.WS",
"AVB",
"AVD",
"AVK",
"AVLR",
"AVNS",
"AVNT",
"AVTR",
"AVTR.PRA",
"AVY",
"AVYA",
"AWF",
"AWI",
"AWK",
"AWP",
"AWR",
"AX",
"AXL",
"AXO",
"AXP",
"AXR",
"AXS",
"AXS.PRE",
"AXTA",
"AYI",
"AYX",
"AZEK",
"AZO",
"AZRE",
"AZUL",
"AZZ",
"B",
"BA",
"BABA",
"BAC",
"BAC.PRA",
"BAC.PRB",
"BAC.PRC",
"BAC.PRE",
"BAC.PRK",
"BAC.PRL",
"BAC.PRM",
"BAC.PRN",
"BAC.PRO",
"BAF",
"BAH",
"BAK",
"BALY",
"BAM",
"BAMH",
"BAMI",
"BANC",
"BANC.PRD",
"BANC.PRE",
"BAP",
"BAX",
"BB",
"BBAR",
"BBD",
"BBDC",
"BBDO",
"BBF",
"BBK",
"BBL",
"BBN",
"BBU",
"BBVA",
"BBW",
"BBY",
"BC",
"BC.PRA",
"BC.PRB",
"BC.PRC",
"BCAT",
"BCC",
"BCE",
"BCEI",
"BCH",
"BCO",
"BCS",
"BCSF",
"BCX",
"BDC",
"BDJ",
"BDN",
"BDX",
"BDXB",
"BE",
"BEDU",
"BEKE",
"BEN",
"BEP",
"BEP.PRA",
"BEPC",
"BERY",
"BEST",
"BF/A",
"BF/B",
"BFAM",
"BFK",
"BFS",
"BFS.PRD",
"BFS.PRE",
"BFT",
"BFT.U",
"BFT.WS",
"BFY",
"BFZ",
"BG",
"BGB",
"BGH",
"BGIO",
"BGR",
"BGS",
"BGSF",
"BGT",
"BGX",
"BGY",
"BH",
"BH.A",
"BHC",
"BHE",
"BHK",
"BHLB",
"BHP",
"BHR",
"BHR.PRB",
"BHR.PRD",
"BHV",
"BHVN",
"BIF",
"BIG",
"BILL",
"BIO",
"BIO/B",
"BIP",
"BIP.PRA",
"BIPC",
"BIT",
"BJ",
"BK",
"BKD",
"BKE",
"BKH",
"BKI",
"BKN",
"BKR",
"BKT",
"BKU",
"BLD",
"BLE",
"BLK",
"BLL",
"BLW",
"BLX",
"BMA",
"BME",
"BMEZ",
"BMI",
"BML.PRG",
"BML.PRH",
"BML.PRJ",
"BML.PRL",
"BMO",
"BMY",
"BNED",
"BNL",
"BNS",
"BNY",
"BOAC",
"BOAC.U",
"BOAC.WS",
"BOE",
"BOH",
"BOOT",
"BORR",
"BOX",
"BP",
"BPMP",
"BPT",
"BQ",
"BR",
"BRBR",
"BRC",
"BRFS",
"BRK/A",
"BRK/B",
"BRMK",
"BRO",
"BRT",
"BRX",
"BSA",
"BSAC",
"BSBR",
"BSD",
"BSE",
"BSIG",
"BSL",
"BSM",
"BSMX",
"BSN",
"BSN.U",
"BSN.WS",
"BST",
"BSTZ",
"BSX",
"BSX.PRA",
"BTA",
"BTI",
"BTO",
"BTT",
"BTU",
"BTZ",
"BUD",
"BUI",
"BUR",
"BURL",
"BV",
"BVH",
"BVN",
"BW",
"BWA",
"BWG",
"BWXT",
"BX",
"BXC",
"BXG",
"BXMT",
"BXMX",
"BXP",
"BXP.PRB",
"BXS",
"BXS.PRA",
"BY",
"BYD",
"BYM",
"BZH",
"BZM",
"C",
"C.PRJ",
"C.PRK",
"C.PRN",
"C.PRS",
"CAAP",
"CABO",
"CACI",
"CADE",
"CAE",
"CAF",
"CAG",
"CAH",
"CAI",
"CAI.PRA",
"CAI.PRB",
"CAJ",
"CAL",
"CALX",
"CANG",
"CAP.U",
"CAPL",
"CARR",
"CARS",
"CAS",
"CAS.U",
"CAS.WS",
"CAT",
"CATO",
"CB",
"CBAH.U",
"CBB",
"CBB.PRB",
"CBD",
"CBH",
"CBRE",
"CBT",
"CBU",
"CBZ",
"CC",
"CCAC",
"CCAC.U",
"CCAC.WS",
"CCC",
"CCEP",
"CCI",
"CCIV",
"CCIV.U",
"CCIV.WS",
"CCJ",
"CCK",
"CCL",
"CCM",
"CCO",
"CCS",
"CCU",
"CCV.U",
"CCX",
"CCX.U",
"CCX.WS",
"CCZ",
"CDAY",
"CDE",
"CDR",
"CDR.PRB",
"CDR.PRC",
"CE",
"CEA",
"CEE",
"CEIX",
"CEL",
"CELG.RT",
"CELP",
"CEM",
"CEN",
"CEO",
"CEPU",
"CEQP",
"CEQP.PR",
"CF",
"CFG",
"CFG.PRD",
"CFG.PRE",
"CFR",
"CFR.PRB",
"CFX",
"CFXA",
"CGA",
"CHCT",
"CHD",
"CHE",
"CHGG",
"CHH",
"CHMI",
"CHMI.PRA",
"CHMI.PRB",
"CHN",
"CHRA",
"CHS",
"CHT",
"CHWY",
"CI",
"CIA",
"CIB",
"CIEN",
"CIF",
"CIG",
"CIG.C",
"CII",
"CIM",
"CIM.PRA",
"CIM.PRB",
"CIM.PRC",
"CIM.PRD",
"CINR",
"CIO",
"CIO.PRA",
"CIR",
"CIT",
"CIT.PRB",
"CIXX",
"CKH",
"CL",
"CLA",
"CLA.U",
"CLA.WS",
"CLAS.U",
"CLB",
"CLDR",
"CLDT",
"CLF",
"CLGX",
"CLH",
"CLI",
"CLII",
"CLII.U",
"CLII.WS",
"CLNC",
"CLNY",
"CLNY.PRG",
"CLNY.PRH",
"CLNY.PRI",
"CLNY.PRJ",
"CLPR",
"CLR",
"CLS",
"CLW",
"CLX",
"CM",
"CMA",
"CMC",
"CMCM",
"CMD",
"CMG",
"CMI",
"CMO",
"CMO.PRE",
"CMP",
"CMRE",
"CMRE.PRB",
"CMRE.PRC",
"CMRE.PRD",
"CMRE.PRE",
"CMS",
"CMS.PRB",
"CMSA",
"CMSC",
"CMSD",
"CMU",
"CNA",
"CNC",
"CND.U",
"CNF",
"CNHI",
"CNI",
"CNK",
"CNMD",
"CNNE",
"CNO",
"CNO.PRA",
"CNP",
"CNP.PRB",
"CNQ",
"CNR",
"CNS",
"CNX",
"CO",
"CODI",
"CODI.PRA",
"CODI.PRB",
"CODI.PRC",
"COE",
"COF",
"COF.PRG",
"COF.PRH",
"COF.PRI",
"COF.PRJ",
"COF.PRK",
"COG",
"COLD",
"COO",
"COP",
"COR",
"CORR",
"CORR.PRA",
"COTY",
"CP",
"CPA",
"CPAC",
"CPB",
"CPE",
"CPF",
"CPG",
"CPK",
"CPLG",
"CPRI",
"CPS",
"CPSR",
"CPSR.U",
"CPSR.WS",
"CPT",
"CR",
"CRC",
"CRD/A",
"CRD/B",
"CRH",
"CRHC",
"CRHC.U",
"CRHC.WS",
"CRI",
"CRK",
"CRL",
"CRM",
"CRS",
"CRT",
"CRU.U",
"CRY",
"CS",
"CSL",
"CSLT",
"CSPR",
"CSR",
"CSR.PRC",
"CSTM",
"CSU",
"CSV",
"CTA.PRA",
"CTA.PRB",
"CTAA",
"CTAC",
"CTAC.U",
"CTAC.WS",
"CTB",
"CTBB",
"CTDD",
"CTK",
"CTLT",
"CTR",
"CTRA",
"CTS",
"CTT",
"CTVA",
"CUB",
"CUBB",
"CUBE",
"CUBI",
"CUBI.PRC",
"CUBI.PRD",
"CUBI.PRE",
"CUBI.PRF",
"CUK",
"CULP",
"CURO",
"CUZ",
"CVA",
"CVE",
"CVE.WS",
"CVEO",
"CVI",
"CVNA",
"CVS",
"CVX",
"CW",
"CWEN",
"CWEN.A",
"CWH",
"CWK",
"CWT",
"CX",
"CXE",
"CXH",
"CXO",
"CXP",
"CXW",
"CYD",
"CYH",
"CZZ",
"D",
"DAC",
"DAL",
"DAN",
"DAO",
"DAR",
"DASH",
"DAVA",
"DB",
"DBD",
"DBI",
"DBL",
"DCF",
"DCI",
"DCO",
"DCP",
"DCP.PRB",
"DCP.PRC",
"DCUE",
"DD",
"DDD",
"DDF",
"DDS",
"DDT",
"DE",
"DEA",
"DECK",
"DEH",
"DEH.U",
"DEH.WS",
"DEI",
"DELL",
"DEN",
"DEO",
"DESP",
"DEX",
"DFIN",
"DFNS",
"DFNS.U",
"DFNS.WS",
"DFP",
"DFS",
"DG",
"DGNR",
"DGNR.U",
"DGNR.WS",
"DGX",
"DHF",
"DHI",
"DHR",
"DHR.PRA",
"DHR.PRB",
"DHT",
"DHX",
"DIAX",
"DIN",
"DIS",
"DK",
"DKL",
"DKS",
"DL",
"DLB",
"DLNG",
"DLNG.PRA",
"DLNG.PRB",
"DLR",
"DLR.PRC",
"DLR.PRJ",
"DLR.PRK",
"DLR.PRL",
"DLX",
"DLY",
"DM",
"DM.WS",
"DMB",
"DMO",
"DMS",
"DMS.WS",
"DMYD",
"DMYD.U",
"DMYD.WS",
"DMYI",
"DMYI.U",
"DMYI.WS",
"DNB",
"DNK",
"DNMR",
"DNMR.WS",
"DNOW",
"DNP",
"DOC",
"DOOR",
"DOV",
"DOW",
"DPG",
"DPZ",
"DQ",
"DRD",
"DRE",
"DRH",
"DRH.PRA",
"DRI",
"DRQ",
"DRUA",
"DS",
"DS.PRB",
"DS.PRC",
"DS.PRD",
"DSE",
"DSL",
"DSM",
"DSSI",
"DSU",
"DSX",
"DSX.PRB",
"DT",
"DTB",
"DTE",
"DTF",
"DTJ",
"DTLA.PR",
"DTP",
"DTW",
"DTY",
"DUC",
"DUK",
"DUK.PRA",
"DUKB",
"DUKH",
"DVA",
"DVD",
"DVN",
"DWIN.U",
"DX",
"DX.PRB",
"DX.PRC",
"DXC",
"DY",
"DYFN",
"E",
"EAF",
"EAI",
"EARN",
"EAT",
"EB",
"EBF",
"EBR",
"EBR.B",
"EBS",
"EC",
"ECC           ",
"ECCB",
"ECCX",
"ECCY",
"ECL",
"ECOM          ",
"ED",
"EDD",
"EDF",
"EDI",
"EDN",
"EDU",
"EEA",
"EEX",
"EFC",
"EFC.PRA",
"EFF",
"EFL",
"EFR",
"EFT",
"EFX",
"EGF",
"EGHT",
"EGO",
"EGP",
"EGY",
"EHC",
"EHI",
"EHT",
"EIC",
"EIG",
"EIX",
"EL",
"ELAN",
"ELAT",
"ELC",
"ELF",
"ELP",
"ELS",
"ELVT",
"ELY",
"EMD",
"EME",
"EMF",
"EMN",
"EMO",
"EMP",
"EMPW",
"EMPW.U",
"EMPW.WS",
"EMR",
"ENB",
"ENBA",
"ENBL",
"ENIA",
"ENIC",
"ENJ",
"ENLC",
"ENO",
"ENPC",
"ENPC.U",
"ENPC.WS",
"ENR",
"ENR.PRA",
"ENS",
"ENV",
"ENVA",
"ENZ",
"EOD",
"EOG",
"EOI",
"EOS",
"EOT",
"EP.PRC",
"EPAC",
"EPAM",
"EPC",
"EPD",
"EPR",
"EPR.PRC",
"EPR.PRE",
"EPR.PRG",
"EPRT",
"EPWR.U",
"EQC",
"EQC.PRD",
"EQD",
"EQD.U",
"EQD.WS",
"EQH",
"EQH.PRA",
"EQH.PRC",
"EQNR",
"EQR",
"EQS",
"EQT",
"ERF",
"ERJ",
"ES",
"ESE",
"ESGC",
"ESI",
"ESNT",
"ESRT",
"ESS",
"ESTC",
"ESTE",
"ET",
"ETB",
"ETG",
"ETH",
"ETI.PR",
"ETJ",
"ETM",
"ETN",
"ETO",
"ETP.PRC",
"ETP.PRD",
"ETP.PRE",
"ETR",
"ETRN",
"ETV",
"ETW",
"ETX           ",
"ETY",
"EURN",
"EV",
"EVA",
"EVC",
"EVF",
"EVG",
"EVH",
"EVN",
"EVR",
"EVRG",
"EVRI",
"EVT",
"EVTC",
"EW",
"EXD",
"EXG",
"EXK",
"EXP",
"EXPR",
"EXR",
"EXTN",
"F",
"F.PRB",
"F.PRC",
"FAF",
"FAII",
"FAII.U",
"FAII.WS",
"FAM",
"FBC",
"FBHS",
"FBK",
"FBM",
"FBP",
"FC",
"FCAU",
"FCAX.U",
"FCF",
"FCN",
"FCPT",
"FCRW",
"FCRZ",
"FCT",
"FCX",
"FDEU",
"FDP",
"FDX",
"FE",
"FEDU",
"FEI           ",
"FENG",
"FEO",
"FET",
"FF",
"FFA",
"FFC",
"FFG",
"FGB",
"FGNA",
"FGNA.U",
"FGNA.WS",
"FHI",
"FHN",
"FHN.PRA",
"FHN.PRB",
"FHN.PRC",
"FHN.PRD",
"FHN.PRE",
"FI",
"FICO",
"FIF",
"FINS",
"FINV",
"FIS",
"FIV",
"FIX",
"FL",
"FLC",
"FLNG",
"FLO",
"FLOW",
"FLR",
"FLS",
"FLT",
"FLY",
"FMAC",
"FMAC.U",
"FMAC.WS",
"FMC",
"FMN",
"FMO",
"FMS",
"FMX",
"FMY",
"FN",
"FNB",
"FNB.PRE",
"FND",
"FNF",
"FNV",
"FOE",
"FOF",
"FOR",
"FOUR",
"FPAC.U",
"FPF",
"FPH",
"FPI",
"FPI.PRB",
"FPL",
"FR",
"FRA",
"FRC",
"FRC.PRG",
"FRC.PRH",
"FRC.PRI",
"FRC.PRJ",
"FRC.PRK",
"FRO",
"FRT",
"FRT.PRC",
"FRX",
"FRX.U",
"FRX.WS",
"FSD",
"FSK",
"FSKR",
"FSLF",
"FSLY",
"FSM",
"FSR",
"FSR.WS",
"FSS",
"FST",
"FST.U",
"FST.WS",
"FT",
"FTAI",
"FTAI.PRA",
"FTAI.PRB",
"FTCH",
"FTHY",
"FTI",
"FTK",
"FTS",
"FTV",
"FTV.PRA",
"FUBO",
"FUL",
"FUN",
"FUSE",
"FUSE.U",
"FUSE.WS",
"FVRR",
"FVT.U",
"G",
"GAB",
"GAB.PRG",
"GAB.PRH",
"GAB.PRJ",
"GAB.PRK",
"GAM",
"GAM.PRB",
"GATO",
"GATX",
"GB",
"GB.WS",
"GBAB",
"GBL",
"GBX",
"GCI",
"GCO",
"GCP",
"GCV",
"GD",
"GDDY",
"GDL",
"GDL.PRC",
"GDO",
"GDOT",
"GDV",
"GDV.PRG",
"GDV.PRH",
"GE",
"GEF",
"GEF.B",
"GEL",
"GEN           ",
"GEO",
"GER",
"GES",
"GF",
"GFF",
"GFI",
"GFL",
"GFLU",
"GFX.U",
"GGB",
"GGG",
"GGM",
"GGT",
"GGT.PRE",
"GGT.PRG",
"GGZ",
"GGZ.PRA",
"GHC",
"GHG",
"GHL",
"GHLD",
"GHM",
"GHY",
"GIB",
"GIK",
"GIK.U",
"GIK.WS",
"GIL",
"GIM",
"GIS",
"GIX",
"GIX.RT",
"GIX.U",
"GIX.WS",
"GJH",
"GJO",
"GJP",
"GJR",
"GJS",
"GJT",
"GKOS",
"GL",
"GL.PRC",
"GLEO",
"GLEO.U",
"GLEO.WS",
"GLOB",
"GLOG",
"GLOG.PRA",
"GLOP",
"GLOP.PRA",
"GLOP.PRB",
"GLOP.PRC",
"GLP",
"GLP.PRA",
"GLT",
"GLW",
"GM",
"GME",
"GMED",
"GMRE",
"GMRE.PRA",
"GMS",
"GMTA",
"GNE",
"GNE.PRA",
"GNK",
"GNL",
"GNL.PRA",
"GNL.PRB",
"GNPK",
"GNPK.U",
"GNPK.WS",
"GNRC",
"GNT",
"GNT.PRA",
"GNW",
"GOAC",
"GOAC.U",
"GOAC.WS",
"GOF",
"GOL",
"GOLD",
"GOLF",
"GOOS",
"GPC",
"GPI",
"GPJA",
"GPK",
"GPM",
"GPMT",
"GPN",
"GPRK",
"GPS",
"GPX",
"GRA",
"GRC",
"GRP.U",
"GRUB",
"GRX",
"GS",
"GS.PRA",
"GS.PRC",
"GS.PRD",
"GS.PRJ",
"GS.PRK",
"GS.PRN",
"GSAH",
"GSAH.U",
"GSAH.WS",
"GSBD",
"GSK",
"GSL",
"GSL.PRB",
"GSLD",
"GSX",
"GTES",
"GTN",
"GTN.A",
"GTS",
"GTT",
"GTY",
"GUT",
"GUT.PRA",
"GUT.PRC",
"GVA",
"GWB",
"GWRE",
"GWW",
"GYC",
"H",
"HAE",
"HAL",
"HASI",
"HBB",
"HBI",
"HBM",
"HCA",
"HCC",
"HCHC",
"HCI",
"HCXY",
"HCXZ",
"HD",
"HDB",
"HE",
"HEI",
"HEI/A",
"HEP",
"HEQ",
"HES",
"HESM",
"HEXO",
"HFC",
"HFRO",
"HFRO.PRA",
"HGH",
"HGLB",
"HGV",
"HHC",
"HI",
"HIE",
"HIG",
"HIG.PRG",
"HIGA",
"HIGA.U",
"HIGA.WS",
"HII",
"HIL",
"HIO",
"HIW",
"HIX",
"HKIB",
"HL",
"HL.PRB",
"HLF",
"HLI",
"HLT",
"HLX",
"HMC",
"HMI",
"HMLP",
"HMLP.PRA",
"HMN",
"HMY",
"HNGR",
"HNI",
"HNP",
"HOG",
"HOME",
"HON",
"HOV",
"HP",
"HPE",
"HPF",
"HPI",
"HPP",
"HPQ",
"HPR",
"HPS",
"HPX",
"HPX.U",
"HPX.WS",
"HQH",
"HQL",
"HR",
"HRB",
"HRC",
"HRI",
"HRL",
"HRTG",
"HSBC",
"HSC",
"HSY",
"HT",
"HT.PRC",
"HT.PRD",
"HT.PRE",
"HTA",
"HTD",
"HTFA",
"HTGC",
"HTH",
"HTPA.U",
"HTY",
"HUBB",
"HUBS",
"HUM",
"HUN",
"HUYA",
"HVT",
"HVT/A",
"HWM",
"HXL",
"HY",
"HYB",
"HYI",
"HYLN",
"HYT",
"HZAC",
"HZAC.U",
"HZAC.WS",
"HZN",
"HZO",
"HZON",
"HZON.U",
"HZON.WS",
"IAA",
"IACA",
"IACA.U",
"IACA.WS",
"IAE",
"IAG",
"IBA",
"IBM",
"IBN",
"IBP",
"ICD",
"ICE",
"ICL",
"IDA",
"IDE",
"IDT",
"IEX",
"IFF",
"IFFT",
"IFN",
"IFS",
"IGA",
"IGD",
"IGI",
"IGR",
"IGT",
"IH",
"IHC",
"IHD",
"IHG",
"IHIT",
"IHTA",
"IIAC",
"IIAC.U",
"IIAC.WS",
"IID",
"IIF",
"IIM",
"IIPR",
"IIPR.PRA",
"IMAX",
"IMPX",
"IMPX.U",
"IMPX.WS",
"INFO",
"INFY",
"ING",
"INGR",
"INN",
"INN.PRD",
"INN.PRE",
"INSI",
"INSP",
"INSW",
"INSW.PRA",
"INT",
"INVH",
"IO",
"IP",
"IPG",
"IPI",
"IPOD",
"IPOD.U",
"IPOD.WS",
"IPOE",
"IPOE.U",
"IPOE.WS",
"IPOF",
"IPOF.U",
"IPOF.WS",
"IPV",
"IPV.U",
"IPV.WS",
"IQI",
"IQV",
"IR",
"IRL",
"IRM",
"IRR",
"IRS",
"IRT",
"ISD",
"IT",
"ITCB",
"ITGR",
"ITT",
"ITUB",
"ITW",
"IVAN.U",
"IVC",
"IVH",
"IVR",
"IVR.PRA",
"IVR.PRB",
"IVR.PRC",
"IVZ",
"IX",
"J",
"JAX",
"JBGS",
"JBK",
"JBL",
"JBT",
"JCE",
"JCI",
"JCO",
"JDD",
"JE",
"JEF",
"JELD",
"JEMD",
"JEQ",
"JFR",
"JGH",
"JHAA",
"JHB",
"JHG",
"JHI",
"JHS",
"JHX",
"JIH",
"JIH.U",
"JIH.WS",
"JILL",
"JKS",
"JLL",
"JLS",
"JMIA",
"JMM",
"JMP",
"JNJ",
"JNPR",
"JOE",
"JOF",
"JP",
"JPC",
"JPI",
"JPM",
"JPM.PRC",
"JPM.PRD",
"JPM.PRG",
"JPM.PRH",
"JPM.PRJ",
"JPS",
"JPT",
"JQC",
"JRI",
"JRO",
"JRS",
"JSD",
"JT",
"JTA",
"JTD",
"JW/A",
"JW/B",
"JWN",
"JWS",
"JWS.U",
"JWS.WS",
"K",
"KAI",
"KAMN",
"KAR",
"KB",
"KBH",
"KBR",
"KEN",
"KEP",
"KEX",
"KEY",
"KEY.PRI",
"KEY.PRJ",
"KEY.PRK",
"KEYS",
"KF",
"KFS",
"KFY",
"KGC",
"KIM",
"KIM.PRL",
"KIM.PRM",
"KIO",
"KKR",
"KKR.PRA",
"KKR.PRB",
"KKR.PRC",
"KL",
"KMB",
"KMF",
"KMI",
"KMPR",
"KMT",
"KMX",
"KN",
"KNL",
"KNOP",
"KNX",
"KO",
"KODK",
"KOF",
"KOP",
"KOS",
"KR",
"KRA",
"KRC",
"KREF",
"KRG",
"KRO",
"KRP",
"KSM",
"KSS",
"KSU",
"KSU.PR",
"KT",
"KTB",
"KTF",
"KTH",
"KTN",
"KUKE",
"KW",
"KWAC.U",
"KWR",
"KYN",
"L",
"LAC",
"LAD",
"LADR",
"LAIX",
"LAZ",
"LB",
"LBRT",
"LC",
"LCI",
"LCII",
"LDL",
"LDOS",
"LDP",
"LEA",
"LEAF",
"LEAP",
"LEAP.U",
"LEAP.WS",
"LEE",
"LEG",
"LEJU",
"LEN",
"LEN.B",
"LEO",
"LEVI",
"LFC",
"LFT",
"LGF.A",
"LGF.B",
"LGI",
"LGVW",
"LGVW.U",
"LGVW.WS",
"LH",
"LHC.U",
"LHX",
"LII",
"LIN",
"LINX",
"LITB",
"LL",
"LLY",
"LMND",
"LMT",
"LNC",
"LND",
"LNFA",
"LNFA.U",
"LNFA.WS",
"LNN",
"LOKB.U",
"LOMA",
"LOW",
"LPG",
"LPI",
"LPL",
"LPX",
"LRN",
"LSI",
"LSPD",
"LTC",
"LTHM",
"LU",
"LUB",
"LUMN",
"LUV",
"LVS",
"LW",
"LXP",
"LXP.PRC",
"LXU",
"LYB",
"LYG",
"LYV",
"LZB",
"M",
"MA",
"MAA",
"MAA.PRI",
"MAC",
"MAIN",
"MAN",
"MANU",
"MAS",
"MATX",
"MAV",
"MAX",
"MAXR",
"MBI",
"MBT",
"MC",
"MCA",
"MCB",
"MCD",
"MCI",
"MCK",
"MCN",
"MCO",
"MCR",
"MCS",
"MCY",
"MD",
"MDC",
"MDLA",
"MDLQ",
"MDLX",
"MDLY",
"MDP",
"MDT",
"MDU",
"MEC",
"MED",
"MEG",
"MEI",
"MEN",
"MER.PRK",
"MET",
"MET.PRA",
"MET.PRE",
"MET.PRF",
"MFA",
"MFA.PRB",
"MFA.PRC",
"MFC",
"MFD",
"MFG",
"MFGP",
"MFL",
"MFM",
"MFT",
"MFV",
"MG",
"MGA",
"MGF",
"MGM",
"MGP",
"MGR",
"MGRB",
"MGU",
"MGY",
"MH.PRA",
"MH.PRC",
"MH.PRD",
"MHD",
"MHE",
"MHF",
"MHI",
"MHK",
"MHLA",
"MHN",
"MHNC",
"MHO",
"MIC",
"MIE",
"MIN",
"MITT",
"MITT.PRA",
"MITT.PRB",
"MITT.PRC",
"MIXT",
"MIY",
"MKC",
"MKC.V",
"MKL",
"MLI",
"MLM",
"MLP",
"MLR",
"MMC",
"MMD",
"MMI",
"MMM",
"MMP",
"MMS",
"MMT",
"MMU",
"MN",
"MNP",
"MNR",
"MNR.PRC",
"MNRL",
"MNSO",
"MO",
"MOD",
"MODN",
"MOG.A",
"MOG.B",
"MOGU",
"MOH",
"MOS",
"MOTV.U",
"MOV",
"MP",
"MP.WS",
"MPA",
"MPC",
"MPLN",
"MPLN.WS",
"MPLX",
"MPV",
"MPW",
"MPX",
"MQT",
"MQY",
"MRC",
"MRK",
"MRO",
"MS",
"MS.PRA",
"MS.PRE",
"MS.PRF",
"MS.PRI",
"MS.PRK",
"MS.PRL",
"MSA",
"MSB",
"MSC",
"MSCI",
"MSD",
"MSGE",
"MSGN",
"MSGS",
"MSI",
"MSM",
"MSP",
"MT",
"MTB",
"MTCN",
"MTD",
"MTDR",
"MTG",
"MTH",
"MTL",
"MTL.PR",
"MTN",
"MTOR",
"MTR",
"MTRN",
"MTT",
"MTW",
"MTX",
"MTZ",
"MUA",
"MUC",
"MUE",
"MUFG",
"MUH",
"MUI",
"MUJ",
"MUR",
"MUS",
"MUSA",
"MUX",
"MVF",
"MVO",
"MVT",
"MWA",
"MX",
"MXE",
"MXF",
"MXL",
"MYC",
"MYD",
"MYE",
"MYF",
"MYI",
"MYJ",
"MYN",
"MYOV",
"MZA",
"NAC",
"NAD",
"NAN",
"NAT",
"NAV",
"NAV.PRD",
"NAZ",
"NBB",
"NBHC",
"NBR",
"NBR.PRA",
"NC",
"NCA",
"NCB",
"NCLH",
"NCR",
"NCV",
"NCV.PRA",
"NCZ",
"NCZ.PRA",
"NDMO",
"NDP",
"NEA",
"NEE",
"NEE.PRK",
"NEE.PRN",
"NEE.PRO",
"NEE.PRP",
"NEE.PRQ",
"NEM",
"NEP",
"NET",
"NEU",
"NEV",
"NEW",
"NEWR",
"NEX",
"NEXA",
"NFG",
"NFH",
"NFH.WS",
"NFJ",
"NGA",
"NGA.U",
"NGA.WS",
"NGAB.U",
"NGG",
"NGL",
"NGL.PRB",
"NGL.PRC",
"NGS",
"NGVC",
"NGVT",
"NHA",
"NHF",
"NHF.PRA",
"NHI",
"NI",
"NI.PRB",
"NID",
"NIE",
"NIM",
"NINE",
"NIO",
"NIQ",
"NJR",
"NJV",
"NKE",
"NKG",
"NKX",
"NL",
"NLS",
"NLSN",
"NLY",
"NLY.PRF",
"NLY.PRG",
"NLY.PRI",
"NM",
"NM.PRG",
"NM.PRH",
"NMCO",
"NMI",
"NMK.PRB",
"NMK.PRC",
"NMM",
"NMR",
"NMS",
"NMT",
"NMY",
"NMZ",
"NNA",
"NNI",
"NNN",
"NNN.PRF",
"NNY",
"NOA",
"NOAH",
"NOC",
"NOK",
"NOM",
"NOMD",
"NOV",
"NOVA",
"NOW",
"NP",
"NPK",
"NPN",
"NPO",
"NPTN",
"NPV",
"NQP",
"NR",
"NREF",
"NREF.PRA",
"NRG",
"NRGX",
"NRK",
"NRP",
"NRT",
"NRUC",
"NRZ",
"NRZ.PRA",
"NRZ.PRB",
"NRZ.PRC",
"NS",
"NS.PRA",
"NS.PRB",
"NS.PRC",
"NSA",
"NSA.PRA",
"NSC",
"NSCO",
"NSCO.WS",
"NSH",
"NSH.U",
"NSH.WS",
"NSL",
"NSP",
"NSS",
"NTB",
"NTCO",
"NTG",
"NTP",
"NTR",
"NTST",
"NTZ",
"NUE",
"NUM",
"NUO",
"NUS",
"NUV",
"NUW",
"NVG",
"NVGS",
"NVO",
"NVR",
"NVRO",
"NVS",
"NVST",
"NVT",
"NVTA",
"NWG",
"NWHM",
"NWN",
"NX",
"NXC",
"NXJ",
"NXN",
"NXP",
"NXQ",
"NXR",
"NXRT",
"NYC",
"NYCB",
"NYCB.PRA",
"NYCB.PRU",
"NYT",
"NYV",
"NZF",
"O",
"OAC",
"OAC.U",
"OAC.WS",
"OACB",
"OACB.U",
"OACB.WS",
"OAK.PRA",
"OAK.PRB",
"OC",
"OCA",
"OCA.U",
"OCA.WS",
"OCFT",
"OCN",
"ODC",
"OEC",
"OFC",
"OFG",
"OFG.PRA",
"OFG.PRB",
"OFG.PRD",
"OGE",
"OGS",
"OHI",
"OI",
"OIA",
"OIBR.C",
"OII",
"OIS",
"OKE",
"OLN",
"OLP",
"OMC",
"OMF",
"OMI",
"ONE",
"ONTO",
"OOMA",
"OPP",
"OPP.PRA",
"OPY",
"OR",
"ORA",
"ORAN",
"ORC",
"ORCC",
"ORCL",
"ORI",
"ORN",
"OSB",
"OSG",
"OSH",
"OSK",
"OTIS",
"OUT",
"OVV",
"OXM",
"OXY",
"OXY.WS",
"PAC",
"PACE",
"PACE.U",
"PACE.WS",
"PACK",
"PAG",
"PAGS",
"PAI",
"PAM",
"PANA",
"PANA.U",
"PANA.WS",
"PANW",
"PAR",
"PARR",
"PAYC",
"PB",
"PBA",
"PBB",
"PBC",
"PBF",
"PBFX",
"PBH",
"PBI",
"PBI.PRB",
"PBR",
"PBR.A",
"PBT",
"PBY",
"PCF",
"PCG",
"PCGU",
"PCI",
"PCK",
"PCM",
"PCN",
"PCPC.U",
"PCPL",
"PCPL.U",
"PCPL.WS",
"PCQ",
"PD",
"PDAC",
"PDAC.U",
"PDAC.WS",
"PDI",
"PDM",
"PDS",
"PDT",
"PEAK",
"PEB",
"PEB.PRC",
"PEB.PRD",
"PEB.PRE",
"PEB.PRF",
"PEG",
"PEI",
"PEI.PRB",
"PEI.PRC",
"PEI.PRD",
"PEN",
"PEO",
"PFD",
"PFE",
"PFGC",
"PFH",
"PFL",
"PFN",
"PFO",
"PFS",
"PFSI",
"PG",
"PGP",
"PGR",
"PGRE",
"PGTI",
"PGZ",
"PH",
"PHD",
"PHG",
"PHI",
"PHK",
"PHM",
"PHR",
"PHT",
"PHX",
"PIAI",
"PIAI.U",
"PIAI.WS",
"PII",
"PIM",
"PINE",
"PING",
"PINS",
"PIPP",
"PIPP.U",
"PIPP.WS",
"PIPR",
"PJT",
"PK",
"PKE",
"PKG",
"PKI",
"PKO",
"PKX",
"PLAN",
"PLD",
"PLNT",
"PLOW",
"PLT",
"PLTR",
"PLYM",
"PM",
"PMF",
"PML",
"PMM",
"PMO",
"PMT",
"PMT.PRA",
"PMT.PRB",
"PMVC",
"PMVC.U",
"PMVC.WS",
"PMX",
"PNC",
"PNC.PRP",
"PNF",
"PNI",
"PNM",
"PNR",
"PNTM.U",
"PNW",
"POR",
"POST",
"PPG",
"PPL",
"PPR",
"PPT",
"PPX",
"PQG",
"PRA",
"PRE.PRG",
"PRE.PRH",
"PRE.PRI",
"PRG",
"PRGO",
"PRI",
"PRIF.PRA",
"PRIF.PRB",
"PRIF.PRC",
"PRIF.PRD",
"PRIF.PRE",
"PRIF.PRF",
"PRLB",
"PRMW",
"PRO",
"PROS",
"PRPB",
"PRPB.U",
"PRPB.WS",
"PRS",
"PRSP",
"PRT",
"PRTY",
"PRU",
"PSA",
"PSA.PRB",
"PSA.PRC",
"PSA.PRD",
"PSA.PRE",
"PSA.PRF",
"PSA.PRG",
"PSA.PRH",
"PSA.PRI",
"PSA.PRJ",
"PSA.PRK",
"PSA.PRL",
"PSA.PRM",
"PSA.PRN",
"PSA.PRO",
"PSB",
"PSB.PRW",
"PSB.PRX",
"PSB.PRY",
"PSB.PRZ",
"PSF",
"PSN",
"PSO",
"PSTG",
"PSTH",
"PSTH.WS",
"PSTL",
"PSX",
"PSXP",
"PTA",
"PTR",
"PTY",
"PUK",
"PUK.PR",
"PUK.PRA",
"PUMP",
"PVG",
"PVH",
"PVL",
"PWR",
"PXD",
"PYN",
"PYS",
"PYT",
"PZC",
"PZN",
"QD",
"QEP",
"QGEN",
"QS",
"QS.WS",
"QSR",
"QTS",
"QTS.PRA",
"QTS.PRB",
"QTWO",
"QUAD",
"QUOT",
"QVCC",
"QVCD",
"R",
"RA",
"RACE",
"RAD",
"RAMP",
"RBA",
"RBAC",
"RBAC.U",
"RBAC.WS",
"RBC",
"RC",
"RCA",
"RCB",
"RCI",
"RCL",
"RCP",
"RCS",
"RCUS",
"RDN",
"RDS.A",
"RDS/B",
"RDY",
"RE",
"RELX",
"RENN",
"RES",
"REV",
"REVG",
"REX",
"REXR",
"REXR.PRA",
"REXR.PRB",
"REXR.PRC",
"REZI",
"RF",
"RF.PRA",
"RF.PRB",
"RF.PRC",
"RFI",
"RFL",
"RFM",
"RFP",
"RGA",
"RGR",
"RGS",
"RGT",
"RH",
"RHI",
"RHP",
"RICE",
"RICE.U",
"RICE.WS",
"RIG",
"RIO",
"RIV",
"RJF",
"RKT",
"RL",
"RLGY",
"RLH",
"RLI",
"RLJ",
"RLJ.PRA",
"RM",
"RMAX",
"RMD",
"RMI",
"RMM",
"RMO",
"RMO.WS",
"RMPL.PR",
"RMT",
"RNG",
"RNGR",
"RNP",
"RNR",
"RNR.PRE",
"RNR.PRF",
"ROG",
"ROK",
"ROL",
"ROP",
"ROT.U",
"RPAI",
"RPLA",
"RPLA.U",
"RPLA.WS",
"RPM",
"RPT",
"RPT.PRD",
"RQI",
"RRC",
"RRD",
"RS",
"RSF",
"RSG",
"RSI",
"RSI.WS",
"RTP",
"RTP.U",
"RTP.WS",
"RTPZ",
"RTPZ.U",
"RTPZ.WS",
"RTX",
"RVI",
"RVLV",
"RVT",
"RWT",
"RXN",
"RY",
"RY.PRT",
"RYAM",
"RYB",
"RYI",
"RYN",
"RZA",
"RZB",
"SA",
"SAF",
"SAFE",
"SAH",
"SAIC",
"SAIL",
"SAK",
"SALT",
"SAM",
"SAN",
"SAND          ",
"SAP",
"SAR",
"SAVE",
"SB",
"SB.PRC",
"SB.PRD",
"SBBA",
"SBE",
"SBE.U",
"SBE.WS",
"SBG",
"SBG.U",
"SBG.WS",
"SBH",
"SBI",
"SBOW",
"SBR",
"SBS",
"SBSW",
"SC",
"SCA",
"SCCO",
"SCD",
"SCE.PRG",
"SCE.PRH",
"SCE.PRJ",
"SCE.PRK",
"SCE.PRL",
"SCHW",
"SCHW.PRC",
"SCHW.PRD",
"SCI",
"SCL",
"SCM",
"SCPE",
"SCPE.U",
"SCPE.WS",
"SCS",
"SCU",
"SCVX",
"SCVX.U",
"SCVX.WS",
"SCX",
"SD",
"SDHY",
"SE",
"SEAH",
"SEAH.U",
"SEAH.WS",
"SEAS",
"SEE",
"SEM",
"SF",
"SF.PRA",
"SF.PRB",
"SF.PRC",
"SFB",
"SFE",
"SFL",
"SFTW",
"SFTW.U",
"SFTW.WS",
"SFUN",
"SGU",
"SHAK",
"SHG",
"SHI",
"SHLX",
"SHO",
"SHO.PRE",
"SHO.PRF",
"SHOP",
"SHW",
"SI",
"SID",
"SIG",
"SII",
"SITC",
"SITC.PRA",
"SITC.PRK",
"SITE",
"SIX",
"SJI",
"SJIJ",
"SJIU",
"SJM",
"SJR",
"SJT",
"SJW",
"SKLZ",
"SKLZ.WS",
"SKM",
"SKT",
"SKX",
"SKY",
"SLB",
"SLCA",
"SLF",
"SLG",
"SLG.PRI",
"SLQT",
"SM",
"SMAR",
"SMFG",
"SMG",
"SMHI",
"SMLP",
"SMM",
"SMP",
"SNA",
"SNAP",
"SNDR",
"SNE",
"SNN",
"SNOW",
"SNP",
"SNPR",
"SNPR.U",
"SNPR.WS",
"SNR",
"SNV",
"SNV.PRD",
"SNV.PRE",
"SNX",
"SO",
"SOAC",
"SOAC.U",
"SOAC.WS",
"SOGO",
"SOI",
"SOJB",
"SOJC",
"SOJD",
"SOJE",
"SOL",
"SOLN",
"SON",
"SOR",
"SOS",
"SPB",
"SPCE",
"SPE",
"SPE.PRB",
"SPFR.U",
"SPG",
"SPG.PRJ",
"SPGI",
"SPH",
"SPLP",
"SPLP.PRA",
"SPNV",
"SPNV.U",
"SPNV.WS",
"SPOT",
"SPR",
"SPRQ",
"SPRQ.U",
"SPRQ.WS",
"SPXC",
"SPXX",
"SQ",
"SQM",
"SQNS",
"SQZ",
"SR",
"SR.PRA",
"SRC",
"SRC.PRA",
"SRE",
"SRE.PRB",
"SREA",
"SRG",
"SRG.PRA",
"SRI",
"SRL",
"SRLP",
"SRT",
"SRV",
"SSD",
"SSL",
"SSTK",
"ST",
"STAG",
"STAG.PRC",
"STAR          ",
"STAR.PRD",
"STAR.PRG",
"STAR.PRI",
"STC",
"STE",
"STG",
"STIC",
"STIC.U",
"STIC.WS",
"STK",
"STL",
"STL.PRA",
"STM",
"STN",
"STNG",
"STON",
"STOR",
"STPC.U",
"STPK",
"STPK.U",
"STPK.WS",
"STT",
"STT.PRD",
"STT.PRG",
"STWD",
"STZ",
"STZ/B",
"SU",
"SUI",
"SUM",
"SUN",
"SUP",
"SUPV",
"SUZ",
"SWBK.U",
"SWCH",
"SWI",
"SWK",
"SWM",
"SWN",
"SWT",
"SWX",
"SWZ",
"SXC",
"SXI",
"SXT",
"SYF",
"SYF.PRA",
"SYK",
"SYX",
"SYY",
"SZC",
"T",
"T.PRA",
"T.PRC",
"TAC",
"TACA.U",
"TAK",
"TAL",
"TALO",
"TAP",
"TAP.A",
"TARO",
"TBA",
"TBB",
"TBC",
"TBI",
"TCI",
"TCP",
"TCS",
"TD",
"TDA",
"TDC",
"TDE",
"TDF",
"TDG",
"TDI",
"TDJ",
"TDOC",
"TDS",
"TDW",
"TDW.WS.A",
"TDW.WS.B",
"TDY",
"TEAF",
"TECK",
"TEF",
"TEI",
"TEL",
"TEN",
"TEO",
"TEVA",
"TEX",
"TFC",
"TFC.PRF",
"TFC.PRG",
"TFC.PRH",
"TFC.PRI",
"TFC.PRO",
"TFC.PRR",
"TFII",
"TFX",
"TG",
"TGH",
"TGI",
"TGNA",
"TGP",
"TGP.PRA",
"TGP.PRB",
"TGS",
"TGT",
"THC",
"THG",
"THO",
"THQ",
"THR",
"THS",
"THW",
"TIMB",
"TINV",
"TINV.U",
"TINV.WS",
"TISI",
"TJX",
"TK",
"TKC",
"TKR",
"TLK",
"TLYS",
"TM",
"TME",
"TMHC",
"TMO",
"TMST",
"TMX",
"TNC",
"TNET",
"TNK",
"TNP",
"TNP.PRD",
"TNP.PRE",
"TNP.PRF",
"TOL",
"TOT",
"TPB",
"TPC",
"TPGY",
"TPGY.U",
"TPGY.WS",
"TPH",
"TPL",
"TPR",
"TPRE",
"TPVG",
"TPVY",
"TPX",
"TPZ",
"TR",
"TRC",
"TREB",
"TREB.U",
"TREB.WS",
"TREC",
"TREX",
"TRGP",
"TRI",
"TRN",
"TRNO",
"TROX",
"TRP",
"TRQ",
"TRTN",
"TRTN.PRA",
"TRTN.PRB",
"TRTN.PRC",
"TRTN.PRD",
"TRTX",
"TRU",
"TRV",
"TS",
"TSE",
"TSI",
"TSLX",
"TSM",
"TSN",
"TSQ",
"TT",
"TTC",
"TTI",
"TTM",
"TTP",
"TU",
"TUFN",
"TUP",
"TV",
"TVC",
"TVE",
"TWI",
"TWLO",
"TWN",
"TWND",
"TWND.U",
"TWND.WS",
"TWO",
"TWO.PRA",
"TWO.PRB",
"TWO.PRC",
"TWO.PRD",
"TWO.PRE",
"TWTR",
"TX",
"TXT",
"TY",
"TY.PR",
"TYG",
"TYL",
"U",
"UA",
"UAA",
"UAN",
"UBA",
"UBER",
"UBP",
"UBP.PRH",
"UBP.PRK",
"UBS",
"UDR",
"UE",
"UFI",
"UFS",
"UGI",
"UGP",
"UHS",
"UHT",
"UI",
"UIS",
"UL",
"UMC",
"UMH",
"UMH.PRC",
"UMH.PRD",
"UNF",
"UNFI",
"UNH",
"UNM",
"UNMA",
"UNP",
"UNVR",
"UPS",
"URI",
"USA",
"USAC",
"USB",
"USB.PRA",
"USB.PRH",
"USB.PRM",
"USB.PRP",
"USB.PRQ",
"USDP",
"USFD",
"USM",
"USNA",
"USPH",
"USX",
"UTF",
"UTI",
"UTL",
"UTZ",
"UVE",
"UVV",
"UZA",
"UZB",
"UZC",
"UZD",
"UZE",
"V",
"VAC",
"VALE",
"VAPO",
"VAR",
"VBF",
"VCIF",
"VCRA",
"VCV",
"VEC",
"VEDL",
"VEEV",
"VEL",
"VER",
"VER.PRF",
"VERT.U",
"VET",
"VFC",
"VGAC",
"VGAC.U",
"VGAC.WS",
"VGI",
"VGM",
"VGR",
"VHC",
"VHI",
"VIAO",
"VICI",
"VIPS",
"VIST",
"VIV",
"VKQ",
"VLO",
"VLRS",
"VLT",
"VMC",
"VMI",
"VMO",
"VMW",
"VNCE",
"VNE",
"VNO",
"VNO.PRK",
"VNO.PRL",
"VNO.PRM",
"VNO.PRN",
"VNT",
"VNTR",
"VOC",
"VOYA",
"VOYA.PRB",
"VPG",
"VPV",
"VRS",
"VRT",
"VRT.WS",
"VRTV",
"VSH",
"VST",
"VST.WS.A",
"VSTO",
"VTA",
"VTN",
"VTOL",
"VTR",
"VVI",
"VVNT",
"VVR",
"VVV",
"VYGG",
"VYGG.U",
"VYGG.WS",
"W",
"WAB",
"WAL",
"WALA",
"WAT",
"WBAI",
"WBK",
"WBS",
"WBS.PRF",
"WBT",
"WCC",
"WCC.PRA",
"WCN",
"WD",
"WDR",
"WEA",
"WEC",
"WEI",
"WELL",
"WES",
"WEX",
"WF",
"WFC",
"WFC.PRA",
"WFC.PRL",
"WFC.PRN",
"WFC.PRO",
"WFC.PRP",
"WFC.PRQ",
"WFC.PRR",
"WFC.PRW",
"WFC.PRX",
"WFC.PRY",
"WFC.PRZ",
"WGO",
"WH",
"WHD",
"WHG",
"WHR",
"WIA",
"WIT",
"WIW",
"WK",
"WLK",
"WLKP",
"WLL",
"WM",
"WMB",
"WMC",
"WMK",
"WMS",
"WMT",
"WNC",
"WNS",
"WOR",
"WORK",
"WOW",
"WPC",
"WPF",
"WPF.U",
"WPF.WS",
"WPG",
"WPG.PRH",
"WPG.PRI",
"WPM",
"WPP",
"WRB",
"WRB.PRC",
"WRB.PRD",
"WRB.PRE",
"WRB.PRF",
"WRB.PRG",
"WRE",
"WRI",
"WRK",
"WSM",
"WSO",
"WSO/B",
"WSR",
"WST",
"WTI",
"WTM",
"WTRG",
"WTRU",
"WTS",
"WTTR",
"WU",
"WWE",
"WWW",
"WY",
"WYND",
"X",
"XAN",
"XAN.PRC",
"XEC",
"XFLT",
"XHR",
"XIN",
"XL",
"XL.WS",
"XOM",
"XPEV",
"XPO",
"XPOA",
"XPOA.U",
"XPOA.WS",
"XRX",
"XYF",
"XYL",
"Y",
"YAC",
"YAC.U",
"YAC.WS",
"YALA",
"YELP",
"YETI",
"YEXT",
"YPF",
"YRD",
"YSG",
"YUM",
"YUMC",
"ZBH",
"ZEN",
"ZNH",
"ZTO",
"ZTR",
"ZTS",
"ZUO",
"ZYME"
}



subreddit = reddit.subreddit("wallstreetbets")


results = []
#convert to json
#json format
# {
#   "stockTicker":
#   "title":
#   "selfText": contents of post
#   "score":
#   "comments": 
#   "linkFlairText":
#   "totalAwardsReceived":
# }



def getCommentConcatenated(submission):
  commentConcatenated = ""
  submission.comments.replace_more(limit=None)
  for comment in submission.comments.list():
      commentConcatenated += comment.body
  return commentConcatenated





for submission in subreddit.controversial(limit=10000):
  target = re.compile('[$][A-Za-z][\S]*')
  result = {}
  if re.match(target, submission.title):
      #could be a post that has a ticker (does this first to elimate unnecessary checks in set)
      candidate = target.search(submission.title).group()
      candidateWithDollarSign = candidate[1:] #the detected stock ticker without $
      if candidateWithDollarSign in tickerSet:
       #definitely a post that has ticker
        stockTicker = candidateWithDollarSign
        title = submission.title
        selfText = submission.selftext
        score = submission.score
        comments = getCommentConcatenated(submission)
        linkFlairText = submission.link_flair_text
        totalAwardsReceived = submission.total_awards_received


        result = {
          "stockTicker":stockTicker,
          "title": title,
          "selfText": selfText,
          "score": score,
          "comment": comments,
          "linkFlairText": linkFlairText,
          "totalAwardsReceived": totalAwardsReceived
        }
        results.append(result)



for submission in subreddit.hot(limit=10000):
  target = re.compile('[$][A-Za-z][\S]*')
  result = {}
  if re.match(target, submission.title):
      #could be a post that has a ticker (does this first to elimate unnecessary checks in set)
      candidate = target.search(submission.title).group()
      candidateWithDollarSign = candidate[1:] #the detected stock ticker without $
      if candidateWithDollarSign in tickerSet:
       #definitely a post that has ticker
        stockTicker = candidateWithDollarSign
        title = submission.title
        selfText = submission.selftext
        score = submission.score
        comments = getCommentConcatenated(submission)
        linkFlairText = submission.link_flair_text
        totalAwardsReceived = submission.total_awards_received


        result = {
          "stockTicker":stockTicker,
          "title": title,
          "selfText": selfText,
          "score": score,
          "comment": comments,
          "linkFlairText": linkFlairText,
          "totalAwardsReceived": totalAwardsReceived
        }
        results.append(result)



for submission in subreddit.new(limit=10000):
  target = re.compile('[$][A-Za-z][\S]*')
  result = {}
  if re.match(target, submission.title):
      #could be a post that has a ticker (does this first to elimate unnecessary checks in set)
      candidate = target.search(submission.title).group()
      candidateWithDollarSign = candidate[1:] #the detected stock ticker without $
      if candidateWithDollarSign in tickerSet:
       #definitely a post that has ticker
        stockTicker = candidateWithDollarSign
        title = submission.title
        selfText = submission.selftext
        score = submission.score
        comments = getCommentConcatenated(submission)
        linkFlairText = submission.link_flair_text
        totalAwardsReceived = submission.total_awards_received


        result = {
          "stockTicker":stockTicker,
          "title": title,
          "selfText": selfText,
          "score": score,
          "comment": comments,
          "linkFlairText": linkFlairText,
          "totalAwardsReceived": totalAwardsReceived
        }
        results.append(result)

for submission in subreddit.rising(limit=10000):
  target = re.compile('[$][A-Za-z][\S]*')
  result = {}
  if re.match(target, submission.title):
      #could be a post that has a ticker (does this first to elimate unnecessary checks in set)
      candidate = target.search(submission.title).group()
      candidateWithDollarSign = candidate[1:] #the detected stock ticker without $
      if candidateWithDollarSign in tickerSet:
       #definitely a post that has ticker
        stockTicker = candidateWithDollarSign
        title = submission.title
        selfText = submission.selftext
        score = submission.score
        comments = getCommentConcatenated(submission)
        linkFlairText = submission.link_flair_text
        totalAwardsReceived = submission.total_awards_received


        result = {
          "stockTicker":stockTicker,
          "title": title,
          "selfText": selfText,
          "score": score,
          "comment": comments,
          "linkFlairText": linkFlairText,
          "totalAwardsReceived": totalAwardsReceived
        }
        results.append(result)
        

for submission in subreddit.top(limit=10000):
  target = re.compile('[$][A-Za-z][\S]*')
  result = {}
  if re.match(target, submission.title):
      #could be a post that has a ticker (does this first to elimate unnecessary checks in set)
      candidate = target.search(submission.title).group()
      candidateWithDollarSign = candidate[1:] #the detected stock ticker without $
      if candidateWithDollarSign in tickerSet:
       #definitely a post that has ticker
        stockTicker = candidateWithDollarSign
        title = submission.title
        selfText = submission.selftext
        score = submission.score
        comments = getCommentConcatenated(submission)
        linkFlairText = submission.link_flair_text
        totalAwardsReceived = submission.total_awards_received


        result = {
          "stockTicker":stockTicker,
          "title": title,
          "selfText": selfText,
          "score": score,
          "comment": comments,
          "linkFlairText": linkFlairText,
          "totalAwardsReceived": totalAwardsReceived
        }
        results.append(result)


print(len(results))


with open("sample.json", "w") as outfile:  
    json.dump(results, outfile) 



    