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
    st.title("Fractal Drawer - Cyrus Correll")
    st.sidebar.title("Controls")
    depth = st.sidebar.slider("Select Sierpinski Triangle Depth", 0, 7, 3)
    if st.sidebar.button("Draw Sierpinski Triangle"):
        draw_sierpinski(depth)
        total_triangles = 0
        for i in range(1,depth+1):
            total_triangles += np.power(3,i)
        total_triangles+=1
        st.title(f"Total triangles: {total_triangles}")

        if(depth == 0):
            st.write("Here we see a simple triangle. The simplest 2D Shape, comprised of three edges and vertices. Many of us go about our day disregarding others, ourselves, and the world around us. More times than not, we take beautifully intricate processes as triangles. I'll admit, I haven't gone to see the sunset in a bit too long either. But as we explore deeper levels of viewing the world, we can truly appreciate the beauty it offers to us.")
        elif(depth == 1):
            st.write("Now we see the first iteration of the Sierpinski process. That is, find the midpoints of the edges of your previous triangle, and use these midpoints to draw a new triangle. This is still a simple shape, yet it stands here with more intention. There is a sense of purpose. I used the colors blue and red to represent divide, as by surrounding ourselves with alternate views we can grow into more holistically knowledgeable people.")
        elif(depth == 2):
            st.write("The pattern is becoming more apparent. As we continue to build, ask yourself, what processes around you do you ignore? Have you truly shown appreciation and gratitude to each triangle that makes up your day? As we will see in a moment, there are a lot! I find that giving attention and gratitude to processes which otherwise would have gone unnoticed leads to a greater sense of fulfillment and connectivity with the world around me.")
        elif(depth == 3):
            st.write("For this depth, I chose to leave the center triangle white. This is meant to blend with the background, and represent how we are often very similar to people around us (the three groups comprising the points of this triangle), yet because of the space between us we think we are somehow different. I found a class like HISC 144 fascinating not only because of the engaging content and wonderful professor, this class was special because of the multidisciplinary nature of my peers, which often led to deeper discussions than I have experienced in other classes.")
        elif(depth == 4):
            st.write("Now we see the first iteration of the Sierpinski process. That is, find the midpoints of the edges of your previous triangle, and use these midpoints to draw a new triangle. This is still a simple shape, yet it stands here with more intention. There is a sense of purpose. I used the colors blue and red to represent divide, as by surrounding ourselves with alternate views we can grow into more holistically knowledgeable people.")
        elif(depth == 5):
            st.write("Now we see the first iteration of the Sierpinski process. That is, find the midpoints of the edges of your previous triangle, and use these midpoints to draw a new triangle. This is still a simple shape, yet it stands here with more intention. There is a sense of purpose. I used the colors blue and red to represent divide, as by surrounding ourselves with alternate views we can grow into more holistically knowledgeable people.")
        elif(depth == 6):
            st.write("Now we see the first iteration of the Sierpinski process. That is, find the midpoints of the edges of your previous triangle, and use these midpoints to draw a new triangle. This is still a simple shape, yet it stands here with more intention. There is a sense of purpose. I used the colors blue and red to represent divide, as by surrounding ourselves with alternate views we can grow into more holistically knowledgeable people.")
        elif(depth == 7):
            st.write("Fractals teach us many things about process ontology. The most important is the fact that there is infinite detail in everything all around us. Question how you view the world, ask yourself how much more you could understand if you look deeper and more intently.")
            
        st.title("Thank you to Professor Papadopoulos for an amazing class!")
    

if __name__ == "__main__":
    main()
