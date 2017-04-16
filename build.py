import os
import subprocess

# ハッシュ 
# https://github.com/tensorflow/models.git

def getClassifyImage():
  subprocess.call(["git","clone","https://github.com/tensorflow/models.git"])
  subprocess.call(["cd","models"])
  subprocess.call(["git","checkout","7ff111ab514df86def76ee5140769b9edb51afd1"])
  subprocess.call(["cd",".."])
  # cp models/tutorials/image/imagenet/classify_image.py .
  subprocess.call(["cp","models/tutorials/image/imagenet/classify_image.py","./classify_image_web.py"])

# ファイルの存在チェック
if not os.path.exists("models"):
  print("found no classify_image.py!")
  getClassifyImage()

subprocess.call(["patch", "-u", "classify_image_web.py", "patch"])
