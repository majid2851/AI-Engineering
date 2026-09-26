import numpy as np
import cv2 as cv
import os



#Lesson-1
# my_list=[1,2,3,4,5]
# print(my_list*2)
#
# array=np.array([1,2,3,4])
# print(array*2)
# print(array)

#Lesson-2

# array = np.array([['A'],['D'],['B'],['C']])
# print(array.ndim)
# print(array.shape)
# print(array[2,0])

# #Lesson-3
#
# array= np.array([
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]
# ])
#
# print(array[:,0:3])

# #Lesson-4
#
# array = np.array([10,20,30])
# print(array+1)
# print(array-2)
# print(np.sqrt(array))
# print(array==30)
# array[array<22]=0
# print(array)

# #Lesson-5 Brodcasting
#
# array1 = np.array([[1,2,3,4]])
# array2= np.array([[1],[2],[3],[4]])
#
# print(array1)
# print(array2)
# print(array1.shape)
# print(array2.shape)
#
# print(array1*array2)

#Lesson-6 Aggregate function

# array= np.array([[1,2,3,4,5],[6,7,8,9,10]])
#
# print(np.sum(array))


# #Lesson-7
# rng=np.random.default_rng()
# print(rng.integers(1,40))


#Reading and writing Video in OpenCV

def videoFromWebcam():
    cap=cv.VideoCapture(0)

    if not cap.isOpened():
        exit()
    while True:
        ret,frame = cap.read()
        if ret:
            cv.imshow('Webcam',frame)
        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    cv.destroyAllWindow()

def videoFromFile():
    root = os.path.dirname(os.path.abspath(__file__))
    vidPath = os.path.join(root, 'files', 'NumPy.mp4')
    cap = cv.VideoCapture(vidPath)

    if not cap.isOpened():
        print('Cannot open video:', vidPath)
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv.imshow('video', frame)
        delay = int(1000 / 60)
        if cv.waitKey(delay) == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

def writeVideoToFile():
    root = os.path.dirname(os.path.abspath(__file__))
    outPath = os.path.join(root, 'files', 'webcam_5s.mp4')

    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print('Cannot open webcam')
        return

    fps = 20
    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    out = cv.VideoWriter(outPath, fourcc, fps, (width, height))

    totalFrames = fps * 5  # 5 seconds
    for _ in range(totalFrames):
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        cv.imshow('Recording (5s)', frame)
        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    out.release()
    cv.destroyAllWindows()
    print('Saved:', outPath)


if __name__ == '__main__':
    writeVideoToFile()
    # videoFromFile()
    # videoFromWebcam()
