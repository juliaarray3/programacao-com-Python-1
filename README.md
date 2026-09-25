# Repositório de Programação com Python

Repositório destinado ao armazenamento das atividades e códigos desenvolvidos durante as aulas da disciplina de Programação com Python.

## Informações Pessoais e Acadêmicas

- **Aluna:** Julia Andrade Rodrigues
- **Escola:** CEEP Assaí
- **Curso:** Técnico em Inteligência Artificial e Dados
- **Série:** 1° ano do Ensino Médio
- **Professor:** João Carboni Gomes

## Conteúdo das Aulas

### Aula 16 - Regex

Introdução às Expressões Regulares em Python utilizando o módulo `re`.

```python
import re

texto = "O código do aluno é 12345"
padrao = r"\d+"
resultado = re.search(padrao, texto)

if resultado:
    print(f"Código encontrado: {resultado.group()}")
```

### Aula 17 - Regex Alfanumérico

Uso de padrões alfanuméricos (`\w`) para validação de caracteres em textos.

```python
import re

usuario = "julia_andrade12"
padrao = r"^\w+$"

if re.match(padrao, usuario):
    print("Usuário válido")
```

### Aulas 18 e 19 - Estrutura de Dados Compostas

Trabalho com estruturas compostas como listas de listas e matrizes.

```python
# Lista composta com informações dos alunos
turma = [
    ["Julia", [10, 9.5]],
    ["João", [8, 9.0]]
]

for aluno in turma:
    nome = aluno[0]
    notas = aluno[1]
    print(f"Aluna: {nome} | Notas: {notas}")
```

### Aula 20 - Dicionário

Armazenamento de dados no formato de chave e valor.

```python
aluna = {
    "nome": "Julia Andrade Rodrigues",
    "curso": "IA e Dados",
    "escola": "CEEP Assaí"
}

print(aluna["nome"])
print(aluna.get("curso"))
```

### Aulas 21 e 22 - Função

Criação e uso de funções reutilizáveis em Python.

```python
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

resultado = calcular_media(9.5, 10)
print(f"A média é: {resultado}")
```

### Aula 23 - Função com Dicionário

Integração de funções que recebem ou retornam dicionários.

```python
def criar_cadastro(nome, curso):
    cadastro = {
        "nome": nome,
        "curso": curso
    }
    return cadastro

nova_aluna = criar_cadastro("Julia", "Inteligência Artificial")
print(nova_aluna)
```

## Como Executar os Códigos

- Clone o repositório em sua máquina.
- Abra o terminal na pasta do projeto.
- Execute os arquivos usando o comando:

```bash
python nome_do_arquivo.py
```
