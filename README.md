# Poly2Mask

Convert your LinkedAI polygons in to image masks.

Place the images in the *images* folder and the json file in the *tags* folder.

## Instanse Segmentation
For this type of segmentation we are going to generate one mask for each label in the image, using the following convention:
`[class name]_[index of tag]_[image name].jpg`

The `PolygonToMask.py` script generate this masks, to set the script to work with your own labels, change line 30:
`data = loadData('tags/Person-mask.json')`
to
`data = loadData('tags/[your labels file].json')`

## Class Segmentation
For this type of segmentation all the items of the same class will be draw on the same mask.

**COMING SOON!**
