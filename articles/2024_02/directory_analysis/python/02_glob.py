import glob

root_path = r"C:\Program Files\Blender Foundation\Blender 3.6\*"

items = glob.glob(root_path)

print("\n".join(items))
# >> C:\Program Files\Blender Foundation\Blender 3.6\3.6
# >> C:\Program Files\Blender Foundation\Blender 3.6\blender-launcher.exe
# >> C:\Program Files\Blender Foundation\Blender 3.6\blender.crt
# ...

print(type(items))
# >> <class 'list'>

# ============================================================================
root_path = r"C:\Program Files\Blender Foundation\Blender 3.6\*"
print(len(glob.glob(root_path)))
# >> 20

root_path = r"C:\Program Files\Blender Foundation\Blender 3.6\**"
print(len(glob.glob(root_path, recursive=True)))
# >> 6321

# ============================================================================
import glob

root_path = r"C:\Program Files\Blender Foundation\Blender 3.6\**"

print("\n".join(glob.glob(root_path, root_dir=root_path, recursive=True)))

# ============================================================================
# root_dir
glob.glob("*", root_dir=r"C:\Program Files\Blender Foundation\Blender 3.6")

# ============================================================================
# root_dir
glob.glob("*",
          root_dir=r"C:\Program Files\Blender Foundation\Blender 3.6",
          dir_fd=1
          )

import os
glob.glob in os.supports_dir_fd