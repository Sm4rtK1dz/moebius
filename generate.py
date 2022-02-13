from PIL import Image
import os, fnmatch, re, json, copy, hashlib


def new_canvas(x_len, y_len):
    global canvas
    canvas = Image.new("RGB", (x_len, y_len))


def set_pixels_of(path):
    global canvas
    canvas_matrix = canvas.load()

    image = Image.open(path)
    image_matrix = image.load()
    x_len, y_len = image.size

    for i in range(0, y_len):
        for j in range(0, x_len):
            if image_matrix[j, i] != (0, 0, 0, 255):
                canvas_matrix[j, i] = image_matrix[j, i]

    image.close()


def save_canvas(name):
    global canvas
    canvas.save("./results/{}.png".format(name))
    canvas.close()


layers = []
for root, dirs, files in os.walk("."):
    for dirname in fnmatch.filter(dirs, "layer*"):
        layers.append(os.path.join(root, dirname))

pics_by_layer = []
for layer in layers:
    # print(layer)

    for root, dirs, files in os.walk(layer):
        for filename in files:

            # print(" ", os.path.join(root, filename))
            index = int(re.search("layer(.+?)", layer).group(1))

            try:
                pics_by_layer[index].append(os.path.join(root, filename))
            except IndexError:
                pics_by_layer.insert(index, [])
                pics_by_layer[index].append(os.path.join(root, filename))


layers_count = len(pics_by_layer)
# print("Found: {} layers".format(layers_count))
# print(json.dumps(pics_by_layer, indent=4))


def craft_image(image_list):

    print(image_list)
    new_canvas(1867, 1867)

    for image in image_list:
        set_pixels_of(image)

    name = hashlib.md5(json.dumps(image_list).encode("utf-8")).hexdigest()
    save_canvas(name)


def recurse(layer=0, image_list=[]):

    if layer == layers_count:
        craft_image(image_list)
        return

    for pic in pics_by_layer[layer]:
        image_list_copy = image_list.copy()
        image_list_copy.append(pic)
        recurse(layer + 1, image_list_copy)


recurse()
