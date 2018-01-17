# FaceDatasets
Some scripts to process face datasets.

# Dataset Overlapping Problem

In face verification, it is important to perform open-set evaluation, i.e. there should be no overlapping identities between the training set and testing set. However, this standard isn't always folllowed by researchers and engineers. In [./VGGFace2/match_names.py](https://github.com/happynear/FaceDatasets/blob/master/VGGFace2/match_names.py), I provide a python script to check if two names are from the same person. The overlapping list between several training and testing datasets are also provided.

[CASIA-Webface and LFW](https://github.com/happynear/FaceDatasets/blob/master/CASIA/webface_lfw_overlap.txt)

[CASIA-Webface and FaceScrub Set 1](https://github.com/happynear/FaceDatasets/blob/master/CASIA/webface_facescrub_overlap.txt)

[VGGFace2 and LFW](https://github.com/happynear/FaceDatasets/blob/master/VGGFace2/vggface2_lfw_overlap.txt)

[VGGFace2 and FaceScrub Set 1](https://github.com/happynear/FaceDatasets/blob/master/VGGFace2/vggface2_facescrub_overlap.txt)
