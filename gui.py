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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"pyRPG", pos = wx.DefaultPosition, size = wx.Size( 350,650 ), style = 0|wx.NO_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		szr_main = wx.BoxSizer( wx.VERTICAL )
		
		self.lbl_title = wx.StaticText( self, wx.ID_ANY, u"pyRPG", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_title.Wrap( -1 )
		self.lbl_title.SetFont( wx.Font( 60, 70, 90, 92, False, "Colonna MT" ) )
		self.lbl_title.SetForegroundColour( wx.Colour( 125, 0, 0 ) )
		
		szr_main.Add( self.lbl_title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn_new = wx.Button( self, wx.ID_ANY, u"New Game", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_new.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_new.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer1.Add( self.btn_new, 1, wx.ALL, 5 )
		
		self.btn_load = wx.Button( self, wx.ID_ANY, u"Load Game", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_load.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_load.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer1.Add( self.btn_load, 1, wx.ALL, 5 )
		
		self.btn_save = wx.Button( self, wx.ID_ANY, u"Save Game", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_save.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_save.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer1.Add( self.btn_save, 1, wx.ALL, 5 )
		
		
		szr_main.Add( bSizer1, 1, wx.EXPAND, 5 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn_prev = wx.Button( self, wx.ID_ANY, u"<- Previous Area", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_prev.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_prev.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer2.Add( self.btn_prev, 1, wx.ALL, 5 )
		
		self.lbl_area = wx.StaticText( self, wx.ID_ANY, u"Area X", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.lbl_area.Wrap( -1 )
		self.lbl_area.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_area.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		bSizer2.Add( self.lbl_area, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.btn_next = wx.Button( self, wx.ID_ANY, u"Next Area ->", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_next.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_next.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer2.Add( self.btn_next, 1, wx.ALL, 5 )
		
		
		szr_main.Add( bSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.btn_enemies = wx.Button( self, wx.ID_ANY, u"Fight Enemies", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_enemies.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_enemies.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		szr_main.Add( self.btn_enemies, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btn_boss = wx.Button( self, wx.ID_ANY, u"Fight Boss", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_boss.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_boss.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		szr_main.Add( self.btn_boss, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btn_materials = wx.Button( self, wx.ID_ANY, u"Gather Materials", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_materials.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_materials.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		szr_main.Add( self.btn_materials, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btn_shop = wx.Button( self, wx.ID_ANY, u"Shop", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_shop.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_shop.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		szr_main.Add( self.btn_shop, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btn_trainer = wx.Button( self, wx.ID_ANY, u"Trainer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_trainer.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_trainer.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		szr_main.Add( self.btn_trainer, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btn_school = wx.Button( self, wx.ID_ANY, u"School", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_school.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_school.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		szr_main.Add( self.btn_school, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btn_tavern = wx.Button( self, wx.ID_ANY, u"Tavern", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_tavern.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_tavern.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		szr_main.Add( self.btn_tavern, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btn_inn = wx.Button( self, wx.ID_ANY, u"Inn", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_inn.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_inn.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		szr_main.Add( self.btn_inn, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btn_party = wx.Button( self, wx.ID_ANY, u"Party", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_party.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_party.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		szr_main.Add( self.btn_party, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btn_manual = wx.Button( self, wx.ID_ANY, u"Manual", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_manual.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_manual.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		szr_main.Add( self.btn_manual, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btn_exit = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_exit.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_exit.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		szr_main.Add( self.btn_exit, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( szr_main )
		self.Layout()
		
		self.Centre( wx.VERTICAL )
		
		# Connect Events
		self.btn_new.Bind( wx.EVT_BUTTON, self.OnBtnNewClick )
		self.btn_load.Bind( wx.EVT_BUTTON, self.OnBtnLoadClick )
		self.btn_party.Bind( wx.EVT_BUTTON, self.OnBtnPartyClick )
		self.btn_exit.Bind( wx.EVT_BUTTON, self.OnBtnExitClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnBtnNewClick( self, event ):
		event.Skip()
	
	def OnBtnLoadClick( self, event ):
		event.Skip()
	
	def OnBtnPartyClick( self, event ):
		event.Skip()
	
	def OnBtnExitClick( self, event ):
		event.Skip()
	

###########################################################################
## Class PartyDialog
###########################################################################

class PartyDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Party", pos = wx.DefaultPosition, size = wx.Size( 1280,750 ), style = wx.STAY_ON_TOP|wx.NO_BORDER )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		szr_party = wx.BoxSizer( wx.VERTICAL )
		
		szr_heroes = wx.BoxSizer( wx.HORIZONTAL )
		
		self.pnl_hero1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		self.pnl_hero1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		szr_hero1 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.bmp_p1 = wx.StaticBitmap( self.pnl_hero1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.bmp_p1, 0, wx.ALL, 10 )
		
		self.lbl_nam1 = wx.StaticText( self.pnl_hero1, wx.ID_ANY, u"p1nam", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_nam1.Wrap( -1 )
		self.lbl_nam1.SetFont( wx.Font( 14, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_nam1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizer1.Add( self.lbl_nam1, 0, wx.ALL, 5 )
		
		self.lbl_lev10 = wx.StaticText( self.pnl_hero1, wx.ID_ANY, u"Level", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_lev10.Wrap( -1 )
		self.lbl_lev10.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_lev10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizer1.Add( self.lbl_lev10, 0, wx.ALL, 5 )
		
		self.lbl_lev1 = wx.StaticText( self.pnl_hero1, wx.ID_ANY, u"%%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_lev1.Wrap( -1 )
		self.lbl_lev1.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_lev1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizer1.Add( self.lbl_lev1, 0, wx.ALL, 5 )
		
		self.lbl_hp10 = wx.StaticText( self.pnl_hero1, wx.ID_ANY, u"HitPoints", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_hp10.Wrap( -1 )
		self.lbl_hp10.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_hp10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizer1.Add( self.lbl_hp10, 0, wx.ALL, 5 )
		
		self.lbl_hp1 = wx.StaticText( self.pnl_hero1, wx.ID_ANY, u"%% / %%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_hp1.Wrap( -1 )
		self.lbl_hp1.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_hp1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizer1.Add( self.lbl_hp1, 0, wx.ALL, 5 )
		
		
		szr_hero1.Add( fgSizer1, 0, wx.EXPAND|wx.LEFT, 5 )
		
		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_gauge1 = wx.Gauge( self.pnl_hero1, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 0 ) 
		bSizer33.Add( self.m_gauge1, 1, wx.ALL, 5 )
		
		
		szr_hero1.Add( bSizer33, 0, wx.EXPAND, 5 )
		
		
		self.pnl_hero1.SetSizer( szr_hero1 )
		self.pnl_hero1.Layout()
		szr_hero1.Fit( self.pnl_hero1 )
		szr_heroes.Add( self.pnl_hero1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.pnl_hero2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		szr_heroes.Add( self.pnl_hero2, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.pnl_hero3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		szr_heroes.Add( self.pnl_hero3, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.pnl_hero4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		szr_heroes.Add( self.pnl_hero4, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.pnl_hero5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		szr_heroes.Add( self.pnl_hero5, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.pnl_btns = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.btn_prev = wx.Button( self.pnl_btns, wx.ID_ANY, u"Previous", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_prev.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_prev.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		gSizer1.Add( self.btn_prev, 0, wx.ALL, 5 )
		
		self.btn_close = wx.Button( self.pnl_btns, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_close.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_close.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		gSizer1.Add( self.btn_close, 0, wx.ALL, 5 )
		
		self.btn_next = wx.Button( self.pnl_btns, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_next.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_next.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		gSizer1.Add( self.btn_next, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		
		self.pnl_btns.SetSizer( gSizer1 )
		self.pnl_btns.Layout()
		gSizer1.Fit( self.pnl_btns )
		szr_heroes.Add( self.pnl_btns, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		szr_party.Add( szr_heroes, 0, wx.EXPAND, 5 )
		
		szr_info = wx.BoxSizer( wx.HORIZONTAL )
		
		self.pnl_stats = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		szr_info.Add( self.pnl_stats, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.pnl_skills = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		szr_info.Add( self.pnl_skills, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.pnl_inventory = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		szr_info.Add( self.pnl_inventory, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_science = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		szr_info.Add( self.m_science, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		szr_party.Add( szr_info, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( szr_party )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_close.Bind( wx.EVT_BUTTON, self.OnBtnCloseClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnBtnCloseClick( self, event ):
		event.Skip()
	

