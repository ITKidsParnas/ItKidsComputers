import cv2

# Открываем видеофайл
video_path = 'youtube.mp4'  # Укажите путь к вашему видео
cap = cv2.VideoCapture(video_path)

# Получаем параметры видео
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Создаем объект для записи обработанного видео
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter('output_video.mp4', fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Применяем обработку к каждому кадру (например, преобразуем в серый цвет)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_YUV420P2BGR)

    # Записываем обработанный кадр в выходное видео
    output_video.write(cv2.cvtColor(gray_frame, cv2.COLOR_BAYER_BG2BGR))

# Освобождаем ресурсы
cap.release()
output_video.release()
cv2.destroyAllWindows()
print("Обработка завершена. Видео сохранено как output_video.mp4")
