import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def draw_triangle(ax, points, color):
    triangle = plt.Polygon(points, color=color)
    ax.add_patch(triangle)

def get_mid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(ax, points, degree):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange','purple']
    draw_triangle(ax, points, colormap[degree])
    if degree > 0:
        sierpinski(ax, [points[0],
                        get_mid(points[0], points[1]),
                        get_mid(points[0], points[2])],
                   degree-1)
        sierpinski(ax, [points[1],
                        get_mid(points[0], points[1]),
                        get_mid(points[1], points[2])],
                   degree-1)
        sierpinski(ax, [points[2],
                        get_mid(points[2], points[1]),
                        get_mid(points[0], points[2])],
                   degree-1)

def draw_sierpinski(depth=3):
    fig, ax = plt.subplots(figsize=(15,15))
    ax.set_aspect('equal')
    ax.axis('off')
    my_points = [[1,0], [0.5, 1], [0, 0]]
    sierpinski(ax, my_points, depth)
    st.pyplot(fig)

def main():
    st.title("Fractal Drawer")
    st.sidebar.title("Controls")
    depth = st.sidebar.slider("Select Sierpinski Triangle Depth", 0, 7, 3)
    total_triangles = 0
    for i in range(1,depth+1):
        total_triangles += np.power(3,i)
    total_triangles+=1
    st.title(f"Total triangles: {total_triangles}")
    if st.sidebar.button("Draw Sierpinski Triangle"):
        draw_sierpinski(depth)

if __name__ == "__main__":
    main()
