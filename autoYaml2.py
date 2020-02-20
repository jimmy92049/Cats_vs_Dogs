import yaml
import subprocess
import time
import random

file = "tensorflow-pod2.yaml"
path = "/home/jimmy/Cats_vs_Dogs"
gpu = 0
#cmd = ["- cd /tmp/; python3 "]
train_py = "train_resnet50-5e.py"

with open("tensorflow-pod.yaml", "r+") as yaml_file:
    yaml_obj = yaml.load(yaml_file.read(), Loader=yaml.FullLoader)
    """
    hostPath_config = yaml_obj["spec"]["volumes"][0]["hostPath"]["path"]
    gpu_config = yaml_obj["spec"]["containers"][0]["resources"]["limits"]["nvidia.com/gpu"]
    cmd_config = yaml_obj["spec"]["containers"][0]["args"]
    podName_config = yaml_obj["metadata"]["name"]
    """
  
with open(file, "w") as yaml_file: 
    #修改hostpath.path
    yaml_obj["spec"]["volumes"][0]["hostPath"]["path"] = path
    #修改nvidia.com/gpu
    yaml_obj["spec"]["containers"][0]["resources"]["limits"]["nvidia.com/gpu"] = gpu
    #修改代入的指令
    yaml_obj["spec"]["containers"][0]["args"] = [yaml_obj["spec"]["containers"][0]["args"][0] +"python3 "+train_py+";"]  ##需要新增USER自訂參數

    #亂數指定pod編號0~200
    num = str(random.randint(0, 200))   ##這邊要改方式
    yaml_obj["metadata"]["name"] = yaml_obj["metadata"]["name"] + num
    #new_yaml = yaml_obj["metadata"]["name"] + num
    
    #輸出yaml
    yaml.dump(yaml_obj, yaml_file)
    time.sleep(1)

subprocess.call(["sudo", "kubectl","apply","-f","tensorflow-pod2.yaml"])
