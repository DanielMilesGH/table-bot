from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Example data structure to store generated object borders and movement details

# TODO :
# call functions:
#   generate borders (return in json format)
#   show movement (return in json format)
# figure out file uploads
# future plans:
#   implement https

object_borders_data = {}
movement_data = {}

@app.route('/api/generate-borders', methods=['POST'])
def generate_borders():
    data = request.get_json()
    image_path = data.get('image')

    # Example: Process to generate object borders based on image_path
    # This is where you would call your image processing or object detection functions
    # Example: object_borders = generate_object_borders(image_path)

    # Placeholder response
    object_borders = f"Object borders generated for {image_path}"
    object_borders_data[image_path] = object_borders

    return jsonify({'message': 'Object borders generated successfully', 'object_borders': object_borders})

# @app.route('/api/show-movement', methods=['POST'])
# def show_movement():
#     data = request.get_json()
#     image_path = data.get('image')
# 
#     # Example: Process to show movement based on image_path
#     # This is where you would call your animation or movement functions
#     # Example: movement_animation = move_generation(image_path)
# 
#     # Placeholder response
#     movement_animation = f"Movement animation shown for {image_path}"
#     movement_data[image_path] = movement_animation
# 
#     return jsonify({'message': 'Movement animation shown successfully', 'movement_animation': movement_animation})
# 
# if __name__ == '__main__':
#     app.run(debug=True)
