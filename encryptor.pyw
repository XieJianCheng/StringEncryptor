# coding:utf-8

# 这原本是另一个项目的产物，
# 但是我忽然发掘到了它的其他作用，
# 于是决定开一个新的项目，作为2.0版本

# 开始时间 2022.1.4 13:33


import wx
from functions import encryption, decrypt

# 版本号
version = 'v2.2'


class StringEncryptor(wx.Frame):
    size = (500, 500)

    def __init__(self, parent=None, id=-1):
        wx.Frame.__init__(self, None, id, f"字符串加密{version}", size=self.size, pos=(700, 300))
        wx.Frame.SetMinSize(self, size=(470, 490))
        pnl = wx.Panel(self)

        title_all = wx.StaticText(pnl, label=f"字符串加密{version}")
        tips_input = wx.StaticText(pnl, label='请输入：')
        self.string_primary = wx.TextCtrl(pnl, style=wx.TE_LEFT | wx.TE_PROCESS_ENTER
                                          , size=(290, 25))    # 输入
        bt_encryption = wx.Button(pnl, label='加密')
        bt_decrypt = wx.Button(pnl, label='解密')

        title_result_encryption = wx.StaticText(pnl, label='加密结果')
        self.string_new_encryption = wx.TextCtrl(pnl, style=wx.TE_LEFT | wx.TE_READONLY | wx.TE_MULTILINE,
                                                 size=(200, 125))   # 加密结果
        bt_copy_encryption = wx.Button(pnl, label='复制')

        title_result_decrypt = wx.StaticText(pnl, label='解密结果')
        self.string_new_decrypt = wx.TextCtrl(pnl, style=wx.TE_LEFT | wx.TE_READONLY | wx.TE_MULTILINE,
                                              size=(200, 125))      # 解密结果
        bt_copy_decrypt = wx.Button(pnl, label='复制')

        bt_about = wx.Button(pnl, label='软件说明')
        bt_updatelog = wx.Button(pnl, label='更新日志')
        bt_quit = wx.Button(pnl, label='退出')

        sur = wx.StaticText(pnl, label=f"{decrypt('o9cega37y7d1g8f2q7dfx')}", pos=(1800, 1000))   # 彩蛋

        # 绑定事件
        bt_encryption.Bind(wx.EVT_BUTTON, self.run_encryption)  # 绑定加密按钮
        self.string_primary.Bind(wx.EVT_TEXT_ENTER, self.enter_text)  # 绑定加密        # 文本框
        bt_decrypt.Bind(wx.EVT_BUTTON, self.run_decrypt)  # 绑定解密按钮
        bt_quit.Bind(wx.EVT_BUTTON, self.bt_exit)  # 绑定退出按钮
        bt_copy_encryption.Bind(wx.EVT_BUTTON, self.copy_encryption)  # 绑定复制按钮
        bt_copy_decrypt.Bind(wx.EVT_BUTTON, self.copy_decrypt)
        bt_about.Bind(wx.EVT_BUTTON, self.show_about)  # 绑定关于按钮
        bt_updatelog.Bind(wx.EVT_BUTTON, self.show_updatelog)  # 绑定提示按钮

        # 字体
        # 字体均来自：字加 https://zijia.foundertype.com/
        font_title_all = wx.Font(pointSize=22, family=wx.DEFAULT, style=wx.NORMAL, weight=wx.LIGHT, underline=False,
                                 faceName='方正力黑 简 ExtraBold')
        font_title_result = wx.Font(pointSize=14, family=wx.DEFAULT, style=wx.NORMAL, weight=wx.LIGHT, underline=False,
                                    faceName='方正字迹-叶根友特楷简体')
        font_content = wx.Font(pointSize=13, family=wx.DEFAULT, style=wx.NORMAL, weight=wx.LIGHT, underline=False,
                               faceName='鬼灵精怪双子座')
        font_button_large = wx.Font(pointSize=18, family=wx.DEFAULT, style=wx.NORMAL, weight=wx.LIGHT, underline=False,
                                    faceName='方正颜真卿楷书 简繁')
        font_button_small = wx.Font(pointSize=13, family=wx.DEFAULT, style=wx.NORMAL, weight=wx.LIGHT, underline=False,
                                    faceName='方正颜真卿楷书 简繁')
        title_all.SetFont(font_title_all)
        tips_input.SetFont(font_content)
        bt_encryption.SetFont(font_button_small)
        bt_decrypt.SetFont(font_button_small)
        title_result_encryption.SetFont(font_title_result)
        bt_copy_encryption.SetFont(font_button_large)
        title_result_decrypt.SetFont(font_title_result)
        bt_copy_decrypt.SetFont(font_button_large)
        bt_about.SetFont(font_button_large)
        bt_updatelog.SetFont(font_button_large)
        bt_quit.SetFont(font_button_large)

        # 布局
        # 标题，横向
        sizer_h_title_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_h_title_1.Add(title_all, proportion=1, flag=wx.ALIGN_CENTER | wx.ALL, border=20)
        sizer_h_title_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_h_title_2.Add(tips_input, proportion=1, flag=wx.ALIGN_LEFT)
        sizer_h_title_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_h_title_3.Add(self.string_primary, proportion=1, flag=wx.ALIGN_LEFT | wx.BOTTOM, border=5)
        sizer_h_title_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_h_title_4.Add(bt_encryption, proportion=0, flag=wx.ALIGN_LEFT | wx.RIGHT, border=5)
        sizer_h_title_4.Add(bt_decrypt, proportion=0, flag=wx.ALIGN_LEFT | wx.LEFT, border=5)
        # 标题，纵向
        sizer_v_title = wx.BoxSizer(wx.VERTICAL)
        sizer_v_title.Add(sizer_h_title_1, proportion=0, flag=wx.ALIGN_CENTER)
        sizer_v_title.Add(sizer_h_title_2, proportion=0, flag=wx.ALIGN_LEFT)
        sizer_v_title.Add(sizer_h_title_3, proportion=0, flag=wx.ALIGN_CENTER)
        sizer_v_title.Add(sizer_h_title_4, proportion=0, flag=wx.ALIGN_LEFT)
        # 加密结果，横向
        sizer_h_encryption_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_h_encryption_1.Add(title_result_encryption, proportion=1, flag=wx.ALIGN_CENTER)
        sizer_h_encryption_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_h_encryption_2.Add(self.string_new_encryption, proportion=1, flag=wx.ALIGN_CENTER)
        sizer_h_encryption_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_h_encryption_3.Add(bt_copy_encryption, proportion=1, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        # 加密结果，纵向
        sizer_v_encryption = wx.BoxSizer(wx.VERTICAL)
        sizer_v_encryption.Add(sizer_h_encryption_1, proportion=0, flag=wx.ALIGN_CENTER)
        sizer_v_encryption.Add(sizer_h_encryption_2, proportion=0, flag=wx.ALIGN_CENTER)
        sizer_v_encryption.Add(sizer_h_encryption_3, proportion=0, flag=wx.ALIGN_CENTER)
        # 解密结果，横向
        sizer_h_decrypt_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_h_decrypt_1.Add(title_result_decrypt, proportion=1, flag=wx.ALIGN_CENTER)
        sizer_h_decrypt_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_h_decrypt_2.Add(self.string_new_decrypt, proportion=1, flag=wx.ALIGN_CENTER)
        sizer_h_decrypt_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_h_decrypt_3.Add(bt_copy_decrypt, proportion=1, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        # 解密结果，纵向
        sizer_v_decrypt = wx.BoxSizer(wx.VERTICAL)
        sizer_v_decrypt.Add(sizer_h_decrypt_1, proportion=0, flag=wx.ALIGN_CENTER)
        sizer_v_decrypt.Add(sizer_h_decrypt_2, proportion=0, flag=wx.ALIGN_CENTER)
        sizer_v_decrypt.Add(sizer_h_decrypt_3, proportion=0, flag=wx.ALIGN_CENTER)
        # 结果，横向
        sizer_h_result = wx.BoxSizer(wx.HORIZONTAL)
        sizer_h_result.Add(sizer_v_encryption, proportion=1, flag=wx.ALIGN_CENTER | wx.RIGHT, border=5)
        sizer_h_result.Add(sizer_v_decrypt, proportion=1, flag=wx.ALIGN_CENTER | wx.LEFT, border=5)
        # 菜单，横向
        sizer_h_buttons = wx.BoxSizer(wx.HORIZONTAL)
        sizer_h_buttons.Add(bt_about, proportion=2, flag=wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=5)
        sizer_h_buttons.Add(bt_updatelog, proportion=2, flag=wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=5)
        sizer_h_buttons.Add(bt_quit, proportion=2, flag=wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=5)
        # 所有，纵向
        sizer_v_all = wx.BoxSizer(wx.VERTICAL)
        sizer_v_all.Add(sizer_v_title, proportion=1, flag=wx.ALIGN_CENTER)
        sizer_v_all.Add(sizer_h_result, proportion=1, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)
        sizer_v_all.Add(sizer_h_buttons, proportion=1, flag=wx.ALIGN_CENTER)
        # 最后一个sizer，为了让所有控件都不会错位
        sizer_final = wx.BoxSizer(wx.VERTICAL)
        sizer_final.Add(sizer_v_all, proportion=0, flag=wx.ALIGN_CENTER)
        # 应用sizer
        pnl.SetSizer(sizer_final)
        # 这是我第一次没有采用传统布局方法

        # 图标
        try:
            open('image/icon.ico', 'rb')
        except FileNotFoundError:
            print("没有找到图标文件")
        else:
            self.icon = wx.Icon(name="image/icon.ico", type=wx.BITMAP_TYPE_ICO)
            self.SetIcon(self.icon)


    def get_run_state(self):
        """
        获取运行状态
        """
        # 这里是为了防止文本框为空时按下回车后报错
        try:
            run_mode = self.string_primary.GetValue()[-1]
        except IndexError:
            run_mode = 'x'

        # 返回
        return run_mode

    def enter_text(self, event):
        """
        文本框检测机制
        """
        # 获取
        run_mode = self.get_run_state()

        # 判断
        if run_mode == 'z':
            self.run_decrypt(self)
        else:
            self.run_encryption(self)

    def run_encryption(self, event):
        """
        用于加密
        """
        string = self.string_primary.GetValue()
        new_string = encryption(string)
        self.string_new_encryption.SetValue(str(new_string))
        print("加密后:", new_string)
        self.copy_encryption(self)
        return new_string

    def run_decrypt(self, event):
        """
        用于解密
        """
        string = self.string_primary.GetValue()
        try:
            new_string = decrypt(string)
        except ValueError:
            wx.MessageBox('原密码损坏', '解密失败')
        else:
            self.string_new_decrypt.SetValue(str(new_string))
            print("解密后:", new_string)
            self.copy_decrypt(self)
            return new_string

    def copy_encryption(self, event):
        from os import popen
        text = self.string_new_encryption.GetValue()
        command = f'echo {text.strip()}| clip'
        popen(command)
        """
        bug记录：
        os.system(cmd)
        的返回值是脚本的退出状态码，只会有0(成功), 1, 2
        os.popen(cmd)
        返回脚本执行的输出内容作为返回值
        """
        print(f"已复制：{text}")

    def copy_decrypt(self, event):
        from os import popen
        text = self.string_new_decrypt.GetValue()
        command = f'echo {text.strip()} | clip'
        popen(command)
        print(f"已复制：{text}")

    @staticmethod
    def show_about(event):
        message = """软件说明

文本框：
文本框中的内容，
如果最后一个字符为z，
运行方式为解密，否则为加密；
如果密码中最后没有x，
明文的最后一个字符不会被解密；
如果有，z必须在x后面
        
一些想说的话:
这原本是另一个项目的产物，
但是我忽然发掘到了它的其他作用，
于是决定写一个新的项目，作为2.0版本。
这原本是2.0，
但是1.x是我第二个Python项目，
因为情怀，所以被留了下来"""
        wx.MessageBox(message, "软件说明")

    @staticmethod
    def show_updatelog(event):
        message = """正式开始时间：2022.1.19 13:24

2022.1.20 11:22
v2.0:
 2.x的第一个版本，
相比1.x，
这次的加密和解密算法不用依赖密码字典，
完全靠数据处理操作

2022.1.21 18:27
v2.1:
添加了文本框检测机制，
同把这个机制运用到加密算法

2022.1.21 20:41
v2.2:
多行文本框"""
        wx.MessageBox(message, "更新日志")

    @staticmethod
    def bt_exit(event):
        from sys import exit
        exit()


if __name__ == '__main__':
    app = wx.App()
    frame = StringEncryptor(parent=None, id=-1)
    frame.Show()
    app.MainLoop()

# 更新时间都写在GUI的日志里了
