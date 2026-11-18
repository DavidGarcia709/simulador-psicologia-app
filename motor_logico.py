import pandas as pd

class MotorLogicoEgerina:
    def __init__(self):
        # Constantes del estándar EGEL Plus
        self.PUNTAJE_MINIMO = 700
        self.PUNTAJE_MAXIMO = 1300
        self.CORTE_SATISFACTORIO = 1000
        self.CORTE_SOBRESALIENTE = 1150

    def calcular_icne_mision(self, aciertos, total_reactivos):
        """
        Convierte los aciertos de una misión clínica al Índice Ceneval (ICNE).
        """
        if total_reactivos == 0: return self.PUNTAJE_MINIMO
        porcentaje = aciertos / total_reactivos
        
        # Cálculo lineal adaptado a la escala 700-1300
        puntaje_final = int(self.PUNTAJE_MINIMO + (porcentaje * (self.PUNTAJE_MAXIMO - self.PUNTAJE_MINIMO)))
        return puntaje_final

    def evaluar_desempeno(self, puntaje_icne):
        """
        Retorna la categoría del EGEL basada en el puntaje.
        """
        if puntaje_icne >= self.CORTE_SOBRESALIENTE:
            return "Sobresaliente", 500  # Retorna categoría y Puntos de Experiencia (EXP)
        elif puntaje_icne >= self.CORTE_SATISFACTORIO:
            return "Satisfactorio", 250
        else:
            return "Aún no satisfactorio", 50

    def calcular_curva_aprendizaje_ema(self, historial_puntajes, span=3):
        """
        Utiliza una Media Móvil Exponencial (EMA) para evaluar la tendencia del usuario.
        Le da más peso a los exámenes recientes para ver si realmente está mejorando.
        """
        if not historial_puntajes:
            return []
            
        df = pd.DataFrame({'puntajes': historial_puntajes})
        # Calculamos la EMA
        df['ema'] = df['puntajes'].ewm(span=span, adjust=False).mean()
        
        # Retorna la lista de tendencia redondeada
        return df['ema'].round(2).tolist()

    def mapear_patrones_error(self, df_metricas):
        """
        Analiza las métricas de reacción para encontrar el 'talón de Aquiles' del estudiante.
        df_metricas debe ser un DataFrame con columnas: ['subarea', 'es_acierto']
        """
        # Filtramos solo los errores
        errores = df_metricas[df_metricas['es_acierto'] == False]
        
        if errores.empty:
            return "¡Excelente! No hay patrones de error."
            
        # Agrupamos por subárea para ver dónde falla más
        conteo_errores = errores.groupby('subarea').size().sort_values(ascending=False)
        area_critica = conteo_errores.index[0]
        
        return f"Atención: Patrón de error detectado en la subárea '{area_critica}'. Aura generará un repaso espaciado para este tema."

# ==========================================
# EJEMPLO DE USO DEL MOTOR
# ==========================================
if __name__ == "__main__":
    motor = MotorLogicoEgerina()
    
    # Simulación de un examen completado
    aciertos = 38
    total = 49 # Reactivos del Área 1
    
    puntaje = motor.calcular_icne_mision(aciertos, total)
    categoria, exp_ganada = motor.evaluar_desempeno(puntaje)
    
    print(f"Puntaje Obtenido: {puntaje} ICNE")
    print(f"Desempeño EGEL: {categoria}")
    print(f"EXP Ganada para el Ranking: +{exp_ganada} puntos")
    
    # Simulación de la curva de aprendizaje (Examen 1 al 5)
    historial = [850, 920, 900, 1050, 1180]
    tendencia_ema = motor.calcular_curva_aprendizaje_ema(historial)
    print(f"Curva de Tendencia (EMA): {tendencia_ema}")