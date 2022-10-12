from flask import Flask, render_template, Response
import cv2
from time import sleep

app = Flask(__name__)
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def GenerateFrames():  
    while True:
        sleep(0.1)
        ref, frame = capture.read()
        if not ref:
            break
        else:
            ref, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/video_feed')
def VideoFeed():
    return Response(GenerateFrames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    # write your raspberry IP
   app.run(host="raspberryIP", port = "8080")
