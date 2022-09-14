#! env python3
##############################################
#
# Name: U5_6_Stadtlauf_Bern_check_text.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 10.09.2022
#
# Purpose: Modul mit den passenden Texten pro Position
#
##############################################

def check_text(x,y):
   '''Prüfen ob und welcher Text angezeigt werden soll'''

   if x>200 and x<250 and y>150 and y<170: 
      text2show='Käfigturm'
      xt,yt=x,y
   elif x>410 and x<460 and y>175 and y<190: 
      text2show='Zytglogge'
      xt,yt=x,y
   elif x>190 and x<240 and y>210 and y<240: 
      text2show='Bundeshaus'
      xt,yt=x,y
   else:
      text2show,xt,yt=None,x,x

   return text2show,xt,yt
