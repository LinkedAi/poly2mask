import cv2
import json
import numpy as np
import matplotlib.pyplot as plt

def loadData(path):
  with open(path) as json_file:
    data = json.load(json_file)
  return data

def createMask(image, data):
  mask = np.zeros(image.shape[0:2], dtype=np.uint8)

  for elem in data:
    arr = np.zeros((len(elem['pos']), 2))
    for i, p in enumerate(elem['pos']):
      #np.append(arr, [[p['x'], p['y']]])
      arr[i,0] = int(round(p['x']))
      arr[i,1] = int(round(p['y']))]

    cv2.drawContours(mask, [arr.astype(np.int32)], -1, (255, 255, 255), -1, cv2.LINE_AA)
  
  return mask

data = loadData('tags/Products-Poly.json')

for img in data:
  image = cv2.imread('images/'+img['image'],0)
  mask = createMask(image, img['tags'])

  plt.imshow(mask)
  plt.show()