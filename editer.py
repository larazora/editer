import wx


def click_save_button(event):
    save_file = open('wxtest.txt','w')
    save_file.write(text.GetValue())
    save_file.close()

if __name__ == '__main__':
    window = wx.App()
    frame = wx.Frame(None, -1, 'テキストエディタテスト', size = (500, 250))

    panel = wx.Panel(frame, -1)
    save_button = wx.Button(panel, -1,pos = (10, 10),label = '保存')

    text = wx.TextCtrl(panel, -1, pos = (10, 50), size = (465, 150))
    save_button.Bind(wx.EVT_BUTTON, click_save_button)
    frame.Show()
    window.MainLoop()
