import numpy as np
import pymeshlab
import polyscope as ps

ms = pymeshlab.MeshSet()
ms.load_new_mesh('final_star.obj')
ms.load_new_mesh('final_scan.obj')

m = ms.current_mesh()
scan_v = m.vertex_matrix()

# hausdorff_distance
ms.get_hausdorff_distance(targetmesh=0, sampledmesh=1, samplevert=True)
dis = ms.mesh(1).vertex_scalar_array()

vmin = 0
vmax = np.percentile(dis, 95)  # p95 or p99

print(np.min(dis), np.max(dis))
print(vmin, vmax)

ps.init()
ps_scan = ps.register_point_cloud("scan", scan_v, radius=0.002,color=np.array([255, 164, 0]) / 255)
ps_scan.add_scalar_quantity("distance", dis,
                            # vminmax=[vmin, vmax],
                            vminmax=[0, 0.008],
                            cmap="jet",  # colormap
                            onscreen_colorbar_enabled=True,  # show the colorbar
                            enabled=True,
                            )

# ps.set_view_projection_mode("orthographic")  # orthographic  perspective
# ps.set_navigation_style("planar")  # ['turntable','free','planar','none','first_person']
ps.set_ground_plane_mode("shadow_only")  # ['none','tile','tile_reflection','shadow_only']
ps.set_shadow_blur_iters(3)
ps.set_shadow_darkness(0.5)
ps.set_up_dir("y_up")
# ps.set_front_dir('x_front')
ps.set_SSAA_factor(4)
ps.show()
