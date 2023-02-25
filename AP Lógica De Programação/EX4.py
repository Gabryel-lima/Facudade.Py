lista = []
id = 0

def cadastrar_funcionario(id):
    '''Nesta função irá se cadastrar um novo funcionário apenas contado com o id.'''
    print('\nO ID do novo funcionário: | {} |'.format(id))
    nome = input('Digite o nome do funcionário: ')
    setor = input('Digite o setor: ')
    salario = input('Informe o salário:R$ ')
    dicionarioFuncionario = {'ID': id,
                             'Nome': nome,
                             'Setor': setor,
                             'Salario': salario}
    lista.append(dicionarioFuncionario.copy())
    print('\nFuncionário cadastrado!'.upper())
    print(62 * '-')
    
def consultar_funcionarios():
    '''Está é a função de consulta onde dará opções para se chegar a certo funcionário especifico, ou todos.'''
    while True:
        try:    
            print('\nBem-vindo ao consultar funcionários!'.upper())
            consulta = int(input('\n(Entre com a opção desejada)\n'
                                '1-Consultar todos os funcionários\n'
                                '2-Consultar Funcionário po id\n'
                                '3-Consultar Funcionários(s) por setor\n'
                                '4-Retornar\n'
                                '=> '))
            if consulta == 1:
                print(62 * '-')
                print('\nBem-vindo consultar todos!'.upper())
                for funcionario in lista:
                    for key, value in funcionario.items():
                        print('{}: {}'.format(key,value))
                        
            elif consulta == 2:
                print(62 * '-')
                print('\nBem-vindo a consultar o id!'.upper())
                entra = int(input('\nDigite o id de funcionário:> '))
                for funcionario in lista:
                    if funcionario['ID'] == entra:
                        for key, value in funcionario.items():
                            print('{}: {}'.format(key,value))    
                            
            elif consulta == 3:
                print(62 * '-')
                print('\nBem-vindo aconsultar funcionário(s) por setor!'.upper())
                entra = input('\nDigite o setor do funcionário:> ')
                for funcionario in lista:
                    if funcionario['Setor'] == entra:
                        for key, value in funcionario.items():
                            print('{}: {}'.format(key,value))
                            
            elif consulta == 4:
                return
            else:
                print('Digite apenas os números apresentados!')
                continue
        except ValueError:
            print('Pare de inserir um valor não correspondente!')

def remover_funcionario():
    '''Finalmente se tem a ultima opção. Se precisar será redirecionado para o menu novamente.'''
    print(62 * '-')
    print('Bem-vindo a remover funcionário(s)!')
    entra = int(input('Digite o id do funcionário:> '))
    for funcionario in lista:
        if funcionario['ID'] == entra:
            lista.remove(funcionario)
            print(62 * '-')
            print('Funionário removido!'.upper())

print('\nBem-vindo ao controle de funcionários do Gabryel Lima Da Silva')
print(62 * '*')

while True:
    try:
        print(23 * '_' + 'MENU PRINCIPAL' + 25 * '_')
        print('\nEscolha alguma opção:')
        print('1-Cadastrar Funcionário')
        print('2-Consultar Funcionário(s)')
        print('3-Remover funcionário')
        print('4-Sair')
        a = int(input('=> '))
        '''No program principal é executado validando a informação de entrada exibida na tabela, logo em seguida
        entra em alguma das funções...'''
        if a == 1:
            print(62 * '-')
            print('\nBem-vindo ao cadastrar funcionários!'.upper())
            id += 1
            cadastrar_funcionario(id)
        elif a == 2:
            print(62 * '-')
            consultar_funcionarios()
        elif a == 3:
            print(62 * '-')
            remover_funcionario()
        elif a == 4:
            '''E está parte encerra o código.'''
            print('\nFinalizando o programa...')
            print(62 * '-')
            break
        else:
            print('\nDigite apenas os números apresentados!'.upper())
            
    except ValueError:
        print('\nPare de inserir um valor não inteiro!'.upper())
        continue 