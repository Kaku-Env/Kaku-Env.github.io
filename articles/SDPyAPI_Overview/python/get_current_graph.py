import sd

ctx = sd.getContext()
app = ctx.getSDApplication()
uiMgr = app.getQtForPythonUIMgr()
c_graph = uiMgr.getCurrentGraph()