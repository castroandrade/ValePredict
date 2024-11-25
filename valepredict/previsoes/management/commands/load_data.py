import json
from django.core.management.base import BaseCommand
from previsoes.models import DadosAgricolas

class Command(BaseCommand):
    help = "Carrega dados de área plantada e valor da produção em um único modelo"

    def handle(self, *args, **kwargs):
        with open('data/area_plantada.json', 'r', encoding='utf-8') as f:
            area_data = json.load(f)
        
        with open('data/valor_producao.json', 'r', encoding='utf-8') as f:
            valor_data = json.load(f)

        for estado, culturas in area_data['valuesMap'].items():
            for cultura, area in culturas.items():
                area_float = float(area.replace('.', '').replace(',', '.'))

                obj, created = DadosAgricolas.objects.update_or_create(
                    estado=estado,
                    cultura=cultura,
                    defaults={'area': area_float} 
                )

                if cultura in valor_data['valuesMap'].get('Brasil', {}):
                    valor = valor_data['valuesMap']['Brasil'][cultura]
                    valor_float = float(valor.replace('.', '').replace(',', '.'))

                    obj.valor = valor_float
                    obj.save()

        self.stdout.write(self.style.SUCCESS('Dados carregados e consolidados com sucesso!'))
