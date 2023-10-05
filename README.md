# Cursed Stone Solana SDK for game development

Este repositório contém código Python para criar uma carteira Solana e transferir Sol de uma carteira para outra. O código utiliza a biblioteca Solathon para interagir com a rede Solana.

## Pré-requisitos

- Python 3.x instalado
- Biblioteca Solathon instalada (você pode instalar usando `pip install solathon`)

## Criação de Carteira

O arquivo `create_wallet.py` contém código para criar uma nova carteira Solana e exibir sua chave pública e privada. Certifique-se de manter sua chave privada em segurança.

Para executar a criação de carteira, use o seguinte comando:

```bash
python create_wallet.py

----------------------------------------------------------------------------
#Transferência de Sol

O arquivo transfer_sol.py permite que você transfira Sol de uma carteira para outra.
Certifique-se de configurar a variável de ambiente PRIVATE_KEY com a chave privada da carteira remetente.
Para executar uma transferência de Sol, use o seguinte comando:

# Transferência de Sol usando Solathon

Este repositório contém um código Python para realizar uma transferência de Sol da sua carteira Solana para outra usando a biblioteca Solathon.

## Pré-requisitos

- Python 3.x instalado
- Biblioteca Solathon instalada (você pode instalá-la usando `pip install solathon`)


4. O código irá transferir a quantidade especificada de Sol para o destinatário.

## Notas de Segurança

- Mantenha a chave privada (`private_key.txt`) protegida e segura. Não compartilhe publicamente ou armazene em locais não seguros.

## Aviso Legal


## Configuração

OPÇÃO COM .ENV :
Configurar uma variável de ambiente `PRIVATE_KEY` com a chave privada da carteira remetente antes de executar o código.
para autenticar a transação.
Você pode configurar a variável de ambiente da seguinte maneira:

```bash
export PRIVATE_KEY=sua_chave_privada
