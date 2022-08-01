from skimage.metrics import structural_similarity
import cv2
import os

class Tools:
    @staticmethod
    def diffutil(actual, expected, similarity=100):

        testlog = os.environ.get('testlog')

        # Load images
        actual = cv2.imread(actual)
        expected = cv2.imread(expected)

        # Convert images to grayscale
        actual_gray = cv2.cvtColor(actual, cv2.COLOR_BGR2GRAY)
        expected_gray = cv2.cvtColor(expected, cv2.COLOR_BGR2GRAY)

        # Compute SSIM between the two images
        (score, diff) = structural_similarity(actual_gray, expected_gray, full=True)
        print("Image Similarity: {:.4f}%".format(score * 100))

        if score * 100 < similarity:

            # The diff image contains the actual image differences between the two images
            # and is represented as a floating point data type in the range [0,1] 
            # so we must convert the array to 8-bit unsigned integers in the range
            # [0,255] before we can use it with OpenCV
            diff = (diff * 255).astype("uint8")

            # Threshold the difference image, followed by finding contours to
            # obtain the regions of the two input images that differ
            thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
            contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contours = contours[0] if len(contours) == 2 else contours[1]

            # mask = np.zeros(before.shape, dtype='uint8')
            # filled_after = after.copy()

            for c in contours:
                area = cv2.contourArea(c)
                if area > 40:
                    x,y,w,h = cv2.boundingRect(c)
                    cv2.rectangle(expected, (x, y), (x + w, y + h), (0, 0, 255), 2)

            #cv2.imshow('actual', actual)
            cv2.imwrite(f"{testlog}\\difference.png", expected)
            #cv2.waitKey()

            assert False, 'Screenshots are differ!'