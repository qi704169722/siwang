# -*- coding:utf-8 -*-
# 计算机视觉 传统目标检测之Harris角点检测 https://mp.weixin.qq.com/s/b__LHgwteXGPETH9NSHu4w
from scipy.ndimage import filters
import cv2
from matplotlib.pylab import *


class Harris(object):
    def __init__(self, img_path):
        self.img = cv2.imread(img_path, 0)

    def calculate_corner_strength(self):
        # 计算图像在x、y方向的梯度
        # 用滤波器采用差分求梯度的方式
        scale = self.scale
        k = self.k
        img = self.img
        gradient_imx, gradient_imy = zeros(img.shape), zeros(img.shape)
        filters.gaussian_filter(img, (scale, scale), (0, 1), gradient_imx)
        filters.gaussian_filter(img, (scale, scale), (1, 0), gradient_imy)

        # 计算矩阵M的每个分量
        I_xx = filters.gaussian_filter(gradient_imx*gradient_imx, scale)
        I_xy = filters.gaussian_filter(gradient_imx*gradient_imy, scale)
        I_yy = filters.gaussian_filter(gradient_imy*gradient_imy, scale)

        # 计算矩阵的迹、特征值和响应强度
        det_M = I_xx * I_yy - I_xy ** 2
        trace_M = I_xx + I_yy
        return det_M + k * trace_M ** 2

    def corner_detect(self, img):
        # 首先对图像进行阈值处理
        _threshold = img.max() * self.threshold
        threshold_img = (img > _threshold) * 1
        corners = array(threshold_img.nonzero()).T
        candidate_values = [img[c[0], c[1]] for c in corners]
        index = argsort(candidate_values)

        # 选取领域空间，如果邻域空间距离小于min的则只选取一个角点
        # 防止角点过于密集
        neighbor = zeros(img.shape)
        neighbor[self.min:-self.min, self.min:-self.min] = 1
        detect_corner = []
        for i in index:
            if neighbor[corners[i, 0], corners[i, 1]] == 1:
                detect_corner.append(corners[i])
                neighbor[(corners[i, 0] - self.min):(corners[i, 0] + self.min),
                (corners[i, 1] - self.min):(corners[i, 1] + self.min)] = 0
        return detect_corner

    def corner_plot(self, img, corner_img):
        figure()
        gray()
        imshow(img)
        plot([p[1] for p in corner_img], [p[0] for p in corner_img], 'ro')
        axis('off')
        show()

    def __call__(self, k=0.04, scale=3, min=15, threshold=0.03):
        self.k = k
        self.scale = scale
        self.min = min
        self.threshold = threshold
        strength_img = self.calculate_corner_strength()
        corner_img = self.corner_detect(strength_img)
        self.corner_plot(self.img, corner_img)


if __name__ == '__main__':
    harris = Harris("E:/images/SpeedThunderIco.jpg")
    harris()

