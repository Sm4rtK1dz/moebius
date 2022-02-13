# moebius

Simple Combinatorics With Python Image Library

## Usage

In order to use this script we need to meet certain criteria in the order of the assets.  
You can test the script by running ``python3 generate.py`` it will recombine all the demo images.

### Requirements

- [Python Image Library](https://pypi.org/project/Pillow/)
- Images must be in JPEG or PNG
- All the images should be of the same size
- Images must meet the coloring criteria

### The layers structure

The following example shows how the directory structure must be placed in order to make the script work.  
Bear in mind that **you can add as many layers as you want**, as long as they respect the name format ``layerN`` where ``N`` is an integer number.  
There is no restriction on the filenames for each image.  

````
├── generate.py
├── layer0
│   ├── rect870.png
│   └── rect871.png
├── layer1
│   ├── rect872.png
│   └── rect873.png
├── layer2
│   ├── rect874.png
│   └── rect875.png
└── results
    ├── 0c2e6e521eac19ff3103765fb80c466d.png
    ├── 17bf02876e28efc20ea64294718aa929.png
    ├── 24f49adc4ac2b709bcba6f33ca1af5ca.png
    ├── 4707fdda6487906734e150fb2e157c01.png
    ├── 59e9a81f91768e7c7b67db214975033b.png
    ├── 7499dcf3d40ba79a41f874467a5b3015.png
    ├── e1a8352487ae91838e7ae8c786e50b5b.png
    └── f0b94b3638e16d84e9a7eac678110c83.png
````

The resulting images are going to be placed within the results folder.  
**You can add as many images as you want on each layer.**

Layers are going to be impronted in the resulting image starting from ``layer0`` onwards, this means that for example, all backgrounds should go on ``layer0``, each layer will override all the previous ones.  

### Coloring Criteria

This script will not impront every single color on the resulting image. There's an special color, that the script will ignore. The color in question is ``#000000`` or ``(0,0,0,255)`` RGB. This means that any pixel that's colored that way will not be impronted on the resulting image.  
**In order to use the black color, you should use some other shade of black.**

