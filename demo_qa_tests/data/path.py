import os

parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
image_path = os.path.join(parent_dir, 'demo_qa_tests/data/resources/image.jpeg')
print(image_path)
