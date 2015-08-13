# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 350,650 ), style = 0|wx.NO_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.lbl_title = wx.StaticText( self, wx.ID_ANY, u"pyRPG", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_title.Wrap( -1 )
		self.lbl_title.SetFont( wx.Font( 60, 70, 90, 92, False, "Colonna MT" ) )
		self.lbl_title.SetForegroundColour( wx.Colour( 125, 0, 0 ) )
		
		bSizer1.Add( self.lbl_title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn_new = wx.Button( self, wx.ID_ANY, u"New Game", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_new.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_new.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer2.Add( self.btn_new, 1, wx.ALL, 5 )
		
		self.btn_load = wx.Button( self, wx.ID_ANY, u"Load Game", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_load.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_load.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer2.Add( self.btn_load, 1, wx.ALL, 5 )
		
		self.btn_save = wx.Button( self, wx.ID_ANY, u"Save Game", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_save.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_save.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer2.Add( self.btn_save, 1, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn_previous = wx.Button( self, wx.ID_ANY, u"<- Previous Area", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_previous.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_previous.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer3.Add( self.btn_previous, 1, wx.ALL, 5 )
		
		self.lbl_area = wx.StaticText( self, wx.ID_ANY, u"Area X", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.lbl_area.Wrap( -1 )
		self.lbl_area.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_area.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		bSizer3.Add( self.lbl_area, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.btn_next = wx.Button( self, wx.ID_ANY, u"Next Area ->", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_next.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_next.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer3.Add( self.btn_next, 1, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.btn_enemies = wx.Button( self, wx.ID_ANY, u"Fight Enemies", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_enemies.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_enemies.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer1.Add( self.btn_enemies, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btn_boss = wx.Button( self, wx.ID_ANY, u"Fight Boss", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_boss.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_boss.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer1.Add( self.btn_boss, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btn_materials = wx.Button( self, wx.ID_ANY, u"Gather Materials", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_materials.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_materials.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer1.Add( self.btn_materials, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btn_shop = wx.Button( self, wx.ID_ANY, u"Shop", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_shop.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_shop.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer1.Add( self.btn_shop, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btn_trainer = wx.Button( self, wx.ID_ANY, u"Trainer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_trainer.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_trainer.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer1.Add( self.btn_trainer, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btn_school = wx.Button( self, wx.ID_ANY, u"School", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_school.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_school.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer1.Add( self.btn_school, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btn_tavern = wx.Button( self, wx.ID_ANY, u"Tavern", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_tavern.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_tavern.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer1.Add( self.btn_tavern, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btn_inn = wx.Button( self, wx.ID_ANY, u"Inn", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_inn.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_inn.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer1.Add( self.btn_inn, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btn_party = wx.Button( self, wx.ID_ANY, u"Party", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_party.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_party.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer1.Add( self.btn_party, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btn_manual = wx.Button( self, wx.ID_ANY, u"Manual", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_manual.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_manual.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer1.Add( self.btn_manual, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btn_exit = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_exit.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_exit.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer1.Add( self.btn_exit, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.VERTICAL )
		
		# Connect Events
		self.btn_new.Bind( wx.EVT_BUTTON, self.BtnNewClick )
		self.btn_load.Bind( wx.EVT_BUTTON, self.BtnLoadClick )
		self.btn_exit.Bind( wx.EVT_BUTTON, self.BtnExitClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def BtnNewClick( self, event ):
		event.Skip()
	
	def BtnLoadClick( self, event ):
		event.Skip()
	
	def BtnExitClick( self, event ):
		event.Skip()
	

