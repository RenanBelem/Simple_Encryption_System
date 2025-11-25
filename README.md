## 📄 README: Sistema de Criptografia Simples em Python (main.py)

Este projeto implementa um sistema de criptografia e descriptografia simples, simulando um protocolo de troca de mensagens entre duas entidades, nomeadas **Bob** e **Alice**. O sistema utiliza uma chave de sessão numérica gerada aleatoriamente e um esquema de substituição de caracteres para "criptografar" as mensagens.

### 👥 Integrantes

  * Thomas Frentzel
  * Renan Belem Biviati

-----

### ✨ Funcionalidades

O programa principal (`main.py`) oferece um menu interativo que simula as seguintes etapas:

1.  **Geração de Chave e Nounce (Bob):**
      * Gera uma **Chave de Sessão** (`K_sessão`) aleatória (número inteiro entre 0 e 100000).
      * Bob insere uma mensagem de texto.
      * A mensagem é "criptografada" usando a função `funcao_de_bob`.
      * Um **Nounce Fixo** (`E24$%`) é anunciado como parte da transmissão.
2.  **Transmissão e Descriptografia (Alice):**
      * Alice recebe a chave de sessão de Bob (simulada por uma entrada manual).
      * Se a chave de sessão estiver correta, Alice é solicitada a inserir o Nounce de Bob.
      * Se o Nounce estiver correto (`E24$%`), a mensagem criptografada de Bob é exibida e, em seguida, "descriptografada" usando a função `descriptografia`.
3.  **Resposta de Alice para Bob:**
      * Alice insere uma nova mensagem para Bob.
      * A mensagem é "criptografada" usando a função `alice_chave_mudanca`.
      * Um **Novo Nounce** aleatório é gerado para Alice.
4.  **Descriptografia da Resposta (Bob):**
      * Bob insere o Novo Nounce de Alice.
      * Se o Nounce estiver correto, a mensagem criptografada de Alice é descriptografada usando a função `descriptografia` e exibida.

-----

### 🔑 Esquema de Criptografia

O sistema utiliza um esquema de substituição simples baseado em classes de caracteres.

#### Funções de Criptografia (`funcao_de_bob` e `alice_chave_mudanca`)

Essas funções substituem caracteres de acordo com as seguintes regras:

| Categoria de Caractere | Caracteres Afetados | Símbolo de Substituição |
| :--------------------- | :------------------ | :---------------------- |
| Vogais/Teclas QWERTY   | `poiuytrewqPOIUYTREWQ` | `%` |
| Consoantes/Teclas ASDFGH | `çlkjhgfdsaÇLKJHGFDSA` | `*` |
| Consoantes/Teclas ZXCVB | `mnbvcxzMNBVCXZ` | `#` |
| Dígitos Numéricos      | `0987654321` | `@` |
| Símbolos               | `!@#$%¨&*()` | `&` |
| Outros                 | Caracteres não listados | **Mantidos** |

#### Função de Descriptografia (`descriptografia`)

A função `descriptografia` atua removendo os símbolos de substituição (`@`, `#`, `%`, `&`, `*`) da string criptografada, restaurando a mensagem original apenas com os caracteres que não foram substituídos.

$$\text{Mensagem Descriptografada} = \text{Mensagem Criptografada} \setminus \{ @, \#, \%, \&, * \}$$

-----

### 💻 Como Executar

1.  **Requisitos:** O programa requer apenas uma instalação padrão do **Python 3**.

2.  **Execução:** Salve o código como `main.py` e execute-o a partir da linha de comando:

    ```bash
    python main.py
    ```

3.  **Interação:** Siga as instruções e os *prompts* de entrada no console para interagir com o sistema.

-----

### ⚠️ Observações de Segurança

  * **Chave de Sessão:** A chave de sessão numérica (`K_sessão`) é usada apenas como um *token* de autenticação inicial (simulado) e não participa da criptografia real da mensagem.
  * **Segurança Criptográfica:** O esquema de criptografia de substituição/remoção é **extremamente simples** e **não oferece segurança criptográfica real**. Ele é destinado apenas a fins demonstrativos e educacionais, simulando a ideia de uma transformação de dados.
  * **Descriptografia:** A função de descriptografia apenas **remove os símbolos** e não consegue reverter a substituição de caracteres, o que significa que a mensagem "descriptografada" **será incompleta e ilegível** (por exemplo, "Alice" criptografada como `*#**%` se tornará uma string vazia após a remoção dos símbolos).
      * *Nota*: A intenção do exercício parece ser a remoção dos caracteres que não foram substituídos (o que na verdade são os *espaços* e outros caracteres que não caíram em nenhuma categoria), mas a implementação remove *todos* os símbolos de substituição (`@`, `#`, `%`, `&`, `*`), resultando em uma string vazia se a mensagem original tiver sido completamente transformada.

-----
