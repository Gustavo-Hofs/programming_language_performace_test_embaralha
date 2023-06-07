#!/usr/bin/env python3


import os
import subprocess
import time
import pyperf


def setup():
    path = os.getcwd()
    subprocess.run(['mkdir', 'executables'])
    subprocess.run(['mkdir', 'results'])
    referencia = b'[[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,2,6,10,14,18,22,26,30,34,38,42,46,50,4,12,20,28,36,44,52,16,32,48,24,8],40]\n'

    print('Build python')
    path_py = "/".join([path, "python"])
    print('Creating executable...')
    subprocess.run(['pyinstaller', '-F', 'embaralha.py'],
                   cwd=path_py, capture_output=True)
    print('Copying executable...')
    subprocess.run(['cp', 'python/dist/embaralha', 'executables/py_embaralha'])
    print('Deleting trash...')
    subprocess.run(['rm', '-r', 'python/build',
                   'python/dist', 'python/embaralha.spec'])
    print('Testing...')
    resposta = subprocess.run(
        ['./executables/py_embaralha', '52'], capture_output=True).stdout
    print('Waiting for:', referencia, len(referencia), type(referencia))
    print('Received:', resposta, len(resposta), type(resposta))
    print('Success!') if resposta == referencia else print('Fails with py!')
    print()

    print('Build go')
    print('Creating executable...')
    subprocess.run(['go', 'build', 'go/main.go', 'go/cards.go'])
    print('Copying executable...')
    subprocess.run(['cp', 'main', 'executables/go_embaralha'])
    print('Deleting trash...')
    subprocess.run(['rm', 'main'])
    print('Testing...')
    resposta = subprocess.run(
        ['./executables/go_embaralha', '52'], capture_output=True).stdout
    print('Waiting for:', referencia, len(referencia), type(referencia))
    print('Received:', resposta, len(resposta), type(resposta))
    print('Success!') if resposta == referencia else print('Fails with go!')
    print()

    print('Build rust')
    print('Creating executable...')
    path_rust = '/'.join([path, 'rust', 'embaralha'])
    subprocess.run(['cargo', 'build', '-r'],
                   cwd=path_rust, capture_output=True)
    print('Copying executable...')
    subprocess.run(
        ['cp', 'rust/embaralha/target/release/embaralha', 'executables/rust_embaralha'])
    print('Deleting trash...')
    subprocess.run(['cargo', 'clean'], cwd=path_rust)
    print('Testing...')
    resposta = subprocess.run(
        ['./executables/rust_embaralha', '52'], capture_output=True).stdout
    print('Waiting for:', referencia, len(referencia), type(referencia))
    print('Received:', resposta, len(resposta), type(resposta))
    print('Success!') if resposta == referencia else print('Fails with rust!')
    print()

    print('Build bash')
    print('Creating executable...')
    subprocess.run(['chmod', '+x', 'bash/embaralha.sh'])
    print('Copying executable...')
    subprocess.run(['cp', 'bash/embaralha.sh', 'executables/bash_embaralha'])
    print('Deleting trash...')
    print('Testing...')
    resposta = subprocess.run(
        ['./executables/bash_embaralha', '52'], capture_output=True).stdout
    print('Waiting for:', referencia, len(referencia), type(referencia))
    print('Received:', resposta, len(resposta), type(resposta))
    print('Success!') if resposta == referencia else print('Fails with bash!')
    print()

    print('Build cpp')
    print('Creating executable...')
    subprocess.run(['g++', 'cpp/embaralha.cpp', '-o', 'cpp_embaralha'])
    print('Copying executable...')
    subprocess.run(['cp', 'cpp_embaralha', 'executables/cpp_embaralha'])
    print('Deleting trash...')
    subprocess.run(['rm', 'cpp_embaralha'])
    print('Testing...')
    resposta = subprocess.run(
        ['./executables/cpp_embaralha', '52'], capture_output=True).stdout
    print('Waiting for:', referencia, len(referencia), type(referencia))
    print('Received:', resposta, len(resposta), type(resposta))
    print('Success!') if resposta == referencia else print('Fails with cpp!')
    print()


def bench2(N, linguagens):
    N = str(N)
    for lingua in linguagens:
        print('Benchmarking '+lingua+' N='+N+' speed...')
        subprocess.run(['pyperf', 'command', '--name', 'speed N='+N, '-o',
                       'results/'+lingua+'_N='+N+'_time.json', './executables/'+lingua+'_embaralha', N])
        print('Benchmarking '+lingua+' N='+N+' memory...')
        subprocess.run(['pyperf', 'command', '--name', 'memory N='+N, '--track-memory',
                       '-o', 'results/'+lingua+'_N='+N+'_memory.json', './executables/'+lingua+'_embaralha', N])
        print()


def show_result(N, linguagens):
    N = str(N)
    print('Results for N='+N)
    t_jsons = ['results/'+i+'_N='+N+'_time.json'for i in linguagens]
    subprocess.run(['pyperf', 'compare_to', '--table', *t_jsons])
    m_jsons = ['results/'+i+'_N='+N+'_memory.json'for i in linguagens]
    subprocess.run(['pyperf', 'compare_to', '--table', *m_jsons])
    print()


def clean():
    subprocess.run(['rm', '-r', 'executables', 'results'])


if __name__ == "__main__":
    print('**Benchmark Embaralha**')
    print()
    print('Initiating Setup:')
    print()
    setup()
    print('Performing Tests:')
    print()
    N, linguagens = 10000, ['py', 'cpp', 'go', 'rust']
    bench2(N, linguagens)
    N2, linguagens2 = 1000000, ['cpp', 'go', 'rust']
    bench2(N2, linguagens2)
    N3, linguagens3 = 1000, ['bash', 'py', 'go']
    bench2(N3, linguagens3)
    N4, linguagens4 = 10000000, ['go', 'rust']
    bench2(N4, linguagens4)
    print('Showing Results:')
    print()
    show_result(N3, linguagens3)
    show_result(N, linguagens)
    show_result(N2, linguagens2)
    show_result(N4, linguagens4)
    print('Deleting Executables e Results...')
    clean()
    print('**Finished!**')
