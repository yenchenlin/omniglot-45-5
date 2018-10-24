import os
import glob
import cv2
import tensorflow as tf
import numpy as np
from tqdm import tqdm


os.environ["CUDA_VISIBLE_DEVICES"]=''


if __name__ == '__main__':
    sess = tf.Session()
    PATH = '/afs/csail.mit.edu/u/y/yenchenlin/Workspace/omniglot-45-5'
    DIRS = [os.path.join(PATH, 'train/*/**/***.png'), os.path.join(PATH, 'test/*/**/***.png')]

    # Graph
    x = tf.placeholder(
            tf.uint8, [None, 105, 105, 3], name='image')
    output = tf.nn.pool(x,
                        window_shape=[4, 4], strides=[4, 4],
                        pooling_type='MAX',
                        padding='VALID')

    def downscale(img_path, sess=sess, x=x, output=output):
        img = cv2.imread(img_path)
        if img.shape[1] == 26:
            processed_img = img
        else:
            img = np.reshape(img, [1]+list(img.shape))
            img = np.ones(img.shape) * 255.0 - img
            processed_img = sess.run(output, {x: img})[0, :, :, :]
        cv2.imwrite(img_path, processed_img)

    for DIR in DIRS:
        img_paths = glob.glob(DIR)
        for img_path in tqdm(img_paths):
            downscale(img_path)
