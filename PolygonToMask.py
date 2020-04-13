import os
import cv2
import json
import numpy as np
import matplotlib.pyplot as plt

# Read json file from a given path
def loadData(path):
  with open(path) as json_file:
    data = json.load(json_file)
  return data

# with the image and the json get all the mask for each label in the same image
def createMasks(image, data):
  masks =  []

  for elem in data:
    mask = np.zeros(image.shape[0:2], dtype=np.uint8)
    arr = np.zeros((len(elem['pos']), 2))

    for i, p in enumerate(elem['pos']):
      arr[i,0] = int(round(p['x']))
      arr[i,1] = int(round(p['y']))

    cv2.drawContours(mask, [arr.astype(np.int32)], -1, (255, 255, 255), -1, cv2.LINE_AA)
    masks.append(mask)

  return np.array(masks)

# Load Data from downloaded JSON
data = loadData('tags/example-mask.json')

# For all the image get the masks for each label
for img in data:
  image = cv2.imread('images/' + img['image'],0)
  masks = createMasks(image, img['tags'])

  plt.imshow(image)
  plt.show()
  
  if (len(masks) == 0):
    continue

  name  = os.path.splitext(img['image'])[0]
  for i, mask in enumerate(masks):
    cv2.imwrite('results/' +  img['tags'][0]['name'] + '_' + str(i) + '_' + name + '.png', mask)

  plt.imshow(masks[0])
  plt.show()