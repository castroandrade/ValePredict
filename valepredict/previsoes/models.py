from django.db import models

class DadosAgricolas(models.Model):
    estado = models.CharField(max_length=100, blank=True, null=True) 
    regiao = models.CharField(max_length=100, blank=True, null=True) 
    cultura = models.CharField(max_length=100)  
    area = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True) 
    valor = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True) 

    def calcular_valor_por_hectare(self):
        """
        Retorna o valor por hectare se os dados estiverem disponíveis.
        """
        if self.area and self.valor:
            return self.valor / self.area
        return None

    def calcular_lucro(self, area_usuario):
        """
        Calcula o lucro baseado na área informada pelo usuário.
        """
        valor_por_hectare = self.calcular_valor_por_hectare()
        if valor_por_hectare:
            return valor_por_hectare * area_usuario
        return None

    def __str__(self):
        if self.estado:
            return f"{self.estado} - {self.cultura}"
        if self.regiao:
            return f"{self.regiao} - {self.cultura}"
        return self.cultura