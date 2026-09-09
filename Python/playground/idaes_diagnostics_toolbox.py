from idaes.core.util.model_diagnostics import DiagnosticsToolbox

print(dir(DiagnosticsToolbox))
# # 实例化DiagnosticsToolbox
# toolbox = DiagnosticsToolbox("fs")

# # 获取DiagnosticsToolbox类的所有属性
attributes = dir(DiagnosticsToolbox)

# # 过滤出所有以"display_"开头的函数
display_functions = [
    attr
    for attr in attributes
    if attr.startswith("display_") and callable(getattr(DiagnosticsToolbox, attr))
]

# # 打印所有找到的函数名称
for func in display_functions:
    print(func)
