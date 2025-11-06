from collections import deque

# ============================
# LISTAS E FILA DE ATENDIMENTO
# ============================
pacientes = []
fila = deque()

# ============================
# FUNÇÕES DO SISTEMA
# ============================

# Cadastrar paciente
def cadastrar():
    try:
        nome = input("Nome: ").strip()
        idade = int(input("Idade: "))
        telefone = input("Telefone: ").strip()
        cpf = input("CPF: ").strip()
        paciente = {"nome": nome, "idade": idade, "telefone": telefone, "cpf": cpf}
        pacientes.append(paciente)
        fila.append(paciente)  # adiciona automaticamente à fila
        print(f"Paciente {nome} cadastrado e adicionado à fila!\n")
    except ValueError:
        print("Erro: Idade deve ser um número inteiro.\n")

# Listar todos os pacientes
def listar():
    if not pacientes:
        print("Nenhum paciente cadastrado.\n")
        return
    print("=== PACIENTES CADASTRADOS ===")
    for i, p in enumerate(pacientes, start=1):
        print(f"{i}. Nome: {p['nome']}, Idade: {p['idade']}, Telefone: {p['telefone']}, CPF: {p['cpf']}")
    print()

# Estatísticas
def estatisticas():
    if not pacientes:
        print("Nenhum paciente cadastrado.\n")
        return
    total = len(pacientes)
    soma_idades = sum(p["idade"] for p in pacientes)
    idade_media = soma_idades / total
    mais_novo = min(pacientes, key=lambda x: x["idade"])
    mais_velho = max(pacientes, key=lambda x: x["idade"])
    print("=== ESTATÍSTICAS ===")
    print(f"Total de pacientes: {total}")
    print(f"Idade média: {idade_media:.1f}")
    print(f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)\n")

# Buscar paciente por nome
def buscar():
    nome_busca = input("Digite o nome do paciente: ").strip()
    encontrados = [p for p in pacientes if p["nome"].lower() == nome_busca.lower()]
    if encontrados:
        print("=== PACIENTE ENCONTRADO ===")
        for p in encontrados:
            print(f"Nome: {p['nome']}, Idade: {p['idade']}, Telefone: {p['telefone']}, CPF: {p['cpf']}")
    else:
        print("Paciente não encontrado.\n")
    print()

# Mostrar fila de atendimento
def listar_fila():
    if not fila:
        print("Fila de atendimento vazia.\n")
        return
    print("=== FILA DE ATENDIMENTO ===")
    for i, p in enumerate(fila, start=1):
        print(f"{i}. {p['nome']} | CPF: {p['cpf']}")
    print()

# ============================
# FUNÇÃO DE CONTROLE DE ACESSO
# ============================

def verificar_acesso():
    print("=== VERIFICAR ACESSO DO PACIENTE ===")
    nome = input("Nome do paciente: ").strip()
    paciente = next((p for p in pacientes if p["nome"].lower() == nome.lower()), None)
    if not paciente:
        print("Paciente não cadastrado.\n")
        return

    # Solicitar informações
    A = input("Paciente tem agendamento? (S/N): ").strip().upper() == "S"
    B = input("Documentos em dia? (S/N): ").strip().upper() == "S"
    C = input("Médico disponível? (S/N): ").strip().upper() == "S"
    D = input("Pagamentos em dia? (S/N): ").strip().upper() == "S"

    # Regras de acesso
    consulta_normal = (A and B and C) or (B and C and D)
    emergencia = C and (B or D)

    # Resultado
    print("\n=== RESULTADO DO CONTROLE DE ACESSO ===")
    if consulta_normal:
        print("Paciente pode ser atendido em CONSULTA NORMAL.")
    else:
        print("Paciente NÃO pode ser atendido em CONSULTA NORMAL.")

    if emergencia:
        print("Paciente pode ser atendido em EMERGÊNCIA.")
    else:
        print("Paciente NÃO pode ser atendido em EMERGÊNCIA.")
    print()

# Atender próximo paciente (após controle de acesso)
def atender():
    if not fila:
        print("Nenhum paciente na fila para atendimento.\n")
        return
    paciente = fila.popleft()
    print(f"Atendendo paciente: {paciente['nome']} | CPF: {paciente['cpf']}\n")

# ============================
# MENU PRINCIPAL
# ============================
def menu():
    while True:
        print("=== SISTEMA CLÍNICA VIDA+ ===")
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar paciente")
        print("4. Listar todos os pacientes")
        print("5. Mostrar fila de atendimento")
        print("6. Verificar acesso do paciente")
        print("7. Atender próximo paciente")
        print("8. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            estatisticas()
        elif opcao == "3":
            buscar()
        elif opcao == "4":
            listar()
        elif opcao == "5":
            listar_fila()
        elif opcao == "6":
            verificar_acesso()
        elif opcao == "7":
            atender()
        elif opcao == "8":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Executa o sistema
menu()
