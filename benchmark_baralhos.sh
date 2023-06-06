#!/usr/bin/env bash

setup () {
  mkdir executables
  mkdir results
  referencia="[[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,2,6,10,14,18,22,26,30,34,38,42,46,50,4,12,20,28,36,44,52,16,32,48,24,8],40]"

  echo 'Build python'
  echo 'Criando executavel...'
  (cd python; pyinstaller -F embaralha.py) &> /dev/null
  echo 'Copiando executavel...'
  cp python/dist/embaralha executables/py_embaralha
  echo 'Deletando lixo...'
  rm -r python/build python/dist python/embaralha.spec
  echo 'Testando...'
  [[ "$(./executables/py_embaralha 52)" == "$referencia" ]] && echo "Sucesso!" || echo "Falha com py!"
  echo 

  echo 'Build go'
  echo 'Criando executavel...'
  go build go/main.go go/cards.go
  echo 'Copiando executavel...'
  cp main executables/go_embaralha
  echo 'Deletando lixo...'
  rm main
  echo 'Testando...'
  [[ "$(./executables/go_embaralha 52)" == "$referencia" ]] && echo "Sucesso!" || echo "Falha com go!"
  echo 

  echo 'Build rust'
  echo 'Criando executavel...'
  (cd rust/embaralha;cargo build -r) &> /dev/null
  echo 'Copiando executavel...'
  cp rust/embaralha/target/release/embaralha executables/rust_embaralha
  echo 'Deletando lixo...'
  cd rust/embaralha
  cargo clean
  cd ../..
  echo 'Testando...'
  [[ "$(./executables/rust_embaralha 52)" == "$referencia" ]] && echo "Sucesso!" || echo "Falha com rust!"
  echo 

  echo 'Build bash'
  echo 'Criando executavel...'
  chmod +x bash/embaralha.sh
  echo 'Copiando executavel...'
  cp bash/embaralha.sh executables/bash_embaralha
  echo 'Deletando lixo...'
  echo 'Testando...'
  [[ "$(./executables/bash_embaralha 52)" == "$referencia" ]] && echo "Sucesso!" || echo "Falha com bash!"
  echo 

  echo 'Build cpp'
  echo 'Criando executavel...'
  g++ cpp/embaralha.cpp -o cpp_embaralha
  echo 'Copiando executavel...'
  cp cpp_embaralha executables/cpp_embaralha
  echo 'Deletando lixo...'
  rm cpp_embaralha
  echo 'Testando...'
  [[ "$(./executables/cpp_embaralha 52)" == "$referencia" ]] && echo "Sucesso!" || echo "Falha com cpp!"
  echo 
}

bench2(){
  args=("$@")
  N=${args[0]}
  unset args[0]
  for lingua in "${args[@]}"; do
    echo "Benchmarking "$lingua" N="$N" speed..."
    #pyperf command --name speed_N=$N -o results/${lingua}_N=${N}_time.json ./executables/${lingua}_embaralha $N
    pyperf command -p 1 --name speed_N=$N -o results/${lingua}_N=${N}_time.json ./executables/${lingua}_embaralha $N
    echo "Benchmarking "$lingua" N="$N" memory..."
    #pyperf command --name memory_N=$N --track-memory -o results/${lingua}_N=${N}_memory.json ./executables/${lingua}_embaralha $N
    pyperf command -p 1 --name memory_N=$N --track-memory -o results/${lingua}_N=${N}_memory.json ./executables/${lingua}_embaralha $N
    echo 
  done
}

show_result(){
  args=("$@")
  N=${args[0]}
  unset args[0]
  echo 'Resultados para N='$N
  t_jsons=""
  m_jsons=""
  for lingua in "${args[@]}"; do
    t_jsons=$t_jsons" results/${lingua}_N=${N}_time.json"
    m_jsons=$m_jsons" results/${lingua}_N=${N}_memory.json"
  done
  pyperf compare_to --table $t_jsons
  pyperf compare_to --table $m_jsons
  echo 
}

clean(){
  rm -r executables results
}

echo "**Benchmark Baralhos**"
echo
echo "Iniciando Setup:"
echo
setup
echo "Realizando Testes:"
echo
bench2 10000 py cpp go rust
bench2 1000000 cpp go rust
bench2 1000 bash py go
bench2 10000000 go rust
echo "Mostrando Resultados:"
echo
show_result 1000 bash py go
show_result 10000 py cpp go rust
show_result 1000000 cpp go rust
show_result 10000000 go rust
echo "Deletando Executaveis e Resultados..."
clean
echo "**Finalizado!**"
