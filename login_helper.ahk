oWhr := ComObjCreate("WinHttp.WinHttpRequest.5.1")
oWhr.Open("GET", "http://127.0.0.1")
oWhr.Send()