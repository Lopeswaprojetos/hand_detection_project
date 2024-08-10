import cv2

# Inicializa a captura de vídeo da webcam
cap = cv2.VideoCapture(0)

# Verifica se a câmera foi aberta com sucesso
if not cap.isOpened():
    print("Erro: Não foi possível acessar a câmera.")
    exit()

while True:
    # Captura frame a frame
    ret, frame = cap.read()

    # Verifica se o frame foi capturado com sucesso
    if not ret:
        print("Erro: Não foi possível capturar o vídeo.")
        break

    # Mostra o frame capturado em uma janela
    cv2.imshow('Webcam', frame)

    # Verifica se a tecla 'q' foi pressionada para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera e fecha as janelas
cap.release()
cv2.destroyAllWindows()