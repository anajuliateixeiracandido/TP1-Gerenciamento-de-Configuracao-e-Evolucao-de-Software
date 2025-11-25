.PHONY: help install dev clean build validate run test test-unit test-integration test-acceptance test-performance server

help:
	@echo "╔══════════════════════════════════════════════════════════╗"
	@echo "║         Loja Online - Sistema de Gerência               ║"
	@echo "╚══════════════════════════════════════════════════════════╝"
	@echo ""
	@echo "📦 CONFIGURAÇÃO:"
	@echo "  make install              Instalar dependências"
	@echo "  make dev                  Configurar ambiente de desenvolvimento"
	@echo "  make clean                Limpar artefatos de build"
	@echo ""
	@echo "🔨 BUILD:"
	@echo "  make build                Executar build completo"
	@echo "  make validate             Validar sintaxe Python"
	@echo ""
	@echo "🚀 EXECUÇÃO:"
	@echo "  make run                  Executar aplicação principal"
	@echo "  make server               Executar servidor Flask (health check)"
	@echo ""
	@echo "🧪 TESTES:"
	@echo "  make test                 Executar todos os testes"
	@echo "  make test-unit            Executar testes unitários"
	@echo "  make test-integration     Executar testes de integração"
	@echo "  make test-acceptance      Executar testes de aceitação"
	@echo "  make test-performance     Executar testes de performance"
	@echo ""

# Instalação de dependências
install:
	@echo "📦 Instalando dependências..."
	pip3 install --upgrade pip
	pip3 install -r requirements.txt
	@echo "✅ Dependências instaladas com sucesso!"

# Ambiente de desenvolvimento
dev: install
	@echo "🔧 Configurando ambiente de desenvolvimento..."
	pip3 install -e .
	@echo "✅ Ambiente de desenvolvimento pronto!"

# Limpeza de artefatos
clean:
	@echo "🧹 Limpando artefatos de build..."
	rm -rf build/ dist/ *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	rm -rf htmlcov/ .coverage
	@echo "✅ Limpeza concluída!"

# Build completo
build: clean validate
	@echo "🔨 Executando build..."
	chmod +x scripts/build.sh
	./scripts/build.sh

# Validação de sintaxe
validate:
	@echo "🔍 Validando sintaxe Python..."
	python3 -m py_compile src/loja_online/*.py
	python3 -m py_compile app.py
	@echo "✅ Sintaxe validada!"

# Execução da aplicação
run:
	@echo "🚀 Executando aplicação..."
	PYTHONPATH=src python3 -m loja_online.main

# Servidor Flask para health check
server:
	@echo "🌐 Iniciando servidor Flask na porta 8000..."
	PORT=8000 python3 app.py

# Testes
test: test-unit test-integration
	@echo "✅ Todos os testes executados!"

test-unit:
	@echo "🧪 Executando testes unitários..."
	python3 -m pytest tests/unit/ -v

test-integration:
	@echo "🔗 Executando testes de integração..."
	python3 -m pytest tests/integration/ -v

test-acceptance:
	@echo "✅ Executando testes de aceitação..."
	python3 -m pytest tests/acceptance/test_fluxo_completo_loja.py -v

test-performance:
	@echo "⚡ Executando testes de performance..."
	python3 -m pytest tests/acceptance/test_performance.py -v
