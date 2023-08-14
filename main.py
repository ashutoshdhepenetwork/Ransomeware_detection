import os
import wx

MALWARE_EXTENSIONS = {".exe", ".dll", ".bat", ".locky"}  # Example malware extensions

class MalwareScannerFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MalwareScannerFrame, self).__init__(*args, **kw)

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour(240, 240, 240))

        self.directory_entry = wx.TextCtrl(self.panel)
        self.browse_button = wx.Button(self.panel, label="Browse")
        self.scan_button = wx.Button(self.panel, label="Scan")
        self.result_text = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)

        self.browse_button.Bind(wx.EVT_BUTTON, self.on_browse)
        self.scan_button.Bind(wx.EVT_BUTTON, self.on_scan)

        self.init_ui()

    def init_ui(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.directory_entry, proportion=0, flag=wx.EXPAND | wx.ALL, border=10)
        sizer.Add(self.browse_button, proportion=0, flag=wx.ALL, border=10)
        sizer.Add(self.scan_button, proportion=0, flag=wx.ALL, border=10)
        sizer.Add(self.result_text, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.panel.SetSizerAndFit(sizer)
        self.Show()

    def on_browse(self, event):
        with wx.DirDialog(self, "Select a directory") as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                self.directory_entry.SetValue(dialog.GetPath())

    def on_scan(self, event):
        target_directory = self.directory_entry.GetValue()
        if not os.path.exists(target_directory):
            wx.MessageBox("Directory does not exist.", "Error", wx.OK | wx.ICON_ERROR)
            return

        found_malware = self.scan_directory(target_directory)

        if found_malware:
            self.result_text.SetValue("Potential malware files found:\n" + "\n".join(found_malware))
        else:
            self.result_text.SetValue("No potential malware files found.")

    def scan_directory(self, directory):
        found_malware = []
        for root, _, files in os.walk(directory):
            for file in files:
                _, ext = os.path.splitext(file)
                if ext.lower() in MALWARE_EXTENSIONS:
                    found_malware.append(os.path.join(root, file))
        return found_malware

if __name__ == "__main__":
    app = wx.App(False)
    frame = MalwareScannerFrame(None, title="Malware Scanner")
    app.MainLoop()
