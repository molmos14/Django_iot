from django.shortcuts import render
import plotly.express as px
import plotly.io as pio

def home_view(request):
    # Datos de ejemplo
    data = {
        'x' : [1,2,3,4,5],
        'y' : [10,11,12,13,14],
        'text' : ['A', 'B', 'C', 'D', 'E']
    }

    # crea la gráfica
    fig = px.scatter(data, x='x', y='y', text='text', title='Ejemplo de Gráfica con Plotly')

    # Configuración adicional (opcional)
    fig.update_layout(
        xaxis_title='Eje X',
        yaxis_title='Eje Y',
    )

    # Convierte la gráfica a HTML
    plot_html = pio.to_html(fig, full_html=False)

    # Renderiza la plantilla con la gráfica incrustada
    return render(request, 'plotly_app/home.html', {'plot': plot_html})

