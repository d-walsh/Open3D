# ----------------------------------------------------------------------------
# -                        Open3D: www.open3d.org                            -
# ----------------------------------------------------------------------------
# The MIT License (MIT)
#
# Copyright (c) 2018-2021 www.open3d.org
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
# ----------------------------------------------------------------------------

import open3d as o3d
import numpy as np
import os, sys

pyexample_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
test_data_path = os.path.join(os.path.dirname(pyexample_path), 'test_data')
sys.path.append(pyexample_path)

if __name__ == "__main__":
    pcd = o3d.io.read_point_cloud(os.path.join(test_data_path, 'fragment.ply'))
    vol = o3d.visualization.read_selection_polygon_volume(
        os.path.join(test_data_path, 'Crop', 'cropped.json'))
    chair = vol.crop_point_cloud(pcd)

    chair.paint_uniform_color([0, 0, 1])
    pcd.paint_uniform_color([1, 0, 0])
    print("Displaying the two point clouds used for calculating distance ...")
    o3d.visualization.draw([pcd, chair])

    dists = pcd.compute_point_cloud_distance(chair)
    dists = np.asarray(dists)
    print("Printing average distance between the two point clouds ...")
    print(dists)
