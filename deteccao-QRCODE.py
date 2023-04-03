import cv2
from pyzbar import pyzbar

#detectando e decodificando código de barras
camera = cv2.VideoCapture(0)

# verifique se a captura esta aberta.
if (camera.isOpened() == False): 
  print("NÃO FOI POSSÍVEL LER O DADOS DA CAMERA")

while True:
    #lê os frames
    ret,frame = camera.read()
    frame = cv2.resize(frame, (600, 600))
    font = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(frame, "PRESS Q To QUIT", (10,30), font, 2, (0,0,255), 2)

    # interpreta o QR code
    data = pyzbar.decode(frame)

    for xywh in data:
      x, y, w, h = xywh.rect

      cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
      text = data[0].data.decode("utf-8")

      #exibe o texto decodificado
      cv2.putText(frame, text, (x,  y-50), font, 1.5, (255,0,255), 2)

    cv2.imshow('QR CODE READER', frame)
    if cv2.waitKey(1) == ord('q'):
      break
camera.release()
cv2.destroyAllWindows()

