from pyrogram import Client, filters, idle
import asyncio 

from pyrogram.errors import FloodWait
# Ganti dengan token bot Anda
API_ID = 21445722
API_HASH = "710f18f90849255dd85837d00d5fe85f"
BOT_TOKEN = "6976707406:AAE5RJn-W-H1NKGvkiu0EG3zH88LBiQYsN8"

app = Client("video_forward_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Fungsi untuk meneruskan video dari satu grup ke grup lainnya

loop = asyncio.get_event_loop()
# Handler untuk menerima pesan video dan meneruskannya 80

#data2 = [34459, 34458, 34457, 34456, 34455, 34454, 34453, 34452, 34451, 34450, 34449, 34448, 34447, 34446, 34445, 34444, 34443, 34442, 34441, 34440, 34439, 34438, 34437, 34436, 34435, 34434, 34433, 34432, 34431, 34430, 34429, 34428, 34427, 34426, 34425, 34424, 34423, 34422, 34421, 34420, 34419, 34418, 34417, 34416, 34415, 34414, 34413, 34412, 34411, 34410, 34409, 34408, 34407, 34406, 34405, 34404, 34403, 34402, 34401, 34400, 34399, 34398, 34397, 34396, 34395, 34394, 34393, 34392, 34391, 34390, 34389, 34388, 34387, 34386, 34385, 34384, 34383, 34382, 34381, 34380, 34379, 34378, 34377, 34376, 34375, 34374, 34373, 34151, 33883, 33826, 33789, 33773, 33772, 33771, 33770, 33755, 33745, 33425, 33342, 33288, 32885, 31960, 30790, 30668, 30550, 30393, 30389, 29994, 29993, 29717, 29715, 29711, 29570, 29328, 29181, 29120, 29069, 29057, 29006, 28932, 28738, 28734, 28590, 28414, 28413, 28412, 28411, 28410, 28396, 28390, 28349, 28348, 27836, 26759, 26671, 26656, 26529, 26404, 26386, 26167, 26060, 25560, 25503, 24666, 24552, 24483, 24474, 24426, 24263, 23918, 23618, 23345, 23291, 22561, 22405, 22292, 22187, 22009, 21388, 21381, 21380, 21379, 21378, 21377, 21298, 21297, 21296, 21295, 21294, 21293, 21292, 21291, 21290, 21289, 21288, 21287, 21286, 21285, 21284, 21283, 21282, 21281, 21280, 21278, 21277, 21276, 21275, 21274, 21273, 21272, 21271, 21270, 21267, 21266, 21263, 21262, 21261, 21260, 21259, 21258, 21257, 21256, 21249, 21248, 21247, 21246, 21245, 21244, 21243, 21242, 21241, 21240, 21237, 21171, 21152, 21050, 20840, 20699, 20490, 20441, 20396, 20373, 20372, 20371, 20370, 20369, 20362, 20361, 20360, 20359, 20358, 20357, 20356, 20296, 20214, 20145, 19827, 19743, 19366, 19107, 18843, 18731, 18635, 18607, 18436, 18435, 18431, 18172, 18171, 18170, 18169, 18168, 18166, 18054, 17910, 17909, 17908, 17907, 17906, 17904, 17896, 17892, 17855, 17854, 17853, 17852, 17848, 17847, 17846, 17845, 17844, 17843, 17842, 17841, 17840, 17839, 17838, 17837, 17836, 17835, 17834, 17833, 17832, 17831, 17829, 17828, 17827, 17826, 17825, 17824, 17823, 17822, 17821, 17820, 17819, 17818, 17817, 17816, 17815, 17814, 17813, 17812, 17811, 17810, 17809, 17808, 17807, 17789, 17787, 17755, 17754, 17708, 17075, 16886, 16753, 16474, 15892, 15654, 15592, 15522, 15480, 15435, 15225, 15116, 15093, 15085, 15028, 15027, 15025, 15024, 15023]
data = [36394, 36301, 36285, 36139, 36127, 36126, 36082, 36053, 35622, 35475, 35474, 35325, 35324, 35323, 35322, 35321, 35320, 35319, 35317, 35316, 35315, 35309, 35301, 35205, 35201, 35200, 34987, 34049, 34025, 33974, 33508, 33274, 33254, 33214, 33213, 33211, 33207, 33056, 33055, 32861, 31914, 31913, 31912, 31251, 31245, 31087, 30572, 30571, 30112, 29817, 29731, 29413, 29412, 29411, 29410, 29409, 29408, 29407, 29406, 29405, 29404, 29403, 29402, 29401, 29400, 29399, 29398, 29397, 29396, 29395, 29394, 29393, 29392, 29389, 29388, 29387, 29386, 29385, 29384, 29383, 29382, 29381, 29380, 29379, 29378, 29377, 29376, 29375, 29374, 29373, 29372, 29371, 29370, 29369, 29368, 29363, 29052, 28613, 28507, 28506, 28256, 28238, 28237, 28236, 27470, 26240, 26239, 25826, 24693, 24405, 24193, 23147, 22540, 22539, 22538, 22537, 22536, 22535, 22534, 22533, 22532, 22531, 22530, 22529, 22528, 22527, 22526, 22525, 22524, 22523, 22522, 22521, 22520, 22519, 22518, 22517, 22516, 22515, 22514, 22513, 22512, 22511, 22510, 22482, 22121, 22119, 22118, 22117, 22002, 21955, 21928, 21693, 21269, 21130, 21122, 21100, 21099, 21098, 21097, 21072, 20960, 20959, 20957, 20956, 20955, 20924, 20922, 20921, 20920, 20919, 20918, 20917, 20916, 20915, 20914, 20913, 20912, 20911, 20910, 20909, 20908, 20907, 20906, 20905, 20904, 20903, 20902, 20901, 20900, 20899, 20898, 20891, 20890, 20889, 20887, 20886, 20885, 20884, 20862, 20623, 20622, 20621, 20620, 20619, 20618, 20617, 20616, 20615, 20614, 20613, 20612, 20611, 20610, 20609, 20608, 20607, 20606, 20605, 20604, 20497, 20496, 20495, 20494, 20493, 20492, 20491, 20490, 20488, 20487, 20486, 20485, 20484, 20483, 20482, 20481, 20480, 20479, 20478, 20477, 20476, 20475, 20474, 20473, 20472, 20471, 20470, 20469, 20468, 20467, 20466, 20465, 20464, 20463, 20462, 20461, 20460, 20459, 20458, 20457, 20456, 20455, 20454, 20453, 20452, 20451, 20450, 20449, 20448, 20447, 20446, 20445, 20444, 20443, 20442, 20441, 20440, 20439, 20438, 20437, 20436, 20435, 20434, 20433, 20432, 20431, 20430, 20429, 20428, 20427, 20426, 20425, 20424, 20423, 20422, 20421, 20420, 20419, 20418, 20417, 20416, 20415, 20414, 20413, 20412, 20411, 20410, 20409, 20408, 20407, 20406, 20405, 20404, 20403, 20402, 20401, 20400, 20399, 20398, 20397, 20396, 20395, 20394, 20393, 20392, 20391, 20390, 20389, 20388, 20387, 20386, 20385, 20384, 20383, 20382, 20381, 20380, 20379, 20378, 20377, 20376, 20375, 20374, 20373, 20372, 20371, 20370, 20369, 20368, 20367, 20366, 20365, 20364, 20363, 20362, 20361, 20360, 20359, 20358, 20357, 20356, 20355, 20354, 20353, 20352, 20351, 20350, 20349, 20348, 20347, 20346, 20345, 20344, 20343, 20342, 20341, 20340, 20339, 20338, 20337, 20336, 20335, 20334, 20333, 20332, 20331, 20329, 20328, 20327, 20326, 20325, 20324, 20323, 20322, 20321, 20320, 20319, 20318, 20317, 20316, 20315, 20314, 20313, 20312, 20311, 20310, 20309, 20308, 20307, 20306, 20305, 20304, 20303, 20302, 20301, 20300, 20299, 20298, 20297, 20296, 20295, 20294, 20293, 20292, 20291, 20290, 20289, 20288, 20287, 20286, 20285, 20284, 20283, 20282, 20281, 20280, 20279, 20278, 20277, 20276, 20275, 20274, 20273, 20272, 20271, 20270, 20269, 20268, 20267, 20266, 20265, 20264, 20263, 20262, 20261, 20260, 20259, 20258, 20257, 20256, 20255, 20254, 20253, 20252, 20251, 20250, 20249, 20248, 20247, 20246, 20245, 20244, 20243, 20242, 20241, 20240, 20239, 20238, 20237, 20236, 20235, 20234, 20233, 20232, 20231, 20230, 20229, 20228, 20227, 20226, 20225, 20224, 20223, 20222, 20221, 20220, 20219, 20218, 20217, 20216, 20215, 20214, 20213, 20211, 20210, 20209, 20208, 20207, 20205, 20204, 20203, 20202, 20200, 20199, 20198, 20197, 20196, 20195, 20194, 20193, 20192, 20191, 20190, 20188, 20187, 20186, 20185, 20184, 20183, 20182, 20181, 20180, 20179, 20178, 20177, 20176, 20175, 20174, 20173, 20172, 20171, 20170, 20169, 20168, 20167, 20166, 20165, 20164, 20163, 20162, 20161, 20160, 20159, 20158, 20157, 20156, 20155, 20154, 20153, 20151, 20149, 20148, 20147, 20146, 20145, 20144, 20143, 20141, 20140, 20139, 20138, 20137, 20136, 20135, 20134, 20133, 20132, 20131, 20130, 20128, 20127, 20126, 20125, 20124, 20123, 20122, 20121, 20120, 20119, 20118, 20117, 20116, 20115, 20114, 20113, 20112, 20111, 20110, 20109, 20108, 20106, 20105, 20104, 20103, 20102, 20101, 20100, 20099, 20098, 20097, 20095, 20094, 20093, 20092, 20091, 20090, 20089, 20088, 20087, 20086, 20085, 20084, 20083, 20082, 20081, 20080, 20079, 20078, 20077, 20076, 20075, 20074, 20073, 20072, 20071, 20070, 20069, 20068, 20067, 20065, 20064, 20063, 20062, 20061, 20060, 20059, 20058, 20057, 20056, 20055, 20054, 20053, 20052, 20051, 20050, 20049, 20048, 20047, 20046, 20045, 20044, 20043, 20042, 20041, 20040, 20039, 20038, 20037, 20036, 20035, 20034, 20033, 20032, 20031, 20030, 20029, 20028, 20027, 20026, 20025, 20024, 20023, 20022, 20021, 20020, 20019, 20018, 20017, 20016, 20015, 20014, 20013, 20012, 20011, 20009, 20008, 20007, 20006, 20005, 20004, 20003, 20002, 20001, 19999, 19998, 19997, 19996, 19995, 19994, 19993, 19992, 19991, 19990, 19989, 19988, 19987, 19986, 19985, 19984, 19983, 19982, 19981, 19980, 19979, 19978, 19977, 19975, 19974, 19973, 19972, 19971, 19970, 19969, 19968, 19967, 19966, 19965, 19964, 19963, 19962, 19961, 19960, 19959, 19958, 19957, 19956, 19955, 19954, 19953, 19952, 19950, 19949, 19948, 19947, 19945, 19944, 19943, 19942, 19941, 19940, 19939, 19938, 19937, 19936, 19935, 19788, 19627, 19626, 19625, 19624, 19623, 19622, 19621, 19620, 19619, 19618, 19617, 19616, 19615, 19614, 19613, 19612, 19611, 19610, 19609, 19608, 19607, 19606, 19605, 19604, 19603, 19602, 19601, 19600, 19599, 19598, 19597, 19596, 19595, 19594, 19593, 19592, 19591, 19590, 19589, 19588, 19587, 19586, 19585, 19584, 19583, 19582, 19581, 19580, 19579, 19578, 19577, 19576, 19575, 19574, 19573, 19572, 19571, 19570, 19569, 19568, 19567, 19566, 19565, 19564, 19563, 19562, 19561, 19560, 19559, 19558, 19557, 19556, 19555, 19554, 19553, 19552, 19551, 19550, 19549, 19548, 19547, 19546, 19545, 19544, 19543, 19542, 19541, 19540, 19539, 19538, 19537, 19536, 19535, 19534, 19533, 19532, 19531, 19530, 19529, 19528, 19527, 19526, 19525, 19524, 19523, 19522, 19521, 19520, 19519, 19518, 19517, 19516, 19515, 19514, 19513, 19512, 19511, 19510, 19509, 19508, 19507, 19506, 19505, 19504, 19503, 19502, 19501, 19500, 19499, 19498, 19497, 19496, 19495, 19494, 19493, 19492, 19491, 19490, 19489, 19488, 19487, 19486, 19485, 19484, 19483, 19482, 19481, 19480, 19479, 19478, 19477, 19476, 19475, 19474, 19473, 19472, 19471, 19470, 19469, 19468, 19467, 19466, 19465, 19464, 19463, 19462, 19461, 19460, 19459, 19458, 19457, 19456, 19455, 19454, 19453, 19452, 19451, 19450, 19449, 19448, 19447, 19446, 19445, 19444, 19443, 19442, 19441, 19440, 19439, 19437, 19436, 19435, 19434, 19433, 19432, 19431, 19430, 19429, 19427, 19426, 19425, 19424, 19423, 19422, 19421, 19420, 19419, 19418, 19417, 19416, 19415, 19414, 19413, 19412, 19411, 19410, 19409, 19408, 19407, 19406, 19405, 19404, 19403, 19402, 19401, 19400, 19399, 19398, 19397, 19396, 19395, 19394, 19393, 19392, 19391, 19389, 19388, 19386, 19385, 19383, 19382, 19381, 19380, 19379, 19378, 19377, 19376, 19375, 19374, 19373, 19372, 19371, 19370, 19369, 19368, 19367, 19366, 19365, 19364, 19363, 19362, 19361, 19360, 19359, 19358, 19357, 19356, 19355, 19354, 19353, 19352, 19351, 19350, 19349, 19348, 19347, 19346, 19345, 19344, 19343, 19342, 19341, 19340, 19339, 19338, 19337, 19336, 19335, 19334, 19333, 19332, 19329, 19328, 19326, 19325, 19324, 19323, 19322, 19321, 19320, 19319, 19318, 19317, 19316, 19315, 19314, 19313, 19312, 19311, 19310, 19309, 19308, 19306, 19305, 19303, 19302, 19301, 19300, 19299, 19298, 19297, 19296, 19295, 19294, 19293, 19292, 19291, 19290, 19289, 19288, 19287, 19286, 19285, 19284, 19283, 19282, 19281, 19280, 19279, 19278, 19277, 19275, 19274, 19273, 19272, 19271, 19270, 19269, 19268, 19267, 19266, 19265, 19264, 19263, 19262, 19261, 19260, 19259, 19258, 19257, 19256, 19255, 19254, 19253, 19252, 19251, 19250, 19249, 19248, 19247, 19246, 19245, 19244, 19243, 19242, 19241, 19240, 19239, 19238, 19233, 19232, 19231, 19230, 19229, 19228, 19226, 19225, 19224, 19223, 19221, 19220, 19219, 19218, 19217, 19216, 19214, 19213, 19212, 19207, 19206, 19205, 19204, 19203, 19201, 19200, 19199, 19198, 19197, 19196, 19194, 19193, 19192, 19191, 19190, 19189, 19188, 19187, 19186, 19185, 19184, 19183, 19182, 19180, 19177, 19176, 19175, 19173, 19172, 19171, 19170, 19169, 19168, 19167, 19166, 19165, 19164, 19163, 19162, 19161, 19160, 19159, 19158, 19157, 19156, 19155, 19154, 19153, 19152, 19151, 19150, 19149, 19148, 19147, 19146, 19145, 19144, 19143, 19142, 19141, 19140, 19139, 19138, 19137, 19136, 19135, 19134, 19133, 19132, 19131, 19130, 19129, 19128, 19127, 19126, 19125, 19123, 19121, 19120, 19119, 19118, 19117, 19116, 19115, 19114, 19113, 19112, 19111, 19110, 19109, 19108, 19107, 19106, 19105, 19104, 19103, 19102, 19101, 19100, 19099, 19098, 19097, 19096, 19095, 19094, 19093, 19092, 19091, 19090, 19089, 19088, 19087, 19086, 19085, 19084, 19083, 19082, 19081, 19080, 19079, 19078, 19077, 19076, 19074, 19073, 19072, 19071, 19070, 19069, 19068, 19067, 19066, 19064, 19063, 19062, 19061, 19060, 19059, 19058, 19057, 19056, 19055, 19054, 19053, 19052, 19050, 18705, 18700, 18346, 18345, 18344, 18343, 18342, 18252, 18251, 18250, 18248, 18247, 18246, 18245, 18244, 18243, 18242, 18241, 18240, 18239, 18238, 18237, 18236, 18235, 18234, 18233, 18232, 18231, 18230, 18229, 18228, 18227, 18226, 18225, 18224, 18223, 18222, 18221, 18220, 18219, 18218, 18217, 18216, 18215, 18214, 18213, 18212, 18211, 18210, 18209, 18208, 18207, 18206, 18205, 18204, 18203, 18202, 18201, 18200, 18199, 18198, 18197, 18196, 18195, 18194, 18193, 18192, 18191, 18190, 18188, 18187, 18186, 18185, 18184, 18183, 18182, 18181, 18180, 18179, 18178, 18177, 18176, 18175, 18174, 18173, 18172, 18171, 18170, 18169, 18168, 18167, 18166, 18165, 18164, 18163, 18162, 18161, 18160, 18159, 18158, 18157, 18156, 18155, 18154, 18153, 18152, 18151, 18150, 18149, 18148, 18147, 18146, 18145, 18144, 18143, 18142, 18141, 18140, 18139, 18137, 18136, 18135, 18134, 18133, 18132, 18131, 18130, 18129, 18128, 18030, 18029, 18028, 18027, 18026, 18025, 18024, 18023, 18022, 18021, 18019, 18018, 18017, 18016, 18015, 18014, 18013, 18012, 18011, 18010, 18009, 18008, 18007, 18006, 18005, 18004, 18003, 18002, 18001, 18000, 17999, 17998, 17997, 17996, 17995, 17994, 17993, 17991, 17990, 17989, 17988, 17987, 17986, 17985, 17984, 17983, 17982, 17981, 17980, 17979, 17978, 17977, 17976, 17975, 17974, 17973, 17972, 17971, 17970, 17969, 17968, 17967, 17966, 17965, 17964, 17963, 17962, 17961, 17960, 17959, 17958, 17957, 17956, 17955, 17954, 17953, 17952, 17951, 17950, 17949, 17948, 17947, 17946, 17945, 17944, 17943, 17942, 17941, 17940, 17939, 17938, 17937, 17936, 17935, 17934, 17933, 17932, 17931, 17930, 17929, 17928, 17927, 17926, 17925, 17924, 17923, 17922, 17921, 17920, 17919, 17918, 17917, 17916, 17915, 17914, 17913, 17912, 17911, 17910, 17909, 17908, 17907, 17906, 17905, 17904, 17903, 17902, 17901, 17900, 17899, 17898, 17897, 17896, 17895, 17894, 17893, 17892, 17891, 17890, 17889, 17888, 17887, 17886, 17885, 17884, 17883, 17882, 17881, 17880, 17879, 17878, 17877, 17876, 17875, 17874, 17873, 17872, 17871, 17870, 17869, 17868, 17867, 17866, 17865, 17864, 17863, 17862, 17861, 17860, 17859, 17858, 17857, 17856, 17855, 17854, 17853, 17852, 17851, 17850, 17849, 17848, 17847, 17846, 17845, 17844, 17843, 17842, 17841, 17840, 17839, 17838, 17837, 17836, 17835, 17834, 17833, 17832, 17831, 17830, 17829, 17828, 17827, 17825, 17824, 17823, 17822, 17821, 17820, 17819, 17818, 17817, 17815, 17814, 17813, 17812, 17811, 17810, 17809, 17808, 17807, 17806, 17805, 17804, 17803, 17802, 17801, 17800, 17799, 17798, 17797, 17796, 17795, 17794, 17793, 17792, 17791, 17790, 17789, 17788, 17785, 17784, 17782, 17781, 17780, 17779, 17778, 17777, 17776, 17775, 17774, 17773, 17772, 17771, 17770, 17769, 17768, 17767, 17766, 17765, 17764, 17763, 17762, 17761, 17760, 17759, 17758, 17757, 17756, 17755, 17754, 17753, 17752, 17751, 17750, 17749, 17748, 17747, 17746, 17745, 17744, 17743, 17742, 17741, 17740, 17739, 17738, 17737, 17736, 17735, 17734, 17733, 17732, 17731, 17730, 17729, 17728, 17727, 17726, 17725, 17724, 17723, 17722, 17721, 17720, 17719, 17718, 17717, 17716, 17715, 17714, 17713, 17712, 17711, 17710, 17709, 17708, 17707, 17706, 17705, 17704, 17703, 17702, 17701, 17700, 17699, 17698, 17697, 17696, 17695, 17694, 17693, 17692, 17691, 17690, 17689, 17688, 17687, 17686, 17685, 17684, 17683, 17682, 17681, 17680, 17679, 17678, 17677, 17676, 17675, 17674, 17673, 17672, 17671, 17670, 17669, 17668, 17667, 17666, 17665, 17664, 17663, 17662, 17661, 17660, 17659, 17658, 17657, 17655, 17654, 17653, 17652, 17651, 17650, 17649, 17648, 17647, 17646, 17645, 17644, 17643, 17642, 17641, 17640, 17639, 17638, 17637, 17636, 17635, 17634, 17633, 17632, 17631, 17630, 17629, 17628, 17626, 17624, 17623, 17622, 17621, 17620, 17619, 17618, 17616, 17615, 17614, 17613, 17612, 17611, 17610, 17609, 17608, 17607, 17606, 17605, 17604, 17603, 17602, 17601, 17600, 17599, 17598, 17597, 17596, 17595, 17594, 17593, 17592, 17591, 17590, 17589, 17588, 17587, 17586, 17585, 17584, 17583, 17582, 17581, 17580, 17579, 17578, 17577, 17576, 17575, 17574, 17573, 17572, 17571, 17570, 17569, 17568, 17567, 17566, 17565, 17564, 17563, 17562, 17561, 17560, 17559, 17558, 17557, 17556, 17555, 17554, 17553, 17552, 17551, 17550, 17549, 17548, 17547, 17546, 17545, 17544, 17543, 17542, 17541, 17540, 17539, 17538, 17537, 17536, 17535, 17534, 17533, 17532, 17531, 17530, 17529, 17528, 17527, 17526, 17525, 17524, 17523, 17522, 17521, 17520, 17519, 17518, 17517, 17516, 17515, 17514, 17513, 17512, 17510, 17509, 17508, 17507, 17506, 17505, 17504, 17503, 17502, 17501, 17500, 17499, 17498, 17497, 17496, 17495, 17494, 17493, 17492, 17491, 17490, 17489, 17488, 17487, 17486, 17485, 17484, 17483, 17482, 17481, 17480, 17479, 17478, 17477, 17475, 17474, 17473, 17472, 17471, 17470, 17469, 17468, 17467, 17466, 17465, 17464, 17463, 17462, 17461, 17460, 17459, 17458, 17457, 17342, 17341, 17340, 17339, 17338, 17337, 17336, 17335, 17334, 17333, 17332, 17331, 17330, 17329, 17328, 17327, 17326, 17325, 17324, 17323, 17322, 17321, 17320, 17319, 17318, 17317, 17316, 17315, 17314, 17313, 17312, 17311, 17310, 17309, 17308, 17307, 17306, 17305, 17304, 17303, 17302, 17301, 17300, 17299, 17298, 17297, 17296, 17295, 17294, 17293, 17292, 17291, 17290, 17289, 17288, 17287, 17286, 17285, 17284, 17283, 17282, 17281, 17280, 17279, 17278, 17277, 17276, 17275, 17274, 17273, 17272, 17271, 17270, 17269, 17268, 17267, 17266, 17265, 17264, 17263, 17262, 17261, 17260, 17259, 17258, 17257, 17256, 17255, 17254, 17253, 17252, 17251, 17250, 17249, 17248, 17247, 17246, 17245, 17244, 17243, 17242, 17241, 17240, 17239, 17238, 17237, 17236, 17235, 17234, 17233, 17232, 17231, 17230, 17229, 17228, 17227, 17226, 17225, 17224, 17223, 17222, 17221, 17220, 17219, 17218, 17217, 17216, 17215, 17214, 17213, 17212, 17211, 17210, 17209, 17208, 17207, 17206, 17205, 17204, 17203, 17202, 17201, 17200, 17199, 17198, 17197, 17196, 17195, 17194, 17193, 17192, 17191, 17190, 17189, 17188, 17187, 17186, 17185, 17184, 17183, 17182, 17181, 17180, 17179, 17178, 17177, 17176, 17175, 17174, 17172, 17171, 17170, 17169, 17168, 17167, 17166, 17165, 17164, 17163, 17162, 17161, 17160, 17159, 17158, 17157, 17156, 17155, 17154, 17153, 17152, 17151, 17150, 17149, 17148, 17147, 17146, 17145, 17144, 17143, 17142, 17141, 17140, 17139, 17138, 17137, 17136, 17135, 17134, 17133, 17132, 17131, 17130, 17129, 17128, 17127, 17126, 17125, 17124, 17123, 17122, 17121, 17120, 17119, 17118, 17117, 17116, 17115, 17114, 17113, 17112, 17111, 17110, 17109, 17108, 17107, 17106, 17105, 17104, 17103, 17102, 17101, 17100, 17099, 17098, 17097, 17096, 17095, 17094, 17093, 17092, 17091, 17090, 17089, 17088, 17087, 17086, 17085, 17084, 17083, 17082, 17081, 17080, 17079, 17078, 17077, 17076, 17075, 17074, 17073, 17072, 17071, 17070, 17069, 17068, 17067, 17066, 17065, 17064, 17063, 17062, 17061, 17060, 17059, 17058, 17057, 17056, 17055, 17054, 17053, 17052, 17051, 17050, 17049, 17047, 17046, 17045, 17044, 17043, 17042, 17041, 17040, 17039, 17038, 17037, 17036, 17035, 17034, 17033, 17032, 17031, 17030, 17029, 17028, 17027, 17026, 17025, 17024, 17023, 17022, 17021, 17020, 17019, 17018, 17017, 17016, 17015, 17014, 17013, 17012, 17011, 17010, 17009, 17008, 17007, 17006, 17005, 17004, 17003, 17002, 17001, 17000, 16999, 16998, 16997, 16996, 16995, 16994, 16993, 16992, 16991, 16990, 16989, 16988, 16987, 16986, 16985, 16984, 16983, 16982, 16981, 16980, 16979, 16978, 16977, 16976, 16975, 16974, 16973, 16972, 16971, 16970, 16969, 16968, 16967, 16966, 16965, 16964, 16963, 16962, 16961, 16960, 16959, 16957, 16956, 16955, 16954, 16953, 16952, 16951, 16950, 16949, 16948, 16947, 16946, 16945, 16944, 16943, 16942, 16941, 16940, 16939, 16938, 16937, 16936, 16935, 16934, 16933, 16932, 16931, 16930, 16929, 16928, 16927, 16926, 16925, 16924, 16923, 16922, 16921, 16920, 16919, 16918, 16917, 16916, 16915, 16914, 16913, 16912, 16911, 16910, 16909, 16908, 16907, 16906, 16905, 16904, 16903, 16902, 16901, 16900, 16899, 16898, 16897, 16896, 16895, 16894, 16893, 16892, 16891, 16890, 16889, 16888, 16887, 16886, 16885, 16884, 16883, 16882, 16881, 16880, 16879, 16878, 16877, 16876, 16875, 16874, 16873, 16872, 16871, 16870, 16869, 16868, 16867, 16866, 16865, 16864, 16863, 16862, 16861, 16860, 16859, 16858, 16857, 16856, 16855, 16854, 16853, 16852, 16851, 16850, 16849, 16848, 16847, 16846, 16845, 16844, 16843, 16842, 16841, 16840, 16839, 16838, 16837, 16836, 16835, 16834, 16833, 16832, 16831, 16830, 16829, 16828, 16827, 16826, 16825, 16824, 16823, 16822, 16821, 16820, 16819, 16818, 16817, 16816, 16815, 16814, 16813, 16812, 16811, 16810, 16809, 16808, 16807, 16806, 16805, 16804, 16803, 16802, 16801, 16800, 16799, 16798, 16797, 16796, 16795, 16794, 16793, 16792, 16791, 16790, 16789, 16788, 16787, 16786, 16785, 16784, 16783, 16782, 16781, 16780, 16779, 16778, 16777, 16776, 16775, 16774, 16773, 16772, 16771, 16770, 16769, 16768, 16767, 16766, 16765, 16764, 16763, 16762, 16761, 16760, 16759, 16758, 16757, 16756, 16755, 16754, 16753, 16752, 16751, 16750, 16749, 16748, 16747, 16746, 16745, 16744, 16743, 16742, 16741, 16740, 16739, 16738, 16737, 16736, 16735, 16734, 16733, 16732, 16731, 16730, 16729, 16728, 16727, 16726, 16725, 16724, 16723, 16722, 16721, 16720, 16719, 16718, 16717, 16716, 16715, 16714, 16713, 16712, 16711, 16710, 16709, 16708, 16707, 16706, 16705, 16704, 16703, 16702, 16701, 16700, 16699, 16698, 16697, 16696, 16695, 16694, 16693, 16692, 16691, 16690, 16689, 16688, 16687, 16686, 16685, 16684, 16683, 16682, 16681, 16680, 16679, 16678, 16677, 16676, 16675, 16674, 16673, 16672, 16671, 16670, 16669, 16668, 16667, 16666, 16665, 16664, 16663, 16662, 16661, 16660, 16659, 16658, 16657, 16656, 16655, 16654, 16653, 16652, 16651, 16650, 16649, 16648, 16647, 16646, 16645, 16644, 16643, 16642, 16641, 16640, 16639, 16638, 16637, 16636, 16635, 16634, 16633, 16632, 16631, 16630, 16629, 16628, 16627, 16626, 16625, 16624, 16623, 16622, 16621, 16620, 16619, 16618, 16617, 16616, 16615, 16614, 16613, 16612, 16611, 16610, 16609, 16608, 16607, 16606, 16605, 16604, 16603, 16602, 16601, 16600, 16599, 16598, 16597, 16596, 16595, 16594, 16593, 16592, 16591, 16590, 16589, 16588, 16587, 16586, 16585, 16584, 16583, 16582, 16581, 16580, 16579, 16578, 16577, 16576, 16575, 16574, 16573, 16572, 16571, 16570, 16569, 16568, 16567, 16566, 16565, 16564, 16563, 16562, 16561, 16560, 16559, 16558, 16557, 16556, 16555, 16554, 16553, 16552, 16551, 16550, 16549, 16548, 16547, 16546, 16545, 16544, 16543, 16542, 16541, 16540, 16539, 16538, 16537, 16536, 16535, 16534, 16533, 16532, 16531, 16530, 16529, 16528, 16527, 16526, 16525, 16524, 16523, 16522, 16521, 16520, 16519, 16518, 16517, 16516, 16515, 16514, 16513, 16512, 16511, 16510, 16509, 16508, 16507, 16506, 16505, 16504, 16503, 16502, 16501, 16500, 16499, 16498, 16497, 16496, 16495, 16494, 16493, 16492, 16491, 16490, 16489, 16488, 16487, 16486, 16485, 16484, 16483, 16482, 16481, 16480, 16479, 16478, 16477, 16476, 16475, 16474, 16473, 16472, 16471, 16470, 16469, 16468, 16467, 16466, 16465, 16464, 16463, 16462, 16461, 16460, 16459, 16458, 16457, 16456, 16455, 16454, 16453, 16452, 16451, 16450, 16449, 16448, 16447, 16446, 16445, 16444, 16443, 16442, 16441, 16440, 16439, 16438, 16437, 16436, 16435, 16434, 16433, 16432, 16431, 16430, 16429, 16428, 16427, 16426, 16425, 16424, 16423, 16422, 16421, 16420, 16419, 16418, 16417, 16416, 16415, 16414, 16413, 16412, 16411, 16410, 16409, 16408, 16407, 16406, 16405, 16404, 16403, 16402, 16401, 16400, 16399, 16398, 16397, 16396, 16395, 16394, 16393, 16392, 16391, 16390, 16389, 16388, 16387, 16386, 16385, 16384, 16383, 16382, 16381, 16380, 16379, 16378, 16377, 16376, 16375, 16374, 16373, 16372, 16371, 16370, 16369, 16368, 16367, 16366, 16365, 16364, 16363, 16362, 16361, 16360, 16359, 16358, 16357, 16356, 16355, 16354, 16353, 16352, 16351, 16350, 16349, 16348, 16347, 16346, 16345, 16344, 16343, 16342, 16341, 16340]

async def init():
    await app.start()


    @app.on_message(filters.command("gasngewe") )
    async def forward_videos(client, message):
    # Ganti "nama_grup_tujuan" dengan nama atau ID grup tujuan
        for id in data:
            try:
                await app.copy_message(-1001766465145, -1002089478686, id)
                await asyncio.sleep(10)
            except FloodWait as e:
               flood_time = e.value
               if flood_time > 200:
                  continue
               await asyncio.sleep(flood_time)
        
# Menjalankan bot
    print("[Bot Copy] - Started")
    await idle()



if __name__ == "__main__":
    loop.run_until_complete(init())
