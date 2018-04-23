import numpy as np
import rasterio

from rastervision.core.raster_transformer import RasterTransformer
from rastervision.protos.raster_transformer_pb2 import RasterTransformer as RasterTransformerProto
from rastervision.utils.misc import save_img


def test():
    options = RasterTransformerProto(
        channel_order=[0, 1, 2], means=[539, 908, 1316], stds=[291, 334, 541])
    rt = RasterTransformer(options)

    chip_path = '/opt/data/lf-dev/processed-data/airbus/2013-0611-OkMoreEast_ortho_1_3.tif'
    out_path = '/opt/data/lf-dev/processed-data/airbus/out.png'

    chip = np.transpose(rasterio.open(chip_path).read(), axes=[1, 2, 0])

    '''
    mask = np.all(chip == 0, axis=2)
    means = []
    stds = []
    for channel_ind in range(chip.shape[2]):
        masked_channel = np.ma.array(chip[:, :, channel_ind], mask=mask)
        mean = np.ma.mean(masked_channel, keepdims=False)
        std = np.ma.std(masked_channel, keepdims=False)
        means.append(mean)
        stds.append(std)

    print(means)
    print(stds)
    '''

    chip = rt.transform(chip)
    save_img(chip, out_path)


if __name__ == '__main__':
    test()
