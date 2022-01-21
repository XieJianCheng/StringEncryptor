# coding:utf-8


def encryption(primary_string):
    """
    用于对字符串进行加密
    """
    # 用于保存结果
    final_password = ''

    for i in primary_string:
        ord_i = str(ord(i))                         # 得到整型的i
        pwd_head_num = int(ord_i[-1])*2              # 密码头参数
        pwd_head = chr(ord('y') - pwd_head_num)     # 生成密码头

        # 生成单个字符的密码，也就是i的密码
        adding_str = f'{pwd_head}{str(hex(int(str(ord(i))[:-1])))[2:]}'      # 我也是迫不得已写得这么乱的

        # 添加
        final_password += adding_str

    # 随便加个东西，懒得重写解密机制
    final_password += 'x'   # 作为本人的姓，x算是用来版权保护吧hhh。
    final_password += 'z'
    # 另外，后面的z是作为一种对软件运行模式的解析，对解密算法没有影响

    return final_password


def decrypt(primary_password):
    """
    用于对字符串进行解密
    """
    # 这是密码头，不是字符集！！
    pwdhead_list = []
    for i in range(103, 122, 2):
        pwdhead_list.append(chr(i))
    pwdhead_list.append('x')  # 这个x有两个作用hhh
    tuple(pwdhead_list)
    # 这是十六进制数，不是字符集！！
    hex_list = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f')

    # 计次
    times = 0
    # 用于记录十六进制数
    tmp_num_hex_str = ''
    # 记录密码头的隐藏信息
    tmp_pwd_head_num = ''
    # 最终的明文
    final_text = ''
    for i in primary_password:
        # 获取每个字符的密文
        if i in pwdhead_list:  # 遍历到数据
            if times > 0:
                # 最终的解密
                adding_chr_int = int(f'{str(int(tmp_num_hex_str, 16))}{str(tmp_pwd_head_num)}')
                adding_chr = chr(adding_chr_int)
                final_text += adding_chr

            # 归零
            tmp_num_hex_str = ''

            # 新的密文字符
            tmp_pwd_head_str = i  # 获取密码头
            tmp_pwd_head_num = str(int((ord('y') - ord(i)) / 2))  # 得到密码头中的隐藏参数

            # 计次
            times += 1
        elif i in hex_list:  # 如果遍历到密码头
            # 获取十六进制数
            tmp_num_hex_str += i  # 是字符串型

            # 计次
            times += 1
        else:
            pass

    return final_text
