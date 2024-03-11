import difflib
from datetime import datetime, timedelta

class PontoApp:
    def __init__(self):
        self.registros = []

    def normalizar_nome(self, nome):
        """Normaliza o nome para facilitar a comparação."""
        return nome.strip().lower()

    def sugerir_correcao_nome(self, nome, nomes_registrados):
        """Sugere correção para o nome com base nos nomes já registrados."""
        correcoes_possiveis = difflib.get_close_matches(nome, nomes_registrados, n=1, cutoff=0.8)
        return correcoes_possiveis[0] if correcoes_possiveis else nome

    def executar(self):
        while True:
            print("\n--- MENU PRINCIPAL ---")
            print("1. Preencher Horário")
            print("2. Gerar Relatório")
            print("3. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.preencher_horario()
            elif opcao == '2':
                self.gerar_relatorio()
            elif opcao == '3':
                print("Saindo...")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

    def preencher_horario(self):
        print("\nPara cadastrar vários funcionários de uma vez, separe os nomes por vírgula.")
        entrada_nomes = input("Digite o nome do(s) funcionário(s) que trabalhou(aram) hoje: ")
        nomes = [self.normalizar_nome(nome) for nome in entrada_nomes.split(',')]
        nomes_registrados = set([self.normalizar_nome(registro[0]) for registro in self.registros])
        nomes_corrigidos = [self.sugerir_correcao_nome(nome, nomes_registrados) for nome in nomes]

        data_servico = self.obter_data_servico()
        hora_entrada = input("Digite a hora de entrada (HH:MM): ")
        hora_saida = input("Digite a hora de saída (HH:MM): ")
        local_trabalho = input("Digite o local de trabalho: ")
        turno = self.obter_opcao_valida("Digite o turno (manha/noite): ", ["manha", "noite"])
        for nome in nomes_corrigidos:
            self.registros.append((nome, data_servico, hora_entrada, hora_saida, local_trabalho, turno))

    def obter_data_servico(self):
        usar_data_atual = self.obter_opcao_valida("Deseja usar a data atual? (s/n): ", ["s", "n"])
        if usar_data_atual == 's':
            return datetime.now().strftime("%d/%m/%y")
        else:
            data_input = input("Digite a data (DD/MM): ")
            data_servico = datetime.strptime(data_input + "/" + str(datetime.now().year), "%d/%m/%Y").strftime("%d/%m/%y")
            return data_servico

    def gerar_relatorio(self):
        print("\n--- RELATÓRIO DE PONTOS ---")
        if not self.registros:
            print("Nenhum registro encontrado.")
            return
        for nome in set(registro[0] for registro in self.registros):
            print(f"\nNome: {nome.title()}")
            total_horas = 0
            for registro in filter(lambda r: r[0].lower() == nome.lower(), self.registros):
                _, data_servico, hora_entrada, hora_saida, local_trabalho, turno = registro
                horas_trabalhadas = self.calcular_horas_trabalhadas(hora_entrada, hora_saida, turno)
                total_horas += horas_trabalhadas
                print(f"Dia: {data_servico} - Hrs Trabalhadas Nesse dia: {horas_trabalhadas:.1f} Hrs local: {local_trabalho.title()}")
            print(f"Total de Horas Acumuladas: {total_horas:.1f} Hrs")

    def calcular_horas_trabalhadas(self, hora_entrada, hora_saida, turno):
        formato_horas = "%H:%M"
        entrada = datetime.strptime(hora_entrada, formato_horas)
        saida = datetime.strptime(hora_saida, formato_horas)
        if saida <= entrada:
            saida += timedelta(days=1)  # Ajuste para turnos que cruzam a meia-noite
        total_horas = (saida - entrada).total_seconds() / 3600
        # Descontar 1 hora para o almoço no turno da manhã
        if turno == "manha":
            total_horas -= 1
        return total_horas

    def obter_opcao_valida(self, mensagem, opcoes_validas):
        while True:
            opcao = input(mensagem).lower()
            if opcao in opcoes_validas:
                return opcao
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

app = PontoApp()
app.executar()
