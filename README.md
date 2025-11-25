# Sistema de Loja Online - TP1

## 📋 Sobre o Projeto

Sistema completo de loja online desenvolvido para o trabalho prático de Gerenciamento de Configuração e Evolução de Software. Inclui funcionalidades de gerenciamento de produtos, carrinho de compras, processamento de pedidos, pagamentos e entregas.

## 🏗️ Estrutura do Projeto

```
.
├── src/loja_online/          # Código fonte da aplicação
│   ├── carrinho.py           # Gerenciamento do carrinho
│   ├── cliente.py            # Cadastro e autenticação de clientes
│   ├── entrega.py            # Sistema de entregas
│   ├── estoque.py            # Controle de estoque
│   ├── loja.py               # Orquestração da loja
│   ├── main.py               # Ponto de entrada da aplicação
│   ├── pagamento.py          # Processamento de pagamentos
│   ├── pedido.py             # Gerenciamento de pedidos
│   ├── produto.py            # Cadastro de produtos
│   └── utilitarios.py        # Funções auxiliares
│
├── tests/                    # Suite completa de testes
│   ├── unit/                 # Testes unitários
│   ├── integration/          # Testes de integração
│   └── acceptance/           # Testes de aceitação e performance
│
├── scripts/                  # Scripts de build e automação
│   ├── build.sh              # Script de build local
│   └── Makefile              # Comandos de build (legado)
│
├── .github/workflows/        # Pipelines CI/CD
│   ├── build.yml             # Pipeline de build
│   ├── tests.yml             # Testes automatizados
│   ├── acceptance-tests.yml  # Testes de aceitação
│   └── deploy.yml            # Deploy automático
│
├── test-results/             # Resultados de testes (não versionado)
├── app.py                    # Servidor Flask para health check
├── setup.py                  # Configuração do pacote Python
├── requirements.txt          # Dependências do projeto
├── pytest.ini                # Configuração do pytest
├── Makefile                  # Comandos principais do projeto
└── README.md                 # Este arquivo
```

## 🚀 Início Rápido

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git

### Instalação

```bash
# Clone o repositório
git clone https://github.com/anajuliateixeiracandido/TP1-Gerenciamento-de-Configuracao-e-Evolucao-de-Software.git
cd TP1-Gerenciamento-de-Configuracao-e-Evolucao-de-Software

# Instale as dependências
make install

# Configure o ambiente de desenvolvimento
make dev
```

### Executando a Aplicação

```bash
# Executar aplicação principal
make run

# Executar servidor Flask (health check)
make server
```

## 🧪 Testes

### Para que Servem os Testes

#### Testes de Aceitação Funcional

Validam se o sistema funciona corretamente do ponto de vista do usuário final, testando o fluxo completo de uso:

**Teste Implementado:** `test_fluxo_completo_compra_sucesso`

- Valida todo o ciclo de vida de uma compra na loja online
- Testa 9 passos completos desde cadastro até finalização
- Garante que todas as funcionalidades integradas funcionam juntas

#### Testes de Performance

Validam requisitos não-funcionais do sistema, como velocidade e capacidade de carga:

1. **Cadastro em Massa** - Testa se o sistema consegue cadastrar 1.000 produtos em menos de 2 segundos
2. **Pedidos Simultâneos** - Verifica se 100 pedidos podem ser criados ao mesmo tempo sem erros
3. **Busca de Produtos** - Testa se 1.000 buscas são realizadas em menos de 1 segundo
4. **Atualização Concorrente** - Valida consistência de dados com 100 operações paralelas no estoque

---

### Testes Unitários

Validam componentes individuais do sistema:

```bash
make test-unit
```

### Testes de Integração

Validam a integração entre componentes:

```bash
make test-integration
```

### Testes de Aceitação

Validam o fluxo completo do ponto de vista do usuário:

```bash
make test-acceptance
```

### Testes de Performance

Validam requisitos não-funcionais (velocidade, capacidade):

```bash
make test-performance
```

**Testes inclusos:**
- **Cadastro em Massa**: 1.000 produtos em < 2s
- **Pedidos Simultâneos**: 100 pedidos concorrentes
- **Busca de Produtos**: 1.000 buscas em < 1s
- **Atualização Concorrente**: 100 operações paralelas no estoque

### Executar Todos os Testes

```bash
make test
```

## 🔨 Build

### Build Local

```bash
# Build completo (inclui validação e geração de artefatos)
make build

# Apenas validar sintaxe Python
make validate

# Limpar artefatos de build
make clean
```

### Build via Scripts

```bash
# Executar script de build detalhado
chmod +x scripts/build.sh
./scripts/build.sh
```

## 📦 Comandos Disponíveis

Execute `make help` ou `make` para ver todos os comandos:

```
📦 CONFIGURAÇÃO:
  make install              Instalar dependências
  make dev                  Configurar ambiente de desenvolvimento
  make clean                Limpar artefatos de build

🔨 BUILD:
  make build                Executar build completo
  make validate             Validar sintaxe Python

🚀 EXECUÇÃO:
  make run                  Executar aplicação principal
  make server               Executar servidor Flask

🧪 TESTES:
  make test                 Executar todos os testes
  make test-unit            Executar testes unitários
  make test-integration     Executar testes de integração
  make test-acceptance      Executar testes de aceitação
  make test-performance     Executar testes de performance
```

## 🔄 CI/CD Pipeline

O projeto possui pipelines automatizados no GitHub Actions:

### Pipeline de Build (`.github/workflows/build.yml`)
- Validação de sintaxe
- Geração de artefatos distribuíveis
- Verificação de integridade

### Pipeline de Testes (`.github/workflows/tests.yml`)
- Testes unitários
- Testes de integração
- Geração de relatórios de cobertura

### Pipeline de Testes de Aceitação (`.github/workflows/acceptance-tests.yml`)

**Quando executa:**
- Push para branch `main` ou `master`
- Pull Request para `main` ou `master`
- Após o workflow de "Testes Automatizados" passar com sucesso

**O que faz:**
1. Configura ambiente Python 3.11
2. Instala dependências automaticamente
3. Inicia a aplicação em background
4. Executa testes de aceitação funcionais
5. Executa testes de performance
6. Captura logs e evidências em caso de falha
7. Faz upload dos resultados como artefatos (disponível por 30 dias)

### Pipeline de Deploy (`.github/workflows/deploy.yml`)
- Deploy automático para Render
- Verificação de health check
- Rollback em caso de falha

## 🌐 Endpoints da Aplicação

### Health Check
```bash
GET /health
```
Retorna status do servidor: `{"status": "ok"}`

## 📊 Estrutura de Dados

### Produto
- ID, nome, descrição, preço, categoria, estoque

### Cliente
- ID, nome, email, CPF, endereço, telefone

### Pedido
- ID, cliente, itens, total, status, data

### Pagamento
- ID, pedido, método, status, valor

### Entrega
- ID, pedido, endereço, status, prazo

## 🛠️ Tecnologias Utilizadas

- **Python 3.11**: Linguagem principal
- **Pytest**: Framework de testes
- **Flask**: Servidor web para health check
- **GitHub Actions**: CI/CD
- **Render**: Plataforma de deploy
- **Make**: Automação de tarefas

## 👥 Equipe

Desenvolvido pela equipe do TP1 - Gerenciamento de Configuração e Evolução de Software

## 📝 Licença

Este projeto é desenvolvido para fins acadêmicos.

## 🔗 Links Úteis

- [Repositório no GitHub](https://github.com/anajuliateixeiracandido/TP1-Gerenciamento-de-Configuracao-e-Evolucao-de-Software)
- [GitHub Actions](https://github.com/anajuliateixeiracandido/TP1-Gerenciamento-de-Configuracao-e-Evolucao-de-Software/actions)
- [Deploy em Produção](https://tp1-gerenciamento-de-configuracao-e.onrender.com/health)
