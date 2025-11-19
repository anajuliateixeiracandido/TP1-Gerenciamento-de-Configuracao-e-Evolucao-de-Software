#!/bin/bash

set -e

echo "Executando Build Local do Sistema Loja Online"
echo "=============================================="

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

if ! command -v python3 &> /dev/null; then
    log_error "Python3 não está instalado!"
    exit 1
fi

log_info "Python $(python3 --version) detectado"

echo -e "\nEtapa 1: Instalando Dependências de Build"
echo "=========================================="

if [ -f "requirements.txt" ]; then
    log_info "Instalando dependências do requirements.txt..."
    pip3 install -r requirements.txt || {
        log_error "Falha na instalação de dependências"
        exit 1
    }
else
    log_warn "requirements.txt não encontrado, instalando dependências básicas..."
    pip3 install build wheel setuptools
fi

log_info "Dependências de build instaladas com sucesso"

echo -e "\nEtapa 2: Validação de Sintaxe Python"
echo "===================================="

log_info "Verificando sintaxe de todos os arquivos Python..."
for file in *.py; do
    if [ -f "$file" ]; then
        python3 -m py_compile "$file" || {
            log_error "Erro de sintaxe em $file"
            exit 1
        }
        log_info "$file - sintaxe válida"
    fi
done

log_info "Validação de sintaxe concluída com sucesso"

echo -e "\nEtapa 3: Verificação de Execução"
echo "================================"

log_info "Testando execução da aplicação..."
if python3 main.py > /dev/null 2>&1; then
    log_info "Aplicação executa sem erros"
else
    log_error "Aplicação falhou na execução"
    log_info "Executando novamente para mostrar erro..."
    python3 main.py
    exit 1
fi

echo -e "\nEtapa 4: Build do Projeto"
echo "========================="

log_info "Limpando artefatos antigos..."
rm -rf build/ dist/ *.egg-info/

log_info "Criando distribuível Python..."
if python3 -m build; then
    log_info "Build concluído com sucesso"
    log_info "Artefatos gerados:"
    for file in dist/*; do
        if [ -f "$file" ]; then
            size=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null)
            log_info "   - $(basename "$file") (${size} bytes)"
        fi
    done
else
    log_error "Falha no build do projeto"
    exit 1
fi

echo -e "\nEtapa 5: Verificação dos Artefatos"
echo "=================================="

log_info "Verificando integridade dos artefatos..."
if [ -d "dist" ] && [ "$(ls -A dist/)" ]; then
    log_info "Diretório dist/ contém artefatos"
    
    wheel_count=$(ls dist/*.whl 2>/dev/null | wc -l)
    tar_count=$(ls dist/*.tar.gz 2>/dev/null | wc -l)
    
    log_info "Resumo dos artefatos:"
    log_info "   - Wheel packages: $wheel_count"
    log_info "   - Source distributions: $tar_count"
    
    if [ "$wheel_count" -gt 0 ] && [ "$tar_count" -gt 0 ]; then
        log_info "Build completo - wheel e source distribution gerados"
    else
        log_warn "Build parcial - alguns tipos de artefatos podem estar faltando"
    fi
else
    log_error "Nenhum artefato foi gerado no diretório dist/"
    exit 1
fi

echo -e "\nBuild Concluído com Sucesso!"
echo "============================"
log_info "Todas as etapas de build foram executadas"
log_info "Artefatos: $(ls dist/ | wc -l) arquivo(s) gerado(s)"
log_info "Tamanho total: $(du -sh dist/ | cut -f1)"

echo -e "\nPróximos Passos (Pipeline CI/CD):"
echo "   1. git add ."
echo "   2. git commit -m 'Implementa infraestrutura de build'"
echo "   3. git push origin main"
echo "   4. Verificar GitHub Actions: https://github.com/anajuliateixeiracandido/TP1-Gerenciamento-de-Configuracao-e-Evolucao-de-Software/actions"

echo -e "\nComandos úteis:"
echo "   - make install  # Instalar dependências"
echo "   - make validate # Validar sintaxe"
echo "   - make build    # Fazer build"
echo "   - make clean    # Limpar artefatos"

echo -e "\nObrigado por usar o pipeline de build!"