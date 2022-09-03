#!/usr/bin/python
import os
import cv2


class Generator:
    def __init__(self):
        with open('AprilTag0.proto', 'r') as f:
            self.proto_template = f.read()

    def generate(self, tag_directory, tag_name, tag_size, webots_tag_size):
        img = cv2.imread(str(tag_directory) + '/' + str(tag_name) + '.png', 0)
        img = cv2.resize(img, (tag_size, tag_size), interpolation=cv2.INTER_NEAREST)

        if not os.path.exists('apriltags/protos'):
            os.makedirs('apriltags/protos')
        if not os.path.exists('apriltags/images'):
            os.makedirs('apriltags/images')
            
        with open('apriltags/protos/' + str(tag_name) + '.proto', 'w') as f:
            protos_text = self.proto_template.replace('AprilTag0', str(tag_name))
            protos_text = protos_text.replace('apriltag0', str(tag_name))
            protos_text = protos_text.replace('0.16', str(webots_tag_size))
            f.write(protos_text)

        cv2.imwrite('apriltags/images/' + str(tag_name) + '.png' , img)


def main():
    # Texture size must be power of two
    # With the default tag image size (10pix), tags will not be clearly rendered due to rescaling and interpolation
    tag_size = 2048
    nr_of_tags = 20
    tags_directory = 'apriltag-imgs/tag36h11'
    tag_family = 'tag36_11_'
    webots_tag_size = 0.16

    generator = Generator()
    for i in range(nr_of_tags):
        generator.generate(tags_directory, tag_family + str(i).zfill(5), tag_size, webots_tag_size)


if __name__ == '__main__':
    main()
