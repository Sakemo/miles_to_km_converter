# Milhas para Quilômetros - Conversor

Este é um aplicativo simples de conversão de milhas para quilômetros criado com o uso da biblioteca Tkinter em Python. O aplicativo fornece uma interface gráfica amigável que permite ao usuário inserir uma quantidade em milhas e convertê-la para quilômetros.

## Como usar

1. Certifique-se de ter o Python instalado no seu computador.
2. Instale a biblioteca `ttkbootstrap` usando o seguinte comando:
   ```
   pip install ttkbootstrap
   ```
3. Clone este repositório ou baixe o código-fonte em seu computador.
4. Execute o código Python.

## Funcionalidades

- **Interface Gráfica**: O aplicativo possui uma interface gráfica simples e fácil de usar, que exibe um campo de entrada para milhas e um botão "Converter".

- **Conversão**: Ao digitar uma quantidade em milhas e clicar no botão "Converter", a aplicação calcula e exibe a equivalência em quilômetros.

- **Tema Escuro**: O aplicativo utiliza um tema escuro para uma experiência de usuário mais agradável.

## Estrutura do Código

O código é organizado em uma classe chamada `ConverterApp`, que possui os seguintes métodos:

- `__init__(self, root)`: Inicializa a interface gráfica e define o tema escuro.

- `convert(self)`: Realiza a conversão de milhas para quilômetros quando o botão "Converter" é pressionado.

- `create_widgets(self)`: Cria os elementos da interface, como rótulos, campos de entrada e botões.

O ponto de entrada principal do programa é o bloco `if __name__ == "__main__"`, que cria uma instância da classe `ConverterApp` e inicia o loop de eventos da interface gráfica.

## Contribuições

Se você quiser contribuir para este projeto, sinta-se à vontade para fazer um fork do repositório e enviar pull requests com melhorias ou correções. Estamos abertos a sugestões e colaborações!

Esperamos que este aplicativo de conversão seja útil e eficaz para você. Divirta-se convertendo milhas em quilômetros!

### Créditos
Este projeto foi desenvolvido por King | Alex K.M. Chaves.
