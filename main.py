import cv2
from cvzone.HandTrackingModule import HandDetector

# Inicializa a webcam
webcam = cv2.VideoCapture(0)

# Inicializa o rastreador de mãos
rastreador = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    # Captura a imagem da webcam
    sucesso, imagem = webcam.read()
    
    if not sucesso:
        break

    # Detecta as mãos no quadro
    hands, imagem_maos = rastreador.findHands(imagem)

    # Mostra o quadro com as marcações
    cv2.imshow("Imagem com Detecção de Mãos", imagem_maos)

    # Verifica se a tecla 'q' foi pressionada para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera e fecha as janelas
webcam.release()
cv2.destroyAllWindows()
