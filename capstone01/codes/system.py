from tensorflow.python.keras.initializers import glorot_uniform
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os
import cv2
from keras.utils.generic_utils import CustomObjectScope
from keras.preprocessing.image import  img_to_array
from dataclasses import dataclass
import glob
import os

class NUM_class:
    class_A: int = 0
    class_B: int = 0
    class_C: int = 0

classA = ['JD(Joint-Displaced)', 'BK(Broken-Pipe)']
classB = ['SD(Surface-Damage)']
classC = ['CC(Crack-Circumferential)', 'CL(Crack-Longitudinal)', 'JF(Joint-Faulty)', 'LP(Lateral-Protruding)','DS(Deposits-Silty)']

class Defect_info:
    Img_loc: str
    defect: str
    Class: chr

class pipe_info:
    type: str
    length: float
    diameter: float

pipe_cost = 0
threshold=0
def count_gauge(NUM_total_img, NUM_complete_pipe):
    calc_progress = NUM_complete_pipe / NUM_total_img
    
    return calc_progress

def calculate_risk(NUM_class):
    Defect_sum = 0
    
    if NUM_class.class_A != 0:
        return 1
    Defect_sum += NUM_class.class_B * 20
    Defect_sum += NUM_class.class_C * 5
    
    if Defect_sum >= 100:
        return 1
    else:
        return 0


def get_picture_html(out, Imgclass, Defectclass, NUM_complete_pipe):
    image_html = """
    <tr>
        <th scope="row">{num}</th>
        <td>{Imgclass_}</td>
        <td>{Defectclass_}</td>
        <td><img src="/static/result/{out_name}" width=200></td>
    </tr>
    """
    return image_html.format(out_name=out, Imgclass_=Imgclass, Defectclass_ = Defectclass, num = NUM_complete_pipe)


def generate_html(out=None, Imgclass=None, Defectclass=None, NUM_complete_pipe=None):

    picture_html = ""

    if out is not None:
        if out.split('.')[1] == 'jpg' or out.split('.')[1] == 'png':
            picture_html += get_picture_html(out, Imgclass, Defectclass, NUM_complete_pipe)
     
    file_content = picture_html

    with open('capstones\\templates\\capstones\\generate.html', 'a') as f:
        f.write(file_content)
        
def final_generate_html(threshold):

    exchange = ""
    
    if(threshold==1):
        exchange+="""
        <td colspan="4" style="color :red;"><i class="bi bi-exclamation-triangle" style="color :red;"></i></i> Pipe state : Dangerous <i class="bi bi-exclamation-triangle" style="color :red;"></i></td>
        """
    else:
        exchange+="""
        <td colspan="4" style="color :blue;"><i class="bi bi-exclamation-triangle" style="color :blue;"></i></i> Pipe state : good <i class="bi bi-exclamation-triangle" style="color :blue;"></i></td>
        """
    
    file_content = exchange

    with open('capstones\\templates\\capstones\\generate.html', 'a') as f:
        f.write(file_content)    
                  
def detect_defect(img, model, NUM_complete_pipe):
    # image folder
    folder_path = 'media\\pipeimages'

    # dimensions of images
    img_width, img_height = 224, 224
    i = 0
    images = []
    img1 = image.load_img(os.path.join(folder_path, img), target_size=(img_width, img_height))
    img2 = img_to_array(img1)
    img2 = np.expand_dims(img2, axis=0)
    classes = model.predict(img2)[0]
    idxs = np.argsort(classes)[::-1][:1]

    classname = ['BK(Broken-Pipe)', 'CC(Crack-Circumferential)', 'CL(Crack-Longitudinal)', 'DS(Deposits-Silty)', 'JD(Joint-Displaced)', 'JF(Joint-Faulty)', 'LP(Lateral-Protruding)',
                'SD(Surface-Damage)', 'UD_IN(Undamaged-Inside)', 'UD_PJ(Undamaged_PipeJoint)']
    ###print(classname)
    out = cv2.imread(os.path.join(folder_path, img))
    img_class = ""
    for (i, j) in enumerate(idxs):
        label = "{}:{:.2f}%".format(classname[idxs[i]], classes[idxs[i]] * 100)
        img_class += classname[idxs[i]] + " "
        if classname[idxs[i]] in classA:
            generate_html(img, img_class, 'A', NUM_complete_pipe)
            NUM_class.class_A += 1
        elif classname[idxs[i]] in classB:
            generate_html(img, img_class, 'B', NUM_complete_pipe)
            NUM_class.class_B += 1
        elif classname[idxs[i]] in classC:
            generate_html(img, img_class, 'C', NUM_complete_pipe)
            NUM_class.class_C += 1
        else:
            generate_html(img, img_class, '-', NUM_complete_pipe)
        
        cv2.putText(out, label, (10, (i * 30) + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    cv2.imwrite("capstones\\static\\result\\%s"%img,out)

def detect_process_run():
    NUM_class.class_A=0
    NUM_class.class_B=0
    NUM_class.class_C=0

    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    # image folder
    folder_path = 'media\\pipeimages'

    # path to model
    model_path = 'sewermodel\\sewer_weight.h5'
    with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
            model = load_model(model_path)

    #이미지 총 개수
    NUM_total_img = len(os.listdir(folder_path))
    NUM_complete_pipe = 0

    f=open('capstones\\templates\\capstones\\generate.html', 'w')

    #이미지 결함 분류
    # ㅇㅣ놈을 실행시키려면 뭔가 메소드 형식으로 만들어줘야지
    # 얘를 실행시킬려면 보통은 python3 system.py 이런식으로 들어가야되는데
    # 장고가 이미 실행중에 이 system.py 를 실행시키는거니깐

    for img in os.listdir(folder_path):
        NUM_complete_pipe += 1
        detect_defect(img, model, NUM_complete_pipe)
        calc_progress = count_gauge(NUM_total_img, NUM_complete_pipe)

    threshold = calculate_risk(NUM_class)
    
    final_generate_html(threshold)