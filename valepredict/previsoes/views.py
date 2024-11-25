from django.shortcuts import render
from .forms import PrevisaoForm
from .models import DadosAgricolas
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'previsoes/home.html')

@login_required(login_url='previsoes/login.html')
def calcular_previsao(request):
    if request.method == "POST":
        form = PrevisaoForm(request.POST)
        if form.is_valid():
            dados_cultura = form.cleaned_data['nome_cultura']
            area = form.cleaned_data['area']

            if dados_cultura:
                # Calculando o lucro com base nos dados da cultura
                lucro_estimado = dados_cultura.calcular_lucro(area)

                return render(request, 'previsoes/resultado.html', {
                    'nome_cultura': dados_cultura.cultura,
                    'area': area,
                    'lucro_estimado': lucro_estimado,
                    'valor_por_hectare': dados_cultura.calcular_valor_por_hectare(),
                })
            else:
                return render(request, 'previsoes/erro.html', {'mensagem': 'Cultura não encontrada no banco de dados.'})
    else:
        form = PrevisaoForm()

    return render(request, 'previsoes/calcular.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'previsoes/register.html', {'form': form})