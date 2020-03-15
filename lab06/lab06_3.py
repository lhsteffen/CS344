'''
This file loads the boston housing dataset from the keras library and prints information
about the dataset.

@author: Luke Steffen (lhs3)
@version: Mar 3, 2020
'''

import numpy as np
from keras.datasets import boston_housing
(train_images, train_labels), (test_images, test_labels) = boston_housing.load_data()

print(
        'training images \
            \n\tcount: {} \
            \n\tdimensions: {} \
            \n\tshape: {} \
            \n\tdata type: {}\n\n'.format(
                len(train_images),
                train_images.ndim,
                train_images.shape,
                train_images.dtype
        ),
        'testing images \
            \n\tcount: {} \
            \n\tdimensions: {} \
            \n\tshape: {} \
            \n\tdata type: {} \
            \n\tvalues: {}\n'.format(
                len(test_labels),
                train_labels.ndim,
                test_labels.shape,
                test_labels.dtype,
                test_labels
        )
    )

