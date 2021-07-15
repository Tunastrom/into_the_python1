import cv2

# open webcam (웹캠 열기)
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()

sample_num = 0
captured_num = 0

# loop through frames
while webcam.isOpened():

    # read frame from webcam
    status, frame = webcam.read()
    sample_num = sample_num + 1

    if not status:
        break

    # display output
    cv2.imshow("captured frames", frame)

    if sample_num == 4:
        captured_num = captured_num + 1
        cv2.imwrite('C:/Users/PC/Pictures/RPS_images/rock/img' + str(captured_num) + '.jpg', frame)  # 바위 이미지 수집시
        # cv2.imwrite('C:/Users/PC/Pictures/RPS_images/paper/img'+str(captured_num)+'.jpg', frame) # 보 이미지 수집시
        # cv2.imwrite('C:/Users/PC/Pictures/RPS_images/scissors/img'+str(captured_num)+'.jpg', frame) # 가위 이미지 수집시
        sample_num = 0

    # press "Q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release resources
webcam.release()
cv2.destroyAllWindows()