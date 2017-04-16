import os
import subprocess
import shutil

# ハッシュ 
# https://github.com/tensorflow/models.git

def getClassifyImage():
  subprocess.call(["git","clone","https://github.com/tensorflow/models.git"])

def patchClassifyImage():
  os.chdir("models")
  subprocess.call(["git","checkout","7ff111ab514df86def76ee5140769b9edb51afd1"])
  os.chdir("..")
  src_path =  os.path.abspath("models/tutorials/image/imagenet/classify_image.py")
  dest_path = os.path.abspath("./classify_image_web.py")
  #print(src_path, dest_path)
  shutil.copyfile(src_path, dest_path)
  subprocess.call(["patch", "--binary","-u", "classify_image_web.py", "patch"])

# ファイルの存在チェック
if not os.path.exists("models"):
  print("found no classify_image.py!")
  getClassifyImage()

patchClassifyImage()
