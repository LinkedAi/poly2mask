# Poly2Mask

Convert your LinkedAI polygons in to image masks.

![Segmentation example](/results/Person_0_people.jpg)

Place the images in the *images* folder and the json file in the *tags* folder.

## Semantic Segmentation
For the segmentation we are going to generate one mask for each label in the image, using the following convention:
`[class name]_[index of tag]_[image name].jpg`

The `PolygonToMask.py` script generate this masks, to set the script to work with your own labels, change line 30:
`data = loadData('tags/example-mask.json')`
to
`data = loadData('tags/[your labels file].json')`

The **masks** array content all the instance of the segmentation objects for each label in one image.
