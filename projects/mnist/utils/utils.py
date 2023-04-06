import streamlit as st
from streamlit_drawable_canvas import st_canvas


def canvas_draw():

    # Create a canvas component
    canvas_result = st_canvas(
        #fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
        stroke_width=20,
        stroke_color="#EEEEEE",
        background_color="#000000",
        background_image=None,
        update_streamlit=True,
        height=250,
        width=250,
        drawing_mode="freedraw",       # "point", "freedraw", "line", "rect", "circle", "transform"
        point_display_radius=0,
        key="canvas",
    )

    return canvas_result.image_data



# # Do something interesting with the image data and paths
# if canvas_result.image_data is not None:
#     print(type(canvas_result.image_data))
#     print(canvas_result.image_data.shape)
#     st.image(canvas_result.image_data)

# if canvas_result.json_data is not None:
#     objects = pd.json_normalize(canvas_result.json_data["objects"]) # need to convert obj to str because PyArrow
#     for col in objects.select_dtypes(include=['object']).columns:
#         objects[col] = objects[col].astype("str")
#     st.dataframe(objects)