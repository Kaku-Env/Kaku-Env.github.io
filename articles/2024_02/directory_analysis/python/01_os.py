import os

root_path = r"C:\Program Files\Blender Foundation\Blender 3.6"

# ============================================================================
# os.listdir()
items = os.listdir(root_path)

print("\n".join(items))
# >> 3.6
#    blender-launcher.exe
#    blender.crt
#    blender.exe ...

print(type(items))
# >> <class 'list'>

# ============================================================================
# 再帰的に

def list_items(path):
    items = os.listdir(path)

    for i in items:
        item = os.path.join(path, i) # フルパスに戻す

        # ファイルの場合
        if os.path.isfile(item):
            print("\t{}".format(i))
        
        # フォルダの場合
        elif os.path.isdir(item):
            print(i)
            list_items(item) # 再帰
        
        else:
            print(None)

list_items(root_path)


# ============================================================================
# ログ書き出し
import os

root_path = r"C:\Program Files\Blender Foundation\Blender 3.6"

def list_items_(f, path):
        items = os.listdir(path)

        for i in items:
            item = os.path.join(path, i) # フルパスに戻す

            # ファイルの場合
            if os.path.isfile(item):
                print("\t{}".format(i), file=f)
            
            # フォルダの場合
            elif os.path.isdir(item):
                print(i, file=f)
                list_items_(f, item) # 再帰
            
            else:
                print(None, file=f)

# with open(os.path.join(os.getcwd(), r"01_os_output.log"), "w", encoding="utf-8") as f:
with open(r"01_os_output.log", "w", encoding="utf-8") as f:
    list_items_(f, root_path)