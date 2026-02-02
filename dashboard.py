import chainlit as cl
import plotly.graph_objects as go

# --- CONFIGURACIÓN INICIAL (SIMULADA) ---
# Acá simulamos que la cliente es "Umbra"
CLIENTE_NOMBRE = "Umbra Lingerie"

@cl.on_chat_start
async def start():
    # 1. Mensaje de Bienvenida Personalizado
    welcome_msg = cl.Message(content=f"👋 **Bienvenida al Panel de Control de {CLIENTE_NOMBRE}**\n\nAcá tenés el resumen de rendimiento de esta semana.")
    await welcome_msg.send()

    # 2. CREACIÓN DEL GRÁFICO (Métricas) 📊
    # Usamos Plotly para dibujar barras (Azul para Alcance, Dorado para Likes)
    fig = go.Figure(data=[
        go.Bar(name='Alcance', x=['Lun', 'Mar', 'Mie', 'Jue', 'Vie'], y=[1200, 1500, 1300, 1700, 2200], marker_color='#1E88E5'),
        go.Bar(name='Likes', x=['Lun', 'Mar', 'Mie', 'Jue', 'Vie'], y=[200, 350, 300, 450, 500], marker_color='#FFC107')
    ])
    
    # Ajustes estéticos del gráfico
    fig.update_layout(
        title_text='Rendimiento en Instagram (Últimos 5 días)',
        barmode='group',
        paper_bgcolor='rgba(0,0,0,0)', # Fondo transparente para que quede bien en modo oscuro
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white") # Letras blancas si usás modo oscuro
    )

    # Convertimos el gráfico en un elemento de Chainlit
    chart_element = cl.Plotly(name="metrics_chart", figure=fig, display="inline")

    # 3. CREACIÓN DE LA TABLA (Cronograma) 📅
    # Usamos Markdown simple para hacer una tabla prolija
    cronograma_md = """
    ### 🗓️ Próximas Publicaciones Programadas
    
    | Fecha | Formato | Título del Contenido | Estado |
    | :--- | :--- | :--- | :--- |
    | **05/02** | 📸 Carrusel | *5 Tips de Cuidado de Encaje* | ✅ Publicado |
    | **07/02** | 🎥 Reel | *Backstage Nueva Colección* | ⏳ Programado |
    | **09/02** | 🖼️ Historia | *Promo San Valentín* | 📝 En Edición |
    
    ---
    👇 **¿Tenés alguna duda sobre estos números? Escribime abajo.**
    """

    # 4. Enviamos todo a la pantalla (Gráfico + Tabla)
    await cl.Message(content=cronograma_md, elements=[chart_element]).send()

@cl.on_message
async def main(message: cl.Message):
    # Por ahora, un eco simple. Acá después conectaremos n8n.
    response = f"🤖 **Asistente de Marketing:** Recibí tu consulta sobre '{message.content}'. \n\n*(Pronto estaré conectado a tu Google Sheet para responder con datos reales)*."
    await cl.Message(content=response).send()