import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import ConvexHull
import matplotlib.tri as mtri

def visualize_convex_envelope():
    # 1. Define the geometric constraints
    # ---------------------------------
    
    # Parameters for the Circle C (The "Hole" at z=0)
    center = np.array([0.5, 0.5])
    radius = 0.25
    n_circle = 60
    
    # Parameters for the Box Boundary (The "Walls" at z=1)
    n_boundary = 20 # points per side
    
    # 2. Generate Point Cloud
    # -----------------------
    points = []
    
    # A. Points on the Circle (z=0)
    # We include the perimeter. The convex hull naturally fills the interior.
    theta = np.linspace(0, 2*np.pi, n_circle)
    for t in theta:
        x = center[0] + radius * np.cos(t)
        y = center[1] + radius * np.sin(t)
        points.append([x, y, 0.0]) # Height 0
        
    # B. Points on the Box Boundary (z=1)
    # Bottom edge (y=0)
    xs = np.linspace(0, 1, n_boundary)
    for x in xs: points.append([x, 0, 1.0])
    # Top edge (y=1)
    for x in xs: points.append([x, 1, 1.0])
    # Left edge (x=0)
    ys = np.linspace(0, 1, n_boundary)
    for y in ys: points.append([0, y, 1.0])
    # Right edge (x=1)
    for y in ys: points.append([1, y, 1.0])

    points = np.array(points)

    # 3. Compute Convex Hull in 3D
    # ----------------------------
    # The maximal convex function f_C is the LOWER surface of this 3D hull.
    hull = ConvexHull(points)

    # 4. Extract Lower Faces
    # ----------------------
    # The Hull gives us triangles (simplices). We only want those facing "down".
    # Normal vector n = (nx, ny, nz). If nz < 0, it's a bottom face.
    
    simplices = hull.simplices
    lower_faces = []
    
    for simplex in simplices:
        # Get vertices of the triangle
        p0, p1, p2 = points[simplex]
        
        # Compute normal via cross product
        v0 = p1 - p0
        v1 = p2 - p0
        normal = np.cross(v0, v1)
        
        # Normalize (optional but good for checking direction)
        if np.linalg.norm(normal) > 0:
            normal /= np.linalg.norm(normal)
            
        # Check z-component. 
        # Note: ConvexHull normals usually point OUTWARDS.
        # For a lower face, the outward normal points DOWN (z < 0).
        if normal[2] < -0.01: # Threshold to avoid vertical walls
            lower_faces.append(simplex)
            
    lower_faces = np.array(lower_faces)

    # 5. Visualization
    # ----------------
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot the triangulation
    # We use plot_trisurf with the filtered triangles
    # Note: matplotlib expects x, y, z arrays and a list of triangles
    ax.plot_trisurf(points[:,0], points[:,1], points[:,2], 
                    triangles=lower_faces, 
                    cmap='viridis', edgecolor='none', alpha=0.9)

    # Decoration
    # Draw the C circle on the floor for reference
    theta_line = np.linspace(0, 2*np.pi, 100)
    cx = center[0] + radius * np.cos(theta_line)
    cy = center[1] + radius * np.sin(theta_line)
    ax.plot(cx, cy, 0, color='red', linewidth=2, label='Set C (z=0)')

    # Draw the boundary at top
    ax.plot([0,1,1,0,0], [0,0,1,1,0], [1,1,1,1,1], color='black', linestyle='--', label='Boundary (z=1)')

    ax.set_title(r"Visualizing Extreme Point $f_C(x)$" + "\n(The 'Tight Tent' over C)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("f(x)")
    ax.set_zlim(0, 1.1)
    ax.view_init(elev=30, azim=45)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    visualize_convex_envelope()