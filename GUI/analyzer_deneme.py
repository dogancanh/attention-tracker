# face detection with mtcnn on a photograph
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle


# draw an image with detected objects
class analyzer:
    def main(self):

        def draw_image_with_boxes(filename, result_list):
            # load the image
            data = pyplot.imread(filename)
            # plot the image
            pyplot.imshow(data)
            # get the context for drawing boxes
            ax = pyplot.gca()
            # plot each box
            for result in result_list:
                # get coordinates
                x, y, width, height = result['box']
                # create the shape
                rect = Rectangle((x, y), width, height, fill=False, color='red')
                # draw the box
                ax.add_patch(rect)
                # draw the dots on eyes nose ..
                for key, value in result['keypoints'].items():
                    # create and draw dot
                    dot = Circle(value, radius=2, color='red')
                    ax.add_patch(dot)
            # show the plot
            pyplot.show()

        """files = []
        for i in range():
            string = 'image'+i
            files.append(string)

        while True:
            for i in range(files):
                filename = i
                # load image from file
                pixels = pyplot.imread(filename)
                # create the detector, using default weights
                detector = MTCNN()
                # detect faces in the image
                faces = detector.detect_faces(pixels)
                # display faces on the original image
                draw_image_with_boxes(filename, faces)"""


