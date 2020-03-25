import cv2

video_path = 'pooya.avi'
vc = cv2.VideoCapture(video_path)
print("status: ", vc.isOpened())

width = vc.get(cv2.CAP_PROP_FRAME_WIDTH)
height = vc.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = vc.get(cv2.CAP_PROP_FPS)
print('width: ', width)
print('height: ', height)
print('fps: ', fps)

while vc.isOpened():
    ret, frame = vc.read()
    if not ret:
        print('not working :(')
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('pooya', frame)
    cv2.imshow('pooya_gray', frame_gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
