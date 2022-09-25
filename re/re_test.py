import re
name = "trk_cam_062_132"
res = re.search(pattern = r".+_\d+_\d+", string = name)
print(res)
# print(dir(re))