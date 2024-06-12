import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        center = (x + w//2, y + h//2)
        radius = min(w, h) // 2
        cv2.circle(frame, center, radius, (0, 0, 255), 2)
        cv2.line(frame, (center[0], center[1] - radius), (center[0], center[1] + radius), (0, 0, 255), 2)
        cv2.line(frame, (center[0] - radius, center[1]), (center[0] + radius, center[1]), (0, 0, 255), 2)
    cv2.imshow('Sniper Crosshair (press q to quit)', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
