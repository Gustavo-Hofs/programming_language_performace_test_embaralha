#!/usr/bin/env python3


import os
import subprocess
import time
import pyperf


def setup():
    '''
    Cria executavel e limpa arquivos não utilizados para cada linguagem.
    '''
    path = os.getcwd()
    subprocess.run(['mkdir', 'executables'])
    subprocess.run(['mkdir', 'results'])
    referencia = b'[[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,2,6,10,14,18,22,26,30,34,38,42,46,50,4,12,20,28,36,44,52,16,32,48,24,8],40]\n'

    print('Build python')
    path_py = "/".join([path, "python"])
    print('Criando executavel...')
    subprocess.run(['pyinstaller', '-F', 'embaralha.py'],
                   cwd=path_py, capture_output=True)
    print('Copiando executavel...')
    subprocess.run(['cp', 'python/dist/embaralha', 'executables/py_embaralha'])
    print('Deletando lixo...')
    subprocess.run(['rm', '-r', 'python/build',
                   'python/dist', 'python/embaralha.spec'])
    print('Testando...')
    resposta = subprocess.run(
        ['./executables/py_embaralha', '52'], capture_output=True).stdout
    print('Esperando:', referencia, len(referencia), type(referencia))
    print('Recebido:', resposta, len(resposta), type(resposta))
    print('Sucesso!') if resposta == referencia else print('Falha com py!')
    print()

    print('Build go')
    print('Criando executavel...')
    subprocess.run(['go', 'build', 'go/main.go', 'go/cards.go'])
    print('Copiando executavel...')
    subprocess.run(['cp', 'main', 'executables/go_embaralha'])
    print('Deletando lixo...')
    subprocess.run(['rm', 'main'])
    print('Testando...')
    resposta = subprocess.run(
        ['./executables/go_embaralha', '52'], capture_output=True).stdout
    print('Esperando:', referencia, len(referencia), type(referencia))
    print('Recebido:', resposta, len(resposta), type(resposta))
    print('Sucesso!') if resposta == referencia else print('Falha com go!')
    print()

    print('Build rust')
    print('Criando executavel...')
    path_rust = '/'.join([path, 'rust', 'embaralha'])
    subprocess.run(['cargo', 'build', '-r'],
                   cwd=path_rust, capture_output=True)
    print('Copiando executavel...')
    subprocess.run(
        ['cp', 'rust/embaralha/target/release/embaralha', 'executables/rust_embaralha'])
    print('Deletando lixo...')
    subprocess.run(['cargo', 'clean'], cwd=path_rust)
    print('Testando...')
    resposta = subprocess.run(
        ['./executables/rust_embaralha', '52'], capture_output=True).stdout
    print('Esperando:', referencia, len(referencia), type(referencia))
    print('Recebido:', resposta, len(resposta), type(resposta))
    print('Sucesso!') if resposta == referencia else print('Falha com rust!')
    print()

    print('Build bash')
    print('Criando executavel...')
    subprocess.run(['chmod', '+x', 'bash/embaralha.sh'])
    print('Copiando executavel...')
    subprocess.run(['cp', 'bash/embaralha.sh', 'executables/bash_embaralha'])
    print('Deletando lixo...')
    print('Testando...')
    resposta = subprocess.run(
        ['./executables/bash_embaralha', '52'], capture_output=True).stdout
    print('Esperando:', referencia, len(referencia), type(referencia))
    print('Recebido:', resposta, len(resposta), type(resposta))
    print('Sucesso!') if resposta == referencia else print('Falha com bash!')
    print()

    print('Build cpp')
    print('Criando executavel...')
    subprocess.run(['g++', 'cpp/embaralha.cpp', '-o', 'cpp_embaralha'])
    print('Copiando executavel...')
    subprocess.run(['cp', 'cpp_embaralha', 'executables/cpp_embaralha'])
    print('Deletando lixo...')
    subprocess.run(['rm', 'cpp_embaralha'])
    print('Testando...')
    resposta = subprocess.run(
        ['./executables/cpp_embaralha', '52'], capture_output=True).stdout
    print('Esperando:', referencia, len(referencia), type(referencia))
    print('Recebido:', resposta, len(resposta), type(resposta))
    print('Sucesso!') if resposta == referencia else print('Falha com cpp!')
    print()


# def benchmark(N):
#     #linguagens = ['py','go','rust']
#     linguagens = ['go','rust']
#     benchs = []
#     for lingua in linguagens:
#         t0 = time.time()
#         res = subprocess.run(['./executables/'+lingua+'_embaralha', N], capture_output=True).stdout
#         t1 = time.time()
#         benchs.append((lingua,t1-t0))
#     return benchs
#
#
# def print_res(benchs):
#     print('Resultados:')
#     for b in benchs:
#         print(b)
#
#
# def bench():
#     N = str(100000)
#     print('Realizando benckmarks para N='+N)
#     res = benchmark(N)
#     print_res(res)


def bench2(N, linguagens):
    N = str(N)
    for lingua in linguagens:
        print('Benchmarking '+lingua+' N='+N+' speed...')
        # subprocess.run(['pyperf','command','--name','speed N='+N,'-o','results/'+lingua+'_N='+N+'_time.json','./executables/'+lingua+'_embaralha',N])
        subprocess.run(['pyperf', 'command', '-p', '1', '--name', 'speed N='+N, '-o',
                       'results/'+lingua+'_N='+N+'_time.json', './executables/'+lingua+'_embaralha', N])
        print('Benchmarking '+lingua+' N='+N+' memory...')
        # subprocess.run(['pyperf','command','--name','memory N='+N,'--track-memory','-o','results/'+lingua+'_N='+N+'_memory.json','./executables/'+lingua+'_embaralha',N])
        subprocess.run(['pyperf', 'command', '-p', '1', '--name', 'memory N='+N, '--track-memory',
                       '-o', 'results/'+lingua+'_N='+N+'_memory.json', './executables/'+lingua+'_embaralha', N])
        print()


def show_result(N, linguagens):
    N = str(N)
    print('Resultados para N='+N)
    t_jsons = ['results/'+i+'_N='+N+'_time.json'for i in linguagens]
    subprocess.run(['pyperf', 'compare_to', '--table', *t_jsons])
    m_jsons = ['results/'+i+'_N='+N+'_memory.json'for i in linguagens]
    subprocess.run(['pyperf', 'compare_to', '--table', *m_jsons])
    print()


def clean():
    subprocess.run(['rm', '-r', 'executables', 'results'])


if __name__ == "__main__":
    print('**Benchmark Baralhos**')
    print()
    print('Iniciando Setup:')
    print()
    setup()
    # bench()
    print('Realizando Testes:')
    print()
    N, linguagens = 10000, ['py', 'cpp', 'go', 'rust']
    bench2(N, linguagens)
    N2, linguagens2 = 1000000, ['cpp', 'go', 'rust']
    bench2(N2, linguagens2)
    N3, linguagens3 = 1000, ['bash', 'py', 'go']
    bench2(N3, linguagens3)
    N4, linguagens4 = 10000000, ['go', 'rust']
    bench2(N4, linguagens4)
    print('Mostrando Resultados:')
    print()
    show_result(N3, linguagens3)
    show_result(N, linguagens)
    show_result(N2, linguagens2)
    show_result(N4, linguagens4)
    print('Deletando Executaveis e Resultados...')
    clean()
    print('**Finalizado!**')
