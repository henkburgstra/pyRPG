# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

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
		self.btn_tavern.Bind( wx.EVT_BUTTON, self.OnBtnTavernClick )
		self.btn_party.Bind( wx.EVT_BUTTON, self.OnBtnPartyClick )
		self.btn_exit.Bind( wx.EVT_BUTTON, self.OnBtnExitClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnBtnNewClick( self, event ):
		event.Skip()
	
	def OnBtnLoadClick( self, event ):
		event.Skip()
	
	def OnBtnTavernClick( self, event ):
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
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Party", pos = wx.DefaultPosition, size = wx.Size( 1280,800 ), style = wx.STAY_ON_TOP|wx.NO_BORDER )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		szr_party = wx.BoxSizer( wx.VERTICAL )
		
		szr_heroes = wx.BoxSizer( wx.HORIZONTAL )
		
		self.pnl_hero1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		self.pnl_hero1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		szr_hero1 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 3, 2, 0, 20 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.bmp_p1 = wx.StaticBitmap( self.pnl_hero1, wx.ID_ANY, wx.NullBitmap, wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		fgSizer1.Add( self.bmp_p1, 0, wx.ALL|wx.EXPAND, 10 )
		
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
		
		self.gau_p1 = wx.Gauge( self.pnl_hero1, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.gau_p1.SetValue( 0 ) 
		self.gau_p1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.gau_p1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer33.Add( self.gau_p1, 1, wx.ALL, 5 )
		
		
		szr_hero1.Add( bSizer33, 0, wx.EXPAND, 5 )
		
		
		self.pnl_hero1.SetSizer( szr_hero1 )
		self.pnl_hero1.Layout()
		szr_hero1.Fit( self.pnl_hero1 )
		szr_heroes.Add( self.pnl_hero1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.pnl_hero2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		szr_hero2 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer11 = wx.FlexGridSizer( 0, 2, 0, 20 )
		fgSizer11.SetFlexibleDirection( wx.BOTH )
		fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.bmp_p2 = wx.StaticBitmap( self.pnl_hero2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		fgSizer11.Add( self.bmp_p2, 0, wx.ALL|wx.EXPAND, 10 )
		
		self.lbl_nam2 = wx.StaticText( self.pnl_hero2, wx.ID_ANY, u"p2nam", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_nam2.Wrap( -1 )
		self.lbl_nam2.SetFont( wx.Font( 14, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_nam2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizer11.Add( self.lbl_nam2, 0, wx.ALL, 5 )
		
		self.lbl_lev20 = wx.StaticText( self.pnl_hero2, wx.ID_ANY, u"Level", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_lev20.Wrap( -1 )
		self.lbl_lev20.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_lev20.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizer11.Add( self.lbl_lev20, 0, wx.ALL, 5 )
		
		self.lbl_lev2 = wx.StaticText( self.pnl_hero2, wx.ID_ANY, u"%%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_lev2.Wrap( -1 )
		self.lbl_lev2.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_lev2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizer11.Add( self.lbl_lev2, 0, wx.ALL, 5 )
		
		self.lbl_hp20 = wx.StaticText( self.pnl_hero2, wx.ID_ANY, u"HitPoints", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_hp20.Wrap( -1 )
		self.lbl_hp20.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_hp20.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizer11.Add( self.lbl_hp20, 0, wx.ALL, 5 )
		
		self.lbl_hp2 = wx.StaticText( self.pnl_hero2, wx.ID_ANY, u"%% / %%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_hp2.Wrap( -1 )
		self.lbl_hp2.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_hp2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizer11.Add( self.lbl_hp2, 0, wx.ALL, 5 )
		
		
		szr_hero2.Add( fgSizer11, 0, wx.EXPAND|wx.LEFT, 5 )
		
		bSizer331 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.gau_p2 = wx.Gauge( self.pnl_hero2, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.gau_p2.SetValue( 0 ) 
		bSizer331.Add( self.gau_p2, 1, wx.ALL, 5 )
		
		
		szr_hero2.Add( bSizer331, 0, wx.EXPAND, 5 )
		
		
		self.pnl_hero2.SetSizer( szr_hero2 )
		self.pnl_hero2.Layout()
		szr_hero2.Fit( self.pnl_hero2 )
		szr_heroes.Add( self.pnl_hero2, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.pnl_hero3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		self.pnl_hero3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		szr_hero3 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer12 = wx.FlexGridSizer( 3, 2, 0, 20 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.bmp_p3 = wx.StaticBitmap( self.pnl_hero3, wx.ID_ANY, wx.NullBitmap, wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		fgSizer12.Add( self.bmp_p3, 0, wx.ALL|wx.EXPAND, 10 )
		
		self.lbl_nam3 = wx.StaticText( self.pnl_hero3, wx.ID_ANY, u"p3nam", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_nam3.Wrap( -1 )
		self.lbl_nam3.SetFont( wx.Font( 14, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_nam3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizer12.Add( self.lbl_nam3, 0, wx.ALL, 5 )
		
		self.lbl_lev30 = wx.StaticText( self.pnl_hero3, wx.ID_ANY, u"Level", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_lev30.Wrap( -1 )
		self.lbl_lev30.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_lev30.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizer12.Add( self.lbl_lev30, 0, wx.ALL, 5 )
		
		self.lbl_lev3 = wx.StaticText( self.pnl_hero3, wx.ID_ANY, u"%%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_lev3.Wrap( -1 )
		self.lbl_lev3.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_lev3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizer12.Add( self.lbl_lev3, 0, wx.ALL, 5 )
		
		self.lbl_hp30 = wx.StaticText( self.pnl_hero3, wx.ID_ANY, u"HitPoints", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_hp30.Wrap( -1 )
		self.lbl_hp30.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_hp30.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizer12.Add( self.lbl_hp30, 0, wx.ALL, 5 )
		
		self.lbl_hp3 = wx.StaticText( self.pnl_hero3, wx.ID_ANY, u"%% / %%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_hp3.Wrap( -1 )
		self.lbl_hp3.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_hp3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizer12.Add( self.lbl_hp3, 0, wx.ALL, 5 )
		
		
		szr_hero3.Add( fgSizer12, 0, wx.EXPAND|wx.LEFT, 5 )
		
		bSizer332 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.gau_p3 = wx.Gauge( self.pnl_hero3, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.gau_p3.SetValue( 0 ) 
		self.gau_p3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.gau_p3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer332.Add( self.gau_p3, 1, wx.ALL, 5 )
		
		
		szr_hero3.Add( bSizer332, 0, wx.EXPAND, 5 )
		
		
		self.pnl_hero3.SetSizer( szr_hero3 )
		self.pnl_hero3.Layout()
		szr_hero3.Fit( self.pnl_hero3 )
		szr_heroes.Add( self.pnl_hero3, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.pnl_hero4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		self.pnl_hero4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		szr_hero4 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer13 = wx.FlexGridSizer( 3, 2, 0, 20 )
		fgSizer13.SetFlexibleDirection( wx.BOTH )
		fgSizer13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.bmp_p4 = wx.StaticBitmap( self.pnl_hero4, wx.ID_ANY, wx.NullBitmap, wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		fgSizer13.Add( self.bmp_p4, 0, wx.ALL|wx.EXPAND, 10 )
		
		self.lbl_nam4 = wx.StaticText( self.pnl_hero4, wx.ID_ANY, u"p4nam", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_nam4.Wrap( -1 )
		self.lbl_nam4.SetFont( wx.Font( 14, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_nam4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizer13.Add( self.lbl_nam4, 0, wx.ALL, 5 )
		
		self.lbl_lev40 = wx.StaticText( self.pnl_hero4, wx.ID_ANY, u"Level", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_lev40.Wrap( -1 )
		self.lbl_lev40.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_lev40.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizer13.Add( self.lbl_lev40, 0, wx.ALL, 5 )
		
		self.lbl_lev4 = wx.StaticText( self.pnl_hero4, wx.ID_ANY, u"%%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_lev4.Wrap( -1 )
		self.lbl_lev4.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_lev4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizer13.Add( self.lbl_lev4, 0, wx.ALL, 5 )
		
		self.lbl_hp40 = wx.StaticText( self.pnl_hero4, wx.ID_ANY, u"HitPoints", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_hp40.Wrap( -1 )
		self.lbl_hp40.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_hp40.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizer13.Add( self.lbl_hp40, 0, wx.ALL, 5 )
		
		self.lbl_hp4 = wx.StaticText( self.pnl_hero4, wx.ID_ANY, u"%% / %%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_hp4.Wrap( -1 )
		self.lbl_hp4.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_hp4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizer13.Add( self.lbl_hp4, 0, wx.ALL, 5 )
		
		
		szr_hero4.Add( fgSizer13, 0, wx.EXPAND|wx.LEFT, 5 )
		
		bSizer333 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.gau_p4 = wx.Gauge( self.pnl_hero4, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.gau_p4.SetValue( 0 ) 
		self.gau_p4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.gau_p4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer333.Add( self.gau_p4, 1, wx.ALL, 5 )
		
		
		szr_hero4.Add( bSizer333, 0, wx.EXPAND, 5 )
		
		
		self.pnl_hero4.SetSizer( szr_hero4 )
		self.pnl_hero4.Layout()
		szr_hero4.Fit( self.pnl_hero4 )
		szr_heroes.Add( self.pnl_hero4, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.pnl_hero5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		self.pnl_hero5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		szr_hero5 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer14 = wx.FlexGridSizer( 3, 2, 0, 20 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.bmp_p5 = wx.StaticBitmap( self.pnl_hero5, wx.ID_ANY, wx.NullBitmap, wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		fgSizer14.Add( self.bmp_p5, 0, wx.ALL|wx.EXPAND, 10 )
		
		self.lbl_nam5 = wx.StaticText( self.pnl_hero5, wx.ID_ANY, u"p5nam", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_nam5.Wrap( -1 )
		self.lbl_nam5.SetFont( wx.Font( 14, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_nam5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizer14.Add( self.lbl_nam5, 0, wx.ALL, 5 )
		
		self.lbl_lev50 = wx.StaticText( self.pnl_hero5, wx.ID_ANY, u"Level", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_lev50.Wrap( -1 )
		self.lbl_lev50.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_lev50.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizer14.Add( self.lbl_lev50, 0, wx.ALL, 5 )
		
		self.lbl_lev5 = wx.StaticText( self.pnl_hero5, wx.ID_ANY, u"%%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_lev5.Wrap( -1 )
		self.lbl_lev5.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_lev5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizer14.Add( self.lbl_lev5, 0, wx.ALL, 5 )
		
		self.lbl_hp50 = wx.StaticText( self.pnl_hero5, wx.ID_ANY, u"HitPoints", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_hp50.Wrap( -1 )
		self.lbl_hp50.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_hp50.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizer14.Add( self.lbl_hp50, 0, wx.ALL, 5 )
		
		self.lbl_hp5 = wx.StaticText( self.pnl_hero5, wx.ID_ANY, u"%% / %%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_hp5.Wrap( -1 )
		self.lbl_hp5.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_hp5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizer14.Add( self.lbl_hp5, 0, wx.ALL, 5 )
		
		
		szr_hero5.Add( fgSizer14, 0, wx.EXPAND|wx.LEFT, 5 )
		
		bSizer334 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.gau_p5 = wx.Gauge( self.pnl_hero5, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.gau_p5.SetValue( 0 ) 
		self.gau_p5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.gau_p5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer334.Add( self.gau_p5, 1, wx.ALL, 5 )
		
		
		szr_hero5.Add( bSizer334, 0, wx.EXPAND, 5 )
		
		
		self.pnl_hero5.SetSizer( szr_hero5 )
		self.pnl_hero5.Layout()
		szr_hero5.Fit( self.pnl_hero5 )
		szr_heroes.Add( self.pnl_hero5, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.pnl_btns = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.btn_prev = wx.Button( self.pnl_btns, wx.ID_ANY, u"&Previous", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_prev.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_prev.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		gSizer1.Add( self.btn_prev, 0, wx.ALL, 5 )
		
		self.btn_close = wx.Button( self.pnl_btns, wx.ID_ANY, u"&Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_close.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btn_close.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		gSizer1.Add( self.btn_close, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.btn_next = wx.Button( self.pnl_btns, wx.ID_ANY, u"&Next", wx.DefaultPosition, wx.DefaultSize, 0 )
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
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.lbl_stats = wx.StaticText( self.pnl_stats, wx.ID_ANY, u"Stats", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_stats.Wrap( -1 )
		self.lbl_stats.SetFont( wx.Font( 14, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_stats.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		bSizer17.Add( self.lbl_stats, 0, wx.TOP|wx.RIGHT|wx.LEFT|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )
		
		self.grid_stats = wx.grid.Grid( self.pnl_stats, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.grid_stats.CreateGrid( 18, 5 )
		self.grid_stats.EnableEditing( False )
		self.grid_stats.EnableGridLines( False )
		self.grid_stats.EnableDragGridSize( False )
		self.grid_stats.SetMargins( 0, 0 )
		
		# Columns
		self.grid_stats.SetColSize( 0, 100 )
		self.grid_stats.SetColSize( 1, 40 )
		self.grid_stats.SetColSize( 2, 40 )
		self.grid_stats.SetColSize( 3, 40 )
		self.grid_stats.SetColSize( 4, 40 )
		self.grid_stats.EnableDragColMove( False )
		self.grid_stats.EnableDragColSize( False )
		self.grid_stats.SetColLabelSize( 0 )
		self.grid_stats.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.grid_stats.AutoSizeRows()
		self.grid_stats.EnableDragRowSize( False )
		self.grid_stats.SetRowLabelSize( 0 )
		self.grid_stats.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.grid_stats.SetDefaultCellBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.grid_stats.SetDefaultCellTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.grid_stats.SetDefaultCellFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		self.grid_stats.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer17.Add( self.grid_stats, 0, wx.ALL, 36 )
		
		
		self.pnl_stats.SetSizer( bSizer17 )
		self.pnl_stats.Layout()
		bSizer17.Fit( self.pnl_stats )
		szr_info.Add( self.pnl_stats, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.pnl_skills = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		bSizer23 = wx.BoxSizer( wx.VERTICAL )
		
		self.lbl_skills = wx.StaticText( self.pnl_skills, wx.ID_ANY, u"Skills", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_skills.Wrap( -1 )
		self.lbl_skills.SetFont( wx.Font( 14, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_skills.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		bSizer23.Add( self.lbl_skills, 0, wx.TOP|wx.RIGHT|wx.LEFT|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )
		
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer22 = wx.BoxSizer( wx.VERTICAL )
		
		self.bmp_chm = wx.StaticBitmap( self.pnl_skills, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer22.Add( self.bmp_chm, 0, wx.ALL, 0 )
		
		self.bmp_dip = wx.StaticBitmap( self.pnl_skills, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer22.Add( self.bmp_dip, 0, wx.ALL, 0 )
		
		self.bmp_lor = wx.StaticBitmap( self.pnl_skills, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer22.Add( self.bmp_lor, 0, wx.ALL, 0 )
		
		self.bmp_mec = wx.StaticBitmap( self.pnl_skills, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer22.Add( self.bmp_mec, 0, wx.ALL, 0 )
		
		self.bmp_med = wx.StaticBitmap( self.pnl_skills, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer22.Add( self.bmp_med, 0, wx.ALL, 0 )
		
		self.bmp_mer = wx.StaticBitmap( self.pnl_skills, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer22.Add( self.bmp_mer, 0, wx.ALL, 0 )
		
		self.bmp_ran = wx.StaticBitmap( self.pnl_skills, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer22.Add( self.bmp_ran, 0, wx.ALL, 0 )
		
		self.bmp_sci = wx.StaticBitmap( self.pnl_skills, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer22.Add( self.bmp_sci, 0, wx.ALL, 0 )
		
		self.bmp_stl = wx.StaticBitmap( self.pnl_skills, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer22.Add( self.bmp_stl, 0, wx.ALL, 0 )
		
		self.bmp_thf = wx.StaticBitmap( self.pnl_skills, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer22.Add( self.bmp_thf, 0, wx.ALL, 0 )
		
		self.bmp_trb = wx.StaticBitmap( self.pnl_skills, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer22.Add( self.bmp_trb, 0, wx.ALL, 0 )
		
		self.bmp_war = wx.StaticBitmap( self.pnl_skills, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer22.Add( self.bmp_war, 0, wx.ALL, 0 )
		
		self.bmp_haf = wx.StaticBitmap( self.pnl_skills, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer22.Add( self.bmp_haf, 0, wx.ALL, 0 )
		
		self.bmp_mis = wx.StaticBitmap( self.pnl_skills, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer22.Add( self.bmp_mis, 0, wx.ALL, 0 )
		
		self.bmp_pol = wx.StaticBitmap( self.pnl_skills, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer22.Add( self.bmp_pol, 0, wx.ALL, 0 )
		
		self.bmp_shd = wx.StaticBitmap( self.pnl_skills, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer22.Add( self.bmp_shd, 0, wx.ALL, 0 )
		
		self.bmp_swd = wx.StaticBitmap( self.pnl_skills, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer22.Add( self.bmp_swd, 0, wx.ALL, 0 )
		
		self.bmp_thr = wx.StaticBitmap( self.pnl_skills, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer22.Add( self.bmp_thr, 0, wx.ALL, 0 )
		
		
		bSizer20.Add( bSizer22, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 30 )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.grid_skills = wx.grid.Grid( self.pnl_skills, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.grid_skills.CreateGrid( 18, 4 )
		self.grid_skills.EnableEditing( False )
		self.grid_skills.EnableGridLines( False )
		self.grid_skills.EnableDragGridSize( False )
		self.grid_skills.SetMargins( 0, 0 )
		
		# Columns
		self.grid_skills.SetColSize( 0, 90 )
		self.grid_skills.SetColSize( 1, 35 )
		self.grid_skills.SetColSize( 2, 40 )
		self.grid_skills.SetColSize( 3, 40 )
		self.grid_skills.EnableDragColMove( False )
		self.grid_skills.EnableDragColSize( False )
		self.grid_skills.SetColLabelSize( 0 )
		self.grid_skills.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.grid_skills.SetRowSize( 0, 30 )
		self.grid_skills.SetRowSize( 1, 30 )
		self.grid_skills.SetRowSize( 2, 30 )
		self.grid_skills.SetRowSize( 3, 30 )
		self.grid_skills.SetRowSize( 4, 30 )
		self.grid_skills.SetRowSize( 5, 30 )
		self.grid_skills.SetRowSize( 6, 30 )
		self.grid_skills.SetRowSize( 7, 30 )
		self.grid_skills.SetRowSize( 8, 30 )
		self.grid_skills.SetRowSize( 9, 30 )
		self.grid_skills.SetRowSize( 10, 30 )
		self.grid_skills.SetRowSize( 11, 30 )
		self.grid_skills.SetRowSize( 12, 30 )
		self.grid_skills.SetRowSize( 13, 30 )
		self.grid_skills.SetRowSize( 14, 30 )
		self.grid_skills.SetRowSize( 15, 30 )
		self.grid_skills.SetRowSize( 16, 30 )
		self.grid_skills.SetRowSize( 17, 30 )
		self.grid_skills.EnableDragRowSize( False )
		self.grid_skills.SetRowLabelSize( 0 )
		self.grid_skills.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.grid_skills.SetDefaultCellBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.grid_skills.SetDefaultCellTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.grid_skills.SetDefaultCellFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		self.grid_skills.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTRE )
		bSizer18.Add( self.grid_skills, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 30 )
		
		
		bSizer20.Add( bSizer18, 1, wx.EXPAND|wx.LEFT, 10 )
		
		
		bSizer23.Add( bSizer20, 1, wx.EXPAND, 5 )
		
		
		self.pnl_skills.SetSizer( bSizer23 )
		self.pnl_skills.Layout()
		bSizer23.Fit( self.pnl_skills )
		szr_info.Add( self.pnl_skills, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.pnl_inventory = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		bSizer26 = wx.BoxSizer( wx.VERTICAL )
		
		self.lbl_inventory = wx.StaticText( self.pnl_inventory, wx.ID_ANY, u"Inventory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_inventory.Wrap( -1 )
		self.lbl_inventory.SetFont( wx.Font( 14, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_inventory.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		bSizer26.Add( self.lbl_inventory, 0, wx.TOP|wx.RIGHT|wx.LEFT|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )
		
		self.pnl_canvas = wx.Panel( self.pnl_inventory, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.pnl_canvas.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer26.Add( self.pnl_canvas, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.pnl_inventory.SetSizer( bSizer26 )
		self.pnl_inventory.Layout()
		bSizer26.Fit( self.pnl_inventory )
		szr_info.Add( self.pnl_inventory, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_science = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		bSizer27 = wx.BoxSizer( wx.VERTICAL )
		
		self.lbl_science = wx.StaticText( self.m_science, wx.ID_ANY, u"Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_science.Wrap( -1 )
		self.lbl_science.SetFont( wx.Font( 14, 70, 90, 90, False, wx.EmptyString ) )
		self.lbl_science.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		bSizer27.Add( self.lbl_science, 0, wx.TOP|wx.RIGHT|wx.LEFT|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )
		
		
		self.m_science.SetSizer( bSizer27 )
		self.m_science.Layout()
		bSizer27.Fit( self.m_science )
		szr_info.Add( self.m_science, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		szr_party.Add( szr_info, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( szr_party )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_prev.Bind( wx.EVT_BUTTON, self.OnBtnPrevClick )
		self.btn_close.Bind( wx.EVT_BUTTON, self.OnBtnCloseClick )
		self.btn_next.Bind( wx.EVT_BUTTON, self.OnBtnNextClick )
		self.pnl_canvas.Bind( wx.EVT_PAINT, self.OnPanelPaint )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnBtnPrevClick( self, event ):
		event.Skip()
	
	def OnBtnCloseClick( self, event ):
		event.Skip()
	
	def OnBtnNextClick( self, event ):
		event.Skip()
	
	def OnPanelPaint( self, event ):
		event.Skip()
	

###########################################################################
## Class HeroDialog
###########################################################################

class HeroDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 623,469 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bSizer25 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer24.Add( self.bSizer25, 1, wx.EXPAND, 5 )
		
		bSizer26 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_grid3 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid3.CreateGrid( 1, 3 )
		self.m_grid3.EnableEditing( True )
		self.m_grid3.EnableGridLines( True )
		self.m_grid3.EnableDragGridSize( False )
		self.m_grid3.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid3.EnableDragColMove( False )
		self.m_grid3.EnableDragColSize( True )
		self.m_grid3.SetColLabelSize( 30 )
		self.m_grid3.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid3.EnableDragRowSize( True )
		self.m_grid3.SetRowLabelSize( 80 )
		self.m_grid3.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid3.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer26.Add( self.m_grid3, 0, wx.ALL, 5 )
		
		
		bSizer24.Add( bSizer26, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer24 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

