# Poly2Mask

Convert your LinkedAI polygons in to image masks.

![Segmentation example](/results/Person_0_people.jpg)

Place the images in the *images* folder and the json file in the *tags* folder.

## Semantic Segmentation
For the segmentation we are going to generate one mask for each image, using the following convention:
`mask_[image name].png`

The `PolygonToMaskSemantic.py` script generate this masks, to set the script to work with your own labels, change line 38:
`data = loadData('tags/example-mask.json')`
to
`data = loadData('tags/[your labels file].json')`

You can find the masks in the *results* folder.


If you want individual png for each instance use `PolygonToMask.py`:
The **masks** array content all the instance of the segmentation objects for each label in one image.
