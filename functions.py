# coding:utf-8


def encryption(primary_string):
    """
    用于对字符串进行加密
    """
    from random import randint

    # 用于保存结果
    final_password = ''
    for i in primary_string:
        rand_num = randint(1, 3)  # 得到随机数
        ord_i = str(ord(i) * rand_num)  # 得到整型的i
        pwd_head_num = int(ord_i[-1])  # 密码头参数
        pwd_head = chr(ord('y') - pwd_head_num)  # 生成密码头

        # 生成单个字符的密码，也就是i的密码
        adding_str = f'{pwd_head}{str(hex(int(str(ord(i) * rand_num)[:-1])))[2:]}{chr(ord(pwd_head) - rand_num * 2)}'
        # 我也是迫不得已写得这么乱的

        # 添加
        final_password += adding_str

    final_password += 'z'    # z是作为一种对软件运行模式的解析，对解密算法没有影响

    return final_password


def decrypt(primary_password):
    """
    用于对字符串进行解密
    """
    # 十六进制数
    hex_list = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f')

    # 记录是否遍历到密码头或密码后缀
    changing_state = 0
    real_state = False
    # 记录每个字符的密文
    tmp_password = ''
    passwords = []
    # 读取密码
    for each_pwd in primary_password.strip().rstrip('z'):
        # 如果遍历到密码头，就更改读写状态
        if each_pwd not in hex_list:
            changing_state += 1
        real_state = bool(int(changing_state % 2))

        # 先写入
        tmp_password += each_pwd
        # real_state为False时，将tmp_password写入passwords，同时将tmp_password归零
        if real_state is False:
            passwords.append(tmp_password)
            tmp_password = ''
    del tmp_password

    # 临时记录密码头
    tmp_pwdhead = ''
    # 临时记录密码主体
    tmp_hex = ''
    # 临时记录密码后缀
    tmp_pwdend = ''
    # 最终的明文
    final_text = ''
    # 处理密码
    for each_char in passwords:
        # 获取信息
        tmp_pwdhead = each_char[0]
        tmp_hex = each_char[1:-1]
        tmp_pwdend = each_char[-1]

        # 分析
        read_pwdhead = str(int(ord('y') - ord(tmp_pwdhead)))
        read_hex = str(int(tmp_hex, 16))
        primary_num = int(f'{read_hex}{read_pwdhead}')
        # 处理
        read_pwdend = int((ord(tmp_pwdhead) - ord(tmp_pwdend)) / 2)
        final_num = int(primary_num / read_pwdend)

        # 得到明文
        final_char = chr(final_num)
        # 写入
        final_text += final_char

    return final_text

    # 加强了加密算法，解密算法就要重写了，焯
