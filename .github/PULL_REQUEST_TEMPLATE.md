## Descrição
<!-- Descreva brevemente as mudanças realizadas e o motivo -->

## Tipo de Mudança
<!-- Marque o tipo de mudança (seguindo Conventional Commits) -->

- [ ]  `fix` - Correção de bug (PATCH)
- [ ]  `feat` - Nova funcionalidade (MINOR)
- [ ]  `docs` - Documentação
- [ ]  `refactor` - Refatoração de código
- [ ]  `test` - Adição/modificação de testes
- [ ]  `build` - Mudanças em dependências ou build
- [ ]  `ci` - Mudanças em CI/CD
- [ ]  `chore` - Outras tarefas de manutenção

## Versionamento
<!-- Se aplicável, informe a nova versão -->

- [ ] Atualizei `setup.py` com a nova versão
- Versão atual: `1.x.x` → Nova versão: `1.x.x`

**Tipo de incremento:**
- [ ] MAJOR (mudança incompatível)
- [ ] MINOR (nova funcionalidade compatível)
- [ ] PATCH (correção de bug)
- [ ] Não aplicável (docs, ci, chore, etc.)

## Checklist de Qualidade

### Código e Testes
- [ ] Código segue as convenções do projeto
- [ ] Mensagens de commit seguem Conventional Commits
- [ ] Testes unitários passaram localmente (`make test-unit`)
- [ ] Testes de integração passaram localmente (`make test-integration`)
- [ ] Cobertura de código ≥ 70% (`pytest --cov=src/loja_online --cov-report=term`)

### Sincronização
- [ ] Branch está atualizada com `main` (git pull origin main)
- [ ] Sem conflitos com `main`
- [ ] Sem arquivos desnecessários (caches, logs, `__pycache__`, etc.)

### Documentação
- [ ] README atualizado (se necessário)
- [ ] Comentários de código adicionados (onde necessário)
- [ ] Docstrings atualizadas (se aplicável)

## Issues Relacionadas
<!-- Exemplo: Closes #42, Fixes #43, Relacionado a #44 -->

Closes #

## Evidências
<!-- Screenshots, logs, ou GIFs demonstrando a mudança (se aplicável) -->

## Notas Adicionais
<!-- Informações extras para os revisores -->
