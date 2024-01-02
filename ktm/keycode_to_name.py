from keyname import KeyName

_keycode_to_name=[
    "\\0","\\1","\\2","\\3","\\4","\\5","\\6","\\7",
    KeyName.KeyName_Backspace.value         ,#8
    KeyName.KeyName_Tab.value               ,#9
    "\\10","\\11","\\12",
    KeyName.KeyName_Enter.value             ,#13
    "\\14","\\15","\\16","\\17","\\18",
    KeyName.KeyName_PauseBreak.value        ,#19
    KeyName.KeyName_CapsLk.value            ,#20
    "\\21","\\22","\\23","\\24","\\25","\\26",
    KeyName.KeyName_Esc.value               ,#27
    "\\28","\\29",
    "\\30","\\31",
    KeyName.KeyName_Space.value             ,#32
    KeyName.KeyName_PageUp.value            ,#33
    KeyName.KeyName_PageDown.value          ,#34
    KeyName.KeyName_End.value               ,#35
    KeyName.KeyName_Home.value              ,#36
    KeyName.KeyName_Left.value              ,#37
    KeyName.KeyName_Up.value                ,#38
    KeyName.KeyName_Right.value             ,#39
    KeyName.KeyName_Down.value              ,#40
    "\\41","\\42","\\43",
    KeyName.KeyName_PrintScreen.value       ,#44
    KeyName.KeyName_Insert.value            ,#45
    KeyName.KeyName_Delete.value            ,#46
    "\\47",
    KeyName.KeyName_0.value                 ,#48
    KeyName.KeyName_1.value                 ,#49
    KeyName.KeyName_2.value                 ,#50
    KeyName.KeyName_3.value                 ,#51
    KeyName.KeyName_4.value                 ,#52
    KeyName.KeyName_5.value                 ,#53
    KeyName.KeyName_6.value                 ,#54
    KeyName.KeyName_7.value                 ,#55
    KeyName.KeyName_8.value                 ,#56
    KeyName.KeyName_9.value                 ,#57
    "\\58","\\59","\\60","\\61","\\62","\\63","\\64",
    KeyName.KeyName_A.value                 ,#65
    KeyName.KeyName_B.value                 ,#66
    KeyName.KeyName_C.value                 ,#67
    KeyName.KeyName_D.value                 ,#68
    KeyName.KeyName_E.value                 ,#69
    KeyName.KeyName_F.value                 ,#70
    KeyName.KeyName_G.value                 ,#71
    KeyName.KeyName_H.value                 ,#72
    KeyName.KeyName_I.value                 ,#73
    KeyName.KeyName_J.value                 ,#74
    KeyName.KeyName_K.value                 ,#75
    KeyName.KeyName_L.value                 ,#76
    KeyName.KeyName_M.value                 ,#77
    KeyName.KeyName_N.value                 ,#78
    KeyName.KeyName_O.value                 ,#79
    KeyName.KeyName_P.value                 ,#80
    KeyName.KeyName_Q.value                 ,#81
    KeyName.KeyName_R.value                 ,#82
    KeyName.KeyName_S.value                 ,#83
    KeyName.KeyName_T.value                 ,#84
    KeyName.KeyName_U.value                 ,#85
    KeyName.KeyName_V.value                 ,#86
    KeyName.KeyName_W.value                 ,#87
    KeyName.KeyName_X.value                 ,#88
    KeyName.KeyName_Y.value                 ,#89
    KeyName.KeyName_Z.value                 ,#90
    KeyName.KeyName_LeftWin.value           ,#91
    KeyName.KeyName_RightWin.value          ,#92
    KeyName.KeyName_Application.value       ,#93
    "\\94","\\95","\\96","\\97","\\98","\\99",
    "\\100","\\101","\\102","\\103","\\104","\\105",
    KeyName.KeyName_Multiply.value          ,#106# Operator*
    KeyName.KeyName_Plus.value              ,#107# Operator+
    "\\108",
    KeyName.KeyName_Minus.value             ,#109# Operator-
    "\\110",
    KeyName.KeyName_Divide.value            ,#111,# Operator/
    KeyName.KeyName_F1.value                ,#112
    KeyName.KeyName_F2.value                ,#113
    KeyName.KeyName_F3.value                ,#114
    KeyName.KeyName_F4.value                ,#115
    KeyName.KeyName_F5.value                ,#116
    KeyName.KeyName_F6.value                ,#117
    KeyName.KeyName_F7.value                ,#118
    KeyName.KeyName_F8.value                ,#119
    KeyName.KeyName_F9.value                ,#120
    KeyName.KeyName_F10.value               ,#121
    KeyName.KeyName_F11.value               ,#122
    KeyName.KeyName_F12.value               ,#123
    "\\124","\\125","\\126","\\127","\\128","\\129",
    "\\130","\\131","\\132","\\133","\\134","\\135","\\136","\\137","\\138","\\139",
    "\\140","\\141","\\142","\\143",
    KeyName.KeyName_NumLock.value           ,#144
    KeyName.KeyName_ScrollLock.value        ,#145
    "\\146","\\147","\\148","\\149",
    "\\150","\\151","\\152","\\153","\\154","\\155","\\156","\\157","\\158","\\159",
    KeyName.KeyName_LeftShift.value         ,#160
    KeyName.KeyName_RightShfit.value        ,#161
    KeyName.KeyName_LeftCtrl.value          ,#162
    KeyName.KeyName_RightCtrl.value         ,#163
    KeyName.KeyName_LeftAlt.value           ,#164
    KeyName.KeyName_RightAlt.value          ,#165
    "\\166","\\167","\\168","\\169",
    "\\170","\\171","\\172","\\173","\\174","\\175","\\176","\\177","\\178","\\179",
    "\\180","\\181","\\182","\\183","\\184","\\185",
    KeyName.KeyName_Semicolon.value         ,#186# ;
    KeyName.KeyName_Equal.value             ,#187# =
    KeyName.KeyName_Comma.value             ,#188# ,
    KeyName.KeyName_Hyphen.value            ,#189# -
    KeyName.KeyName_Period.value            ,#190# .
    KeyName.KeyName_Slash.value             ,#191# /
    KeyName.KeyName_BackQuote.value         ,#192# `
    "\\193","\\194","\\195","\\196","\\197","\\198","\\199",
    "\\200","\\201","\\202","\\203","\\204","\\205","\\206","\\207","\\208","\\209",
    "\\210","\\211","\\212","\\213","\\214","\\215","\\216","\\217","\\218",
    KeyName.KeyName_LeftSquareBracket.value ,#219# [
    KeyName.KeyName_VerticalBar.value       ,#220# |
    KeyName.KeyName_RightSquareBracket.value,#221# ]
    KeyName.KeyName_SingleQuote.value       ,#222# '
    "\\223","\\224","\\225","\\226","\\227","\\228","\\229",
    "\\230","\\231","\\232","\\233","\\234","\\235","\\236","\\237","\\238","\\239",
    "\\240","\\241","\\242","\\243","\\244","\\245","\\246","\\247","\\248","\\249",
    "\\250","\\251","\\252","\\253","\\254","\\255"
]

def keycode_to_name(key):
    return _keycode_to_name[key]
