#coding:utf-8
import random
import time
import datetime


class DataCreate(object):

    def __init__(self):
        pass

    # 生成中文名字
    def get_chinese_name(self, *num):

        last_name_str = u'赵钱孙李周吴郑王冯陈楮卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚' \
                        u'范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康伍余' \
                        u'元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董梁杜阮蓝闽级席季' \
                        u'麻强贾路娄危江童颜郭梅盛林刁锺徐丘骆高夏蔡田樊胡凌霍虞万支柯昝管卢莫经房裘缪干解应宗丁宣贲' \
                        u'邓郁单杭洪包诸左石崔吉钮龚程嵇邢滑裴陆荣翁荀羊於惠甄麹家封芮羿储靳汲邴糜松井段富巫乌焦巴弓' \
                        u'牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘斜厉戎祖武符刘景詹束龙叶幸司韶郜黎蓟薄印宿白怀蒲' \
                        u'邰从鄂索咸籍赖卓蔺屠蒙池乔阴郁胥能苍双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍郤璩桑桂濮牛寿通边扈' \
                        u'燕冀郏浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘匡国文寇广禄阙' \
                        u'东欧殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空曾毋沙乜养鞠须丰巢关蒯相查后荆红游竺权逑' \
                        u'盖益桓公万俟司马上官欧阳夏侯诸葛闻人东方赫连皇甫尉迟公羊澹台公冶宗政濮阳淳于单于太叔申屠公' \
                        u'孙仲孙轩辕令狐锺离宇文长孙慕容鲜于闾丘司徒司空丌官司寇仉督子车颛孙端木巫马公西漆雕乐正壤驷' \
                        u'邓郁单杭洪包诸左石崔吉钮龚程嵇邢滑裴陆荣翁荀羊於惠甄麹家封芮羿储靳汲邴糜松井段富巫乌焦巴弓' \
                        u'牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘斜厉戎祖武符刘景詹束龙叶幸司韶郜黎蓟薄印宿白怀蒲' \
                        u'邰从鄂索咸籍赖卓蔺屠蒙池乔阴郁胥能苍双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍郤璩桑桂濮牛寿通边扈' \
                        u'燕冀郏浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘匡国文寇广禄阙' \
                        u'东欧殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空曾毋沙乜养鞠须丰巢关蒯相查后荆红游竺权逑' \
                        u'邓郁单杭洪包诸左石崔吉钮龚程嵇邢滑裴陆荣翁荀羊於惠甄麹家封芮羿储靳汲邴糜松井段富巫乌焦巴弓' \
                        u'牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘斜厉戎祖武符刘景詹束龙叶幸司韶郜黎蓟薄印宿白怀蒲' \
                        u'邰从鄂索咸籍赖卓蔺屠蒙池乔阴郁胥能苍双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍郤璩桑桂濮牛寿通边扈' \
                        u'燕冀郏浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘匡国文寇广禄阙' \
                        u'东欧殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空曾毋沙乜养鞠须丰巢关蒯相查后荆红游竺权逑' \
                        u'盖益桓公万俟司马上官欧阳夏侯诸葛闻人东方赫连皇甫尉迟公羊澹台公冶宗政濮阳淳于单于太叔申屠公' \
                        u'盖益桓公万俟司马上官欧阳夏侯诸葛闻人东方赫连皇甫尉迟公羊澹台公冶宗政濮阳淳于单于太叔申屠公' \
                        u'公良拓拔夹谷宰父谷梁晋楚阎法汝鄢涂钦段干百里东郭南门呼延归海羊舌微生岳帅缑亢况后有琴梁丘左' \
                        u'丘东门西门商牟佘佴伯赏南宫墨哈谯笪年爱阳佟'

        first_name_str = u'婷倩睿瑜嘉君盈男萱雨乐欣悦雯晨珺月雪秀晓然冰新淑玟萌凝文展露静智丹宁颖平佳玲彤芸莉璐云聆芝' \
                         u'娟超香英菲涓洁萍蓉潞笑迪敏靓菁慧涵韵琳燕依妙美宜尚诗钰娜仪娇谊语彩清好睻曼蔓茜沁韶舒盛越琪' \
                         u'邓郁单杭洪包诸左石崔吉钮龚程嵇邢滑裴陆荣翁荀羊於惠甄麹家封芮羿储靳汲邴糜松井段富巫乌焦巴弓' \
                         u'牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘斜厉戎祖武符刘景詹束龙叶幸司韶郜黎蓟薄印宿白怀蒲' \
                         u'邰从鄂索咸籍赖卓蔺屠蒙池乔阴郁胥能苍双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍郤璩桑桂濮牛寿通边扈' \
                         u'燕冀郏浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘匡国文寇广禄阙' \
                         u'东欧殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空曾毋沙乜养鞠须丰巢关蒯相查后荆红游竺权逑' \
                         u'盖益桓公万俟司马上官欧阳夏侯诸葛闻人东方赫连皇甫尉迟公羊澹台公冶宗政濮阳淳于单于太叔申屠公' \
                         u'霞艺函迎虹爽瑞珏桐筱苹莹名晗甜晴亭吉玉晶妍凤蒙霖希宣昕丽心可旻阳真蓝畅荣岚乔育芷姿妹姗瑾奕' \
                         u'兰航蕾艳怡青珊才小子允加巧冉北朵多羽如帆伶采西贝其春易咏亚明秋泓伦朔哲益轩容玹津启婧晟婉常' \
                         u'浩景茗尧雅杰媛诒翔为捷钧毓意琸靖渺渲熙微祺梦赫菡纶铭齐华菏毅瑶品梓国卿振卫叶亿娆漫兴蓓融嫒' \
                         u'锦翰科润霏灿忆聪怿蕊谨丰丛璇议馨瀚潇莺珑俪骄骁灵忻昭金昊志辰宇安凡禾竹愉丫珂洺苒若偌珮棋淇' \
                         u'群会维影逸娴赏霄辉莲优瑷朦涛识誉巍鑫逦湾中予卉永同州任宏卓晨轩清睿宝涛华国亮新凯志明伟嘉东' \
                         u'洪建文子云杰兴友才振辰航达鹏宇衡佳强宁丰波森学民永翔鸿海飞义生凡连良乐勇辉龙川宏谦锋双霆玉' \
                         u'智增名进德聚军兵忠廷先江昌政君泽超信腾恒礼元磊阳月士洋欣升恩迅科富函业胜震福瀚瑞朔津韵荣为' \
                         u'诚斌广庆成峰可健英功冬锦立正禾平旭同全豪源安顺帆向雄材利希风林奇易来咏岩启坤昊朋和纪艺昭映' \
                         u'威奎帅星春营章高伦庭蔚益城牧钊刚洲家晗迎罡浩景珂策皓栋起棠登越盛语钧亿基理采备纶献维瑜齐凤' \
                         u'霞艺函迎虹爽瑞珏桐筱苹莹名晗甜晴亭吉玉晶妍凤蒙霖希宣昕丽心可旻阳真蓝畅荣岚乔育芷姿妹姗瑾奕' \
                         u'兰航蕾艳怡青珊才小子允加巧冉北朵多羽如帆伶采西贝其春易咏亚明秋泓伦朔哲益轩容玹津启婧晟婉常' \
                         u'浩景茗尧雅杰媛诒翔为捷钧毓意琸靖渺渲熙微祺梦赫菡纶铭齐华菏毅瑶品梓国卿振卫叶亿娆漫兴蓓融嫒' \
                         u'锦翰科润霏灿忆聪怿蕊谨丰丛璇议馨瀚潇莺珑俪骄骁灵忻昭金昊志辰宇安凡禾竹愉丫珂洺苒若偌珮棋淇' \
                         u'群会维影逸娴赏霄辉莲优瑷朦涛识誉巍鑫逦湾中予卉永同州任宏卓晨轩清睿宝涛华国亮新凯志明伟嘉东' \
                         u'洪建文子云杰兴友才振辰航达鹏宇衡佳强宁丰波森学民永翔鸿海飞义生凡连良乐勇辉龙川宏谦锋双霆玉' \
                         u'智增名进德聚军兵忠廷先江昌政君泽超信腾恒礼元磊阳月士洋欣升恩迅科富函业胜震福瀚瑞朔津韵荣为' \
                         u'诚斌广庆成峰可健英功冬锦立正禾平旭同全豪源安顺帆向雄材利希风林奇易来咏岩启坤昊朋和纪艺昭映' \
                         u'霞艺函迎虹爽瑞珏桐筱苹莹名晗甜晴亭吉玉晶妍凤蒙霖希宣昕丽心可旻阳真蓝畅荣岚乔育芷姿妹姗瑾奕' \
                         u'兰航蕾艳怡青珊才小子允加巧冉北朵多羽如帆伶采西贝其春易咏亚明秋泓伦朔哲益轩容玹津启婧晟婉常' \
                         u'浩景茗尧雅杰媛诒翔为捷钧毓意琸靖渺渲熙微祺梦赫菡纶铭齐华菏毅瑶品梓国卿振卫叶亿娆漫兴蓓融嫒' \
                         u'锦翰科润霏灿忆聪怿蕊谨丰丛璇议馨瀚潇莺珑俪骄骁灵忻昭金昊志辰宇安凡禾竹愉丫珂洺苒若偌珮棋淇' \
                         u'群会维影逸娴赏霄辉莲优瑷朦涛识誉巍鑫逦湾中予卉永同州任宏卓晨轩清睿宝涛华国亮新凯志明伟嘉东' \
                         u'洪建文子云杰兴友才振辰航达鹏宇衡佳强宁丰波森学民永翔鸿海飞义生凡连良乐勇辉龙川宏谦锋双霆玉' \
                         u'智增名进德聚军兵忠廷先江昌政君泽超信腾恒礼元磊阳月士洋欣升恩迅科富函业胜震福瀚瑞朔津韵荣为' \
                         u'诚斌广庆成峰可健英功冬锦立正禾平旭同全豪源安顺帆向雄材利希风林奇易来咏岩启坤昊朋和纪艺昭映' \
                         u'毅谊贤逸卫万臻儒钢洁霖隆远聪耀誉继珑哲岚舜钦琛金彰亭泓蒙祥意鑫朗晟晓晔融谋宪励璟骏颜焘垒尚' \
                         u'镇济雨蕾韬选议曦奕彦虹宣蓝冠谱泰泊跃韦怡骁俊沣骅歌畅与圣铭溓滔溪巩影锐展笑祖时略敖堂崊绍崇' \
                         u'悦邦望尧珺然涵博淼琪群驰照传诗靖会力大山之中方仁世梓竹至充亦丞州言佚序宜'

        # 生成姓名
        last_name = last_name_str[random.randint(0, len(last_name_str) - 1)]
        mid_name = first_name_str[random.randint(0, len(first_name_str) - 1)]
        first_name = first_name_str[random.randint(0, len(first_name_str) - 1)]

        # 根据输入参数数值生成对应长度的中文名字
        if num == (1,):
            return last_name
        elif num == (2,) or num == ():
            return last_name + first_name
        else:
            return last_name + mid_name*(int(num[0])-2) + first_name

    # 生成英文名字
    def get_english_name(self):

        first_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        e_name1 = random.choice(first_letter)
        e_name2 = ''.join(random.sample(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                                       'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                                       'z'], 6)).replace(" ", "")
        return e_name1 + e_name2

    # 生成数字姓名
    def get_number_name(self):
        num_name = ''.join(random.sample(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], 6)).replace(" ", "")
        return num_name

    # 生成汉字、空格、数字、中点、字母、下点混合的姓名
    def get_mix_name(self):
        name1 = ''.join(random.sample(['赵', '钱', '孙', '李', '周', '吴', '郑', '王'], 1)).replace(" ", "")
        name2 = ''.join(random.sample(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], 6)).replace(" ", "")
        name3 = ''.join(random.sample(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                                       'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                                       'z'], 3)).replace(" ", "")
        name4 = ''.join(random.sample(['洪', '建', '文', '子', '云', '杰', '兴', '友'], 1)).replace(" ", "")
        return name1 + ' ' + name2 + '·' + name3 + '.' + name4

    # 根据指定的年龄区间，随机生成18位合法身份证号码
    def get_eighteen_certId(self, ageStart, ageEnd):
        ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
        LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
        u''' 随机生成新的18为身份证号码 '''
        t = time.localtime()[0]
        x = '%02d%02d%02d%04d%02d%02d%03d' % (random.randint(10, 99),
                                            random.randint(1, 99),
                                            random.randint(1, 99),
                                            random.randint(t - int(ageEnd), t - int(ageStart)),
                                            random.randint(1, 12),
                                            random.randint(1, 28),
                                            random.randint(1, 999))
        y = 0
        for i in range(17):
            y += int(x[i]) * ARR[i]

        return '%s%s' % (x, LAST[y % 11])

    # 根据指定年龄区间，随机生成15位的身份证号
    def get_fifteen_certId(self, ageStart, ageEnd):

        t = int(time.strftime("%y", time.localtime()))
        x = '%02d%02d%02d%02d%02d%02d%03d' % (random.randint(10, 99),
                                            random.randint(1, 99),
                                            random.randint(1, 99),
                                            abs(random.randint(t - int(ageEnd), t - int(ageStart))),
                                            random.randint(1, 12),
                                            random.randint(1, 28),
                                            random.randint(1, 999))

        return x

    # 生成指定位数的手机号
    def get_phone(self, num):

        phone_number_list = [133, 153, 180, 181, 189, 130, 131, 132, 145, 155, 156, 185, 186, 134, 135, 136, 137,
                             138, 139, 147, 150, 151, 152, 157, 158, 159, 182, 183, 184, 187, 188]
        count = int(num) - 3
        phone_number = ''
        eight_number_count = 0
        phone_three_start_number = phone_number_list[random.randint(0, len(phone_number_list) - 1)]
        phone_number += str(phone_three_start_number)
        while eight_number_count < count:
            phone_number += str(random.randint(0, 9))
            eight_number_count += 1
            pass
        return phone_number

    # 生成头两位非法的手机号
    def get_unnormal_phone(self):
        phone_number_list1 = random.choice([2, 3, 4, 5, 6, 7, 8, 9])
        phone_number_list2 = random.choice([1, 2, 6, 9])
        phone_number_list3 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])

        phone_number = ''
        eight_number_count = 0
        phone_three_start_number = str(phone_number_list1) + str(phone_number_list2) + str(phone_number_list3)
        phone_number += str(phone_three_start_number)
        while eight_number_count < 8:
            phone_number += str(random.randint(0, 9))
            eight_number_count += 1
            pass
        return phone_number

    def get_bank_card_no(self, accBankName):
        bank_card = {
            '中国工商银行': 62220241000,
            '中国农业银行': 62284820320,
            '中国银行': 60138201000,
            '中国建设银行': 62270019350,
            '中信实业银行': 62269004,
            '中国光大银行': 62266388,
            '华夏银行': 62263088,
            '中国民生银行': 47206800,
            '广东发展银行': 62256821210,
            '招商银行': 95555002,
            '兴业银行': 6229083285,
            '中国邮政': 62215161700,
        }
        return str(bank_card[accBankName]) + ''.join([str(i) for i in random.sample(range(0, 9), 8)])

    def get_bank_branch(self):
        bank_list = ['中国工商银行','中国农业银行','中国银行','中国建设银行','中信实业银行','中国光大银行','华夏银行','中国民生银行','广东发展银行','招商银行','兴业银行','中国邮政']
        bank_branch = random.choice(bank_list)

        return bank_branch

    def get_member_id(self):
        id = "1"
        time1 = time.strftime('%H%M%S')
        random_num = random.randint(int(100), int(999))
        member_id = id + str(time1) + str(random_num)
        return member_id

    # 生成cust_id
    def get_cust_id(self):
        datatime = time.strftime('%y%m%d%H%M%S')
        timestamp = str(int(time.time() * 1000))[5:]
        random_num = random.randint(int(10), int(99))
        cust_id = str(datatime) + timestamp + str(random_num)
        return cust_id

    # 生成指定长度的手机号
    def get_phone(self, num):

        phone_number_list = [133, 153, 180, 181, 189, 130, 131, 132, 145, 155, 156, 185, 186, 134, 135, 136, 137,
                             138, 139, 147, 150, 151, 152, 157, 158, 159, 182, 183, 184, 187, 188]
        count = int(num) - 3
        phone_number = ''
        eight_number_count = 0
        phone_three_start_number = phone_number_list[random.randint(0, len(phone_number_list) - 1)]
        phone_number += str(phone_three_start_number)
        while eight_number_count < count:
            phone_number += str(random.randint(0, 9))
            eight_number_count += 1
            pass
        return phone_number

    # 根据输入日期，生成天数大于、等于、小于的日期值
    def get_datetime_boundary_days(self, datetime_input):

        datetime_base = datetime.datetime.strptime(datetime_input, '%Y-%m-%d %H:%M:%S')
        datetime_base_plus = datetime_base + datetime.timedelta(days=1)
        datetime_base_minus = datetime_base + datetime.timedelta(days=-1)

        return datetime_base_minus, datetime_base, datetime_base_plus

    # 根据输入日期，生成时数大于、等于、小于的日期值
    def get_datetime_boundary_hours(self, datetime_input):

        datetime_base = datetime.datetime.strptime(datetime_input, '%Y-%m-%d %H:%M:%S')

        datetime_base_plus = datetime_base + datetime.timedelta(hours=1)
        datetime_base_minus = datetime_base + datetime.timedelta(hours=-1)

        return datetime_base_minus, datetime_base, datetime_base_plus

    # 根据输入日期，生成分数大于、等于、小于的日期值
    def get_datetime_boundary_minutes(self, datetime_input):

        datetime_base = datetime.datetime.strptime(datetime_input, '%Y-%m-%d %H:%M:%S')

        datetime_base_plus = datetime_base + datetime.timedelta(minutes=1)
        datetime_base_minus = datetime_base + datetime.timedelta(minutes=-1)

        return datetime_base_minus, datetime_base, datetime_base_plus

    # 根据输入日期，生成秒数大于、等于、小于的日期值
    def get_datetime_boundary_seconds(self, datetime_input):

        datetime_base = datetime.datetime.strptime(datetime_input, '%Y-%m-%d %H:%M:%S')

        datetime_base_plus = datetime_base + datetime.timedelta(seconds=1)
        datetime_base_minus = datetime_base + datetime.timedelta(seconds=-1)

        return datetime_base_minus, datetime_base, datetime_base_plus

    # 根据输入数值，生成钱数大于、等于、小于数值的两位钱数值
    def get_amount_boundary(self, amount_input):

        amount_base = format(float(amount_input), '.2f')
        amount_base_minus = format(float(amount_input-1), '.2f')
        amount_base_plus = format(float(amount_input+1), '.2f')

        return amount_base_minus, amount_base, amount_base_plus

    #获取N位随机数字符串
    def gen_random_numstr(self,num):
        base_str = "1234567890"
        temp = []
        for i in range(int(num)):
            temp.append(random.choice(base_str))
        new = ''.join(temp)
        return new

    #获取当前时间，如 ： 20180918
    def getnowdate(self):
        now = datetime.datetime.now()
        str = now.strftime("%Y%m%d")
        return str

if __name__ == "__main__":
    run = DataCreate()
    res = run.get_eighteen_certId(11,22)

    print (res)