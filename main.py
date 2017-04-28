from imutils import paths
import argparse, cv2, shutil, os

os.mkdir("blurry")
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
	help="path to input directory of images")
ap.add_argument("-t", "--threshold", type=float, default=200.0,
	help="focus measures that fall below this value will be considered 'blurry'")
ap.add_argument("-d", "--destination", default="blurry",
        help="blurry images will move to this folder")
args = vars(ap.parse_args())

for imagePath in paths.list_images(args["images"]):
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if cv2.Laplacian(gray, cv2.CV_64F).var()< args["threshold"]:
        shutil.move(imagePath, args["destination"])
if len(os.listdir("blurry"))==0:
    os.rmdir("blurry")

cv2.waitKey(0)
cv2.destroyAllWindows()
