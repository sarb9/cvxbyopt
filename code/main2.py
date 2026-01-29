import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import ConvexHull

def get_circle_points(r=1.0, n=80):
    theta = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return np.column_stack((x, y))

def get_square_points(l=1.0, n_side=20):
    # Generate points along the perimeter of a square
    pts = []
    # Bottom
    xs = np.linspace(-l, l, n_side)
    for x in xs: pts.append([x, -l])
    # Right
    ys = np.linspace(-l, l, n_side)
    for y in ys: pts.append([l, y])
    # Top
    for x in xs[::-1]: pts.append([x, l])
    # Left
    for y in ys[::-1]: pts.append([-l, y])
    return np.array(pts)

def get_segment_points(p1, p2, n=20):
    # Generate points along a line segment
    ts = np.linspace(0, 1, n)
    return np.array([(1-t)*np.array(p1) + t*np.array(p2) for t in ts])

def plot_lower_hull(ax, V_points, Q_points, title):
    """
    Computes and plots the lower convex hull (F_V)
    V_points: Points at z=0
    Q_points: Points at z=1
    """
    # 1. Lift points to 3D
    V_3d = np.column_stack((V_points, np.zeros(len(V_points))))
    Q_3d = np.column_stack((Q_points, np.ones(len(Q_points))))
    points = np.vstack((V_3d, Q_3d))
    
    # 2. Compute Convex Hull
    hull = ConvexHull(points)
    
    # 3. Filter for Lower Faces (Normals pointing down)
    lower_faces = []
    for simplex in hull.simplices:
        p0, p1, p2 = points[simplex]
        # Normal vector calculation
        v0 = p1 - p0
        v1 = p2 - p0
        normal = np.cross(v0, v1)
        if np.linalg.norm(normal) > 0:
            normal /= np.linalg.norm(normal)
        
        # We want normals pointing down (z < 0).
        # We allow a small epsilon to catch flat tops if strictly needed, 
        # but usually we want the sides.
        if normal[2] < -0.001:
            lower_faces.append(simplex)
            
    lower_faces = np.array(lower_faces)

    # 4. Plot
    ax.plot_trisurf(points[:,0], points[:,1], points[:,2], 
                    triangles=lower_faces, 
                    cmap='viridis', edgecolor='none', alpha=0.9, shade=True)
    
    # Draw outlines for clarity
    ax.plot(V_points[:,0], V_points[:,1], 0, 'r-', lw=2, label='V (z=0)')
    ax.plot(Q_points[:,0], Q_points[:,1], 1, 'k--', lw=2, label='Q (z=1)')
    
    ax.set_title(title)
    ax.set_zlim(0, 1)
    ax.view_init(elev=25, azim=45)

# --- Main Execution ---

fig = plt.figure(figsize=(14, 6))

# Example 1: Square Bottom (V), Circle Top (Q)
# --------------------------------------------
ax1 = fig.add_subplot(121, projection='3d')
V1 = get_square_points(l=0.3)  # Small square
Q1 = get_circle_points(r=1.0)  # Large circle
plot_lower_hull(ax1, V1, Q1, r"Ex 1: Square Bottom ($V$), Circle Top ($Q$)")

# Example 2: Segment Bottom (V), Square Top (Q)
# ---------------------------------------------
ax2 = fig.add_subplot(122, projection='3d')
V2 = get_segment_points([-0.5, -0.5], [0.5, 0.5]) # Diagonal segment
Q2 = get_square_points(l=1.0) # Square domain
plot_lower_hull(ax2, V2, Q2, r"Ex 2: Segment Bottom ($V$), Square Top ($Q$)")

plt.legend()
plt.tight_layout()
plt.show()