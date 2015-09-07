
import wx
import wx.grid


class DotDict(dict):
    """dot.notation access to dictionary attributes"""
    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError

    def __setattr__(self, key, value):
        self[key] = value


class ImageRenderer(wx.grid.GridCellRenderer):
    def __init__(self, img):
        wx.grid.GridCellRenderer.__init__(self)
        self._img = img

    def Draw(self, grid, attr, dc, rect, row, col, is_selected):
        image = wx.MemoryDC()
        image.SelectObject(self._img)
        dc.SetBackgroundMode(wx.SOLID)
        if is_selected:
            dc.SetBrush(wx.Brush((64, 64, 64), wx.SOLID))
        else:
            dc.SetBrush(wx.Brush(wx.BLACK, wx.SOLID))
        dc.DrawRectangle(rect)
        width, height = self._img.GetWidth(), self._img.GetHeight()
        dc.Blit(rect.x, rect.y, width, height, image, 0, 0, wx.COPY, True)
