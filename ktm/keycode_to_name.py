from keyname import KeyName

_keycode_to_name=[
    "\\0","\\1","\\2","\\3","\\4","\\5","\\6","\\7",
    KeyName._Backspace         ,#8
    KeyName._Tab               ,#9
    "\\10","\\11","\\12",
    KeyName._Enter             ,#13
    "\\14","\\15","\\16","\\17","\\18",
    KeyName._PauseBreak        ,#19
    KeyName._CapsLk            ,#20
    "\\21","\\22","\\23","\\24","\\25","\\26",
    KeyName._Esc               ,#27
    "\\28","\\29",
    "\\30","\\31",
    KeyName._Space             ,#32
    KeyName._PageUp            ,#33
    KeyName._PageDown          ,#34
    KeyName._End               ,#35
    KeyName._Home              ,#36
    KeyName._Left              ,#37
    KeyName._Up                ,#38
    KeyName._Right             ,#39
    KeyName._Down              ,#40
    "\\41","\\42","\\43",
    KeyName._PrintScreen       ,#44
    KeyName._Insert            ,#45
    KeyName._Delete            ,#46
    "\\47",
    KeyName._0                 ,#48
    KeyName._1                 ,#49
    KeyName._2                 ,#50
    KeyName._3                 ,#51
    KeyName._4                 ,#52
    KeyName._5                 ,#53
    KeyName._6                 ,#54
    KeyName._7                 ,#55
    KeyName._8                 ,#56
    KeyName._9                 ,#57
    "\\58","\\59","\\60","\\61","\\62","\\63","\\64",
    KeyName._A                 ,#65
    KeyName._B                 ,#66
    KeyName._C                 ,#67
    KeyName._D                 ,#68
    KeyName._E                 ,#69
    KeyName._F                 ,#70
    KeyName._G                 ,#71
    KeyName._H                 ,#72
    KeyName._I                 ,#73
    KeyName._J                 ,#74
    KeyName._K                 ,#75
    KeyName._L                 ,#76
    KeyName._M                 ,#77
    KeyName._N                 ,#78
    KeyName._O                 ,#79
    KeyName._P                 ,#80
    KeyName._Q                 ,#81
    KeyName._R                 ,#82
    KeyName._S                 ,#83
    KeyName._T                 ,#84
    KeyName._U                 ,#85
    KeyName._V                 ,#86
    KeyName._W                 ,#87
    KeyName._X                 ,#88
    KeyName._Y                 ,#89
    KeyName._Z                 ,#90
    KeyName._LeftWin           ,#91
    KeyName._RightWin          ,#92
    KeyName._Application       ,#93
    "\\94","\\95","\\96","\\97","\\98","\\99",
    "\\100","\\101","\\102","\\103","\\104","\\105",
    KeyName._Multiply          ,#106# Operator*
    KeyName._Plus              ,#107# Operator+
    "\\108",
    KeyName._Minus             ,#109# Operator-
    "\\110",
    KeyName._Divide            ,#111,# Operator/
    KeyName._F1                ,#112
    KeyName._F2                ,#113
    KeyName._F3                ,#114
    KeyName._F4                ,#115
    KeyName._F5                ,#116
    KeyName._F6                ,#117
    KeyName._F7                ,#118
    KeyName._F8                ,#119
    KeyName._F9                ,#120
    KeyName._F10               ,#121
    KeyName._F11               ,#122
    KeyName._F12               ,#123
    KeyName._F13               ,#124
    KeyName._F14               ,#125
    KeyName._F15               ,#126
    KeyName._F16               ,#127
    KeyName._F17               ,#128
    KeyName._F18               ,#129
    KeyName._F19               ,#130
    KeyName._F20               ,#131
    "\\132","\\133","\\134","\\135","\\136","\\137","\\138","\\139",
    "\\140","\\141","\\142","\\143",
    KeyName._NumLock           ,#144
    KeyName._ScrollLock        ,#145
    "\\146","\\147","\\148","\\149",
    "\\150","\\151","\\152","\\153","\\154","\\155","\\156","\\157","\\158","\\159",
    KeyName._LeftShift         ,#160
    KeyName._RightShfit        ,#161
    KeyName._LeftCtrl          ,#162
    KeyName._RightCtrl         ,#163
    KeyName._LeftAlt           ,#164
    KeyName._RightAlt          ,#165
    "\\166","\\167","\\168","\\169",
    "\\170","\\171","\\172",
    KeyName._MediaVolumeMute   ,#173
    KeyName._MediaVolumeDown   ,#174
    KeyName._MediaVolumeUp     ,#175
    KeyName._MediaNextTrack    ,#176
    KeyName._MediaPrevTrack    ,#177
    KeyName._MediaStop         ,#178
    KeyName._MediaPlayPause    ,#179
    "\\180","\\181","\\182","\\183","\\184","\\185",
    KeyName._Semicolon         ,#186# ;
    KeyName._Equal             ,#187# =
    KeyName._Comma             ,#188# ,
    KeyName._Hyphen            ,#189# -
    KeyName._Period            ,#190# .
    KeyName._Slash             ,#191# /
    KeyName._BackQuote         ,#192# `
    "\\193","\\194","\\195","\\196","\\197","\\198","\\199",
    "\\200","\\201","\\202","\\203","\\204","\\205","\\206","\\207","\\208","\\209",
    "\\210","\\211","\\212","\\213","\\214","\\215","\\216","\\217","\\218",
    KeyName._LeftSquareBracket ,#219# [
    KeyName._VerticalBar       ,#220# |
    KeyName._RightSquareBracket,#221# ]
    KeyName._SingleQuote       ,#222# '
    "\\223","\\224","\\225","\\226","\\227","\\228","\\229",
    "\\230","\\231","\\232","\\233","\\234","\\235","\\236","\\237","\\238","\\239",
    "\\240","\\241","\\242","\\243","\\244","\\245","\\246","\\247","\\248","\\249",
    "\\250","\\251","\\252","\\253","\\254","\\255"
]

def keycode_to_name(key):
    global _keycode_to_name
    return _keycode_to_name[key]