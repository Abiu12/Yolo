import os
import torch
import cv2
import numpy as np
import cv2
from  hubconf import custom
from cv2.cuda import Stream
def load_model():
    model_name='yolov7.pt'
    model = custom(path_or_model=model_name)  # custom example
    return model

def sel_color(val):
    if val == 0:
        return (0,255,0)
    elif val == 1:
        return (255,0,0)
    elif val == 2:
        return (0,0,255)
    elif val == 3:
        return (0,255,255)
    elif val == 4:
        return (227,207,87)
    elif val == 5:
        return (152,245,255)
    elif val == 6:
        return (210,105,30)

def pred_frame(frame, model):
    res = model(frame)

    boxes = res.pandas().xyxy[0].to_numpy()

    for x1, y1, x2, y2, conf, detclass, name in boxes:
        if conf > 0.5:
            centerBB = (int(x1) + int((x2 - x1)/2)), (int(y1) + int((y2 - y1)/2))
            cv2.rectangle(frame, pt1=(int(x1), int(y1)), pt2=(int(x2), int(y2)), color= sel_color(1), thickness = 2)
            cv2.circle(frame, centerBB, radius=3, color=(0, 0, 255), thickness=-1)   
    return frame




def detector(cap: object):
    model = load_model()  
    result = None
 
    while cap.isOpened():
      status, frame = cap.read()
      if result == None:
          fps = cap.get(cv2.CAP_PROP_FPS)
          num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        #   result = cv2.VideoWriter('test_video.mp4',  cv2.VideoWriter_fourcc(*'mp4v'), fps,(1280*620))
      if not status:
        break

    #redimensionamos la imagen
    
      # img = cv2.resize(frame,  interpolation = cv2.INTER_LINEAR)   
      preds = pred_frame(frame, model)

    #   result.write(preds)
    cv2.imshow(preds)
   

    cap.release()
    result.release()
    print("Video terminado")

if __name__ == '__main__':
  cap = cv2.VideoCapture("caballo.mp4")
  detector(cap)