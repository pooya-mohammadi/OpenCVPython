import cv2

camera_index = 1  # 0
vc = cv2.VideoCapture(camera_index)
print("status: ", vc.isOpened())

width = vc.get(cv2.CAP_PROP_FRAME_WIDTH)
height = vc.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = vc.get(cv2.CAP_PROP_FPS)
print('width: ', width)
print('height: ', height)
print('fps: ', fps)

save_path = 'pooya.avi'
fourcc = cv2.VideoWriter_fourcc(*"XVID")

vw = cv2.VideoWriter(save_path, fourcc, int(fps), (int(width), int(height)), True)

while vc.isOpened():
    ret, frame = vc.read()
    if not ret:
        print('not working :(')
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('pooya', frame)
    cv2.imshow('pooya_gray', frame_gray)

    vw.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
