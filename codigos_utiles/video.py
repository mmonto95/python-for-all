from moviepy.editor import concatenate_videoclips, TextClip


def crear_diapositiva(texto, duracion, ancho, alto):
    # Configurar la apariencia de la diapositiva
    fuente = "Arial"
    tamano_fuente = 24
    color_fuente = "yellow"
    color_fondo = "blue"

    # Crear la diapositiva
    diapositiva = TextClip(
        texto,
        size=(ancho, alto),
        fontsize=tamano_fuente,
        font=fuente,
        color=color_fuente,
        bg_color=color_fondo
    )
    diapositiva = diapositiva.set_duration(duracion)
    diapositiva = diapositiva.set_position(("center", "center"))

    return diapositiva


def crear_video():
    # Configurar el tamaño del video y la duración de cada diapositiva
    ancho = 1200
    alto = 750
    duracion_diapositiva = 2  # en segundos

    # Crear las diapositivas
    diapositivas = [
        crear_diapositiva("Sistema integral de riesgos (SIAR)", duracion_diapositiva,
                          ancho, alto),
        crear_diapositiva("Identificar, medir, controlar, monitorear",
                          duracion_diapositiva, ancho, alto),
        crear_diapositiva("Políticas, estructura, procedimientos, documentación",
                          duracion_diapositiva, ancho, alto),
        crear_diapositiva("SARLAFT, SARO, SARC, SARL, SARM", duracion_diapositiva,
                          ancho, alto),
        crear_diapositiva("Principios éticos y conducta", duracion_diapositiva, ancho,
                          alto)
    ]

    # Crear la secuencia de video con las diapositivas
    secuencia = concatenate_videoclips(diapositivas, method="compose")

    # Configurar el video final
    video = secuencia.set_duration(sum(duracion_diapositiva for _ in diapositivas))
    video = video.set_fps(30)
    video = video.set_audio(None)
    video = video.resize((ancho, alto))

    # Guardar el video en un archivo
    ruta_video = "video2.mp4"
    video.write_videofile(ruta_video, codec="libx264")


crear_video()
